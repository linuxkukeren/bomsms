from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.get('https://www.instagram.com/')
time.sleep(3.2)
userq = 'toxir18569@j24blog.com'
log = driver.find_element_by_name('username').send_keys(userq)
logi = driver.find_element_by_name('password').send_keys('anginmalam')
butlog = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div').click()
time.sleep(4)
pop1 = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
time.sleep(3)
pop = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
for i in range(8):
    for i in range(5):
        i = driver.find_element_by_xpath('//button[text()="Follow"]').click()
        time.sleep(1)
    driver.refresh()