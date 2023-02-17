# Implementation of Selenium WebDriver with Python using PyTest
# Для запуска тестов необходимо загрузить Selenium WebDriver с https://chromedriver.chromium.org/downloads
# (версию, совместимую с используемым браузером)
# запускать командой pytest test_visa.py --verbose --capture=no в терминале


import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

import pytest
import selenium
from selenium import webdriver
import sys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from time import sleep


def test_visa_statuse():
    chrome_driver = webdriver.Chrome()

    chrome_driver.get('https://frs.gov.cz/en/ioff/application-status')
    chrome_driver.maximize_window()
    sleep(1)
    field = chrome_driver.find_element("id", "edit-ioff-zov")
    field.send_keys('BELG202211150001')
    button_verify = chrome_driver.find_element("id", "edit-submit-button")
    button_verify.click()
    sleep(1)
    result = chrome_driver.find_element("xpath", "/html/body/div[2]/div/section/div[1]/ul/li[1]/p/span/strong")
    assert "In Process" in result.text
    chrome_driver.close()


