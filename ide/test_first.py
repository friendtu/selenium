# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestFirst():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_first(self):
    self.driver.get("https://www.baidu.com/")
    self.driver.set_window_size(977, 639)
    self.driver.find_element(By.ID, "kw").send_keys("selenium")
    self.driver.find_element(By.ID, "su").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "下一页 >")))
    assert self.driver.title == "glob:selenium*"
  
