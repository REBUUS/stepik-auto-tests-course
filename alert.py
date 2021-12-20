import math
from selenium import webdriver
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    but1 = browser.find_element_by_css_selector("button[class='btn btn-primary']")
    but1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    #browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    #radiobut = browser.find_element_by_css_selector("#robotsRule")
    #radiobut.click()
    #checkbut = browser.find_element_by_css_selector("#robotCheckbox")
    #checkbut.click()
    butt = browser.find_element_by_css_selector("button[class='btn btn-primary']")
    butt.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
