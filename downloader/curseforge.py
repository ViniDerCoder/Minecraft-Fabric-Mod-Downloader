from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import requests

def downloadCurseForgeMod(browser, url, version, path):
    filesUrl = f"{url}/files/all?page=1&pageSize=50&version={version}&gameVersionTypeId=4"

    print("> File Page url: " + filesUrl)
    print("> Starting page...")

    browser.get(filesUrl)

    print("> Page loaded")
    print("> Waiting for file declarations...")

    fileSearchResults = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "file-row-details"))
    )

    print("> Found file declarations")

    numOne = fileSearchResults[0].get_attribute("href").split("/")[-1][:4]
    numTwo = fileSearchResults[0].get_attribute("href").split("/")[-1][4:]

    versionValidation = version in list(
        map(lambda str: str.get_attribute("textContent"), 
            fileSearchResults[0].find_elements(By.CLASS_NAME, "tooltip-wrapper")[1]
            .find_element(By.CLASS_NAME, "tooltip-small")
            .find_elements(By.TAG_NAME, "li")
        )
    )
    
    if not versionValidation:
        print("> No matching version found")
        return False

    print("> Matching File ID: " + numOne + " " + numTwo)

    fileInfoUrl = f"{url}/files/{numOne}{numTwo}"

    print("> FileInfo Page url: " + fileInfoUrl)
    print("> Starting page...")

    browser.get(fileInfoUrl)

    print("> Page loaded")
    print("> Waiting for file name...")

    fileNameSection = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "section-file-name"))
    )[0]

    print("> Found file name section")

    fileName = fileNameSection.find_element(By.CLASS_NAME, "wrap").text

    print("> File Name: " + fileName)
    print("> Generatiog download url...")

    downloadUrl = f"https://mediafilez.forgecdn.net/files/{f'{numOne}/'.lstrip('0')}{f'{numTwo}/'.lstrip('0')}{fileName.replace('+', '%2B')}"

    print("> Download URL: " + downloadUrl)
    print("> Downloading file...")
    
    response = requests.get(downloadUrl)

    if response.status_code == 200:

        with open(path + "/" + fileName, 'wb') as file:
            file.write(response.content)
        return True
    else:
        return False
