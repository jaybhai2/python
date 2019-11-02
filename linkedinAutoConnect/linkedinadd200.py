from selenium import webdriver
import time 
import pyautogui
from selenium.webdriver.common.keys import Keys


connect_btn_img = 'img/connect.PNG'
addnote = 'img/addNote.PNG'
send = 'img/sendNow.PNG'
next = 'img/next.PNG'

f = open('config.txt','r')
line = f.read()
credential = line.split(',')
f.close()


# ------------------------function ----------------------
def do_connect(first_name):
    

    pyautogui.moveTo(887,500)
    try: 

        connectPos = pyautogui.locateCenterOnScreen(connect_btn_img)
    except TypeError:
        print('no available connection found')
        return 

    if connectPos[1] > 300:
        return  

    pyautogui.moveTo(connectPos[0],connectPos[1],0.5)
    pyautogui.click()

    time.sleep(0.5)

    pyautogui.moveTo(887,500)
    try:
        addnotePos = pyautogui.locateCenterOnScreen(addnote)
    except TypeError:
        print('no add note btn found')
        return 

    pyautogui.moveTo(addnotePos[0],addnotePos[1],0.5)
    pyautogui.click()

    pyautogui.typewrite('hi ' + first_name + ', can i join your network to learn more?', interval=0.1)

    time.sleep(0.5)
    
    pyautogui.moveTo(887,500)
    try:
        sendPos = pyautogui.locateCenterOnScreen(send)
    except TypeError:
        print('not able to connect with this person')
        pyautogui.moveTo(887,500)
        pyautogui.click()
        return 

    pyautogui.moveTo(sendPos[0],sendPos[1],0.5)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)


# ------------------------Main ----------------------

driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
driver.get('https://www.linkedin.com/login')

driver.find_element_by_id('username').send_keys(credential[0])
driver.find_element_by_id('password').send_keys(credential[1])
time.sleep(0.25)
driver.find_element_by_class_name('btn__primary--large').send_keys(Keys.RETURN)

driver.set_window_size(1000,690)
time.sleep(1)

user_confirm = input('when you are in connectin page, press enter')


for page in range(0,2):
    
    i=0
    time.sleep(1)
    nameElements = driver.find_elements_by_class_name('actor-name')
    name_list = []

    while len(nameElements) < 10:

        #1928
        name_list = [] 
        i +=1
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(0,%d)" % (i*250))
        time.sleep(1)

        nameElements = driver.find_elements_by_class_name('actor-name')

        for element in nameElements:
            name = element.get_attribute('innerHTML')
            first_name = name.split(' ')[0]
            name_list.append(first_name)
            
        if i>=7:
            break

        print(name_list)

    time.sleep(3)

    for ei in range(0,len(nameElements)):

        driver.execute_script("arguments[0].scrollIntoView();",nameElements[ei])
    
        yOffset = driver.execute_script("return window.pageYOffset;")
        driver.execute_script("window.scrollTo(0,%d)" % (yOffset - 80))
        time.sleep(0.5)

        do_connect(name_list[ei])
        time.sleep(1)

    print('page - %d completed' % (page))
    nextdPos = pyautogui.locateCenterOnScreen(next)
    pyautogui.moveTo(nextdPos[0],nextdPos[1],0.5)
    pyautogui.click()

    time.sleep(1)
    pyautogui.moveTo(100,100,2)
