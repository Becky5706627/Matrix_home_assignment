import pytest
from front.data_for_test.login_data import LoginData
from front.pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.page_url = LoginData.get_page_url()
        self.login_page.go_to_login_url(self.page_url)

    @pytest.mark.parametrize('valid_login', LoginData.valid_login())
    def test_valid_login(self, valid_login):
        self.login_page.login(valid_login['username'], valid_login['password'])
        self.login_page.verify_success_login(valid_login['redirected_page_url'])
        # log out
        self.login_page.go_to_login_url(self.page_url)
