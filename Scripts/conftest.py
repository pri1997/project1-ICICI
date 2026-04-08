import pytest
from selenium.webdriver import Chrome
from time import sleep




@pytest.fixture()
def setup():
   driver=Chrome()
   driver.maximize_window()
   driver.get("https://www.icici.bank.in/")
   sleep(4)
   yield driver
   driver.close()