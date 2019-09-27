# dep-pack

This utility will download all unique npm dependencies specified in a package-lock.json. Each dependency will be packaged into a tarball which can be uploaded into the repository manager like Nexus.

# usage
py main.py "./package-lock.json"
