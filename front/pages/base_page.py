from typing import Any, Optional, List

from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def click_element(self, locator: tuple[By, str], timeout: int = 10) -> None:
        element = self.wait_for_element_to_be_clickable(locator, timeout)
        element.click()

    @staticmethod
    def click(element: WebElement) -> None:
        try:
            element.click()
        except ElementClickInterceptedException as e:
            raise Exception(f"Error: Element is not clickable as it is obscured: {e}")
        except ElementNotInteractableException as e:
            raise Exception(f"Error: Element is not interactable: {e}")
        except StaleElementReferenceException as e:
            raise Exception(f"Error: Element is no longer attached to the DOM: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _find(self, condition: Any, locator: tuple[By, str], timeout: int, exception_message: str,
              elem_none_if_no_found: bool = False) -> Optional[WebElement] | None:
        try:
            return WebDriverWait(self.driver, timeout).until(condition(locator))
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            if elem_none_if_no_found:
                return None
            else:
                raise Exception(exception_message)

    def find_element(self, locator: tuple[By, str], timeout: int = 60,
                     elem_none_if_no_found: bool = False) -> Optional[WebElement]:
        return self._find(EC.presence_of_element_located, locator, timeout, "Element not found or timed out",
                          elem_none_if_no_found)

    def find_elements(self, locator: tuple[By, str], timeout: int = 60,
                      elem_none_if_no_found: bool = False) -> List[WebElement] | None:
        return self._find(EC.presence_of_all_elements_located, locator, timeout, "Elements not found or timed out",
                          elem_none_if_no_found)

    @staticmethod
    def find_element_within(parent_element: WebElement, search_param: str, search_type=By.CSS_SELECTOR,
                            timeout: int = 10,
                            elem_none_if_no_found=False) -> Optional[WebElement]:
        try:
            element = WebDriverWait(parent_element, timeout).until(
                EC.presence_of_element_located((search_type, search_param))
            )
            return element
        except TimeoutException:
            if elem_none_if_no_found:
                return
            raise TimeoutException(
                f"Could not find element with search parameter '{search_param}' within {parent_element}")

    def wait_for_element_to_be_clickable(self, locator: tuple[By, str], timeout: int = 60) -> WebElement:
        return self._find(EC.element_to_be_clickable, locator, timeout, "Timed out waiting for element to be clickable")

    def wait_for_element(self, locator: tuple[By, str], timeout: int = 60,
                         elem_none_if_no_found: bool = False) -> Optional[WebElement]:
        return self._find(EC.visibility_of_element_located, locator, timeout,
                          f"Timed out waiting for element locator: {locator}",
                          elem_none_if_no_found)

    def get_element_text(self, locator: tuple[By, str], timeout: int = 60) -> str:
        element = self.wait_for_element(locator, timeout)
        return element.text

    @staticmethod
    def get_text(element) -> str:
        return element.text

    def is_element_present(self, locator: tuple[By, str], timeout=5) -> bool:
        element = self.find_element(locator, timeout, elem_none_if_no_found=True)
        return element is not None

    def fill_input_filed(self, locator: tuple[By, str], text: str, timeout: int = 10) -> None:
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_attribute_value(self, locator: tuple[By, str], attribute: str, timeout: int = 10) -> str:
        element = self.wait_for_element(locator, timeout)
        return element.get_attribute(attribute)

    @staticmethod
    def get_attribute_value_from_element(element: WebElement, attribute: str) -> str:
        return element.get_attribute(attribute)

    def scroll_to_element(self, element: WebElement) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
