import os
from typing import Dict
from front.utils.helper import Helper


class LoginData:
    ROOT_DIR: str = os.path.dirname(os.path.abspath(__file__))
    config_file_path: str = os.path.join(ROOT_DIR, "test_data.json")
    config_file: str = Helper.load_file(config_file_path)
    login_data: dict = Helper.get_config_value_by_name(config_file, ['login_data'])

    @staticmethod
    def get_page_url() -> str:
        return Helper.get_config_value_by_name(LoginData.login_data, ['url'])

    @staticmethod
    def valid_login() -> list[Dict]:
        user_data: dict = Helper.get_config_value_by_name(LoginData.login_data, ['user_data'])
        page_url = LoginData.get_page_url()
        redirected_page_url = f'{page_url}app.html'
        return [{"username": user_data['username'], "password": user_data['password'],
                 "redirected_page_url": redirected_page_url,
                 "page_url": page_url}]
