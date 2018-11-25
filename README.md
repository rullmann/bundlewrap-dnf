# bundlewrap-dnf

`bundlewrap-dnf` installs `dnf`, removes unnecessary default repo lists and optionally sets up automatic download and updates of packages.
Beside that the bundle provides an action to update the dnf metadata cache which can be used by other bundles whenever a repo list is being modified.

## Metadata

    'metadata': {
        'dnf': { #optional
            'auto_downloads': True, # configure yum-cron and download updates
            'auto_update': True, # if auto_downloads: True, also install updates
            'update_cmd': 'default', # define which updates will be installed, e.g. 'security'
            'send_mails': True, # send emails for yum-cron actions, defaults to False
            'extra_packages': ['git-email'], # optional, installs any given package with dnf
            'remove_extra_packages': ['fedora-release-notes'], # optional, remove any packages with dnf
            'repositories': { # optional, add additional repositories, e.g. for usage in metadata.py
                'influxdb': { # example repo_id in this case
                    'name': 'InfluxDB Repository - RHEL 7', # optional, if not set repo_id will be used
                    'baseurl': 'https://repos.influxdata.com/rhel/7/x86_64/stable', # required
                    'enabled': '1', # optional, 1 by default
                    'gpgcheck': '1', # optional, 1 by default
                    'gpgkey': 'https://repos.influxdata.com/influxdb.key', # optional
                },
            },
        },
    }

## Usage in metadata.py

### Repositories

You may want to use the same repository in various bundles. To make sure there aren't any conflicts it's possible to use the `metadata.py`.
In the following example the Influx Repo for RHEL 7 is being used:

    @metadata_processor
    def dnf(metadata):
        if node.has_bundle('dnf'):
            metadata.setdefault('dnf', {})
            metadata['dnf'].setdefault('repositories', {})
            metadata['dnf']['repositories'].setdefault('influxdb', {})
            metadata['dnf']['repositories']['influxdb'].setdefault(
                'name',
                'InfluxDB Repository - RHEL 7',
            )
            metadata['dnf']['repositories']['influxdb'].setdefault(
                'baseurl',
                'https://repos.influxdata.com/rhel/7/x86_64/stable',
            )
            metadata['dnf']['repositories']['influxdb'].setdefault(
                'gpgkey',
                'https://repos.influxdata.com/influxdb.key',
            )
        return metadata, DONE

### Extra Packages

Some bundles may need packages which are not bound to one bundle only. You can use a separate bundle to just install one or two packages or put these dependencies into the `metadata.py`. By doing so you can define the same dependency in more than one bundle.
The following example will install OpenJDK:

    @metadata_processor
    def dnf(metadata):
        if node.has_bundle('dnf'):
            metadata.setdefault('dnf', {})
            metadata['dnf'].setdefault('extra_packages', [])
            for package in ['java-1.8.0-openjdk-headless']:
                if package not in metadata['dnf']['extra_packages']:
                    metadata['dnf']['extra_packages'].append(package)
        return metadata, DONE
