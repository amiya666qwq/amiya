from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

PATH = "G:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://popcat.click/")
clicking=ActionChains(driver)
clickbutton=driver.find_element(By.XPATH,'//*[@id="app"]/div')
for i in range (114514):
    clicking.click(clickbutton)
    clicking.perform()
driver.close()