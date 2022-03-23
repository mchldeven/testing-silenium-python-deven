from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver .get('https://google.co.id')
    yield driver
    driver.quit()


def test_googling(driver):
    
    driver.find_element_by_name('q').send_keys('Michael Deven' + Keys.ENTER)
    assert 'Michael Deven' in driver.find_element_by_css_selector('h3').text
    assert 'Michael Deven' == driver.tittle
    