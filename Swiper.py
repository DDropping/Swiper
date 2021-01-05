# Sign into amazon account

# Find the product (within price range)

# Wait until the product is available

# Add to cart

# Add payment methon (if applicable)

# checkout

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import presence_of_element_located
# from random import randict, randrange
# import time
# import random

# PATH = "C:\Program Files (x86)\chromedriver.exe"
# WEBPAGE = "https://www.amazon.com/ref=nav_logo"
# driver = webdriver.Chrome(PATH)

# driver.get(WEBPAGE)

# search = driver.find_element_by_name("nav-logo-sprites")
# driver.find_element(By.ID, "twotabsearchtextbox").send_keys(
#     "cheese" + Keys.RETURN)
# search.send_keys("logitech g pro superlight")
# search.send_keys(Keys.RETURN)

# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "nav-subnav"))
#     )
#     print(main.text)
# except:
#     driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from random import randint, randrange
import time
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"
WEBPAGE = "https://www.amazon.com/Logitech-Superlight-Wireless-Gaming-Mouse/dp/B087LP6F4Y/ref=sr_1_2?dchild=1&keywords=g%2Bpro%2Bsuperlight&qid=1609189487&sr=8-2&th=1"
USER_EMAIL = "<user email>"
USER_PASSWORD = "<user password>"

driver = webdriver.Chrome(PATH)
driver.get(WEBPAGE)

# click login button
try:
    loginButton = WebDriverWait(driver, 10).until(
        presence_of_element_located((By.ID, "nav-link-accountList"))
    )
    loginButton.click()
except:
    driver.close()

# enter email and password
try:
    # email
    email_field = WebDriverWait(driver, 10).until(
        presence_of_element_located((By.ID, "ap_email"))
    )
    email_field.send_keys(USER_EMAIL)

    continue_button = WebDriverWait(driver, 10).until(
        presence_of_element_located((By.ID, "continue"))
    )
    continue_button.click()

    # password
    password_field = WebDriverWait(driver, 10).until(
        presence_of_element_located((By.ID, "ap_password"))
    )
    password_field.clear()
    password_field.send_keys(USER_PASSWORD)

    signin_button = WebDriverWait(driver, 10).until(
        presence_of_element_located((By.ID, "signInSubmit"))
    )
    signin_button.click()
except:
    driver.close()


# check if product is available
def check_if_available():
    try:
        buy_now_button = WebDriverWait(driver, 1).until(
            presence_of_element_located((By.ID, "buy-now-button"))
        )
    except:
        driver.refresh()
        check_if_available()


# keep refreshing page until 'buy now' option is available
check_if_available()

# click buy now
buy_now_button = WebDriverWait(driver, 3).until(
    presence_of_element_located((By.ID, "buy-now-button"))
)
buy_now_button.click()

# place order
place_order_button = WebDriverWait(driver, 3).until(
    presence_of_element_located((By.ID, "turbo-checkout-pyo-button"))
)
place_order_button.click()
