pkg_yum = {
    "yum": {},
}

actions = {
    'yum_makecache': {
        'command': "yum makecache",
        'triggered': True,
    },
}

files = {}

if node.metadata.get('yum', {}).get('auto_downloads', False):
    pkg_yum['yum-cron'] = {}

    svc_systemd = {
        'yum-cron': {
            'enabled': True,
            'needs': [
                "pkg_yum:yum-cron",
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
            "pkg_yum:yum-cron",
        ],
    }

    files['/etc/yum/yum-cron-hourly.conf'] = {
        'source': "yum-cron-hourly.conf",
        'mode': "0644",
        'owner': "root",
        'group': "root",
        'content_type': "mako",
        'needs': [
            "pkg_yum:yum-cron",
        ],
    }

for package in node.metadata.get('yum', {}).get('extra_packages', {}):
    pkg_yum['{}'.format(package)] = {}
