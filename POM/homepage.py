from object_repository.homepage_locators import HomePageLocators
home = HomePageLocators()

class HomePage:
    def __init__(self, driver):
        self.driver = driver
    def click_deposit(self):
        self.driver.find_element(*home.deposits).click()

    def click_fixed_deposit(self):
        self.driver.find_element(*home.fixed_deposits).click()

    def click_amount(self):
        self.driver.find_element(*home.amount).click()

    def click_interest(self):
        self.driver.find_element(*home.interest).click()

    def click_category(self):
        self.driver.find_element(*home.category).click()

    def click_next(self):
        self.driver.find_element(*home.next).click()

    def click_check(self):
        self.driver.find_element(*home.check).click()