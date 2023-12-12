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
        """Test the page of meta dashboard"""
        wait = WebDriverWait(self.driver, 10)  # wait for up to 10 seconds
        # wait for the span that visually represents the checkbox to be clickable
        checkbox_span = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "span[role='checkbox']")))

        # click the span to change the checkbox state
        checkbox_span.click()

        # verify that the aria-checked attribute is now 'true'
        assert "true" == checkbox_span.get_attribute(
            "aria-checked"), "Checkbox is not checked."

        # wait for the radio button that corresponds to "meta dashboard" to be present
        meta_dashboard_radio = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'input[type="radio"].st-b0')))

        # check if the radio button is selected
        is_meta_dashboard_radio_selected = meta_dashboard_radio.is_selected()

        assert is_meta_dashboard_radio_selected, "The Meta Dashboard radio button is not \
        selected."

        # check if the Meta Dashboard of the page is present
        meta_dashboard_locator = (
            By.XPATH, "//*[contains(text(), 'Meta Dashboard')]")

        # wait for the text to be present in the page
        meta_dashboard_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(meta_dashboard_locator)
        )

        assert 'Meta Dashboard' in meta_dashboard_text.text, "Meta Dashboard text not \
        found on the page"

        # check if the Metrics for Facebook and Instagram of the page is present
        metrics_text_locator = (
            By.XPATH, "//*[contains(text(), 'Metrics for Facebook and Instagram')]")
        metrics_like_text_locator = (
            By.XPATH, "//*[contains(text(), 'Likes')]")
        metrics_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(metrics_text_locator)
        )
        metrics_like_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(metrics_like_text_locator)
        )
        assert 'Metrics for Facebook and Instagram' in metrics_text.text, "Metrics text \
        not found on the page"
        assert 'Likes' in metrics_like_text.text, "Metrics text not found on the page"

        # check if the Advertisment Tendancy of the page is present
        tendancy_text_locator = (
            By.XPATH, "//*[contains(text(), 'Advertisment Tendancy')]")
        tendancy_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(tendancy_text_locator)
        )
        assert 'Advertisment Tendancy' in tendancy_text.text, "Advertisment Tendancy \
        text not found on the page"

        # check if there are 2 images in the page
        images = self.driver.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="stImage"]')
        assert len(images) == 2, "There should be 2 images in the page"

        # check if the Representation of the number of likes by cities
        representation_text_locator = (
            By.XPATH, "//*[contains(text(), 'Representation of the number of likes by cities')]")
        representation_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(representation_text_locator)
        )
        pie_chart = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'canvas.bk'))
        )
        assert 'Representation of the number of likes by cities' in \
            representation_text.text, "Representation of the number of likes by cities \
            text not found on the page"
        assert pie_chart is not None, "There should be at least 3 pie charts in the page"

        # check the Comparaison of the reach destribution Facebook Instagram August/Sep
        comparasion_text_locator = (
            By.XPATH, "//*[contains(text(), 'Comparaison of the reach destribution Facebook Instagram August/Sep')]")
        comparasion_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(comparasion_text_locator)
        )
        assert 'Comparaison of the reach destribution Facebook Instagram August/Sep' in \
            comparasion_text.text, "Comparaison of the reach destribution Facebook Instagram \
            August/Sep text not found on the page"

        # check the Representation 1 and Representation 2
        representation1_text_locator = (
            By.XPATH, "//*[contains(text(), 'Representation 1')]")
        representation2_text_locator = (
            By.XPATH, "//*[contains(text(), 'Representation 2')]")
        representation1_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(representation1_text_locator)
        )
        representation2_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(representation2_text_locator)
        )
        representations_graphs = self.driver.find_elements(
            By.CSS_SELECTOR, 'div.chart-wrapper')
        assert 'Representation 2' in representation2_text.text, "Representation 2 text \
        not found on the page"
        assert 'Representation 1' in representation1_text.text, "Representation 1 text \
        not found on the page"
        assert len(representations_graphs) == 2, "There should be 2 representations graphs \
        in the page"

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
