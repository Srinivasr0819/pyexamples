from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
 # Update with the actual path
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

time.sleep(2)  # Wait for the page to load

# Click on 'Gmail' link
gmail_link = driver.find_element(By.LINK_TEXT, "Gmail")
gmail_link.click()

time.sleep(2)  # Wait for the page to load

driver.back()

time.sleep(2)  # Wait for the page to reload

# Click on 'Images' link
images_link = driver.find_element(By.LINK_TEXT, "Images")
images_link.click()

time.sleep(2)  # Wait for the page to load

# Enter text in the search box
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("srinivasa rao gadesula")
search_box.send_keys(Keys.RETURN)

time.sleep(20000)  # Wait for search results

print("Thank you!")

driver.quit()  # Close the browser
