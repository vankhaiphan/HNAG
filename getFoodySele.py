from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
#driver=webdriver.firefox()
#driver=webdriver.ie()
print("sample test case started")

#maximize the window size
driver.maximize_window()

#navigate to the url
driver.get("https://www.foody.vn/da-nang/nha-hang")
time.sleep(1)

button = driver.find_element_by_xpath("/html/body/div[2]/section/div/div[2]/div/div/div/div/div[2]/div[8]/a")

for i in range(5):
    button.click()
    time.sleep(1)
#Number = driver.find_element_by_xpath("/html/body/div[20]/div/div[1]/div/div[1]/div[3]/div[2]/ul/li[1]/div[1]").text
#print("Số người nhiễm: ", Number)
#print(driver.find_element_by_class_name("statistic_number red"))
# close the browser
# driver.close()
# print("sample test case successfully completed")