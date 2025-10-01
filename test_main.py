import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

 #фикстра авторизации
@pytest.fixture()
def authorization():
    browser = webdriver.Chrome()
    browser.get("http://localhost:8080/index")
    browser.maximize_window()

    browser.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("admin@mail.com")
    browser.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("admin")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    yield browser
    browser.quit()

 # проверка нашего тавара что карточка отрывается, тест-кейс1
def test_product(authorization):
    product = authorization
    product.find_element(By.CSS_SELECTOR, "a[href='/products/1']").click()
    h1_text = product.find_element(By.TAG_NAME, 'h1').text
    assert h1_text =='Информация о товаре'



