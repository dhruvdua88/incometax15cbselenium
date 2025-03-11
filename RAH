from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


##functions 

def click_with_retry(driver, xpath, max_attempts=10):
    """
    Tries to click an element multiple times if it fails.
    
    :param driver: Selenium WebDriver instance
    :param xpath: The XPath of the element to click
    :param max_attempts: Number of retry attempts (default = 10)
    """
    for attempt in range(max_attempts):
        try:
            element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
            print(f"✅ Clicked element successfully on attempt {attempt + 1}")
            return True  # Success, exit function
        except Exception as e:
            print(f"⚠️ Attempt {attempt + 1} failed, retrying in 1 second...")
            time.sleep(1)  # Wait 1 second before retrying

    print("❌ Element could not be clicked after multiple attempts.")
    return False  # All attempts failed




chrome_options = Options()

# ✅ Hide "Chrome is being controlled by automated test software" banner
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# ✅ Use a normal user profile (optional, but helps)
chrome_options.add_argument("C:\\Users\\pc\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_argument("--profile-directory=Profile 1")

# ✅ Disable bot detection techniques
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# Set ChromeDriver path
chromedriver_path = "C:\\Users\\pc\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service = Service(chromedriver_path)

# Start Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()


# Open the website
driver.get("https://eportal.incometax.gov.in/iec/foservices/#/login")

# Find input field using XPath and enter value
input_field = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div[3]/app-login/div/app-login-page/div/div[2]/div[1]/mat-form-field/div[1]/div/div[2]/input")
input_field.send_keys("ARCA531607")

# Find the button using XPath and click it
login_button = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div[3]/app-login/div/app-login-page/div/div[2]/div[1]/div[2]/button")
login_button.click()

time.sleep(2)

# Step 1: Wait for the checkbox to be clickable
checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[3]/app-login/div/app-password-page/div[1]/div[2]/div[1]/div[3]/mat-checkbox"))
)

# Step 2: Click the checkbox
checkbox.click()

# Step 4: Wait for the password field and enter password
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div[1]/div[3]/app-login/div/app-password-page/div[1]/div[2]/div[1]/div[4]/mat-form-field/div[1]/div/div[2]/input"))
)
password_field.send_keys("Arundua@001")

time.sleep(3)


# Wait for the login button and click it
click_with_retry(driver, "/html/body/app-root/div[1]/div[3]/app-login/div/app-password-page/div[1]/div[2]/div[1]/div[5]/button")


time.sleep(3)


#################################### Next Page after login ###################################

# Step 1: Click the first button (Navigation link)
first_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[1]/app-navbar/mat-toolbar/div/div/div[1]/a[2]/span[2]"))
)
first_button.click()

# Step 2: Click the second button (Popup button)
second_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/span/span/div/button"))
)
second_button.click()

# Step 3: Click the third button (Confirmation button)
third_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div/div/span[1]/span/button"))
)
third_button.click()

#################################### Form SEelction screen ###################################

# Step 1: Click the element

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/div/mat-card/div/mat-tab-group/mat-tab-header/div/div/div/div[3]"))
)

element.click()

# Step 2: Click 15CB


element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/div/mat-card/div/mat-tab-group/div/mat-tab-body[3]/div/div/div/mat-card/div[9]/div/mat-card/mat-card-content/div/div[2]")))
element.click()

time.sleep(3)

#################################### Enter basic 15CB information ###################################

# Wait for the radio button to be clickable
radio_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-select-form-details/div[3]/div[1]/form/mat-card/div[1]/div[2]/div/fieldset/mat-radio-group/mat-radio-button[1]/div/div/div[1]"))
)

# Click the radio button
radio_button.click()

time.sleep(1)


element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-select-form-details/div[3]/div[1]/form/mat-card/div[3]/div/div/mat-form-field/div[1]/div/div[2]/mat-select")))
element.click(); WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//mat-option[span[contains(text(),'2024-25')]]"))).click()

time.sleep(1)

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-select-form-details/div[3]/div[1]/div[3]/div[2]/button")))
element.click()

time.sleep(1)

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-instruction-screen/div/div[1]/div/div[1]/div[3]/div[2]/button")))
element.click()

time.sleep(1)


element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-form15cb/div[3]/div/div/div[2]/mat-form-field/div[1]/div/div[2]/input")))
element.send_keys("AADCR0731R")

time.sleep(1)


element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-form15cb/div[3]/div/div/div[3]/button")))
element.click()

#################################### Enter 15CB details  ###################################






















# Optional: Wait for a few seconds to ensure the login is processed










input("Press Enter to exit...")  # Keeps the browser open until you press Enter

# Close browser
driver.quit()
