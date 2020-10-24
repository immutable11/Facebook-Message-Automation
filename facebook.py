from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

class facebook():
    def __init__(self,username,password,name,text):
        self.username=username
        self.password=password
        self.name=name
        self.text=text
        
    def engine(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://facebook.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def logins(self):
        self.driver.find_element_by_name("email").send_keys(self.username)
        self.driver.find_element_by_name("pass").send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input').click()  
        time.sleep(10)  

    def cookies(self):
        self.cookiees=self.driver.get_cookies()
        print(len(self.cookiees))
        print(self.cookiees)
        self.driver.delete_all_cookies()
        time.sleep(3)

    def message(self):
        self.driver.implicitly_wait(3)
        self.wait=WebDriverWait(self.driver,4)
        self.messenger=self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div[1]/div[2]/span/div/div[1]")))
        self.messenger.click()
        
        self.wait1=WebDriverWait(self.driver,4)
        self.button=self.wait1.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[10]/div/div/div/div[1]/div[3]/div[1]/label[1]/input")))
        self.button.click()
       
        time.sleep(4)
        self.driver.find_element_by_name("email").send_keys(self.username)
        self.driver.find_element_by_name("pass").send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input').click()
        time.sleep(4)
        
    def sendingmessage(self):
        self.driver.implicitly_wait(3)
            
        self.wait2=WebDriverWait(self.driver,4)
        self.messenger=self.wait2.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div[1]/div[2]/span/div/div[1]")))
        self.messenger.click()
        time.sleep(4)

        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div[3]/span/a').click()
        time.sleep(3)
        self.timer=WebDriverWait(self.driver,5)
        self.to=self.timer.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[2]/div/div/span/input")))
        
        self.to.click()
        self.to.send_keys(self.name)
        time.sleep(2)

        self.msg=Select(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[5]/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div'))
        self.msg.select_by_index(0)
        '''
        
        self.amar=self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[5]/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div/ul/li[1]/div/div[1]/div')
        self.amar.click()
        time.sleep(2)'''

        self.box=self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div[3]/div/div[2]/form/div/div[2]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div')
        self.box.send_keys(self.text)
        
        self.send=self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div[3]/div/div[2]/form/div/div[2]/span[2]/div')
        self.send.click()
        time.sleep(3)

    def close(self):
        self.driver.quit()

        

object=facebook('username','password','message to whome','type message') 
object.engine()
object.logins()
object.cookies()
object.message()
object.sendingmessage()
object.close()



