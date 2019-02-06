import smtplib

pw0 = open("C:\\Users\\jweif\\Documents\\0010084.txt",'r')
pw = pw0.readline()
pw0.close()
conn = smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()  #connect to server
conn.starttls()  #put the connection to server at tls mode or encrpted mode
conn.login(user = 'cops2132@gmail.com', password = pw)
conn.sendmail(from_addr = 'cops2132@gmail.com',to_addrs='cops2132@gmail.com',msg = 'Subjects: Mysubject \n\nDear Jay, \n I am sending you a messgae \n\n jay')
conn.quit()

#note: gmail security setting Less secure app access turn on or use google app specific password
# Gmail     smtp.gmail.com
# Outlook/Hotmail   smtp-mail.outlook
# smtp.mail.yahoo.com
# smtp.mail.att.net port 465