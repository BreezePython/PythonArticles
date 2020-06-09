# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/7/2 0:55.记一次python配置文件的大坑
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : selenium_cookie.py

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.jianshu.com/u/d23fd5012bed")
driver.delete_all_cookies()
driver.find_element_by_id('sign_in').click()
driver.find_element_by_id('session_email_or_mobile_number').send_keys('')
driver.find_element_by_id('session_password').send_keys('输入密码')
driver.find_element_by_id('sign-in-form-submit-btn').click()
# 此时我们手动进行登录验证操作操作
time.sleep(30)

# cookie 关键字
key = 'remember_user_token'
user_token = driver.get_cookie(key)
print(user_token)
cookies = driver.get_cookies()
print(cookies)
driver.quit()

cookie = {'name': key, 'value': user_token['value']}
driver = webdriver.Chrome()
driver.get("https://www.jianshu.com/u/d23fd5012bed")
driver.add_cookie(cookie)
driver.get("https://www.jianshu.com/u/d23fd5012bed")
time.sleep(3)
driver.close()
