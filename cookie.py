from selenium import webdriver
wd=webdriver.Chrome()
wd.get('https://www.baidu.com')
print(wd.get_cookies())
wd.add_cookie({'name':'foo','value':'bar'})
value=wd.get_cookie('foo')
print(value)

wd.delete_cookie('foo')
print(wd.get_cookies())
wd.delete_all_cookies()
print(wd.get_cookies())