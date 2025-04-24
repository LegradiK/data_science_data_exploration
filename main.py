import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Set up the driver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the URL
URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
driver.get(URL)
time.sleep(5)

# Store results here
results = []

# Loop through pages 1 to 31
for page in range(1, 32):
    print(f"Scraping Page {page}...")
    time.sleep(3)  # Let the table load

    # Find table rows
    rows = driver.find_elements(By.CSS_SELECTOR, "table.data-table tbody tr")

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 5:
            rank = cols[0].text
            major = cols[1].text
            degree_type = "Bachelor's Degree"
            early_career_pay = cols[3].text
            mid_career_pay = cols[4].text


            results.append({
                "Rank": rank,
                "Major": major,
                "Degree": degree_type,
                "Early Career Pay": early_career_pay,
                "Mid Career Pay": mid_career_pay
            })

    # Try to click the "Next" button
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'a.pagination__next-btn')
        if "disabled" in next_button.get_attribute("class"):
            print("Reached last page.")
            break
        else:
            next_button.click()
    except NoSuchElementException:
        print("Next button not found.")
        break

# Close browser
driver.quit()
df = pd.DataFrame(results)

df["Early Career Pay"] = df["Early Career Pay"].replace('[\$,]', '', regex=True).astype(float)
df["Mid Career Pay"] = df["Mid Career Pay"].replace('[\$,]', '', regex=True).astype(float)

df.to_csv('college.csv')
