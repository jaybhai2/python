import imapclient #third party package
import datetime
import pyzmail    #packege to easily read fetched email
fo= open('C:\\Users\\jweif\\Documents\\0010084.txt')
pw = fo.readline()
fo.close()

conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)
conn.login('cops2132@gmail.com',pw)
mailInfo = conn.select_folder('INBOX',readonly=True)
#print(mailInfo)

today_s = datetime.datetime.now().strftime("%d-%b-%Y")

#print( '%d recent message' %  mailInfo[b'RECENT'])
EmailID = conn.search([u'SINCE', today_s])  # 01-FEB-2019
print('Message received today: ' + ','.join(str(x) for x in EmailID))
'''
#print(conn.fetch([2405],['BODY[]']))
 for msgId, data in conn.fetch(EmailID,['ENVELOPE']).items():

    subjectLine =  data[b'ENVELOPE'].subject.decode()
    fromName =  data[b'ENVELOPE'].from_[0].name.decode()
    fromEmail = data[b'ENVELOPE'].from_[0].host.decode()
    receivedDT = data[b'ENVELOPE'].date.strftime('%m%d%Y')
    print([type(receivedDT),type(fromEmail)])
    print('ID# %d: %s from %s(%s) received %s' % (msgId, subjectLine, fromName, fromEmail, receivedDT))
'''
# USING pyzmail  
for msgId, rawMessage in conn.fetch(EmailID,['BODY[]','FLAGS']):
    message = pyzmail.PyzMessage.factory(rawMessage[msgId][b'BODY[]'])
    message.get_addresses('from');
    message.text_part.get_payload().decode('UTF-8')
    #message.text_part.charset == None   if true UTF-8 works fine

conn.logout()
