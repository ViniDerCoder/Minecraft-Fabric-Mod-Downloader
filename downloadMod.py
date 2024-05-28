from downloader.curseforge import downloadCurseForgeMod
from downloader.modrinth import downloadModrinthMod
from downloader.github import downloadGitHubMod

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def startBrowser(browserPath, servicePath):
    print("Starting browser...")
    
    options = Options()
    options.binary_location = browserPath
    
    options.add_argument('-headless')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537')
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options, service=Service(servicePath))
    print("Browser started")
    return driver

def downloadMod(driver, site, url, modName, minecraftVersion, path):
    print("")
    print("Downloading mod: " + modName + " from " + site)
    print("URL: " + url)
    print("Minecraft Version: " + minecraftVersion)

    success = False

    match site:
        case "curseforge":
            print("Downloading from CurseForge")

            success = downloadCurseForgeMod(driver, url, minecraftVersion, path)

        case "modrinth":
            print("Downloading from Modrinth")

            success = downloadModrinthMod(driver, url, minecraftVersion, path)

        case "github":
            print("Downloading from GitHub")

            success = downloadGitHubMod(driver, url, minecraftVersion, path)

    if not success:
        print("Failed to download " + modName)
        return False
    else:
        print("Download complete")
        return True