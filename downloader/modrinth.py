from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import requests

def downloadModrinthMod(browser, url, version, path):
    filesUrl = f"{url}/versions?l=fabric&g={version}"

    print("> File Page url: " + filesUrl)
    print("> Starting page...")

    browser.get(filesUrl)

    print("> Page loaded")
    print("> Waiting for file declarations...")

    fileSearchResults = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "version-button"))
    )

    print("> Found file declarations")
    
    print("> Generatiog download url...")

    downloadUrl = f"{fileSearchResults[0].find_element(By.CLASS_NAME, 'download-button').get_attribute('href')}"

    print("> Download URL: " + downloadUrl)
    print("> Downloading file...")
    
    response = requests.get(downloadUrl)

    if response.status_code == 200:

        with open(path + "/" + downloadUrl.split("/")[-1], 'wb') as file:
            file.write(response.content)
        return True
    else:
        return False
