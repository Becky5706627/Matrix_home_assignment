import pytest

from front.data_for_test.login_data import LoginData
from front.data_for_test.transactions_data import TransactionsData
from front.pages.login_page import LoginPage
from front.pages.transactions_page import TransactionsPage
from front.utils.assertions import AssertionHandler


@pytest.mark.usefixtures("setup")
class TestTransaction:

    @pytest.fixture(scope="class", autouse=True)
    def transactions_page_setup(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        login_data = LoginData.valid_login()[0]
        login_page.go_to_login_url(LoginData.get_page_url())
        login_page.login(login_data["username"], login_data["password"])
        transactions_page = TransactionsPage(driver)
        return transactions_page

    @pytest.mark.parametrize('transactions_data', TransactionsData.successful_transaction_count())
    def test_successful_transaction_count(self, transactions_page_setup, transactions_data):
        successful_transactions = transactions_page_setup.count_successful_transactions()
        AssertionHandler.assert_equal(successful_transactions,
                                      transactions_data['transaction_count'])

