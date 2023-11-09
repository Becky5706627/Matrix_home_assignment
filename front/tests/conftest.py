import os
from pytest import fixture
from front.utils.driver_manager import DriverManger

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


@fixture(autouse=True, scope="session")
def setup():
    driver = DriverManger.get_driver()
    DriverManger.maximized_window(driver)
    yield driver
    driver.quit()
