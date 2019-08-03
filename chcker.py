import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import subprocess

def main():
    # /Users/milind/ItsCracker/chromedriver
    # /C:\Users\Eric Ahn\Desktop\yale\chromedriver
    driver = webdriver.Chrome(executable_path=r"\Users\Eric Ahn\Desktop\yale\chromedriver.exe")
    driver.get("https://accounts.google.com/signin/v2/identifier?service=grandcentral&passive=1209600&continue=https%3A%2F%2Fvoice.google.com%2Fsignup&followup=https%3A%2F%2Fvoice.google.com%2Fsignup&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    time.sleep(20)
    driver.get("https://apps.admissions.yale.edu/portal/on_campus_interviews")
    while(True):
        driver.refresh()
        numOfAvailables = len(driver.find_elements_by_class_name("available"))
        if(numOfAvailables>1):
            break
        time.sleep(600)
    ericPhone = "https://voice.google.com/u/0/messages?itemId=t.%2B16783341607"
    driver.get(ericPhone)
    time.sleep(15)
    elem = driver.find_element_by_id("input_1")
    elem.send_keys("Yale Interview is available")
    elem.send_keys(Keys.ENTER)
    elem.send_keys(Keys.RETURN)



if __name__ == "__main__":
    main()