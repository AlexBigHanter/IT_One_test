import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_main import authorization

def test_admin(authorization):
    admin = authorization
    admin.find_element(By.CSS_SELECTOR, "button[onclick=\"location.href='/admin'\"]").click()
    h2_text = admin.find_element(By.XPATH, "/html/body/h2").text
    assert h2_text == 'Админ-панель'
    # print(h2_text)

