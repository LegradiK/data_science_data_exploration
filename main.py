import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless") # run in headless mode
driver=webdriver.Chrome(service=Service(ChromeDriveManager().install()))

URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"

page = 1

# while page <= 31:
