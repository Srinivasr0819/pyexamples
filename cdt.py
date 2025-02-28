from selenium import webdriver
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Open Google.com
driver.get("https://www.google.com")

# Wait for 3 seconds
time.sleep(3)

# Close the browser
driver.quit()
