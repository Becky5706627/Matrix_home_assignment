from selenium.webdriver.common.by import By
from front.pages.base_page import BasePage


class LoginPage(BasePage):
    TITLE: tuple[By, str] = (By.TAG_NAME, "h4")
    INPUT_USERNAME: tuple[By, str] = (By.ID, "username")
    INPUT_PASSWORD: tuple[By, str] = (By.ID, "password")
    LOGIN_BUTTON: tuple[By, str] = (By.ID, "log-in")
    CHECKBOX: tuple[By, str] = (By.ID, "input[type='checkbox']")
    TOP_MENU: tuple[By, str] = (By.CSS_SELECTOR, "div.top-menu-controls")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def go_to_login_url(self, url: str) -> None:
        self.open_url(url)

    def enter_username(self, user_name: str) -> None:
        self.fill_input_filed(self.INPUT_USERNAME, user_name)

    def enter_password(self, password: str) -> None:
        self.fill_input_filed(self.INPUT_PASSWORD, password)

    def submit(self) -> None:
        self.click_element(self.LOGIN_BUTTON)

    def verify_success_login(self, redirected_page_url: str) -> None:
        assert self.get_current_url() == redirected_page_url, "Error: Login has failed."

    def login(self, user_name: str, password: str) -> None:
        if not self.is_user_logged_in():
            self.scroll_to_element(self.find_element(self.INPUT_USERNAME))
            self.enter_username(user_name)
            self.enter_password(password)
            self.submit()
        else:
            print("User already logged in")

    def is_user_logged_in(self) -> bool:
        top_menu = self.find_element(self.TOP_MENU, timeout=1, elem_none_if_no_found=True)
        return True if top_menu else False
