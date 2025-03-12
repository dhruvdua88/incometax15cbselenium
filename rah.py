from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import ttk
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import ttk
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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


def select_dropdown_value(driver, dropdown_xpath, option_xpath):
    # Click the dropdown to open options
    dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
    dropdown.click()

    # Get all dropdown options
    options = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "mat-option")))
    dropdown_values = [option.text for option in options]  # Extract text from each option

    # GUI for user selection
    def select_option():
        selected_option = search_var.get()
        root.destroy()  # Close the GUI

        # Click the selected option in Selenium
        selected_xpath = f"//mat-option/span[contains(text(), '{selected_option}')]"
        option_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, selected_xpath)))
        option_element.click()
        print(f"✅ Selected: {selected_option}")

    # Live search function
    def update_dropdown(*args):
        search_text = search_var.get().lower()
        filtered_values = [val for val in dropdown_values if search_text in val.lower()]
        combo["values"] = filtered_values

    # Tkinter GUI
    root = tk.Tk()
    root.title("Select an Option")
    root.geometry("350x200")  # Set window size

    label = tk.Label(root, text="Search & Select:")
    label.pack(pady=5)

    # Entry field for searching
    search_var = tk.StringVar()
    search_var.trace("w", update_dropdown)  # Update dropdown on typing
    entry = tk.Entry(root, textvariable=search_var, width=30)
    entry.pack(pady=5)

    # Dropdown list
    combo = ttk.Combobox(root, values=dropdown_values, state="readonly", width=27)
    combo.pack(pady=5)
    combo.current(0)  # Default to first option

    button = tk.Button(root, text="OK", command=select_option)
    button.pack(pady=10)

    root.mainloop()



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

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-select-form-details/div[3]/div[1]/form/mat-card/div[1]/div[2]/div/fieldset/mat-radio-group/mat-radio-button[1]/div/label")))
element.click()

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

time.sleep(1)




#################################### Enter 15CB details -CERTIFICATION ###################################


##Click Certification 
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-form15cb/div[2]/div[2]/div[2]/mat-accordion/div/mat-expansion-panel/mat-expansion-panel-header/span[1]/div/div")))
element.click()

time.sleep(1)  # Wait 1 second


# Click the dropdown to open options
dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-form15cb/div[2]/div[2]/div[3]/mat-accordion/div/mat-expansion-panel/div/div/div[1]/div/iec-select[1]/div/mat-form-field/div[1]/div/div[2]/mat-select")))
dropdown.click()

# Select the option containing "We"
option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[contains(text(), 'We')]")))
option.click()

time.sleep(1)  # Wait 1 second


import pyautogui
import time

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.press('down')
pyautogui.press('down')

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.press('down')
pyautogui.press('down')

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.write("FORESCOUT")

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-form15cb/div[2]/div[2]/div[3]/mat-accordion/div/div/div[2]/button")))
element.click()

time.sleep(1)  # Wait 1 second


#################################### Enter 15CB details -RECIPIENT DETAILS ###################################
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-form15cb/div[2]/div[2]/div[2]/mat-accordion/mat-expansion-panel[1]/mat-expansion-panel-header/span[1]")))
element.click()

time.sleep(1)  # Wait 1 second


# DropDown

# Click the dropdown to open options
dropdown_xpath = "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-form15cb/div[2]/div[2]/div[3]/mat-accordion/mat-expansion-panel[1]/div/div/div[3]/iec-address/div/div[1]/div/iec-select/div/div[2]/mat-form-field/div[1]/div/div[2]/mat-select"

dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown.click()

# Select "Angola"
option_xpath = "//mat-option/span[contains(text(), 'United States Of America')]"
option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
option.click()


time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.write("address1")

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.write("address2")

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.write("999999")

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.write("Foreign")

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.write("Foreign")

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.write("Foreign")

time.sleep(1)  # Wait 1 second

# Click the button
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-form15cb/div[2]/div[2]/div[3]/mat-accordion/div[2]/div[2]/button")))
element.click()

time.sleep(1)  # Wait 1 second

#################################### Enter 15CB details -REMITTANCE  DETAILS ###################################

##Click remittance details 




# Click the dropdown to open options
dropdown_xpath = "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-form15cb/div[2]/div[2]/div[3]/mat-accordion/mat-expansion-panel[2]/div/div/div[1]/div[1]/iec-select/div/mat-form-field/div[1]/div/div[2]/mat-select"

dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown.click()

# Select "United States Of America"
option_xpath = "//mat-option/span[contains(text(), 'United States Of America')]"
option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
option.click()

time.sleep(1) 

# Click the dropdown to open options
dropdown_xpath = "/html/body/app-root/div[1]/div[4]/app-dashboard/app-file-income-tax-forms/app-form15cb/div[2]/div[2]/div[3]/mat-accordion/mat-expansion-panel[2]/div/div/div[2]/iec-select/div/mat-form-field/div[1]/div/div[2]/mat-select"

dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown.click()

# Select "USD"
option_xpath = "//mat-option/span[contains(text(), 'USD')]"
option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
option.click()

time.sleep(1) 


import pyautogui
import time

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.write("100")

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.write("1000")

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.write("CITI0000002")

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')

time.sleep(1)  # Wait 1 second
pyautogui.write("9999999")

time.sleep(1)  # Wait 1 second
pyautogui.press('tab')










#################################### Logout  ###################################

#element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/button[3]/span/span")))
#element.click()




















# Optional: Wait for a few seconds to ensure the login is processed










input("Press Enter to exit...")  # Keeps the browser open until you press Enter

# Close browser
driver.quit()
