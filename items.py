pkg_dnf = {}

actions = {
    'dnf_makecache': {
        'command': 'dnf makecache',
        'triggered': True,
    },
}

files = {
    '/etc/dnf/dnf.conf': {
        'source': 'dnf.conf',
        'mode': '0644',
    },
}

if node.metadata.get('dnf', {}).get('auto_downloads', False):
    pkg_dnf['yum-cron'] = {}

    svc_systemd = {
        'yum-cron': {
            'needs': ['pkg_dnf:yum-cron'],
        },
    }

    files['/etc/yum/yum-cron.conf'] = {
        'source': 'yum-cron.conf',
        'mode': '0644',
        'content_type': 'mako',
        'needs': ['pkg_dnf:yum-cron'],
    }

    files['/etc/yum/yum-cron-hourly.conf'] = {
        'source': 'yum-cron-hourly.conf',
        'mode': '0644',
        'content_type': 'mako',
        'needs': ['pkg_dnf:yum-cron'],
    }

for package in node.metadata.get('dnf', {}).get('extra_packages', {}):
    pkg_dnf['{}'.format(package)] = {}

for package in node.metadata.get('dnf', {}).get('remove_extra_packages', {}):
    pkg_dnf['{}'.format(package)] = {
        'installed': False,
    }

for repo_id, repo in sorted(node.metadata.get('dnf', {}).get('repositories', {}).items()):
    files['/etc/yum.repos.d/{}.repo'.format(repo_id)] = {
        'content_type': 'mako',
        'source': 'repo_template',
        'mode': '0644',
        'context': {
            'repo_items': repo,
            'repo_id': repo_id,
        },
        'triggers': ['action:dnf_makecache'],
    }
