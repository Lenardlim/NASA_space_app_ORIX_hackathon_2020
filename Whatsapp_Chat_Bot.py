from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
import time
import math


class Message():
    def __init__(self, user, message):
        self.user = user
        self.message = message

    def __eq__(self, other):
        return self.message == other.message


if os.name == "nt":
    driverPath = "driver/chromedriver_2.24.exe"
    dataPath = "Data"
else:
    driverPath = "driver/chromedriver"
    dataPath = "Data/ChatBot"


options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=" + dataPath)
driver = webdriver.Chrome(chrome_options=options, executable_path=driverPath)
driver.get('https://web.whatsapp.com')
driver.execute_script("window.open('','_blank');")
driver.switch_to_window(driver.window_handles[1])
driver.get('http://www.square-bear.co.uk/mitsuku/nfchat.htm')
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

run=[] #script link
chatHistory = []
replyQueue = []
firstRun = True

print("Starting...")

## Script removed


# DEPRECATED
    #     # print("Querries =", len(replyQueue))
    #
    #     firstRun = False
    #     if len(replyQueue) == 0:
    #         continue
    #
    #     # Switch tabs and get Response
    #     driver.switch_to_window(driver.window_handles[1])
    #     driver.switch_to_default_content()
    #     driver.switch_to.frame('input')
    #     textField = driver.find_elements_by_tag_name("input")[1]
    #
    #     responses = []
    #
    #     for message in replyQueue:
    #
    #         textField.send_keys(message.message[1:] + Keys.ENTER)
    #         responseBody = None
    #         fontTags = driver.find_elements_by_tag_name("font")
    #
    #         for tag in fontTags:
    #             if tag.get_attribute("face") == "Trebuchet MS,Arial" and tag.get_attribute("color") == "#000000":
    #                 responseBody = tag
    #                 break
    #
    #         start = responseBody.text.find("Μitsuku")
    #         end = responseBody.text.find("You", 4)
    #         firstName = message.user.split(' ')[0]
    #         resp = responseBody.text[start + 10:end - 2]
    #         print(start, end, repr(resp))
    #         responses.append("@" + firstName + " : " + resp)
    #
    #     replyQueue = []
    #     # Switch tabs and reply on whatsapp
    #     driver.switch_to_window(driver.window_handles[0])
    #     inputMessage = messageDiv.find_element_by_class_name(
    #         'pluggable-input-body')
    #
    #     for response in responses:
    #         lines = response.split('\n')
    #         for line in lines:
    #             inputMessage.send_keys(line)
    #             inputMessage.send_keys(Keys.SHIFT, Keys.ENTER)
    #         inputMessage.send_keys(Keys.ENTER)
    #
    # except Exception as e:
    #     exc_type, exc_obj, exc_tb = sys.exc_info()
    #     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #     print(exc_type, fname, exc_tb.tb_lineno)
