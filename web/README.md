# Example basic file server

File server for install-time artifacts. Run it somewhere with a static IP

This is to support the scripts in the current repo, so that they may have a location to target.

Suggested layout - place files down a `bin/<product-name>/<version>/<actual-file>` path

```
web/htdocs/
└── bin
    ├── rustdesk
    │   └── 1.4.2
    │       └── rustdesk-1.4.2-x86_64.deb
    └── solarwinds
        └── 2.0.27
            └── Solarwinds_Discovery_Agent_2.0.27_2.0.10_1138_210_installer.tar.gz
```

These can be referenced directly by scripts. Remember to also take the sha256 hash of the binary and use it in the install script to validate the download.
