# coding: utf8

from selenium import webdriver
import time

def login():  # 自動ログイン
    url = 'ログイン対象のページ'
    email = 'メールアドレス'
    pw = 'パスワード'

    driver = webdriver.Chrome(executable_path='')  # Chromeのpathを""内に記載
    driver.get(url)

    # ID/PASSを入力
    driver.find_element_by_id("email部分の要素<id>").send_keys(email)
    driver.find_element_by_id("pw部分の要素<id>").send_keys(pw)

    time.sleep(1)

    # ログインボタンをクリック
    driver.find_element_by_id("ログインボタンの要素<id>").click()

if __name__ == '__main__':
    login()
