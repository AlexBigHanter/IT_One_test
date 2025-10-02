import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_main import authorization
import allure

# кнопка Корзина , тест-кейс №4
@allure.feature("Раздел корзина")
@allure.story('проверка кнопки Корзина')
def test_cart(authorization):
    cart = authorization
    cart.find_element(By.CSS_SELECTOR, "button[onclick=\"location.href='/cart'\"]").click()
    h2_text = cart.find_element(By.XPATH, "/html/body/h2" ).text
    assert h2_text == 'Корзина пуста'