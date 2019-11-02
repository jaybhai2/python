# click first connect button 
# click send now 
# click second connect button 
# click send now 

# at the end of the screen 
# scroll down to find more connection 

# click first connect button 
# click send now 
# click second connect button 
# click send now 

# at the end of the page, 
# click nect page button 

# repeat every thing 

import pyautogui
import time 

print('haha')
#pyautogui.displayMousePosition()
for i in range(1,10):

    for pos in pyautogui.locateAllOnScreen('connect_button_image.PNG'):
        print(pos)  
        x, y, w, h = pos 
        pyautogui.moveTo(x,y,2)
        pyautogui.click()
        time.sleep(2)
        try: 
            sendNow_pos = pyautogui.locateCenterOnScreen('sendNow_image.PNG')
        except TypeError:
            print("send button not found!!") 
        else: 
            print(sendNow_pos)
            x1, y1 = sendNow_pos

            pyautogui.moveTo(x1,y1,2)
            pyautogui.click()
            time.sleep(2)

    time.sleep(3)
    pyautogui.scroll(-300)
    time.sleep(3)
    
    for pos in pyautogui.locateAllOnScreen('connect_button_image.PNG'):
        
        print(pos)  
        x, y, w, h = pos 
        pyautogui.moveTo(x,y,2)
        pyautogui.click()
        time.sleep(2) 
        try: 
            sendNow_pos = pyautogui.locateCenterOnScreen('sendNow_image.PNG')
        except TypeError:
            print("send button not found!!") 
        else: 
            print(sendNow_pos)
            x1, y1 = sendNow_pos

            pyautogui.moveTo(x1,y1,2)
            pyautogui.click()
            time.sleep(2)


    nextButton_pos = pyautogui.locateCenterOnScreen('nextButton_image.PNG')
    x2, y2 = nextButton_pos
        
    pyautogui.moveTo(x2,y2,5)
    pyautogui.click()
    time.sleep(5)



#pyautogui.click()