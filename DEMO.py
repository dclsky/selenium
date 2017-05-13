# coding=utf-8
from selenium import webdriver
from time import sleep
import time
from Value import sid
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

##每天未日结门店截图
li = ["CN755132","CN769040","CN755058","CN731001","CN755082","CN021040","CN020064","CN755066"]
for i in li:
        driver = webdriver.Chrome(executable_path="/Library/Frameworks/Python.framework/Versions/3.5/chromedriver")
        driver.set_window_size(1400,1400)
        driver.get("http://store-erp.zkungfu.com")
        driver.refresh()
        driver.find_element_by_xpath(".//*[@id='edit-name']").send_keys("admin")
        driver.find_element_by_xpath(".//*[@id='edit-pass']").send_keys("abcd1234")
        driver.find_element_by_xpath(".//*[@id='edit-submit']").click()
        WebDriverWait(driver,5).until(EC.presence_of_element_located(("xpath", ".//*[@id='admin-menu-menu']/li[6]/a")))
        driver.find_element_by_xpath(".//*[@id='admin-menu-menu']/li[6]/a").click()
        driver.find_element_by_xpath(".//*[@id='edit-combine']").send_keys("%s"%i)
        print ("%s"%i)
        driver.find_element_by_xpath(".//*[@id='edit-submit-admin-views-user']").click()
        sleep(1)
        driver.find_element_by_xpath(".//*[@id='views-form-admin-views-user-system-1']/div/table[2]/tbody/tr[1]/td[2]/a").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(("xpath", ".//*[@id='content']/div/a")))
        driver.find_element_by_xpath(".//*[@id='content']/div/a").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(("xpath", ".//*[@id='block-menu-block-1']/div/ul/li[1]/span")))
        driver.find_element_by_xpath(".//*[@id='block-menu-block-1']/div/ul/li[1]/span").click()
        driver.find_element_by_xpath(".//*[@id='block-menu-block-1']/div/ul/li[10]/span").click()
        driver.find_element_by_xpath(".//*[@id='block-menu-block-1']/div/ul/li[10]/ul/li[2]/a").click()
        nowtime = time.strftime("%Y%m%d.%H.%M.%S")
        name = i+"-"+nowtime
        driver.get_screenshot_as_file("/Users/zhouxiaoming/Desktop/日结照片/%s.jpg" %name)
        driver.find_element_by_xpath(".//*[@id='block-system-user-menu']/ul/li/a").click()
        driver.close()

