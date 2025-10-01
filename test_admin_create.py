import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


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

def test_admin_create(authorization2):
    create = authorization2
    create.find_element(By.CSS_SELECTOR, "button[onclick=\"window.location.href='/users/new'\"]").click()
    email = create.find_element(By.CSS_SELECTOR, "label[for='email']").text
    assert email == 'Эл. почта:'
    # print(email)