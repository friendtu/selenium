from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from DataPool import DataPool

dp=DataPool('demo')
driver=webdriver.Chrome()

driver.get( dp.get('BAIDU_HOME_URL') )
driver.find_element_by_css_selector('#kw').send_keys("selenium")
driver.find_element_by_id('su').click()
#driver.maximize_window()
#driver.find_element_by_link_text('百度首页').click()
#print(driver.name,driver.title,driver.current_url)
WebDriverWait(driver,5).until(lambda x: 'selenium' in x.title)
assert('selenium_' in driver.title)
driver.close()
driver.quit()
