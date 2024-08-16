from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
url = "https://www.ikea.com/ie/en/cat/sofas-fu003/"

# Open the webpage
driver.get(url)

# Handle cookie banner if present
try:
    accept_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_button.click()
except:
    pass  # If no cookie banner is present, continue without error

# Function to extract product links
def extract_links():
    links = []
    products = driver.find_elements(By.CLASS_NAME, "plp-product__image-link")
    for product in products:
        links.append(product.get_attribute("href"))
    return links

# Open a file to save the links
with open("product_links.txt", "w") as file:
    while True:
        # Extract and save the product links
        product_links = extract_links()
        for link in product_links:
            file.write(link + "\n")
        
        # Try to click the "Show more" button
        try:
            wait = WebDriverWait(driver, 20)
            show_more_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Show more")))

            # Scroll into view and click
            driver.execute_script("arguments[0].scrollIntoView(true);", show_more_button)
            driver.execute_script("arguments[0].click();", show_more_button)
        except:
            print("No more 'Show more' buttons to click.")
            break

# Wait a bit to ensure everything is loaded
time.sleep(20)

# Clean up
driver.quit()
