import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlsplit
from tqdm import tqdm
from tqdm.notebook import tqdm as tqdm_notebook
import os
import json
import pandas as pd
import time

class OAuthHandler:
    def __init__(self, login: str, password: str) -> str:
        self.driver = webdriver.Firefox()
        self.login_xpath = '/html/body/div/div/div/div[2]/form/div/div/input[6]'
        self.password_xpath = '/html/body/div/div/div/div[2]/form/div/div/input[7]'
        self.button_xpath = '//*[@id="install_allow"]'
        self.login = login
        self.password = password

    def auth(self, link):
        self.driver.get(link)
        try:
            email_field = self.driver.find_element_by_xpath(self.login_xpath)
            password_field = self.driver.find_element_by_xpath(self.password_xpath)

            email_field.send_keys(self.login)
            password_field.send_keys(self.password)

            self.driver.find_element_by_xpath(self.button_xpath).click()
        except:
            pass
        return self.driver.current_url

def get_token(APP_ID: int) -> str:
    login = input('Phone or email: ')
    password = input('Password: ')
    AUTH_URL = "https://oauth.vk.com/authorize?client_id={APP_ID}&display=page&response_type=token&v=5.103"
    response = OAuthHandler(login, password).auth(AUTH_URL.format(APP_ID=APP_ID))
    token = urlsplit(response, scheme='https').fragment.split('&')[0].split('=')[-1]
    return token

def get_single_leader(uid: str, access_token: str, attempt: int=5) -> dict:
    url_single_execute = f"https://api.vk.com/method/execute.singleLeader?user={{}}&access_token={access_token}&v=5.103"

    for i in range(attempt):
        response = requests.get(url_single_execute.format(uid)).json()
        if response.get('response'):
            return response
        print("Sleep")
        time.sleep(1)
    raise Exception(f"After {attempt} attempts no response!!!")

def save_single_leader(uid: str, path: str, access_token: str):
    data = get_single_leader(uid, access_token)
    assert len(data["response"]) == 3
    with open(f"{path}/{uid}.json", 'w') as f:
        f.write(json.dumps(data))

def main():
    savepath = input('Absolute path to directory to save to: ')
    userscsv_path = input('Absolute path to users.csv file: ')
    APP_ID = int(input('VK Standalone App ID: '))
    TOKEN = get_token(APP_ID)

    users = pd.read_csv(userscsv_path).uid
    debug_data = []
    for uid in tqdm(users):
        if not os.path.exists(savepath):
            os.makedirs(savepath)
        debug_data.append(save_single_leader(str(uid), savepath, TOKEN))

    with open('./debug_data.txt', encoding='utf-8', mode='w') as f:
        for dd in debug_data:
            f.write(dd+'\n')

if __name__=='__main__':
    main()
