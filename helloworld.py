from selenium import webdriver
from selenium.webdriver.common.by import By

path = '/Users/phoenix/rcw/pachong_leetcode/chromedriver'


driver = webdriver.Chrome(executable_path=path)

url = 'https://leetcode-cn.com/problems/two-sum/'
url = 'https://leetcode-cn.com/problems/add-two-numbers/'
# url = 'http://hotel.qunar.com/city/beijing_city/'

driver.get(url)
print(1)
# hotel_info = driver.find_element_by_id( 'js_plugin_tag_beijing_city_65457' )
# hotel_info = driver.find_elements_by_css_selector('lc-home > div > div.css-bu99vi-HeaderCn.e1t1fzqp0 > div.css-1ldtbl2-Container.e171bd600 > div > div.css-r0ewhb-Left.e171bd602 > div > button:nth-child(3) > span')
info = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[1]/div/button[1]')
# info = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/button[1]')
# info = driver.find_element_by_class_name('btn__r7r7 css-1rdgofi')
# print(hotel_info)
print(info)
print(info.text, url)
print(1)
driver.close()
# hotel_list = driver.find_elements_by_css_selector("[class= b_result_box js_list_block  b_result_commentbox ]")
# print(hotel_list)
# //*[@id="lc-home"]/div/div[1]/div[2]/div/div[1]/div/button[1]/span
# /html/body/div[1]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/button[1]
# /html/body/div[1]/div/div[3]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/button[1]

# /html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/table/tbody[1]/tr[1]/td[3]/div/a
# /html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/table/tbody[1]/tr[2]/td[3]/div/a
# /html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/table/tbody[1]/tr[7]/td[3]/div/a