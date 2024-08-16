from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
url = "https://www.ikea.com/ie/en/cat/sofas-fu003/"

driver.get(url)

# Handle cookie banner if present
try:
    accept_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_button.click()
except:
    pass  # If no cookie banner is present, continue without error

# Wait until the "Show more" button is clickable
while True:
    try:
        wait = WebDriverWait(driver, 20)
        show_more_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Show more")))

        # Scroll into view and click
        driver.execute_script("arguments[0].scrollIntoView(true);", show_more_button)
        driver.execute_script("arguments[0].click();", show_more_button)
    except:
        print("done maybe")
        break

time.sleep(20)
# Clean up
driver.quit()

