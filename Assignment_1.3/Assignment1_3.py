#1 Chiranjit Mandal
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.ID,"name").send_keys("Arka Pan")

driver.find_element(By.NAME,"input1").send_keys("very good")

time.sleep(2)
driver.find_element(By.TAG_NAME,"input").clear()
time.sleep(2)

driver.find_element(By.CLASS_NAME,"form-check-input").click()
driver.find_element(By.LINK_TEXT,"Udemy Courses").click()


time.sleep(5)
driver.quit()


              #2 Akash Mandal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time



driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()


links = driver.find_elements(By.TAG_NAME, "a")


print("Total number of links:", len(links))


for link in links:
    print(link.text)

time.sleep(5)

driver.quit()

             #3 Arka Pan
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

elements=driver.find_elements(By.CSS_SELECTOR, "*[id^='a']")

for i in elements:
    print(i.text)


time.sleep(2)
driver.quit()

                 #4 Arka Pan
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.CSS_SELECTOR,"div.form-group > input.form-control").send_keys("Chiranjit")

driver.find_element(By.CSS_SELECTOR,"div.widget-content > ul > li > a[href*='udemy']").click()

time.sleep(2)
driver.quit()
