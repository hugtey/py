from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

driver.get('http://qldt.actvn.edu.vn/CMCSoft.IU.Web.info/Login.aspx')
sleep(1)
driver.find_element("xpath", '/html/body/form/table/tbody/tr/td/div[1]/div/table[2]/tbody/tr/td/table/tbody/tr[1]/td[2]/input').send_keys('AT170525')
driver.find_element("xpath", '/html/body/form/table/tbody/tr/td/div[1]/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/input').send_keys('123456')
driver.find_element("xpath", '/html/body/form/table/tbody/tr/td/div[1]/div/table[2]/tbody/tr/td/table/tbody/tr[3]/td[1]/input').click()
sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)


