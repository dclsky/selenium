from pyse import Pyse, TestRunner
from time import sleep
from Value import url,order_date,identity_card_tangshi,identity_card_waimai,select_date,order_date_test,estimate_date,transaction_date
from Login import login
from nose.tools import with_setup
from selenium.webdriver.common.keys import Keys
import time
import unittest

class ErpTest(unittest.TestCase):

    def my_setup_function(self):
        print("test case start")

    def my_teardown_function(self):
        print("test case end")
#_login
    def test_1(self):

        ''' erp-login search key : pyse '''

        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400, 1400)
        driver.open("%s" %(url()))
        driver.F5()
        login().user_login(driver)
        driver.element_wait("css=>.logo",10)
        print("After login==================")
        title=driver.get_title()
        print(title)
        now_url=driver.get_url()
        print(now_url)
        user=driver.get_text("css=>#block-block-1>a")
        print(user)
        login().user_loginout(driver)
        driver.quit()

#_cash_other
    @with_setup(my_setup_function, my_teardown_function)
    def test_2(self):

        ''' erp-cash search key : pyse '''

        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400, 1400)
        driver.open("%s" % (url()))
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        login().cash_list(driver)
        driver.click("css=>.first.leaf.menu-mlid-4793>a")
        cash_other_income = driver.get_text("css=>.first.leaf.menu-mlid-4793>a")
        print(cash_other_income)
        driver.click("xpath=>.//*[@id='content']/div/div[1]/div/ul/li/a")
        other_cash_url = driver.get_url()
        print(other_cash_url)
        driver.get_display("css=>.navbar-title")
        driver.type("xpath=>.//*[@id='otherincome-form']/div/table[2]/tbody/tr[1]/td[3]/div/input", "101")
        driver.type("xpath=>.//*[@id='otherincome-form']/div/table[2]/tbody/tr[1]/td[4]/div/input", "2")
        driver.is_option_value_present("method[197]","option","value")
        driver.type("xpath=>.//*[@id='otherincome-form']/div/table[2]/tbody/tr[1]/td[6]/div/input", u"其他")

        driver.type("xpath=>.//*[@id='otherincome-form']/div/table[2]/tbody/tr[2]/td[3]/div/input", "102")
        driver.type("xpath=>.//*[@id='otherincome-form']/div/table[2]/tbody/tr[2]/td[4]/div/input", "1")
        driver.type("xpath=>.//*[@id='otherincome-form']/div/table[2]/tbody/tr[2]/td[6]/div/input", u"废品")

        driver.type("xpath=>.//*[@id='otherincome-form']/div/table[2]/tbody/tr[3]/td[3]/div/input", "103")
        driver.type("xpath=>.//*[@id='otherincome-form']/div/table[2]/tbody/tr[3]/td[4]/div/input", "3")
        driver.type("xpath=>.//*[@id='otherincome-form']/div/table[2]/tbody/tr[3]/td[6]/div/input", u"废料")

        driver.click("xpath=>.//*[@id='edit-submit']")
        number = driver.get_text("xpath=>.//*[@id='content']/div/div[2]/table/tbody/tr[1]/td[3]")
        if number == u"101.00":
            print(u"其他收入录入金额101正确")
        else:
            print(u"校验失败")
        self.assertTrue(u"新增其他收入", driver.get_title())
        driver.quit()

    @with_setup(my_setup_function, my_teardown_function)
    def test_3_deposit_check(self):

        ''' erp-deposit search key : pyse '''

        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400, 1400)
        driver.open("%s" % (url()))
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        login().cash_list(driver)
        driver.click("css=>.leaf.menu-mlid-4791>a")
        deposit_income = driver.get_text("css=>.leaf.menu-mlid-4791>a")
        print(deposit_income)
        driver.click("xpath=>.//*[@id='content']/div/div[1]/div/ul/li/a")
        deposit_url = driver.get_url()
        print(deposit_url)
        driver.get_display("xpath=>.//*[@id='header']/div[2]")
        driver.is_option_value_present("bankname","option","value")
        driver.type("xpath=>.//*[@id='depositcheque-form']/div/table[2]/tbody/tr/td[2]/div/input", "320283199304195511")
        driver.type("xpath=>.//*[@id='depositcheque-form']/div/table[2]/tbody/tr/td[5]/div/input", "1000.01")
        driver.click("xpath=>.//*[@id='edit-submit']")
        number = driver.get_text("xpath=>.//*[@id='content']/div/div[2]/table/tbody/tr[1]/td[7]")
        if number == u"1,000.01":
            print(u"存款录入金额1,000.01校验正确")
        else:
            print(u"校验失败")
        print(number)
        self.assertTrue(u"存款与支票记录", driver.get_title())
        driver.quit()

    @with_setup(my_setup_function, my_teardown_function)
    def test_4_nonbusiness(self):

        ''' erp-nonbusiness search key : pyse '''

        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400, 1400)
        driver.open("%s" % (url()))
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        login().cash_list(driver)
        driver.click("css=>.leaf.menu-mlid-4795>a")
        nonbusiness_income=driver.get_text("css=>.leaf.menu-mlid-4795>a")
        print(nonbusiness_income)
        driver.click("xpath=>.//*[@id='content']/div/div/div/ul/li/a")
        deposit_url = driver.get_url()
        print(deposit_url)
        driver.get_display("xpath=>.//*[@id='header']/div[2]")
        driver.is_option_value_present("method[200]","option","value")
        driver.type("xpath=>.//*[@id='nonoperatingrevenue-form']/div/table[2]/tbody/tr/td[3]/div/input", "100.05")
        driver.type("xpath=>.//*[@id='nonoperatingrevenue-form']/div/table[2]/tbody/tr/td[4]/div/input", "6")
        driver.type("xpath=>.//*[@id='nonoperatingrevenue-form']/div/table[2]/tbody/tr/td[6]/div/input","卖桌子")
        driver.click("xpath=>.//*[@id='edit-submit']")
        number = driver.get_text("xpath=>.//*[@id='content']/div/div[2]/table/tbody/tr/td[3]")
        if number == u"100.05":
            print(u"营业外收入录入金额100.05校验正确")
        else:
            print(u"校验失败")
        self.assertTrue(u"营业外收入记录", driver.get_title())
        driver.quit()

    @with_setup(my_setup_function, my_teardown_function)
    def test_5_deposit_received(self):

        ''' erp-deposit_received search key : pyse '''

        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400, 1400)
        driver.open("%s" % (url()))
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        login().cash_list(driver)
        driver.click("css=>.leaf.menu-mlid-4797>a")
        deposit_received_income = driver.get_text("css=>.leaf.menu-mlid-4797>a")
        print(deposit_received_income)
        driver.click("xpath=>.//*[@id='content']/div/div[1]/div/ul/li/a")
        deposit_url = driver.get_url()
        print(deposit_url)
        driver.get_display("xpath=>.//*[@id='header']/div[2]")
        driver.type("xpath=>.//*[@id='depositreceived-form']/div/table[2]/tbody/tr[1]/td[4]/div/input", "100.05")
        driver.is_option_value_present("method[196]","option","value")
        driver.type("xpath=>.//*[@id='depositreceived-form']/div/table[2]/tbody/tr[1]/td[6]/div/input", "储值卡充值")

        driver.is_option_value_present("customer[201]","option","value")
        driver.type("xpath=>.//*[@id='depositreceived-form']/div/table[2]/tbody/tr[2]/td[4]/div/input", "100.00")
        driver.is_option_value_present("method[201]","option","value")
        driver.type("xpath=>.//*[@id='depositreceived-form']/div/table[2]/tbody/tr[2]/td[6]/div/input","团定订金")

        driver.is_option_value_present("method[203]", "option", "value")
        driver.type("xpath=>.//*[@id='depositreceived-form']/div/table[2]/tbody/tr[3]/td[4]/div/input","55.00")
        driver.type("xpath=>.//*[@id='depositreceived-form']/div/table[2]/tbody/tr[3]/td[6]/div/input","真情卡销售")

        driver.is_option_value_present("method[206]", "option", "value")
        driver.type("xpath=>.//*[@id='depositreceived-form']/div/table[2]/tbody/tr[4]/td[4]/div/input","60.00")
        driver.type("xpath=>.//*[@id='depositreceived-form']/div/table[2]/tbody/tr[4]/td[6]/div/input","销售餐券")

        driver.click("xpath=>.//*[@id='edit-submit']")
        number = driver.get_text("xpath=>.//*[@id='content']/div/div[2]/table/tbody/tr[1]/td[3]")
        if number == u"100.05":
            print(u"预售账款录入金额100.05校验正确")
        else:
            print(u"number校验失败")

        number1 = driver.get_text("xpath=>.//*[@id='content']/div/div[2]/table/tbody/tr[2]/td[3]")
        if number1 == u"100.00":
            print(u"预售账款录入金额100.00校验正确")
        else:
            print(u"number1校验失败")

        number2 = driver.get_text("xpath=>.//*[@id='content']/div/div[2]/table/tbody/tr[3]/td[3]")
        if number2 == u"55.00":
            print(u"预售账款录入金额55.00校验正确")
        else:
            print(u"number2校验失败")

        number3 = driver.get_text("xpath=>.//*[@id='content']/div/div[2]/table/tbody/tr[4]/td[3]")
        if number3 == u"60.00":
            print(u"预售账款录入金额60.00校验正确")
        else:
            print(u"number3校验失败")

        self.assertTrue(u"预售账款记录", driver.get_title())
        driver.quit()

    @with_setup(my_setup_function, my_teardown_function)
    def test_6_spent_cash(self):

        ''' erp-spent_cash search key : pyse '''

        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400, 1400)
        driver.open("%s" % (url()))
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        login().cash_list(driver)
        driver.click("css=>.leaf.menu-mlid-4799>a")
        spent_cash_income = driver.get_text("css=>.leaf.menu-mlid-4799>a")
        print(spent_cash_income)
        driver.click("xpath=>.//*[@id='content']/table[2]/tbody/tr/td[1]/a")
        driver.click("xpath=>.//*[@id='content']/div/div/div/ul/li/a")
        spent_cash_url = driver.get_url()
        print(spent_cash_url)
        driver.get_display("xpath=>.//*[@id='header']/div[2]")
        driver.type("xpath=>.//*[@id='pettycash-form']/div/table[2]/tbody/tr/td[1]/div/input", "500.50")
        driver.type("xpath=>.//*[@id='pettycash-form']/div/table[2]/tbody/tr/td[2]/div/input", "财务审批金额")

        driver.click("xpath=>.//*[@id='edit-submit']")
        number = driver.get_text("xpath=>.//*[@id='content']/div/div[2]/table/tbody/tr[1]/td[2]")
        if number == u"500.50":
            print(u"零用金录入金额500.50校验正确")
        else:
            print(u"零用金录入校验失败")
        driver.click("css=>.leaf.menu-mlid-4799>a")
        number1 = driver.get_text("xpath=>.//*[@id='content']/table[2]/tbody/tr/td[3]")
        if number1 ==str(float(number)+5000):
            print("零用金总金额校验成功！！！")
        else:
            print("零用金总金额校验失败！！！")
        self.assertTrue(u"领用金领入记录", driver.get_title())
        driver.quit()

    @with_setup(my_setup_function, my_teardown_function)
    def test_7_spend_detail(self):

        ''' erp-spend_detail search key : pyse '''

        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400, 1400)
        driver.open("%s" % (url()))
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        login().cash_list(driver)
        driver.click("css=>.leaf.menu-mlid-4811>a")
        spend_detail_income = driver.get_text("css=>.leaf.menu-mlid-4811>a")
        print(spend_detail_income)
        driver.click("xpath=>.//*[@id='content']/div/div/div/ul/li/a")
        spend_detail_url = driver.get_url()
        print(spend_detail_url)
        driver.get_display("xpath=>.//*[@id='header']/div[2]")
        driver.type("xpath=>.//*[@id='addexpenses-form']/div/table[2]/tbody/tr[1]/td[3]/div/input", "5.55")
        driver.type("xpath=>.//*[@id='addexpenses-form']/div/table[2]/tbody/tr[1]/td[4]/div/input", "2")
        driver.type("xpath=>.//*[@id='addexpenses-form']/div/table[2]/tbody/tr[1]/td[5]/div/input","其他")

        driver.type("xpath=>.//*[@id='addexpenses-form']/div/table[2]/tbody/tr[2]/td[3]/div/input", "8.00")
        driver.type("xpath=>.//*[@id='addexpenses-form']/div/table[2]/tbody/tr[2]/td[4]/div/input", "1")
        driver.type("xpath=>.//*[@id='addexpenses-form']/div/table[2]/tbody/tr[2]/td[5]/div/input", "铅笔、钢笔")

        driver.type("xpath=>.//*[@id='addexpenses-form']/div/table[2]/tbody/tr[3]/td[3]/div/input", "7.00")
        driver.type("xpath=>.//*[@id='addexpenses-form']/div/table[2]/tbody/tr[3]/td[4]/div/input", "3")
        driver.type("xpath=>.//*[@id='addexpenses-form']/div/table[2]/tbody/tr[3]/td[5]/div/input", "培训费")

        driver.type("xpath=>.//*[@id='addexpenses-form']/div/table[2]/tbody/tr[4]/td[3]/div/input", "11.11")
        driver.type("xpath=>.//*[@id='addexpenses-form']/div/table[2]/tbody/tr[4]/td[4]/div/input", "4")
        driver.type("xpath=>.//*[@id='addexpenses-form']/div/table[2]/tbody/tr[4]/td[5]/div/input", "废料丢弃")

        driver.click("xpath=>.//*[@id='edit-submit']")
        number = driver.get_text("xpath=>.//*[@id='content']/div/div[2]/table/tbody/tr[1]/td[3]")
        if number == u"5.55":
            print(u"其他费用录入金额5.55校验正确")
        else:
            print(u"其他费用录入校验失败")

        number1 = driver.get_text("xpath=>.//*[@id='content']/div/div[2]/table/tbody/tr[2]/td[3]")
        if number1 == u"8.00":
            print(u"办公用品录入金额8.00校验正确")
        else:
            print(u"办公用品录入校验失败")

        number2 = driver.get_text("xpath=>.//*[@id='content']/div/div[2]/table/tbody/tr[3]/td[3]")
        if number2 == u"7.00":
            print(u"管理费用录入金额7.00校验正确")
        else:
            print(u"管理费用录入校验失败")

        number = driver.get_text("xpath=>.//*[@id='content']/div/div[2]/table/tbody/tr[4]/td[3]")
        if number == u"11.11":
            print(u"费用类录入金额11.11校验正确")
        else:
            print(u"费用类录入校验失败")

        self.assertTrue(u"支出明细记录", driver.get_title())
        driver.quit()

    @with_setup(my_setup_function, my_teardown_function)
    def test_8_daily_operations(self):

        ''' erp-daily_operations search key : pyse '''

        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400, 1400)
        driver.open("%s" % (url()))
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        login().cash_list(driver)
        driver.click("css=>.leaf.menu-mlid-9115>a")
        spend_detail_income = driver.get_text("css=>.leaf.menu-mlid-9115>a")
        print(spend_detail_income)
        driver.click("xpath=>.//*[@id='content']/div/div[1]/div/ul/li/a")
        daily_operations_url = driver.get_url()
        print(daily_operations_url)
        driver.get_display("xpath=>.//*[@id='header']/div[2]")
        driver.is_option_value_present("field_weather[und]","option","value")
        driver.click("xpath=>.//*[@id='select2-edit-field-weather-und-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","晴天")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-field-event-und-0-value']", "春节来了")
        driver.type("xpath=>.//*[@id='edit-field-morningmanager-und-0-value']", "周大明")
        driver.type("xpath=>.//*[@id='edit-field-eveningmanager-und-0-value']", "姚遥")
        driver.click("xpath=>.//*[@id='edit-submit']")
        weather= driver.get_text("xpath=>.//*[@id='content']/div[2]/div[3]/table/tbody/tr/td[2]")
        if weather == u"晴天":
            print(u"添加日运营信息校验正确")
        else:
            print(u"日运营信息校验失败")

        self.assertTrue(u"日运营信息管理", driver.get_title())
        driver.quit()

    @with_setup(my_setup_function, my_teardown_function)
    def test_9_run_report(self):

        ''' erp-run_report search key : pyse '''

        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400, 1400)
        driver.open("%s" % (url()))
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        login().cash_list(driver)
        driver.click("css=>.last.leaf.menu-mlid-9113>a")
        run_report_income = driver.get_text("css=>.leaf.menu-mlid-9113>a")
        print(run_report_income)
        driver.click("xpath=>.//*[@id='content']/div/div/div/ul/li/a")
        run_report_url = driver.get_url()
        print(run_report_url)
        driver.get_display("xpath=>.//*[@id='header']/div[2]")
        driver.type("xpath=>.//*[@id='edit-field-budgets-und-0-value']","10.05")
        driver.type("xpath=>.//*[@id='edit-field-forecast-s-und-0-value']", "8.88")
        driver.type("xpath=>.//*[@id='edit-field-forecast-tc-und-0-value']", "10")
        driver.type("xpath=>.//*[@id='edit-field-cashcommentstarget-und-0-value']", "50.00")
        driver.type("xpath=>.//*[@id='edit-field-discardedtarget-und-0-value']", "50.00")
        driver.type("xpath=>.//*[@id='edit-field-discrepancyratetarget-und-0-value']","10.00")
        driver.type("xpath=>.//*[@id='edit-field-dietarygoal-und-0-value']", "99.99")
        driver.type("xpath=>.//*[@id='edit-field-electricitytarget-und-0-value']","3")
        driver.type("xpath=>.//*[@id='edit-field-gas-target-und-0-value']","2")
        driver.type("xpath=>.//*[@id='edit-field-wagestarget-und-0-value']", "5000.00")
        driver.type("xpath=>.//*[@id='edit-field-tcpmh-und-0-value']", "100.00")
        driver.type("xpath=>.//*[@id='edit-field-avewagelastmonth-und-0-value']","4500.00")

        driver.click("xpath=>.//*[@id='edit-submit']")
        budget_s = driver.get_text("xpath=>.//*[@id='content']/div[2]/div[2]/table/tbody/tr/td[2]")
        if budget_s == u"10.05":
            print(u"预算s校验正确")
        else:
            print(u"预算s校验失败")

        forecast_s=driver.get_text("xpath=>.//*[@id='content']/div[2]/div[2]/table/tbody/tr/td[3]")
        if forecast_s == u"8.88":
            print(u"预估s校验正确")
        else:
            print(u"预估s校验失败")

        forecast_tc = driver.get_text("xpath=>.//*[@id='content']/div[2]/div[2]/table/tbody/tr/td[4]")
        if forecast_tc == u"10.00":
            print(u"预估tc校验正确")
        else:
            print(u"预估tc校验失败")

        cash_difference = driver.get_text("xpath=>.//*[@id='content']/div[2]/div[2]/table/tbody/tr/td[5]")
        if cash_difference == u"50.00":
            print(u"现金差异目标校验正确")
        else:
            print(u"现金差异目标校验失败")

        discard = driver.get_text("xpath=>.//*[@id='content']/div[2]/div[2]/table/tbody/tr/td[6]")
        if discard == u"50.00":
            print(u"丢弃目标校验正确")
        else:
            print(u"丢弃目标校验失败")

        difference_rate = driver.get_text("xpath=>.//*[@id='content']/div[2]/div[2]/table/tbody/tr/td[7]")
        if difference_rate == u"10.00":
            print(u"差异率目标校验正确")
        else:
            print(u"差异率目标校验失败")

        dietary = driver.get_text("xpath=>.//*[@id='content']/div[2]/div[2]/table/tbody/tr/td[8]")
        if dietary == u"99.99":
            print(u"膳食目标校验正确")
        else:
            print(u"膳食目标校验失败")

        electric_power = driver.get_text("xpath=>.//*[@id='content']/div[2]/div[2]/table/tbody/tr/td[9]")
        if electric_power == u"3.00":
            print(u"电力目标校验正确")
        else:
            print(u"电力目标校验失败")

        combustion_force = driver.get_text("xpath=>.//*[@id='content']/div[2]/div[2]/table/tbody/tr/td[10]")
        if combustion_force == u"2.00":
            print(u"燃气目标校验正确")
        else:
            print(u"燃气目标校验失败")

        working = driver.get_text("xpath=>.//*[@id='content']/div[2]/div[2]/table/tbody/tr/td[11]")
        if working == u"5000.00":
            print(u"工薪目标校验正确")
        else:
            print(u"工薪目标校验失败")

        TCPMH = driver.get_text("xpath=>.//*[@id='content']/div[2]/div[2]/table/tbody/tr/td[12]")
        if TCPMH == u"100.00":
            print(u"TCPMH校验正确")
        else:
            print(u"TCPMH校验失败")

        avg_working = driver.get_text("xpath=>.//*[@id='content']/div[2]/div[2]/table/tbody/tr/td[13]")
        if avg_working == u"4500.00":
            print(u"上月平均工薪校验正确")
        else:
            print(u"上月平均工薪校验失败")

        self.assertTrue(u"运营报告管理", driver.get_title())
        driver.quit()

    @with_setup(my_setup_function,my_teardown_function)
    def test_10_delivery_routes(self):

        ''' erp-test_delivery_routes search key : pyse '''

        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400,1400)
        driver.open(url())
        driver.F5()
        login().houqin_login(driver)
        print("After login==================")
        driver.click("css=>.last.leaf.menu-mlid-4819>a")
        delivery_income=driver.get_text("css=>.last.leaf.menu-mlid-4819>a")
        print(delivery_income)
        driver.click("xpath=>.//*[@id='content']/div/div[1]/div/ul/li/a")
        delivery_routes_url=driver.get_url()
        print(delivery_routes_url)
        driver.get_display("xpath=>.//*[@id='edit-title']")
        driver.type("xpath=>.//*[@id='edit-title']","测试专用路线")
        driver.click("xpath=>.//*[@id='select2-edit-state-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","草稿")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='circle']/div/div/button")
        driver.click("xpath=>.//*[@id='circle']/div/div/div/ul/li[1]/label/input")
        driver.click("xpath=>.//*[@id='zkf-store-select-filter']")
        driver.click("xpath=>.//*[@id='market']/div/div/button")
        driver.click("xpath=>.//*[@id='market']/div/div/div/ul/li[1]/label/input")
        driver.click("xpath=>.//*[@id='zkf-store-select-filter']")
        driver.click("xpath=>.//*[@id='address']/div/div/button")
        driver.click("xpath=>.//*[@id='address']/div/div/div/ul/li[1]/label/input")
        driver.click("xpath=>.//*[@id='zkf-store-select-filter']")
        driver.click("xpath=>.//*[@id='zkf-store-select-all']")
        driver.click("xpath=>.//*[@id='zkf-store-select-all']")
        sleep(1)
        driver.click("xpath=>.//*[@id='edit-submit']")
        test_routes=driver.get_text("xpath=>.//*[@id='views-form-distribution-plan-page-1']/div/table/tbody/tr[1]/td[2]")
        if test_routes == u"测试专用路线":
            print("添加草稿路线成功!")
        else :
            print("添加草稿路线失败!")
        driver.click("xpath=>.//*[@id='edit-views-bulk-operations-0']")
        driver.click("xpath=>.//*[@id='edit-actionpass-review']")
        if driver.get_text("xpath=>.//*[@id='content']/div[1]/em") == "审核通过":
            print("审核通过")
        else:
            print("审核失败")
        driver.quit()

    @with_setup(my_setup_function,my_teardown_function)
    def test_11_distribution_plan(self):
        ''' erp-test_distribution_plan search key : pyse '''

        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400,1400)
        driver.open(url())
        driver.F5()
        login().houqin_login(driver)
        print("After login==================")
        driver.click("css=>.link-send")
        plan_income=driver.get_text("css=>.link-send")
        print(plan_income)
        driver.click("xpath=>.//*[@id='content']/div/div[1]/div/ul/li/a")
        driver.get_display("css=>.navbar-title")
        driver.type("xpath=>.//*[@id='edit-field-delivery-id-und-0-value']","测试计划")
        driver.type("xpath=>.//*[@id='edit-title']","测试计划")
        driver.click("xpath=>.//*[@id='select2-edit-state-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","草稿")
        driver.enter("html/body/span/span/span[1]/input")
        driver.clear("xpath=>.//*[@id='edit-field-delivery-date-und-0-value-datepicker-popup-0']")
        driver.type("xpath=>.//*[@id='edit-field-delivery-date-und-0-value-datepicker-popup-0']","%s"%(select_date()))
        driver.type("xpath=>.//*[@id='edit-field-delivery-date-offset-und-0-value']","2")
        driver.click("xpath=>.//*[@id='select2-edit-field-delivery-type-und-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","日订")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-field-distribution-route-ref-und-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","测试专用路线")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='edit-submit']")
        plan_title=driver.get_text("xpath=>.//*[@id='views-form-distribution-plan-page']/div/table/tbody/tr[1]/td[2]")
        if plan_title == "测试计划":
            print("添加配送计划成功")
        else:
            print("添加失败")
        get_plan_text=driver.get_text("xpath=>.//*[@id='content']/div[1]")
        print(get_plan_text)
        driver.click("xpath=>.//*[@id='edit-views-bulk-operations-0']")
        driver.click("xpath=>.//*[@id='edit-actionpass-review']")
        plan_audit_text = driver.get_text("xpath=>.//*[@id='content']/div[1]/em")
        if plan_audit_text == "审核通过":
            print("配送计划审核通过")
        else:
            print("配送计划审核不通过")
        driver.click("css=>.link-date")
        get_plan_date=driver.get_text("xpath=>.//*[@id='delivery_schedule-%s-0']/div/div[2]/div/div/div[1]/div/span/a" %(select_date()))
        if get_plan_date == "%s" %(order_date_test()):
            print("审核通过后在排班计划显示成功")
        else:
            print("日订 %s未在排班计划中显示" %(order_date_test()))
        driver.click("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[1]/ul/li[2]/a")
        driver.click("xpath=>.//*[@id='views-form-distribution-plan-page']/div/table/tbody/tr[1]/td[9]/a[3]")
        driver.get_display("css=>.navbar-title")
        driver.click("xpath=>.//*[@id='edit-submit']")
        driver.click("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[1]/ul/li[3]/a")
        driver.click("xpath=>.//*[@id='views-form-distribution-plan-page-1']/div/table/tbody/tr[1]/td[5]/a[3]")
        driver.get_display("xpath=>.//*[@id='header']/div[2]")
        driver.click("xpath=>.//*[@id='edit-submit']")
        sleep(2)
        driver.quit()

    @with_setup(my_setup_function,my_teardown_function)
    def test_12_order(self):
        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400,1400)
        driver.open(url())
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        driver.click("xpath=>.//*[@id='delivery_schedule-%s-0']/div/div/div/div/div[1]/div/span/a" %(order_date()))
        driver.clear("xpath=>.//*[@id='edit-data-11031055-adjust-value']")
        driver.type("xpath=>.//*[@id='edit-data-11031055-adjust-value']","1.2")
        driver.click("xpath=>.//*[@id='edit-filter-actions-submit']")
        driver.move_to_element("xpath=>.//*[@id='edit-header']/div[1]/div/i")
        now_time=time.strftime("%Y-%m-%d %X", time.gmtime(time.time()))
        driver.cut_map("/Users/zhouxiaoming/Desktop/untitled/picture/thousand_dosage%s.png"%now_time)
        driver.clear("xpath=>.//*[@id='edit-header-adjust-rate']")
        driver.type("xpath=>.//*[@id='edit-header-adjust-rate']","1.5")
        driver.click("xpath=>.//*[@id='erp-purchase-order-purchase-order-form']/div/div[1]/div")
        driver.clear("xpath=>.//*[@id='edit-header-adjust-value--2']")
        driver.type("xpath=>.//*[@id='edit-header-adjust-value--2']","500")
        driver.click("xpath=>.//*[@id='erp-purchase-order-purchase-order-form--2']/div/div[1]/div")
        # calculated_value = driver.accept_alert("edit-header-estimate-value--3")
        # coefficient = driver.accept_alert("edit-header-adjust-rate--3")
        # insurance_turnover = driver.accept_alert("edit-header-adjust-value--4")
        # order_cycle_theory = calculated_value*coefficient+insurance_turnover
        order_cycle = driver.get_attr("edit-header-final-value--3")
        print(order_cycle)
        sleep(2)
        if order_cycle == "60500":
            print("订货周期营业额计算正确")
        else :
            print("计算错误！！！")
        lettuce_estimate = driver.get_text("xpath=>.//*[@id='erp-purchase-order-purchase-order-form--3']/div/div[3]/table[2]/tbody/tr[2]/td[7]")
        if lettuce_estimate == "72.6000" :
            print("生菜预估用量计算正确")
        else:
            print("生菜预估用量不正确")
        driver.cut_map("/Users/zhouxiaoming/Desktop/untitled/picture/back_thousand_dosage%s.png" % now_time)
        driver.clear("xpath=>.//*[@id='edit-data-11031055-quantity--3']")
        driver.type("xpath=>.//*[@id='edit-data-11031055-quantity--3']","3")
        sleep(1)
        # driver.js("document.getElementById(\"page\").scrollTop=1000")
        # driver.click("xpath=>.//*[@id='erp-purchase-order-purchase-order-form']/div/div[3]/table[2]/tbody/tr[15]/td[13]")
        # driver.clear("xpath=>.//*[@id='edit-data-11031059-quantity']")
        # driver.type("xpath=>.//*[@id='edit-data-11031059-quantity']","2")
        # sleep(1)
        driver.js("document.getElementById(\"page\").scrollTop=10000")
        driver.click("xpath=>.//*[@id='edit-actions-submit-save-review--3']")
        order_status=driver.get_text("xpath=>.//*[@id='views-form-purchase-order-management-page']/div/table/tbody/tr[1]/td[11]")
        if order_status == "已审核" :
            print("订货单状态为已审核状态")
        else :
            print("订货单提交到NC失败为保存状态")
        driver.quit()

    @with_setup(my_setup_function,my_teardown_function)
    def test_13_estimate_manage(self):
        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400,1400)
        driver.open(url())
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        print(driver.get_text("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[6]/a"))
        driver.click("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[6]/a")
        driver.get_display("css=>.navbar-title")
        driver.is_option_value_present("date","option","value")
        driver.clear("xpath=>.//*[@id='edit-data-%s-estimate-turnover']"%(estimate_date()))
        driver.type("xpath=>.//*[@id='edit-data-%s-estimate-turnover']"%(estimate_date()),"5000")
        driver.clear("xpath=>.//*[@id='edit-data-%s-estimate-ac']"%(estimate_date()))
        driver.type("xpath=>.//*[@id='edit-data-%s-estimate-ac']"%(estimate_date()),"10")
        driver.clear("xpath=>.//*[@id='edit-data-%s-estimate-tc']"%(estimate_date()))
        driver.type("xpath=>.//*[@id='edit-data-%s-estimate-tc']"%(estimate_date()),"20")
        driver.clear("xpath=>.//*[@id='edit-data-%s-note']"%(estimate_date()))
        driver.type("xpath=>.//*[@id='edit-data-%s-note']"%(estimate_date()),"1号预估")
        sleep(1)
        driver.js("document.getElementById(\"page\").scrollTop=10000")
        driver.click("xpath=>.//*[@id='edit-actions-submit']")
        sleep(1)
        driver.js("document.getElementById(\"page\").scrollTop=0")
        sleep(1)
        forecast_turnover = driver.get_attr("edit-data-%s-estimate-turnover"%(estimate_date()))
        if forecast_turnover == "5000.00" :
            print("预估营业额录入保存成功")
        else :
            print("预估营业额保存失效")
        forecast_AC = driver.get_attr("edit-data-%s-estimate-ac"%(estimate_date()))
        if forecast_AC == "10.00" :
            print("AC录入数据保存成功")
        else :
            print("AC保存失效")
        forecast_TC = driver.get_attr("edit-data-%s-estimate-tc"%(estimate_date()))
        if forecast_TC == "20.00" :
            print("TC录入保存数据成功")
        else:
            print("TC保存失效")
        driver.quit()

    @with_setup(my_setup_function,my_teardown_function)
    def test_14_Information_management(self):
        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400,1400)
        driver.open(url())
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        login().staff_management(driver)
        driver.click("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[7]/ul/li[1]/a")
        Information_management_list = driver.get_text("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[7]/ul/li[1]/a")
        print(Information_management_list)
        driver.click("xpath=>.//*[@id='content']/div/div[1]/div/ul/li/a")
        driver.get_display("css=>.navbar-title")
        driver.type("xpath=>.//*[@id='edit-name']","小小")
        driver.is_option_value_present("IDcard_type","option","value")
        driver.type("xpath=>.//*[@id='edit-id-number']","%s"%(identity_card_tangshi()))
        driver.type("xpath=>.//*[@id='edit-id-number-confirm']","%s"%(identity_card_tangshi()))
        driver.click("xpath=>.//*[@id='edit-next']")
        driver.type("xpath=>.//*[@id='edit-id-address']",u"上海闪派信息技术有限公司")
        driver.click("xpath=>.//*[@id='select2-edit-marital-status-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","未婚")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-educational-background-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","本科")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-political-status-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","其他")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-blood-type-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","A")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-recruitment-channels-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","其它")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-phone-number']","18552053546")
        driver.type("xpath=>.//*[@id='edit-address']",u"上海闪派信息技术有限公司")
        driver.type("xpath=>.//*[@id='edit-mail']","xmzhou@sparkpad.com")
        driver.click("xpath=>.//*[@id='select2-edit-social-security-address-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","其他")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-account-nature-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","其它")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-account-address']","无锡")
        driver.click("xpath=>.//*[@id='select2-edit-birthplace-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","广东省")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-urgent-contact']","周晓明")
        driver.type("xpath=>.//*[@id='edit-urgent-number']","18552053546")
        driver.click("xpath=>.//*[@id='select2-edit-relationship-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","父子")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-urgent-address']","上海闪派信息技术有限公司")
        driver.type("xpath=>.//*[@id='edit-urgent-unit']","闪派")
        driver.click("xpath=>.//*[@id='select2-edit-paybank-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","中信银行")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-cities-account']","上海")
        driver.type("xpath=>.//*[@id='edit-bank-name']","中国银行")
        driver.type("xpath=>.//*[@id='edit-bank-account']","320283199304195511")
        driver.type("xpath=>.//*[@id='edit-scale-minimum']","10")
        driver.click("xpath=>.//*[@id='select2-edit-agreement-company-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","上海真功夫快餐管理有限公司")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-position-name-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","组长")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-job-type-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","全日制时薪")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-employment-permit-date-datepicker-popup-0']","2017-01-17")
        driver.type("xpath=>.//*[@id='edit-job-start-date-datepicker-popup-0']","2017-01-17")
        driver.type("xpath=>.//*[@id='edit-health-certificate']","123456")
        driver.type("xpath=>.//*[@id='edit-health-certificate-date-datepicker-popup-0']","2017-01-17")
        driver.type("xpath=>.//*[@id='edit-temporary-residence-date-datepicker-popup-0']","2017-01-17")
        driver.type("xpath=>.//*[@id='edit-family-plan-date-datepicker-popup-0']","2017-01-17")
        driver.click("xpath=>.//*[@id='edit-finish']")
        hourly_restaurant = driver.get_text("xpath=>.//*[@id='content']/div/div[3]/table/tbody/tr[1]/td[2]")
        if hourly_restaurant == "小小" :
            print("时薪员工添加成功")
        else :
            print("时薪员工添加失败")
        driver.click("xpath=>.//*[@id='content']/nav/ul/li[1]/a")
        driver.click("xpath=>.//*[@id='content']/div/div[1]/div/ul/li/a")
        driver.get_display("css=>.navbar-title")
        driver.type("xpath=>.//*[@id='edit-name']","小小")
        driver.is_option_value_present("IDcard_type","option","value")
        driver.type("xpath=>.//*[@id='edit-id-number']","%s"%(identity_card_waimai()))
        driver.type("xpath=>.//*[@id='edit-id-number-confirm']","%s"%(identity_card_waimai()))
        driver.click("xpath=>.//*[@id='edit-next']")
        driver.type("xpath=>.//*[@id='edit-id-address']","上海闪派信息技术有限公司")
        driver.click("xpath=>.//*[@id='select2-edit-marital-status-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input", "未婚")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-educational-background-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input", "本科")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-political-status-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input", "其他")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-blood-type-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input", "A")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-recruitment-channels-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input", "其它")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-phone-number']","18552053546")
        driver.type("xpath=>.//*[@id='edit-address']","上海闪派信息技术有限公司")
        driver.type("xpath=>.//*[@id='edit-mail']","xmzhou@sparkpad.com")
        driver.click("xpath=>.//*[@id='select2-edit-social-security-address-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input", "其他")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-account-nature-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input", "其它")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-account-address']", "无锡")
        driver.click("xpath=>.//*[@id='select2-edit-birthplace-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input", "广东省")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-urgent-contact']", "周晓明")
        driver.type("xpath=>.//*[@id='edit-urgent-number']", "18552053546")
        driver.click("xpath=>.//*[@id='select2-edit-relationship-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input", "父子")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-urgent-address']", "上海闪派信息技术有限公司")
        driver.type("xpath=>.//*[@id='edit-urgent-unit']", "闪派")
        driver.click("xpath=>.//*[@id='select2-edit-paybank-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input", "中信银行")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-cities-account']", "无锡")
        driver.type("xpath=>.//*[@id='edit-bank-name']", "中信农业银行")
        driver.type("xpath=>.//*[@id='edit-bank-account']", "320283199304195511")
        driver.type("xpath=>.//*[@id='edit-scale-minimum']", "10.5")
        driver.click("xpath=>.//*[@id='select2-edit-agreement-company-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input", "上海真功夫快餐管理有限公司")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-position-name-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input", "外送队长")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-job-type-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input", "全日制时薪")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-employment-permit-date-datepicker-popup-0']", "2017-01-17")
        driver.type("xpath=>.//*[@id='edit-job-start-date-datepicker-popup-0']", "2017-01-17")
        driver.type("xpath=>.//*[@id='edit-health-certificate']", "123456")
        driver.type("xpath=>.//*[@id='edit-health-certificate-date-datepicker-popup-0']", "2017-01-17")
        driver.type("xpath=>.//*[@id='edit-temporary-residence-date-datepicker-popup-0']", "2017-01-17")
        driver.type("xpath=>.//*[@id='edit-family-plan-date-datepicker-popup-0']", "2017-01-17")
        driver.clear("xpath=>.//*[@id='edit-job-subsidy']")
        driver.type("xpath=>.//*[@id='edit-job-subsidy']", "100")
        driver.clear("xpath=>.//*[@id='edit-bill-subsidy']")
        driver.type("xpath=>.//*[@id='edit-bill-subsidy']", "100")
        driver.clear("xpath=>.//*[@id='edit-car-subsidy']")
        driver.type("xpath=>.//*[@id='edit-car-subsidy']", "150")
        driver.click("xpath=>.//*[@id='edit-finish']")
        hourly_restaurant1 = driver.get_text("xpath=>.//*[@id='content']/div/div[3]/table/tbody/tr/td[2]")
        if hourly_restaurant1 == "小小":
            print("时薪员工添加成功")
        else:
            print("时薪员工添加失败")
        driver.quit()

    @with_setup(my_setup_function,my_teardown_function)
    def test_15_contract_management(self):
        driver= Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400,1400)
        driver.open(url())
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        login().staff_management(driver)
        driver.click("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[7]/ul/li[2]/a")
        contract_management_list = driver.get_text("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[7]/ul/li[2]/a")
        print(contract_management_list)
        driver.click("xpath=>.//*[@id='content']/div/div[1]/div/ul/li/a")
        driver.type("xpath=>.//*[@id='edit-name']","小小")
        sleep(2)
        driver.click("xpath=>.//*[@id='autocomplete']/ul/li[1]")
        driver.click("xpath=>.//*[@id='select2-edit-agreement-change-type--2-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","正常")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-agreement-term--2-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","固定期限")
        driver.enter("html/body/span/span/span[1]/input")
        driver.click("xpath=>.//*[@id='select2-edit-agreement-company--2-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","上海真功夫快餐管理有限公司")
        driver.enter("html/body/span/span/span[1]/input")
        driver.js("document.getElementById(\"page\").scrollTop=1000")
        driver.type("xpath=>.//*[@id='edit-remark--2']","上海")
        driver.click("xpath=>.//*[@id='edit-submit--2']")
        contract_management_list = driver.get_text("xpath=>.//*[@id='content']/div/div[3]/table/tbody/tr/td[2]")
        print(contract_management_list)
        if contract_management_list == "小小" :
            print("员工合同管理添加成功")
        else :
            print("员工合同管理添加失败")
        driver.quit()

    @with_setup(my_setup_function,my_teardown_function)
    def test_16_dimission_management(self):
        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400,1400)
        driver.open(url())
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        login().staff_management(driver)
        driver.click("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[7]/ul/li[3]/a")
        dimission_management_list = driver.get_text("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[7]/ul/li[3]/a")
        print(dimission_management_list)
        driver.click("xpath=>.//*[@id='content']/div/div[1]/div/ul/li/a")
        driver.get_display("xpath=>.//*[@id='header']/div[2]")
        driver.type("xpath=>.//*[@id='edit-name']","小小")
        driver.click("xpath=>.//*[@id='autocomplete']/ul/li[1]/div")
        driver.click("xpath=>.//*[@id='select2-edit-turnover-hierarchical-select-selects-0--2-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","主动离职")
        driver.enter("html/body/span/span/span[1]/input")
        sleep(1)
        try :
            driver.is_option_value_present("turnover[hierarchical_select][selects][0]","option","value")
        except FileNotFoundError:
            print("异常！")
        try:
            driver.is_option_value_present("turnover[hierarchical_select][selects][1]","option","value")
        except FileNotFoundError:
            print("异常!")
        try :
            driver.is_option_value_present("turnover[hierarchical_select][selects][2]","option","value")
        except FileNotFoundError:
            print("异常")
        driver.type("xpath=>.//*[@id='edit-turnover-remark--2']","主动离职")
        sleep(1)
        driver.click("xpath=>.//*[@id='edit-submit--2']")
        driver.accept_alert()
        driver.get_display("xpath=>.//*[@id='header']/div[2]")
        dimission_name_list = driver.get_text("xpath=>.//*[@id='content']/div/div[3]/table/tbody/tr[1]/td[1]")
        if dimission_name_list == "小小" :
            print("小小离职成功")
        else:
            print("离职失败")
        driver.quit()

    @with_setup(my_setup_function,my_teardown_function)
    def test_17_black_manage(self):
        driver = Pyse("chrome")
        driver.set_window(1400,1400)
        driver.wait(5)
        driver.open(url())
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        login().staff_management(driver)
        driver.click("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[7]/ul/li[4]/a")
        black_manage_list = driver.get_text("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[7]/ul/li[4]/a")
        print(black_manage_list)
        driver.click("xpath=>.//*[@id='content']/div/div[1]/div/ul/li/a")
        driver.get_display("xpath=>.//*[@id='header']/div[2]")
        driver.type("xpath=>.//*[@id='edit-name']","小小")
        driver.click("xpath=>.//*[@id='autocomplete']/ul/li/div")
        driver.click("xpath=>.//*[@id='select2-edit-blacklist-reason--2-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","有其他损害公司利益的行为")
        driver.enter("html/body/span/span/span[1]/input")
        sleep(1)
        driver.type("xpath=>.//*[@id='edit-remark--2']","不想干了！")
        sleep(1)
        driver.click("xpath=>.//*[@id='edit-submit--2']")
        driver.accept_alert()
        black_manage_name = driver.get_text("xpath=>.//*[@id='content']/div/div[3]/table/tbody/tr/td[1]")
        print(black_manage_name)
        if black_manage_name == "小小" :
            print("添加黑名单成功")
        else:
            print("添加黑名单失败")
        driver.quit()

    @with_setup(my_setup_function,my_teardown_function)
    def test_18_transaction_mangen(self):
        driver = Pyse("chrome")
        driver.wait(5)
        driver.set_window(1400,1400)
        driver.open(url())
        driver.F5()
        login().user_login(driver)
        print("After login==================")
        login().transaction_mangen(driver)
        driver.click("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[8]/ul/li/a")
        transaction_mangen_list = driver.get_text("xpath=>.//*[@id='block-menu-block-1']/div/ul/li[8]/ul/li/a")
        print(transaction_mangen_list)
        driver.click("xpath=>.//*[@id='content']/div/div[1]/div/ul/li/a")
        driver.get_display("xpath=>.//*[@id='header']/div[2]")
        driver.type("xpath=>.//*[@id='edit-name']","小小")
        driver.click("xpath=>.//*[@id='autocomplete']/ul/li/div")
        sleep(1)
        try :
            driver.is_option_value_present("change_type","option","value")
        except FileNotFoundError:
            print("异常了！")
        driver.type("xpath=>.//*[@id='edit-change-effect-date--2-datepicker-popup-1']","%s"%transaction_date())
        driver.click("xpath=>.//*[@id='select2-edit-position-name-after--2-container']")
        driver.type("xpath=>html/body/span/span/span[1]/input","组长")
        driver.enter("html/body/span/span/span[1]/input")
        driver.type("xpath=>.//*[@id='edit-remark--2']","升职加薪")
        sleep(1)
        driver.click("xpath=>.//*[@id='edit-submit--2']")
        sleep(1)
        transaction_mangenz_name = driver.get_text("xpath=>.//*[@id='content']/div/div[3]/table/tbody/tr[1]/td[1]")
        transaction_mangenz_job = driver.get_text("xpath=>.//*[@id='content']/div/div[3]/table/tbody/tr[1]/td[6]")
        print(transaction_mangenz_name)
        if transaction_mangenz_name == "小小" and transaction_mangenz_job == "组长":
            print("异动人员修改成功")
        else :
            print("异动人员修改失败")
        driver.quit()

if __name__ == '__main__':
    runner = TestRunner('./','ERP测试用例(HQ020001)','测试环境：Chrome')
    runner.run()