from typing import Dict


class TransactionsData:

    @staticmethod
    def successful_transaction_count() -> list[Dict]:
        return [{"transaction_count": 2}]
