from selenium import webdriver
import inspect

driver = webdriver.Chrome(executable_path="/Library/Frameworks/Python.framework/Versions/3.5/chromedriver")


def test_001():
    assert 2 == 1


def test_0002():
    assert 3 == 1


def test_learn_3():
    try:
        driver.get("http://www.baidu.com")
        driver.find_element_by_id("id")
    except Exception as e:
        driver.get_screenshot_as_file("\\Users\\zhouxiaoming\\Desktop\\untitled" % (inspect.stack()[0][3]))
        raise