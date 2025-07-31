from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import csv
import re

USERNAME = "your_email@gmail.com"  
PASSWORD = "your_password"
MAX_PAGES = 100            


def random_delay(min_sec=2.5, max_sec=5.5):
    delay = random.uniform(min_sec, max_sec)
    print(f"⏳ Waiting {round(delay, 2)}s")
    time.sleep(delay)

def is_valid_name(name):
    """
    Temporarily relaxed name filter:
    - At least 2 words
    """
    if not name:
        return False
    if len(name.split()) < 2:
        return False
    return True


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)


driver.get("https://www.linkedin.com/login")
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
random_delay()


search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Search')]")))
search_box.send_keys("Hospitals")
search_box.send_keys(Keys.RETURN)
random_delay(4, 6)


try:
    people_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='People']")))
    people_button.click()
    print("✅ 'People' filter clicked.")
except:
    print("❌ Couldn't find People filter")
random_delay()


all_names = set()
for page in range(1, MAX_PAGES + 1):
    print(f"\n🔄 Scraping page {page}")
    random_delay()
    name_elements = driver.find_elements(By.XPATH, "//span[contains(@class, 'entity-result__title-text')]/a//span")
    if not name_elements:
        name_elements = driver.find_elements(By.XPATH, "//span[@dir='ltr']")
    print(f"🧪 Found {len(name_elements)} elements on page {page}")

    for span in name_elements:
        name = span.text.strip()
        print("🧾 Raw:", name)
        if is_valid_name(name):
            all_names.add(name)
            print("✅", name)

    try:
        next_btn = driver.find_element(By.XPATH, "//button[@aria-label='Next")
        driver.execute_script("arguments[0].click();", next_btn)
    except:
        print("❌ No next button or end of pages")
        break


with open("linkedin_names_only.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Full Name"])
    for name in sorted(all_names):
        writer.writerow([name])

print(f"\n✅ Scraping complete. Total names: {len(all_names)}")
driver.quit()
