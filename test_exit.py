import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_main import authorization
import allure


# кнопка Выйти , тест-кейс №5
@allure.feature("кнопка Выйти")
@allure.story('кнопка Выйти')
def test_exit(authorization):
    exit = authorization
    exit.find_element(By.CSS_SELECTOR, "input[value='Выйти']").click()
    h3_text = exit.find_element(By.XPATH, "/html/body/form/h3").text
    assert h3_text == 'Логин'
    # print(h3_text)