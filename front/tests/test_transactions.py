import pytest

from front.data_for_test.login_data import LoginData
from front.data_for_test.transactions_data import TransactionsData
from front.pages.login_page import LoginPage
from front.pages.transactions_page import TransactionsPage
from front.utils.assertions import AssertionHandler


@pytest.mark.usefixtures("setup")
class TestTransaction:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.transactions_page = TransactionsPage(self.driver)
        self.login_page = LoginPage(self.driver)
        login_data = LoginData.valid_login()[0]
        self.login_page.go_to_login_url(LoginData.get_page_url())
        self.login_page.login(login_data["username"], login_data["password"])

    @pytest.mark.parametrize('transactions_data', TransactionsData.successful_transaction_count())
    def test_successful_transaction_count(self, transactions_data):
        successful_transactions = self.transactions_page.count_successful_transactions()
        AssertionHandler.assert_equal(successful_transactions,
                                      transactions_data['transaction_count'])
