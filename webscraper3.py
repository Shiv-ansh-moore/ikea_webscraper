from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

i=2

with open ("product_links.txt", "r") as file:
    for links in file:
        url = links
        if url.endswith("\n"):
            url = url[:-1]
        driver.get(url)
        time.sleep(i)
        try:
            accept_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_button.click()
        except:
            pass  # If no cookie banner is present, continue without error
        try:
            title = driver.find_element(By.XPATH, "//*[@id=\"pip-buy-module-content\"]/div[1]/div[1]/div[1]/div/span/h1/div/div[1]/span[1]").text
            price = driver.find_element(By.XPATH, "//*[@id=\"pip-buy-module-content\"]/div[1]/div[1]/div[2]/div/span/span[1]/span/span[2]").text
            header_description = driver.find_element(By.XPATH, "//*[@id=\"pip-buy-module-content\"]/div[1]/div[1]/div[1]/div/span/h1/div/div[1]/span[2]/span").text
            summary_description  = driver.find_element(By.XPATH, "//*[@id=\"content\"]/div/div[1]/div/div[2]/div[3]/div[1]/div/p").text
            product_details_button=driver.find_element(By.XPATH, "//*[@id=\"pip-product-information-section-list-0\"]/button")
            product_details_button.click()
            time.sleep(1)
            product_details = driver.find_element(By.XPATH, "//*[@id=\"range-modal-mount-node\"]/div/div[3]/div/div[2]/div/div/div").text
            try:
                good_to_know_button = driver.find_element(By.XPATH, "//*[@id=\"product-details-good-to-know\"]/div[1]/button")
                good_to_know_button.click()
                good_to_know = driver.find_element(By.XPATH, "//*[@id=\"SEC_product-details-good-to-know\"]/div/div").text
            except:
                good_to_know = ""
            time.sleep(1)
            try:
                matarials_and_care_button = driver.find_element(By.XPATH, "//*[@id=\"product-details-material-and-care\"]/div[1]/button")
                matarials_and_care_button.click()
                time.sleep(1)
                matarials_and_care = driver.find_element(By.XPATH, "//*[@id=\"SEC_product-details-material-and-care\"]/div").text
            except:
                matarials_and_care = ""
            exit_button = driver.find_element(By.XPATH, "//*[@id=\"range-modal-mount-node\"]/div/div[3]/div/div[1]/button")
            exit_button.click()
            time.sleep(1)
            try:
                second_button = driver.find_element(By.XPATH, "//*[@id=\"pip-product-information-section-list-1\"]/button")
                second_button.click()
                time.sleep(1)
                x = driver.find_element(By.XPATH, "//*[@id=\"range-modal-mount-node\"]/div/div[3]/div/div[2]/div/div").text
                if x[1] == "h":
                    what_included = x
                    exit_button = driver.find_element(By.XPATH, "//*[@id=\"range-modal-mount-node\"]/div/div[3]/div/div[1]/button")
                    exit_button.click()
                    time.sleep(1)
                    weight_and_measeurment_button = driver.find_element(By.XPATH, "//*[@id=\"pip-product-information-section-list-2\"]/button")
                    weight_and_measeurment_button.click()
                    time.sleep(1)
                    weight_and_measeurment = driver.find_element(By.XPATH, "//*[@id=\"range-modal-mount-node\"]/div/div[3]/div/div[2]/div/div").text
                else:
                    weight_and_measeurment = x
                    what_included = ""
            except:
                pass
            with open ("sofas.md", "a") as file:
                file.write(f"### Item: {title}  \n")
                file.write(f"- **url**: {url}  \n")
                file.write(f"- **Price**: {price}  \n")
                file.write(f"- **Header Description**: {header_description}  \n")
                file.write(f"- **Summary Description**: {summary_description}  \n")
                file.write(f"- **Product Details**: {product_details}  \n")
                if good_to_know != "":
                    file.write(f"- **Good to know**: {good_to_know}  \n")
                if matarials_and_care != "":
                    file.write(f"- **Materials and Care**: {matarials_and_care}  \n")
                if what_included != "":
                    file.write(f"- **What's included**: {what_included}  \n")
                file.write(f"- **Weight and measurement**: {weight_and_measeurment}  \n")
            if i == 2:
                i = 0
        except:
            pass