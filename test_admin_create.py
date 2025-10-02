import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@pytest.fixture()
def authorization2():
    browser = webdriver.Chrome()
    browser.get("http://localhost:8080/index")
    browser.maximize_window()

    browser.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("admin@mail.com")
    browser.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("admin")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    browser.find_element(By.CSS_SELECTOR, "button[onclick=\"location.href='/admin'\"]").click()
    yield browser
    browser.quit()


# кнопка создания пользователя тест-кейс №1
@allure.feature("Админка")
@allure.story('Создания пользователя')
def test_admin_create(authorization2):
    create = authorization2
    create.find_element(By.CSS_SELECTOR, "button[onclick=\"window.location.href='/users/new'\"]").click()
    email = create.find_element(By.CSS_SELECTOR, "label[for='email']").text
    assert email == 'Эл. почта:'
    # print(email)


# кнопка (админ-понель) тест-кейс №2
@allure.feature("Админка")
@allure.story('Кнопка админ-понель')
def test_admin(authorization2):
    admin = authorization2
    admin.find_element(By.CSS_SELECTOR, "button[onclick=\"location.href='/admin'\"]").click()
    h2_text = admin.find_element(By.XPATH, "/html/body/h2").text
    assert h2_text == 'Админ-панель'
    # print(h2_text)
