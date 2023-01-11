from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r'./chromedriver')

def betfair_horse_racing_sequence():

    def init_sequence(uname, pword):
        # cookie clicker
        l = driver.find_element("xpath", "//div[@class = 'ssc-cp-right ssc-cp-bottom']")
        l.click()

        # username input
        l = driver.find_element("xpath", "//input[@id = 'ssc-liu']")
        l.send_keys(uname)

        # password input
        l = driver.find_element("xpath", "//input[@id = 'ssc-lipw']")
        l.send_keys(pword)

        # login clicker
        l = driver.find_element("xpath", "//input[@id = 'ssc-lis']")
        l.click()

        sleep(15)


    def find_saddle_nums():
        # finds the list of saddlenumbers and clicks the specific saddle numbers lay cell
        saddlenumbers = (driver.find_elements("xpath", "//p[@class = 'saddle-cloth']"))
        saddlenums = []
        for i in saddlenumbers:
            saddlenums.append(int(i.text))
        return saddlenums

    def find_saddle_number_pos(saddle_number):
        # finds the list of saddlenumbers and clicks the specific saddle numbers lay cell
        saddlenumbers = (driver.find_elements("xpath", "//p[@class = 'saddle-cloth']"))
        index = 0
        for i in saddlenumbers:
            if int(i.text) == saddle_number:
                return index
            index += 1

    def find_liquidity(saddle_num_row):
        # prints the liquidity of the first lay cell
        l = driver.find_elements("xpath", "//td[@class = 'bet-buttons lay-cell first-lay-cell']")[saddle_num_row]
        i = 0
        while i < len(l.text):
            if (l.text[i] == '$'):
                i += 1
                return l.text[i:]
            else:
                i += 1

    def click_specified_horse(saddle_num_row):
        l = driver.find_elements("xpath", "//td[@class = 'bet-buttons lay-cell first-lay-cell']")[saddle_num_row]
        l.click()

    def place_bet(betsize, liq):
        if betsize <= int(liq):
            l = driver.find_element("xpath", "//input[@maxlength = '9']")
            print(l.is_displayed())
            print(l.is_enabled())
            l.click()
            l.send_keys(betsize)

            l = driver.find_element("xpath", "//button[@type = 'submit' and @class = 'DFMoS Qe-26 AUP11 _8USKG ge-UC']")
            l.click()

    def betfairtest():
        # maximize browser
        driver.maximize_window()
        driver.get('https://www.betfair.com.au/exchange/plus/horse-racing/market/1.208135441?nodeId=31994269')
        # driver.execute_script("arguments[0].click();", l)
        for _ in range(10):
            sleep(10)
            init_sequence("username", "password")
            row_num = find_saddle_number_pos(1)
            liq = find_liquidity(row_num)
            click_specified_horse(row_num)
            betsize = 1
            place_bet(betsize, liq)
            sleep(1)
        driver.quit()

    print(betfairtest())


#print(betfair_horse_racing_sequence())
