from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

PATH = "G:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://tsj.tw/")
blow = driver.find_element(By.ID,"click")
blow_count = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')
things=[]
things.append(driver.find_element(By.XPATH,"//*[@id='app']/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]"))
things.append(driver.find_element(By.XPATH,"//*[@id='app']/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]"))
things.append(driver.find_element(By.XPATH,"//*[@id='app']/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]"))
prices=[]
prices.append(driver.find_element(By.XPATH,"//*[@id='app']/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]"))
prices.append(driver.find_element(By.XPATH,"//*[@id='app']/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]"))
prices.append(driver.find_element(By.XPATH,"//*[@id='app']/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]"))

actions = ActionChains(driver)
for i in range(10000):
    actions.click(blow)
    actions.perform()
    count=int(blow_count.text.replace("您目前擁有","").replace("技術點",""))
    for j in range(3):
        price=int(prices[j].text.replace("技術點",""))
        if count>=price:
            upgrade_actions=ActionChains(driver)
            upgrade_actions.move_to_element(things[j])
            upgrade_actions.click()
            upgrade_actions.perform()
            break