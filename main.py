import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

# Counter variable
iteration = 1

# Infinite loop
while True:
    try:
        # Configure the web driver (e.g., ChromeDriver)
        driver = webdriver.Chrome()

        # Open the website
        url = "https://fan.at/news/64b28755838ec41ca02b51a1"
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

        # Click on the "Sturm" button
        sturm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sturm')]"))
        )
        sturm_button.click()

        # Find the radio button for "Ali Moghadam Shad" and click it
        moghadam_shad_radio_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-base-container/div[1]/div/news-detail/div/div[1]/div[1]/news-list-item/app-news-link/div/div[2]/div/lib-news-text/p[3]/fanat-widget/div/app-tab-group/app-tab[4]/div/app-voting-section/div/app-voting-item[13]/div/div/div[1]"))
        )
        moghadam_shad_radio_button.click()

        # Scroll down the page
        driver.execute_script("window.scrollBy(0, 500)")

        # Find the "Mittelfeld" button
        mittelfeld_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Mittelfeld')]"))
        )

        # Scroll to the "Mittelfeld" button
        actions = ActionChains(driver)
        actions.move_to_element(mittelfeld_button).perform()

        # Click on the "Mittelfeld" button
        mittelfeld_button.click()

        # Find the radio button for "Iulian Puhace" and click it
        puhace_radio_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Iulian Puhace')]/ancestor::div[@class='title-container']"))
        )
        puhace_radio_button.click()

        # Scroll down the page
        driver.execute_script("window.scrollBy(0, 500)")

        # Find the "Abstimmen" button
        abstimmen_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-base-container/div[1]/div/news-detail/div/div[1]/div[1]/news-list-item/app-news-link/div/div[2]/div/lib-news-text/p[3]/fanat-widget/app-voting-navigation/div/div[2]/button"))
        )
        abstimmen_button.click()

        # Perform any desired actions on the resulting page
        # You can add additional code here to interact with the page, extract data, etc.

    except TimeoutException:
        print("Abstimmen button not found within the given timeout. Proceeding to the next iteration.")

    # Close the browser window
    driver.quit()

    # Print iteration number and timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Iteration: {iteration} - Timestamp: {current_time}")

    # Increment the iteration counter
    iteration += 1

    # Wait for 5 minutes and 1 second before the next iteration
    time.sleep(301)

# The code will keep running in an infinite loop until manually stopped.
