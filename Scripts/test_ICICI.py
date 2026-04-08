from POM.homepage import HomePage

from time import sleep


def test_case(setup):
   hp = HomePage(setup)

   hp.click_deposit()
   sleep(2)
   hp.click_fixed_deposit()
   sleep(2)
   hp.click_amount()
   sleep(2)
   hp.click_interest()
   sleep(2)
   hp.click_category()
   sleep(2)
   hp.click_next()
   sleep(2)
   hp.click_check()
   sleep(2)
