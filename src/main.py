import os
import argparse
from selenium import webdriver

def login(driver, room_address:str, username:str, password:str, guest:str, nickname:str):
    """login to skyroom"""
    driver.get(room_address)
    #check nickname option at login
    if nickname and driver.find_element_by_xpath('//*[@id="nickname"]').send_keys(nickname):
        driver.find_element_by_xpath().send_keys(nickname)
    #login with username and password or guest
    if username and password:
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        driver.find_element_by_xpath('//*[@id="btn_login"]').click()
    elif guest:
        driver.find_element_by_xpath('//*[@id="btn_guest"]').click()

def record_browser_tab(driver):
    """record video with ffmpeg from skyroom tab in chrome"""

def check_environment():
    """check environment variables are set or not"""
    if os.getenv('SKYROOM_ADDRESS') is None:
        return False
    else:
        if os.getenv('SKYROOM_USERNAME') and os.getenv('SKYROOM_PASSWORD') or os.getenv('SKYROOM_GUEST'):
            return True
        else:
            return False

def main():
    """main function"""
    parser = argparse.ArgumentParser()
    user_group = parser.add_mutually_exclusive_group()
    user_group.add_argument("-u", "--username", help="skyroom login username")
    user_group.add_argument("-p", "--password", help="skyroom login password")
    parser.add_argument("-r", "--room", help="skyroom room address")
    parser.add_argument("-g", "--guest", help="login as guest to skyroom", action='store_true')
    parser.add_argument("-n", "--nickname", help="nickname for account if allowed")
    args = parser.parse_args()
    driver = webdriver.Chrome()
    login(driver, args.room, args.username, args.password, args.guest, args.nickname)
    record_browser_tab(driver)

if __name__ == '__main__':
    main()
