# Installed packages
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestAppE2E(unittest.TestCase):
    def setUp(self):
        # initialize the driver
        options = Options()
        s = Service("chromedriver-win64/chromedriver.exe")

        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.get("http://localhost:8501")

    def test_select_policy(self):
        """Test deleting an item from the list."""
        wait = WebDriverWait(self.driver, 10)  # wait for up to 10 seconds
        checkbox = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@role='checkbox']")))

        if not checkbox.is_selected():
            checkbox.click()

        assert checkbox.is_selected(), "The checkbox is not selected."
        meta_dashboard_locator = (
            By.XPATH, "//*[contains(text(), 'Meta Dashboard')]")
        metrics_text_locator = (
            By.XPATH, "//*[contains(text(), 'Metrics for Facebook and Instagram')]")

        # wait for the text to be present in the page
        meta_dashboard_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(meta_dashboard_locator)
        )

        metrics_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(metrics_text_locator)
        )

        assert 'Meta Dashboard' in meta_dashboard_text.text, "Meta Dashboard text not found on the page"
        assert 'Metrics for Facebook and Instagram' in metrics_text.text, "Metrics text not found on the page"
        input()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
