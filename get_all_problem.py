from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from tqdm import tqdm
import pandas as pd


# path = '/Users/phoenix/rcw/pachong_leetcode/chromedriver'

# driver = webdriver.Chrome(executable_path=path)

# url = 'https://leetcode-cn.com/problemset/all/'

# driver.get(url)

# print(1)
# doc = driver.page_source
# print(type(doc))
# mouse = Select(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/span/select'))



def get_problem_list(links):
    problem_list = []
    for link in links:
        problem_url = link.get_attribute('href')
        if problem_url[:33] == 'https://leetcode-cn.com/problems/' and problem_url[-8:] != 'solution':
            problem_list.append(problem_url)
    print(len(problem_list))
    return problem_list[1:]

def get_problem_info(driver, url, times=3):
    for i in range(times):
        try:
            driver.get(url)
            info_list = []
            name = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[1]/h4')
            # likes = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[1]/div/button[1]')
            likes = driver.find_element_by_xpath('//*[@id="lc-home"]/div/div[1]/div[2]/div/div[1]/div/button[1]')
            # dislikes = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[1]/div/button[2]')
            difficulty = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[1]/div/span[2]')
            passed_times = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[1]/p[2]')
            submited_times = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[3]/p[2]')
            # print(name.text, likes.text, difficulty.text)
            problem_name = url[len('https://leetcode-cn.com/problems/'):].replace('-', ' ').title()
            info_list = [name.text, problem_name, likes.text, difficulty.text, passed_times.text, submited_times.text, url]
            # print(info_list)
            # driver.close()
            flag = False
            return info_list
        except:
            print("error")
            continue
    # driver.close()

def save_to_csv(info, i):
    name = ['name1', 'name', 'liked', 'difficulty', 'passed', 'submitted', 'url']
    df = pd.DataFrame(columns=name, data=info)
    # print(df)
    filename = './info' + str(i) + '.csv'
    df.to_csv(filename)

def main():
    path = '/Users/phoenix/rcw/pachong_leetcode/chromedriver'
    driver = webdriver.Chrome(executable_path=path)
    url = 'https://leetcode-cn.com/problemset/all/'
    driver.get(url)
    mouse = Select(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/span/select'))
    mouse.select_by_value('9007199254740991')
    # mouse.select_by_value('100')
    links = driver.find_elements_by_xpath("//*[@href]")
    problem_list = get_problem_list(links)
    driver.close()
    print(problem_list, len(problem_list))
    info = []
    noinfo = []
    k = 2
    for i in tqdm(range(50*k, 50*(k+1))):
        problem = problem_list[i]
        driver = webdriver.Chrome(executable_path=path)
        problem_info = get_problem_info(driver, problem)
        # print("rate is: {:.2%}, infomation is: {}".format((1-(len(noinfo)/len(problem_list))) , problem_info))
        print(problem_info)
        if problem_info:
            info.append(problem_info)
        else:
            # info.append([])
            noinfo.append(i)
        if i % 10 == 0:
            save_to_csv(info, k)
    print(info)
    print(noinfo)
    save_to_csv(info,k)
main()