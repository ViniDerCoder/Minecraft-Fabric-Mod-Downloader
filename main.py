import re, os

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from downloadMod import downloadMod, startBrowser 

if __name__ == '__main__':

    stream = open("config.yml", 'r')
    configDict = load(stream, Loader)

    version = input("Enter Minecraft Version: ")

    if not re.match(r"^\d+\.\d+\.\d+$", version):
        print("Invalid version format. Please use the format x.x.x")
        exit()

    if version.endswith(".0"):
        version = version[:-2]

    input("Press Enter to start download for version " + version)

    
    output = configDict.get("Output")
    fullPath = output.get("path") + "/" + output.get("folderName").replace("%version%", version)

    print("Using specified output directory: " + fullPath)
    
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    
    browserPaths = configDict.get("Browser")
    driver = startBrowser(browserPaths.get("path"), browserPaths.get("servicePath"))


    failedDownloads = []

    for site in configDict.get("Mods"):
        for modSiteName, modSiteData in site.items():
            for mod in modSiteData["mods"]:
                if not downloadMod(driver, modSiteName, modSiteData["baseurl"] + "/" + mod["id"], mod["name"], version, fullPath):
                    failedDownloads.append(mod["name"])

    print("")
    print("Download of all mods finished.")
    if len(failedDownloads) > 0:
        print("Failed to download the following mods:")
        for mod in failedDownloads:
            print("- " + mod)
    else:
        print("All mods downloaded successfully.")