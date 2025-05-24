import re, os

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from downloadMod import downloadMod, startBrowser 
import sys

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.yml")
    
    stream = open(config_path, 'r')
    configDict = load(stream, Loader)

    if len(sys.argv) > 1 and sys.argv[1]:
        configDict["Output"]["path"] = sys.argv[1]

    version = input("Enter Minecraft Version: ")

    if not re.match(r"^\d+\.\d+\.\d+$", version):
        print("Invalid version format. Please use the format x.x.x")
        exit()

    if version.endswith(".0"):
        version = version[:-2]

    input("Press Enter to start download for version " + version)

    
    output = configDict.get("Output")
    output_path = output.get("path")

    if not os.path.isabs(output_path):
        output_path = os.path.join(script_dir, output_path)

    fullPath = os.path.join(output_path, output.get("folderName").replace("%version%", version))

    print("Using specified output directory: " + fullPath)
    
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    
    browserPaths = configDict.get("Browser")

    if browserPaths.get("path") and not os.path.isabs(browserPaths.get("path")):
        browserPaths["path"] = os.path.join(script_dir, browserPaths.get("path"))
    if browserPaths.get("servicePath") and not os.path.isabs(browserPaths.get("servicePath")):
        browserPaths["servicePath"] = os.path.join(script_dir, browserPaths.get("servicePath"))
        
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