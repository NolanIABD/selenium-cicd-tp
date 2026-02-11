import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)  # Selenium Manager gère le driver
    yield driver
    driver.quit()

def test_addition(driver):
    file_path = os.path.abspath("src/index.html")
    driver.get(f"file:///{file_path}")

    driver.find_element(By.ID, "num1").send_keys("5")
    driver.find_element(By.ID, "num2").send_keys("3")

    # Sélection de l'addition (plus robuste que send_keys sur <select>)
    select = driver.find_element(By.ID, "operation")
    select.find_element(By.CSS_SELECTOR, "option[value='add']").click()

    driver.find_element(By.ID, "calculate").click()
    time.sleep(0.5)

    result = driver.find_element(By.ID, "result").text
    assert "8" in result