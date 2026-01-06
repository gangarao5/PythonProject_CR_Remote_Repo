# import pytest
import time

from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_ui_login_page():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    page = LoginPage(driver)
    page.open_url("https://www.flipkart.com/")
    time.sleep(5)
    title = page.get_title()
    print(title)
    assert "Online Shopping" in page.get_title()

    driver.quit()
