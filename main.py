import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Counter variable
iteration = 1

# Infinite loop
while True:
    try:
        # Configure the web driver (e.g., ChromeDriver)
        driver = webdriver.Chrome()

        # Open the website
        url = "https://fan.at/news/64ba8158306eeb5a7062db10"
        driver.get(url)

        # Wait for 2 seconds
        time.sleep(2)

        # Find the "Alles akzeptieren" button
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='cookiescript_accept' and text()='Alles akzeptieren']"))
        )
        accept_button.click()

        # Wait for the cookie pop-up to disappear
        WebDriverWait(driver, 10).until_not(
            EC.visibility_of_element_located((By.ID, "cookiescript_accept"))
        )

        # Find the radio button for "Ali Moghadam Shad" and click it
        moghadam_shad_radio_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Ali Moghadam Shad')]/ancestor::div[@class='title-container']"))
        )
        moghadam_shad_radio_button.click()

        # Find the "Abstimmen" button using the provided HTML
        abstimmen_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Abstimmen')]"))
        )
        abstimmen_button.click()

        # Wait for 3 seconds after clicking the "Abstimmen" button
        time.sleep(3)

        # Perform any desired actions on the resulting page
        # You can add additional code here to interact with the page, extract data, etc.

    except TimeoutException:
        print("Abstimmen button not found within the given timeout. Waiting for the next iteration.")
        # Close the browser window
        driver.quit()
        # Wait for 5 minutes and 1 second before the next iteration
        time.sleep(301)
        continue
    finally:
        # Close the browser window
        driver.quit()

        # Print iteration number and timestamp if no error caught
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Iteration: {iteration} - Timestamp: {current_time}")

        # Increment the iteration counter if no error caught
        iteration += 1

        # Wait for 5 minutes and 1 second before the next iteration
        time.sleep(301)

# The code will keep running in an infinite loop until manually stopped.

