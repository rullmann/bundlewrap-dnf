pkg_yum = {
    "yum": {},
}

actions = {
    'yum_makecache': {
        'command': "yum makecache",
        'triggered': True,
    },
}
