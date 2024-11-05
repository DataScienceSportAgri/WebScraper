import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def initialize_browser():
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    chromedriver_path = "C:/Program Files (x86)/chromedriver-win64/chromedriver.exe"

    # Check if ChromeDriver exists
    if not os.path.isfile(chromedriver_path):
        raise FileNotFoundError(f"ChromeDriver not found at {chromedriver_path}")

    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    option.add_argument("--headless")
    option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=option)

    return driver