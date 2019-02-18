from selenium import webdriver
import time
url = 'https://google.com/'
browser = webdriver.Chrome(r'C:\Users\jweif\Downloads\chromedriver_win32\chromedriver.exe')  #if use chrome download chromedriver from google, 

time.sleep(5)
browser.get(url)

time.sleep(5)
searchBox = browser.find_element_by_css_selector(r'#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input')
#elem = browser.find_element_by_name('q')
searchBox.send_keys('where is Trump today')
time.sleep(5)
searchBox.submit()
time.sleep(5)
firstResult = browser.find_element_by_css_selector('#rso > div:nth-child(1) > div > div > div > div.r > a > h3')
firstResult.click()

'''
#rso                                    #<div id='ros'>
#rso > div:nth-child(1) > div
#rso > div:nth-child(1) > div > div     #div data-hveid ='CAcQAA'
#rso > div:nth-child(1) > div > div > div.rc
#rso > div:nth-child(1) > div > div > div.rc > div.r
#rso > div:nth-child(1) > div > div > div.rc > div.r > a
#rso > div:nth-child(1) > div > div > div > div.r > a > h3


browser.back()
broswer.forward()
broswer.refresh
someButton = browser.find_element_by_css_selector(r'')
someButton.click()
'''
#browser.quit()
