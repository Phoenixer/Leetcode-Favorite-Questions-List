from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from tqdm import tqdm
import pandas as pd


def get_problem_list(links):
    problem_list = []
    for link in links:
        problem_url = link.get_attribute('href')
        if problem_url[:33] == 'https://leetcode-cn.com/problems/' and problem_url[-8:] != 'solution':
            problem_list.append(problem_url)
    print(len(problem_list))
    return problem_list[1:]

def get_problem_info(driver, url, times=3, inter=False):
    if inter:
        url = url[:16]+url[19:]
    for i in range(times):
        try:
            if inter:
                print(url)
                driver.get(url)
                info_list = []
                name = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[1]')
                # likes = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[1]/div/button[1]')
                likes = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/button[1]')
                dislikes = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/button[2]')
                difficulty = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]')
                passed_times = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/div[2]')
                submited_times = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]')
                # print(name.text, likes.text, difficulty.text)
                problem_name = url[len('https://leetcode-cn.com/problems/'):].replace('-', ' ').title()
                info_list = [name.text, problem_name, likes.text, dislikes.text, difficulty.text, passed_times.text, submited_times.text, url]
                # print(info_list)
                # driver.close()
                flag = False
                return info_list
            else:
                driver.get(url)
                info_list = []
                name = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[1]/h4')
                likes = driver.find_element_by_xpath('//*[@id="lc-home"]/div/div[1]/div[2]/div/div[1]/div/button[1]')
                # dislikes = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[1]/div/button[2]')
                difficulty = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[1]/div/span[2]')
                passed_times = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[1]/p[2]')
                submited_times = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[3]/p[2]')
                problem_name = url[len('https://leetcode-cn.com/problems/'):].replace('-', ' ').title()
                info_list = [name.text, problem_name, likes.text, difficulty.text, passed_times.text, submited_times.text, url]
                flag = False
                return info_list
        except:
            print("error")
            continue
    # driver.close()

def save_to_csv(info, i, inter=False):
    if inter:
        name = ['name1', 'name', 'liked', 'dislikes', 'difficulty', 'passed', 'submitted', 'url']
        df = pd.DataFrame(columns=name, data=info)
        filename = './info' + str(i) + 'inter' + '.csv'
        df.to_csv(filename)
    else:
        name = ['name1', 'name', 'liked', 'difficulty', 'passed', 'submitted', 'url']
        df = pd.DataFrame(columns=name, data=info)
        filename = './info' + str(i) + '.csv'
        df.to_csv(filename)

def main():
    path = r'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    url = 'https://leetcode-cn.com/problemset/all/'
    driver.get(url)
    mouse = Select(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/span/select'))
    mouse.select_by_value('9007199254740991')
    # mouse.select_by_value('20')
    links = driver.find_elements_by_xpath("//*[@href]")
    problem_list = get_problem_list(links)
    driver.quit()
    print(problem_list, len(problem_list))
    info = []
    noinfo = []
    for k in range(20, len(problem_list)//50+1):
    # for k in range(1):
        for i in tqdm(range(50*k, min(50*(k+1), len(problem_list)))):
            problem = problem_list[i]
            driver = webdriver.Chrome(executable_path=path)
            problem_info = get_problem_info(driver, problem, inter=True)
            print(problem_info)
            driver.quit()
            if problem_info:
                info.append(problem_info)
            else:
                # info.append([])
                noinfo.append(i)
            if (i+1) % 10 == 0:
                save_to_csv(info,k, inter=True)
        print(info)
        print(noinfo)
        save_to_csv(info,k, inter=True)
main()