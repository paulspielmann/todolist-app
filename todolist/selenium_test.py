from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from random import randint
import datetime
from time import sleep

# Initialize the WebDriver
# driver = webdriver.Chrome(keep_alive=True)
driver = webdriver.Firefox()

# Navigate to the URL
driver.get("http://localhost:5000/")
sleep(1)
# Find and click the link named "Create task"
create_task_link = driver.find_element(By.LINK_TEXT, "Create task")
create_task_link.click()
sleep(1)
# Find the input fields and fill them with appropriate values
name_field = driver.find_element(By.NAME, "name")
#current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
text_to_write = f'Test {randint(1, 100_000_000)}'
for c in text_to_write:
    name_field.send_keys(c)
    sleep(randint(1, 100) / 500.0)
name_field.send_keys(" -- Ce texte va apparaître instantanément")
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
"""Maintenant, je suis sur la page /tasks, je veux vérifier que ma tâche est bien créée avec les paramètres que j'ai

j'ai deux variables qui m'indiquent des choses utiles:
- priorities
- text_to_write

Que faire ??!?!?
"""
# todo: complete that.
tasks_candidates = driver.find_elements(By.CSS_SELECTOR, 'div.ca-ne-marchera-pas-ca')

# Close the WebDriver

driver.quit()
