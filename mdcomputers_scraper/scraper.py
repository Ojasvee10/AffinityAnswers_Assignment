from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

search = input("Enter product to search: ")

url = f"https://mdcomputers.in/?route=product/search&search={search.replace(' ', '+')}"

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get(url)

time.sleep(5)

products = driver.find_elements(By.CSS_SELECTOR, "div.product-grid-item")

print(f"Found {len(products)} products")

data = []

for product in products:

    # Product Name
    try:
        name = product.find_element(
            By.CSS_SELECTOR,
            "h3.product-entities-title a"
        ).text
    except:
        name = "N/A"

    # Product Link
    try:
        link = product.find_element(
            By.CSS_SELECTOR,
            "h3.product-entities-title a"
        ).get_attribute("href")
    except:
        link = "N/A"

    # Price
    try:
        price = product.find_element(
            By.CSS_SELECTOR,
            "span.ins span.amount"
        ).text
    except:
        try:
            price = product.find_element(
                By.CSS_SELECTOR,
                "span.price span.amount"
            ).text
        except:
            price = "N/A"

    print(name)
    print(price)
    print(link)
    print("-" * 60)

    data.append({
        "Product Name": name,
        "Price": price,
        "Product Link": link
    })

driver.quit()

df = pd.DataFrame(data)

df.to_csv("output.csv", index=False)

print("\nSaved to output.csv")