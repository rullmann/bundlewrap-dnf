# bundlewrap-yum

`bundlewrap-yum` does something.

## Compatibility

This bundle has been tested on the following systems:

| OS          | [x] |
| ----------- | --- |
| CentOS 7    | [x] |
| Fedora 24   | [ ] |
| RHEL 7      | [x] |
| Fedberry 23 | [ ] |

## Requirements

* *none*

## Metadata

    'metadata': {
        'yum': { #optional
            'auto_downloads': True, # configure yum-cron and download updates
            'auto_update': True, # if auto_downloads: True, also install updates
            'update_cmd': 'default', # define which updates will be installed, e.g. 'security'
        },
    }