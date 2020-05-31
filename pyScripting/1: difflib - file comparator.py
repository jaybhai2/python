```
import difflib

firstFile = 'firstfile.txt'
secondFile = 'secondfile.txt'

firstFileLines = open(firstFile).readlines()
secondFileLines = open(secondFile).readlines()

diff = difflib.HtmlDiff().make_file(firstFileLines,secondFileLines,firstFile,secondFile)
#diff = difflib.HtmlDiff().make_table(firstFileLines,secondFileLines,firstFile,secondFile)

diff_writer = open('difference_output.html','w')
diff_writer.write(diff)
diff_writer.close()


```
![Image](https://github.com/jayjayjohn/python/blob/master/pyScripting/im/difflib01.PNG)
