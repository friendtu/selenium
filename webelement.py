from selenium.webdriver.remote import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import  TimeoutException

wd=webdriver.WebDriver(command_executor="http://192.168.31.110:4444/wd/hub",desired_capabilities=DesiredCapabilities.CHROME)

wd.get('https://www.baidu.com')
div=wd.find_element_by_class_name('s_form_wrapper')
subdiv=div.find_element_by_id('lg')
form=div.find_element_by_css_selector('#form')
print(div.get_attribute('name'))
print(div.id)
print(div.is_displayed())
print(div.is_enabled())
if subdiv.parent==form.parent:
    print("same")
else:
    print("not same")
print(div.text)

kw=wd.find_element_by_id('kw')
kw.send_keys("selenium")
print(kw.get_attribute('value'))

wd.get("file:///C:/Users/tud/GitHub/selenium/list.html")
selectLang=wd.find_element_by_css_selector('#lang')
options=selectLang.find_elements_by_tag_name('option')

options[2].click()

for i in range(len(options)):
    if options[i].get_attribute('value')=='python':
        options[i].click()
        break

for i in range(len(options)):
    if options[i].text=='RUBY':
        options[i].click()
        break

for i in range(len(options)):
    if options[i].get_attribute('selected'):
        print(options[i].get_attribute('text'))
        print(options[i].get_attribute('value'))
        break

select=Select(selectLang)
optionList=select.options
select.select_by_index(1)
select.select_by_value=('python')
select.select_by_visible_text('PYTHON')
option=select.first_selected_option
print(option.get_attribute('value'))

wd.find_element_by_id('alert').click()
alt=wd.switch_to.alert
alt.accept()

#wd.find_element_by_id('alert').click()
wd.execute_script('alert("ok")')
alt=Alert(wd)
alt.dismiss()

script='''
var callback=arguments[arguments.length-1];
window.setTimeout(function(){callback('timeout')},3000);
'''

result=wd.execute_async_script(script)
print(result)

try:
    #wd.find_element_by_id('alert').click()
    result=WebDriverWait(wd,5).until(expected_conditions.alert_is_present(),"Timed out waiting for alert")
    print(result)
    alt=Alert(wd)
    print(alt.text)
    alt.accept()
except TimeoutException:
    print("no alert")






wd.close()

