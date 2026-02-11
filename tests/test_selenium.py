import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class TestCalculator:
    @pytest.fixture(scope="class")
    def driver(self):
        options = webdriver.ChromeOptions()

        # En CI, on force le headless
        if os.getenv("CI"):
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)  # Selenium Manager
        driver.implicitly_wait(5)
        yield driver
        driver.quit()

    def _open(self, driver):
        file_path = os.path.abspath("src/index.html")
        driver.get(f"file:///{file_path}")

    def test_page_loads(self, driver):
        self._open(driver)
        assert "Calculatrice Simple" in driver.title
        assert driver.find_element(By.ID, "num1").is_displayed()
        assert driver.find_element(By.ID, "num2").is_displayed()
        assert driver.find_element(By.ID, "operation").is_displayed()
        assert driver.find_element(By.ID, "calculate").is_displayed()

    def test_addition(self, driver):
        self._open(driver)
        driver.find_element(By.ID, "num1").clear()
        driver.find_element(By.ID, "num2").clear()
        driver.find_element(By.ID, "num1").send_keys("10")
        driver.find_element(By.ID, "num2").send_keys("5")

        select = Select(driver.find_element(By.ID, "operation"))
        select.select_by_value("add")

        driver.find_element(By.ID, "calculate").click()

        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )
        assert "Résultat: 15" in result.text

    def test_division_by_zero(self, driver):
        self._open(driver)
        driver.find_element(By.ID, "num1").clear()
        driver.find_element(By.ID, "num2").clear()
        driver.find_element(By.ID, "num1").send_keys("10")
        driver.find_element(By.ID, "num2").send_keys("0")

        select = Select(driver.find_element(By.ID, "operation"))
        select.select_by_value("divide")

        driver.find_element(By.ID, "calculate").click()

        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )
        assert "Erreur: Division par zéro" in result.text

    def test_all_operations(self, driver):
        self._open(driver)

        operations = [
            ("add", "8", "2", "10"),
            ("subtract", "8", "2", "6"),
            ("multiply", "8", "2", "16"),
            ("divide", "8", "2", "4"),
        ]

        for op, n1, n2, expected in operations:
            driver.find_element(By.ID, "num1").clear()
            driver.find_element(By.ID, "num2").clear()
            driver.find_element(By.ID, "num1").send_keys(n1)
            driver.find_element(By.ID, "num2").send_keys(n2)

            Select(driver.find_element(By.ID, "operation")).select_by_value(op)
            driver.find_element(By.ID, "calculate").click()

            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "result"))
            )
            assert f"Résultat: {expected}" in result.text
