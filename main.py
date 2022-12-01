import sys
import time
import urllib.request

import pydub
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os
import speech_recognition as sr

os.environ['PATH'] += r"C:\Users\SL LAPTOP\PycharmProjects\pythonProject/chromedriver.exe"
driver = webdriver.Chrome()
driver.get('https://www.google.com/recaptcha/api2/demo')
time.sleep(2)
iframe1=driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
time.sleep(2)
box = driver.find_element(By.XPATH,'//*[@id="recaptcha-anchor"]').click()
time.sleep(2)
if driver.find_element(By.XPATH,'//*[@id="recaptcha-anchor"]/div[3]').is_selected():
    print('Run the further script you want')
    time.sleep(2)
else:
    time.sleep(1)
    driver.switch_to.default_content()
    iframe2 = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/iframe')#https://www.google.com/recaptcha/api2/bframe?hl
    driver.switch_to.frame(iframe2)
    print(driver.title)
    time.sleep(1)
    sound = driver.find_element(By.XPATH, '//*[@id="recaptcha-audio-button"]').click()
    time.sleep(2)
    download = driver.find_element(By.XPATH,'//*[@id="rc-audio"]/div[7]/a') #RC audio betrayed Need to click the hyper link of play.
    #Change the driver by using the URL of SRC download or either play
    time.sleep(2)
    #Download Audio File
    src = driver.find_element(By.ID, "audio-source").get_attribute("src")
    print(f"[INFO] Audio src: {src}")

    path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), "sample.mp3"))
    path_to_wav = os.path.normpath(os.path.join(os.getcwd(), "sample.wav"))

    # download the mp3 audio file from the source
    urllib.request.urlretrieve(src, path_to_mp3)
    #I couldn't find the
    driver.get('https://speech-to-text-demo-nlu.mybluemix.net/')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[5]/button[2]')

    try:
        sound = pydub.AudioSegment.from_mp3(path_to_mp3)
        sound.export(path_to_wav, format="wav")
        sample_audio = sr.AudioFile(path_to_wav)
    except Exception:
        sys.exit(
            "[ERR] Please run program as administrator or download ffmpeg manually, "
            "https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/")

    r = sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)
    key = r.recognize_google(audio)
    print(f"[INFO] Recaptcha Passcode: {key}")

    driver.find_element(By.ID,"audio-response").send_keys(key.lower())
    driver.find_element(By.ID,"audio-response").send_keys(Keys.ENTER)
    time.sleep(5)
    driver.switch_to.default_content()
    time.sleep(5)
    driver.find_element(By.ID, "recaptcha-demo-submit").click()
