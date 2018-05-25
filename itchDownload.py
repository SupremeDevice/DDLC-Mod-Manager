from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from six.moves.urllib.request import urlretrieve
import glob, os, re, sys, time, zipfile, shutil, configparser, platform, tarfile

curOS = platform.system()
is64 = platform.machine().endswith('64')

print("itchDl.py started")
dragNDrop = ''.join(sys.argv[1:])
done = False
owd = os.getcwd()
if not os.path.exists(os.environ['temp'] + "\itchiotempdir"):
    os.makedirs(os.environ['temp'] + "\itchiotempdir")
downloadDir = os.environ['temp'] + "\itchiotempdir"

#Check whether to use chrome or firefox
config = configparser.ConfigParser(allow_no_value=True)
config.read('config.ini')
curBr = config['DEFAULT']['dlBrowser']
print("curBr is " + curBr)
drv = False



if os.path.isfile(curBr + '.ini'):
    ini = open(curBr + '.ini', 'r')
    locationString = ini.read()
    drv = True
else:
    if curBr == "Chrome":
        if os.path.isfile('chromedriver.exe'):
            locationString = 'chromedriver.exe'
            drv = True
        if os.path.isfile('chromedriver'):
            locationString = 'chromedriver'
            drv = True
    elif curBr == "Firefox":
        if os.path.isfile('geckodriver.exe'):
            locationString = 'geckodriver.exe'
            drv = True
        if os.path.isfile('geckodriver'):
            locationString = 'geckodriver'
            drv = True
if drv == False:#Download browser driver if needed
    print("Driver not found, attempting to download automatically...")
    if curBr == "Chrome":
        if curOS == "Windows":
            response = urlretrieve('https://chromedriver.storage.googleapis.com/2.38/chromedriver_win32.zip','driver.zip')
            locationString = 'chromedriver.exe'
        elif curOS == "Linux":
            response = urlretrieve('https://chromedriver.storage.googleapis.com/2.38/chromedriver_linux64.zip','driver.zip')
            locationString = 'chromedriver'
        elif curOS == "Darwin":
            response = urlretrieve('https://chromedriver.storage.googleapis.com/2.38/chromedriver_mac64.zip','driver.zip')
            locationString = 'chromedriver'
    else:#Get drivers for firefox instead
        if curOS == "Windows":
            locationString = 'geckodriver.exe'
            if is64 == True:
                response = urlretrieve('https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-win64.zip','driver.zip')
            else:
                response = urlretrieve('https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-win32.zip','driver.zip')
        elif curOS == "Linux":
            locationString = 'geckodriver'
            if is64 == True:
                response = urlretrieve('https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz','driver.tar.gz')
            else:
                response = urlretrieve('https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux32.tar.gz','driver.tar.gz')
        elif curOS == "Darwin":
            locationString = 'geckodriver'
            response = urlretrieve('https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-macos.tar.gz','driver.tar.gz')
    if os.path.isfile('driver.zip'):
        zip_ref = zipfile.ZipFile("driver.zip", 'r')
        zip_ref.extractall(owd)
        zip_ref.close
        os.remove('driver.zip')
    elif os.path.isfile('driver.tar.gz'):
        tar = tarfile.open(fname, "r:gz")
        tar.extractall(owd)
        tar.close()
        os.remove('driver.tar.gz')
    else:
        print("woops, looks like driver didn't download!")


if curBr == "Chrome":
    print("setting up chrome")
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : downloadDir}
    chromeOptions.add_experimental_option("prefs",prefs)

#    if os.path.isfile('chrome.ini'):
#        ini = open('chrome.ini', 'r')
#        locationString = ini.read()
#    elif os.path.isfile('chromedriver.exe'):
#        locationString = 'chromedriver.exe'
#    else:
#        response = urlretrieve('https://chromedriver.storage.googleapis.com/2.33/chromedriver_win32.zip','chromedriver.zip')
#        zip_ref = zipfile.ZipFile("chromedriver.zip", 'r')
#        zip_ref.extractall(owd)
#        zip_ref.close
#        locationString = 'chromedriver.exe'
    driver = webdriver.Chrome(executable_path=(locationString), chrome_options=chromeOptions)
else:#Launches firefox driver instead if chrome was not selected
    print("setting up firefox")
    geckoPath = os.path.join(owd, locationString)
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", downloadDir)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

    driver = webdriver.Firefox(executable_path = geckoPath, firefox_profile = profile)


driver.set_window_position(9000, 10000)
driver.set_page_load_timeout(600)





if os.path.isfile("repo.ini"):
    with open ("repo.ini", "r") as myfile:
        fullURL = myfile.read()
        doubSlash = fullURL.index("//")
        ioSlash = fullURL.index("io/")
        gameName = fullURL[ioSlash+3:]
        teamName = fullURL[doubSlash+2:ioSlash-6]
elif dragNDrop == "":
    teamName = raw_input("\nInput the Team Name\n>")
    gameName = raw_input("\nInput the Game Name\n>")
else:
    doubSlash = dragNDrop.index("//")
    ioSlash = dragNDrop.index("io/")
    gameName = dragNDrop[ioSlash:]
    teamName = dragNDrop[doubSlash:ioSlash-6]

siteString = "https://" + teamName + ".itch.io/" + gameName

driver.get(siteString)
print("Attempting to open website")

driver.find_element_by_xpath("//a[@class='button buy_btn']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='direct_download_btn']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='button download_btn']").click()
time.sleep(2)

if curBr == "Chrome": #Check for game to finish downloading when using
    while done == False:
        for fname in os.listdir(downloadDir):
            if fname.endswith('.zip'):
                done = True
else: #Alternate code for checking if DL is done when using Firefox
    while done == False:
        os.chdir
        gameVer = "ddlc-win.zip.part"
        if os.path.isfile(os.path.join(downloadDir, gameVer)) == False:
            done = True

print("Download complete, extracting...")

os.chdir(downloadDir)
for file in glob.glob("*.zip"):
    zipFile = file

zip_ref = zipfile.ZipFile(zipFile, 'r')
zip_ref.extractall(os.path.join(owd, "temp"))
zip_ref.close
print("Extraction complete")

time.sleep(2)
driver.quit()
print("Closing driver...")
time.sleep(2)
print("Attempting to delete temp folder...")
try:
    shutil.rmtree(downloadDir)
    print("Temporary directory removed")
except PermissionError:
    print("Can't delete temporary DL directory")
