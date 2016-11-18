pkg_dnf = {
    "yum": {},
}

actions = {
    'dnf_makecache': {
        'command': "dnf makecache",
        'triggered': True,
    },
}

files = {}

if node.metadata.get('dnf', {}).get('auto_downloads', False):
    pkg_dnf['yum-cron'] = {}

    svc_systemd = {
        'yum-cron': {
            'enabled': True,
            'needs': [
                "pkg_dnf:yum-cron",
            ],
        },
    }

    files['/etc/yum/yum-cron.conf'] = {
        'source': "yum-cron.conf",
        'mode': "0644",
        'owner': "root",
        'group': "root",
        'content_type': "mako",
        'needs': [
            "pkg_dnf:yum-cron",
        ],
    }

    files['/etc/yum/yum-cron-hourly.conf'] = {
        'source': "yum-cron-hourly.conf",
        'mode': "0644",
        'owner': "root",
        'group': "root",
        'content_type': "mako",
        'needs': [
            "pkg_dnf:yum-cron",
        ],
    }

for package in node.metadata.get('dnf', {}).get('extra_packages', {}):
    pkg_dnf['{}'.format(package)] = {}
