
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import pyautogui

connect_btn_img = 'im/connect_btn_img.PNG'
add_note_btn_img = 'im/add_note_btn_img.PNG'
send_img = 'im/send_img.PNG'
next_pg_img = 'im/nextPg.PNG'

f=open('C:/Users/jweif/config558.py','r')
line=f.read()
credential = line.split(' ')

def current_nm_list(driver):
	actor_name_elms = driver.find_elements_by_class_name('actor-name')
	nm_ls = []
	for elm in actor_name_elms:
		nm = elm.get_attribute('innerHTML')
		nm_str_ls = nm.split(' ')

		if len(nm_str_ls[0]) > 1: 
			nm_ls.append(nm_str_ls[0])
		else:
			length=len(nm_str_ls)
			nm_ls.append(nm_str_ls[length-1])   
	return [nm_ls,actor_name_elms]


def set_window_size(w,h):
	print('current window size: ')
	print(driver.get_window_size())

	print('\nresizing window size to : %d x %d' % (w,h))
	driver.set_window_size(w,h)
	#driver.maximize_window()


def doconnect(name):
	time.sleep(2)
	
	connectPos = pyautogui.locateCenterOnScreen(connect_btn_img)
	if connectPos[1] > 315:
		return None

	pyautogui.moveTo(connectPos[0],connectPos[1],2)
	pyautogui.click()
	
	time.sleep(1)
	addNotePos = pyautogui.locateCenterOnScreen(add_note_btn_img)
	pyautogui.moveTo(addNotePos[0],addNotePos[1],2)
	pyautogui.click()
	
	time.sleep(1)
	pyautogui.typewrite('Hi '+ name + ', can i join your network? :) ',interval=0.2)

	time.sleep(1)
	sendImgPos = pyautogui.locateCenterOnScreen(send_img)
	pyautogui.moveTo(sendImgPos[0],sendImgPos[1],2)
	pyautogui.click()
	time.sleep(1)

print('Launch webdrive')
driver = webdriver.Chrome("C:/Users/jweif/Downloads/chromedriver_win32/chromedriver.exe")  #if use chrome download chromedriver from google, 
driver.get('https://linkedin.com/login')
assert "LinkedIn Log" in driver.title

time.sleep(1)
set_window_size(1280,720)
time.sleep(2)

driver.find_element_by_id('username').send_keys(credential[0])
driver.find_element_by_id('password').send_keys(credential[1])
sign_in_btn= driver.find_element_by_class_name('btn__primary--large')
assert 'Sign in' in sign_in_btn.get_attribute('innerHTML')
sign_in_btn.send_keys(Keys.RETURN)

user_ready = input('when you are in people search page, press enter')

current_elements = current_nm_list(driver)
name_list = current_elements[0]
name_elements_list = current_elements[1]

print(current_elements)
i = 0

while len(name_list) !=10:
	i +=1
	time.sleep(1)
	#driver.execute_script("return document.body.scrollHeight")
	#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	driver.execute_script("window.scrollTo(0,%d)" % (i*250))
	current_elements = current_nm_list(driver)
	name_list = current_elements[0]
	name_elements_list = current_elements[1]
	print(name_list)
	time.sleep(3) 
	if i >=7:
		break

print('name fetching complete, jumping to first connection')
time.sleep(3)

for i in range(0,len(name_elements_list)):	
	time.sleep(1)
	driver.execute_script("arguments[0].scrollIntoView();", name_elements_list[i])
	time.sleep(1)
	yoffset = driver.execute_script("return window.pageYOffset;")# 316 for i = 1, 440 for i=2
	driver.execute_script("window.scrollTo(0,%d)" % (yoffset-80))
	print('offset for next iteration : %d' % (yoffset))
	time.sleep(2)

	doconnect(name_list[i])


nextPgPos = pyautogui.locateCenterOnScreen(next_pg_img)
pyautogui.moveTo(nextPgPos[0],nextPgPos[1],2)
pyautogui.click()


'''

htmlsrc = driver.page_source

fo = open('text009.txt','w',encoding='utf8')
fo.write(htmlsrc)
fo.close()
'''
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()


# from selenium import webdriver
# import time
# url = 'https://www.google.com'
# browser = webdriver.Chrome(r'C:\Users\jweif\Downloads\chromedriver_win32\chromedriver.exe')  #if use chrome download chromedriver from google, 

# time.sleep(3)
# browser.get(url)

# time.sleep(5)
# searchBox = browser.find_element_by_css_selector(r'#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input')
# #elem = browser.find_element_by_name('q')
# searchBox.send_keys('where is Trump today')
# time.sleep(3)
# searchBox.submit()
# time.sleep(3)
# firstResult = browser.find_element_by_css_selector('#rso > div:nth-child(1) > div > div > div > div.r > a > h3')
# firstResult.click()



#rso                                    #<div id='ros'>
#rso > div:nth-child(1) > div
#rso > div:nth-child(1) > div > div     #div data-hveid ='CAcQAA'
#rso > div:nth-child(1) > div > div > div.rc
#rso > div:nth-child(1) > div > div > div.rc > div.r
#rso > div:nth-child(1) > div > div > div.rc > div.r > a
#rso > div:nth-child(1) > div > div > div > div.r > a > h3


# browser.back()
# broswer.forward()
# broswer.refresh
# someButton = browser.find_element_by_css_selector(r'')
# someButton.click()

#browser.quit()