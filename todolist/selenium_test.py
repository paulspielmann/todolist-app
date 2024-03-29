from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from random import randint
import datetime
from time import sleep

# Initialize the WebDriver
driver = webdriver.Chrome(keep_alive=True)

# Navigate to the URL
driver.get("http://localhost:5000/")
sleep(3)
# Find and click the link named "Create task"
create_task_link = driver.find_element(By.LINK_TEXT, "Create task")
create_task_link.click()

# Find the input fields and fill them with appropriate values
name_field = driver.find_element(By.NAME, "name")
current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
name_field.send_keys("Test - " + current_date_time)

sleep(1)
priority_field = Select(driver.find_element(By.NAME, "priority"))
# Selecting a priority option from dropdown by value (you may need to adapt this based on your HTML)
priorities = ['low', 'normal', 'urgent'][randint(0, 2)]
priority_field.select_by_value(priorities)
sleep(2)

# Submit the form
submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_button.click()

sleep(10)
# Close the WebDriver
driver.quit()
