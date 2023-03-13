import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from decimal import Decimal
import argparse

stocks = [
    "https://finance.vietstock.vn/TCB-ngan-hang-tmcp-ky-thuong-viet-nam.htm"
]

tcb = stocks[0]

def webdriver_setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    return driver

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='An example argparse program.')
    parser.add_argument('-p', '--price', help='target price', required=True)
    args = parser.parse_args()
    target_price = Decimal(args.price)

    driver = webdriver_setup()
    driver.get(tcb)
    stock_price_as_text = driver.find_element(By.ID, "stockprice").text
    stock_price_in_decimal = Decimal(stock_price_as_text.replace(",", "."))
    print(stock_price_in_decimal)
    if stock_price_in_decimal < target_price:
        subprocess.run(["say", "TCB hit target price. Place order now"])

