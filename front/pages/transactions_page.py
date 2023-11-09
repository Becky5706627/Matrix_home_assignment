from selenium.webdriver.common.by import By
from front.pages.base_page import BasePage


class TransactionsPage(BasePage):
    TRANSACTIONS_TABLE: tuple[By, str] = (By.CSS_SELECTOR, "tbody>tr")
    SUCCESS_STATUS: str = 'Complete'

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def count_successful_transactions(self) -> int:
        rows = self.get_transactions_table()
        return sum(1 for row in rows if self.SUCCESS_STATUS in row.text)

    def get_transactions_table(self) -> list:
        return self.find_elements(self.TRANSACTIONS_TABLE)
