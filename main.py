import json
import sys
import os

path = sys.argv[1]
packagesToDownload = set()
dependencyCount = 0

# Main routine
def main():
    if not os.path.isfile(path):
        print("File path {} does not exist. Exiting...".format(path))
        sys.exit()

    with open(path, 'r') as fp:
        data = json.load(fp)
        for name in data["dependencies"]:
            addDependency(name, data["dependencies"][name])
        for pkg in sorted(packagesToDownload):
            fetchNpmPackage(pkg)
        printResults()

# Adds the dependency and its required dependencies to the queue to package
def addDependency(name, meta):
    addToDownload(name, meta["version"])
    if "requires" in meta.keys():
        for pkg in meta["requires"]:
            addToDownload(pkg, meta["requires"][pkg])
    if "dependencies" in meta.keys():
        for pkg in meta["dependencies"]:
            addDependency(pkg, meta["dependencies"][pkg])

# Packs the specified package in a tarball
def fetchNpmPackage(pkg):
    #print(pkg)
    os.system("npm pack {}".format(pkg))

# Adds the package to the queue of packages to download
def addToDownload(name, version):
    global dependencyCount 
    dependencyCount += 1
    packagesToDownload.add("{}@{}".format(name, version))

def printResults():
    print("Found {} dependencies\nPackaging {} unique dependencies".format(dependencyCount, len(packagesToDownload)))

if __name__ == '__main__':
    main()