import pyautogui as pygui

#0,0 being top left corner,  
#[failsave exception] in case you completely lost control of your mouse, slap you cursor to the 0,0 , the program will stop, this is built-in in the pakage 



''' -------------------------Basic Function ---------------------
print(pygui.size()) # return tuple for scree size.
width, height = pygui.size()
pygui.position() #return current position of your cursor
pygui.displayMousePosition() # continusely display your cursor coordinate and RGB, you next command will haul
pygui.moveTo(5,5,duration=1) #MOVE TO ABOLUTE COORDINATE
pygui.moveRel(200,0) # relative move 
pygui.click(x=,y=)
pygui.doubleClick(x=,y=)
pygui.rightClick(x=,y=)

pygui.typewrite("Hello my friend", interval=0.2)
pygui.typewrite(['a','left','S'],interval=1)    # type a , left arrow, left arrow, type S
pygui.KEYBOARD_KEYS # RETURN A LIST OF KEY NAME
pygui.press('f5')
pygui.hotkey('ctrl','c')  # press crtl + c
''' 

''' ----------------------- draw a squre on paint------------------------ 
pygui.click()
l = 100
while l > 0:
    print(l,0)
    pygui.dragRel(l,0) #click and drag to x++
    l -= 25
    pygui.dragRel(0,l)  # drag down y++
    pygui.dragRel(-l,0)
    l -= 25
    pygui.dragRel(0,-l)
'''

''' -----------------------Image Recognition ---------------------
pygui.screenshot('c:\\myScreenShot.png')   
pygui.locateOnScreen('image') # find position of your image on screen, recturn (x,y,width,heigh) x,y being top left corner of you image

MinButton = pygui.locateCenterOnScreen("im\\MinimizeButton.png") 
pygui.click(MinButton,duration = 3)

'''