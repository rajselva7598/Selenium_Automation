import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.yield_fixture()
def setupMethod():
    global driver
    driver = webdriver.Chrome(executable_path=r"C:\Users\user\Desktop\chromedriver_win32\chromedriver.exe")
    driver.get('https://www.flipkart.com/')
    driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/button').click()
    yield
    driver.close()
    driver.quit()

@pytest.fixture()
def test_methodA(setupMethod):
    print('demo1: method A excution')
    time.sleep(3)
    driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys('laptops')
    time.sleep(3)
    driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()

def test_laptoprequirements(test_methodA):
    time.sleep(3)
    input_Corelist = driver.find_element(by=By.XPATH,
                                     value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[4]/div[2]/div[1]/div[1]/input').send_keys("Core i5")
    time.sleep(3)
    input_Search = driver.find_element(by=By.XPATH,
                                   value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[4]/div[2]/div[1]/div[2]/div/label/div[2]').click()
    time.sleep(5)
    time.sleep(3)
    hardisk_List = driver.find_element(by=By.XPATH,
                                       value='//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[10]/div').click()
    time.sleep(3)
    hardisk_capacity_Type = driver.find_element(by=By.XPATH,
                                     value='//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[10]/div[2]/div/div[1]/div/label/div[2]').click()
@pytest.fixture()
def test_methodB(setupMethod):
    print('demo1: method A excution')
    time.sleep(3)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys(
        'phone')
    time.sleep(3)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()

def test_phoneRequirements(test_methodB):
    time.sleep(3)
    ram_Search = driver.find_element(by=By.XPATH,
                                     value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[7]/div[2]/div/div[5]/div/label/div[2]').click()
    time.sleep(3)
    hardisk_List = driver.find_element(by=By.XPATH,
                                       value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[8]/div').click()
    time.sleep(3)
    hardisk_capacity_Type = driver.find_element(by=By.XPATH,
                                                value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[8]/div[2]/div/div[2]/div/label/div[2]').click()
    time.sleep(3)
    network_List = driver.find_element(by=By.XPATH,
                                       value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[17]/div[1]').click()
    time.sleep(3)
    ram_Type = driver.find_element(by=By.XPATH,
                                   value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[17]/div[2]/div/div[3]/div/label/div[2]').click()





