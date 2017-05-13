from Value import url
class login():
    def user_login(self,driver):
        driver.type("css=>#edit-name","王会娟")
        driver.type("css=>#edit-pass","123456")
        driver.click("css=>#edit-submit")

    def houqin_login(self,driver):
        driver.type("css=>#edit-name","houqin_hn")
        driver.type("css=>#edit-pass","abcd@1234")
        driver.click("css=>#edit-submit")

    def user_loginout(self,driver):
        driver.click("css=>.link-logout")
        driver.quit()

    def cash_list(self,driver):
        driver.click("css=>.link-cash.nolink")

    def distribution_plan_list(self,driver):
        driver.click("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[1]/span")

    def staff_management(self,driver):
        driver.click("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[7]/span")

    def transaction_mangen(self,driver):
        driver.click("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[8]/span")

