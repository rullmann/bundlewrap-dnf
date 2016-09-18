# bundlewrap-yum

`bundlewrap-yum` installs `yum`, removes unnecessary default repo lists and optionally sets up automatic download and updates of packages.
Beside that the bundle provides an action to update the yum metadata cache which can be used by other bundles whenever a repo list is being modified.

## Compatibility

This bundle has been tested on the following systems:

| OS          | `[x]` |
| ----------- | ----- |
| Fedora 24   | `[x]` |
| Fedberry 23 | `[ ]` |

## Metadata

    'metadata': {
        'yum': { #optional
            'auto_downloads': True, # configure yum-cron and download updates
            'auto_update': True, # if auto_downloads: True, also install updates
            'update_cmd': 'default', # define which updates will be installed, e.g. 'security'
            'extra_packages': ['git-email'], # optional, installs any given package with yum
        },
    }
