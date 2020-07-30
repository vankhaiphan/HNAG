from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
import time

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
# driver = webdriver.firefox()
#driver = webdriver.ie()
print("Thực thi kiểm thử")

# phong to cua so trinh duyet
# driver.maximize_window()

# truy cap den dia chi url
driver.get("http://127.0.0.1:8000/")
time.sleep(1)

# hien thi tieu de cua trang hien tai
title = driver.title
print("Trang web hiện tại là: ", title)

# dien username
username = driver.find_element_by_name("username")
username.send_keys("khai")

# dien password
password = driver.find_element_by_name("password")
password.send_keys("khaikhai")

# tim va nhan nut login
button = driver.find_element_by_name("login")
button.click()

# neu dang nhap khong thanh cong -> trang web hien popup
# -> hien thi popup va bam dong y popup
try:
    WebDriverWait(driver, 1).until(expected_conditions.alert_is_present())
    alert = driver.switch_to_alert
    print("Đăng nhập thất bại")
    time.sleep(2)
    print("Nội dung thông báo trên trang web: ", Alert(driver).text)
    Alert(driver).accept()
except TimeoutException:
    # kiem tra tieu de moi sau khi dang nhap
    new_title = driver.title
    print("Trang web hiện tại là: ", new_title)

    if (new_title == "Hôm nay ăn gì?"):
        print("Đăng nhập và chuyển hướng thành công")
        print("Sau 5s sẽ thực hiện đăng xuất")
        time.sleep(5)
        print("Thực hiện đăng xuất")
        button = driver.find_element_by_xpath("/html/body/div/nav/form[2]/button")
        button.click()
        try:
            WebDriverWait(driver, 1).until(expected_conditions.alert_is_present())
            alert = driver.switch_to_alert
            print("Đăng xuất thành công")
            print("Nội dung thông báo trên trang web: ", Alert(driver).text)
            time.sleep(2)
            Alert(driver).accept()
        except TimeoutException:
            print("Đăng xuất không thành công, kiểm tra lại đường dẫn")
    else:    
        print("Đăng nhập thành công nhưng chuyển hướng sai địa chỉ")

# dong trinh duyet
driver.close()
print("Kiểm thử hoàn thành")