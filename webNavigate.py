import webbrowser
import sys
import pyperclip
import requests
import time

'''----------easily execute set up-----batchfile---------
#sys.argv # a list of sys arguement with delimiter space  ['pyscriptname', 'arg1','arg2']
url = 'https://www.google.com/maps/place/'

if len(sys.argv) > 1: # check if there is arguement 
    addr = ' '.join(sys.argv[1:]) #  joint list element 1 to end  

else:
    addr = pyperclip.paste()

webbrowser.open(url + addr)
'''
''' -------get from web, write to file ---------
url = r'your url'
response = requests.get(url)
print('Exception: ' + str(response.raise_for_status())) 
print('Status Code: ' + str(response.status_code))
print(len(response.text))
print(response.text[:100])

fo = open('ref/text001.txt','wb')
for chunk in response.iter_content(10000): #5000 bytes at a time
        # print(chunk)
        # time.sleep(1)
        fo.write(chunk)

fo.close()
'''