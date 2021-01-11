from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import random

def createItem():
    create = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[1]/div/div[1]/div/div[3]/div[1]/div[2]/div/div/div[6]/div/span/a")))
    create.click()

    item = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div[1]/span/div/a")))
    item.click()

def tab():
    actions = ActionChains(browser) 
    actions.send_keys(Keys.TAB).perform()

def click():
    elem = browser.switch_to.active_element
    elem.click()
    time.sleep(0.5)

def send(keys):
    elem = browser.switch_to.active_element
    elem.send_keys(keys)
    time.sleep(0.5)

def down():
    actions = ActionChains(browser) 
    actions.send_keys(Keys.DOWN).perform()

def enter():
    actions = ActionChains(browser) 
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

def post(first, imgs, title, price, description, location):
    addImage = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div")))
    addImage.click()
    time.sleep(1.5)
    pyautogui.write(imgs)
    pyautogui.press('enter')
    time.sleep(0.125)
    titleInput = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/div[2]/div/div/label/div/div/input")))
    titleInput.send_keys(title)
    priceInput = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/div[3]/div/div/label/div/div/input")))
    priceInput.send_keys(price)
    category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/div[4]/div/div/div/label/div/div[1]/div/div")))
    category.click()
    furniture = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div[2]/div[1]/div/div[4]/div/div/div[1]/div[1]/div/div/div/div/div[3]/div/div[1]/div/div")))
    furniture.click()
    condition = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/div[5]/div/div/div/label/div/div[1]/div/div")))
    condition.click()
    used = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div[2]/div[1]/div/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/span")))
    used.click()
    for i in range(4):
        tab()
    if first:
        descriptionInput = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/div[2]/div/div[2]/div[8]/div/div/label/div/div/textarea")))
        descriptionInput.send_keys(description)
        descriptionInput.send_keys(Keys.CONTROL, 'a')
        descriptionInput.send_keys(Keys.CONTROL, 'c')
    else:
        descriptionInput = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/div[2]/div/div[2]/div[8]/div/div/label/div/div/textarea")))
        descriptionInput.send_keys(Keys.CONTROL, 'v')
    tab()
    locationInput = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/div[2]/div/div[2]/div[9]/div/div/div/div/div/div/div/label/div/div[2]/input")))
    locationInput.send_keys(location)
    zipcode = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[1]/div/ul/li[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/span")))
    zipcode.click()
    time.sleep(500)
    publish = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div[5]/div")))
    publish.click()

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("start-maximized")
usernameStr = "" # Enter username of account
passwordStr = "" # Enter passowrd of account

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get(('https://www.facebook.com/?stype=lo&jlou=Afd49KfzrAchGSYUEySQMjwDpNyn822XLiydplvRukwkAVFiSpN50hBRWPG0zKrjx-5ML-kYJ_HRv_OhdvOIK9vCVQ3V7X6otp78lI5DlrNdGA&smuh=10249&lh=Ac_G89whAREG6zRo'))

wait = WebDriverWait(browser, 10)
username = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
username.send_keys(usernameStr)
password = wait.until(EC.element_to_be_clickable((By.ID, 'pass')))
password.send_keys(passwordStr)
login = wait.until(EC.element_to_be_clickable((By.ID, 'u_0_b')))
login.click()

marketplace = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/a")))
marketplace.click()

create = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/div/div/div[5]/div/span/a")))
create.click()

item = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div[1]/span/div/a")))
item.click()

arr = []
for i in range(1, 50):
    arr.append(i)
random.shuffle(arr)

titles = [] # Enter the title(s) of your desire
title = "" # Initial post title
prices = []  # Enter the price(s) of your desire
price = 0 # Initial price
description = "" # Enter desired description for the post
imgs = "" # Enter the path to the image desired to post
location = 0 # Initial zip-code
post(True, imgs, title, price, description, location)
locations = [] # Enter any other locations to post in
createItem()
for i in range(1, int(len(locations)/5)):
    for j in range(5):
        imgs = "" + str(arr[0]) + ".jpg" # Enter the path to the folder that contains the images
        location = locations[i]
        price = prices[j % 10]
        title = titles[j % 5]
        if location == 10468:
            continue
        post(False, imgs, title, price, description, location)
        createItem()
        arr.pop(0)
