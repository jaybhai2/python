import imapclient #third party package
import datetime
fo= open('C:\\Users\\jweif\\Documents\\0010084.txt')
pw = fo.readline()
fo.close()

conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)
conn.login('cops2132@gmail.com',pw)
mailInfo = conn.select_folder('INBOX',readonly=True)
print(mailInfo)
print( '%d recent message' %  mailInfo[b'RECENT'])
EmailID = conn.search([u'SINCE', '05-Feb-2019'])
print('message received today: ' + ','.join(str(x) for x in EmailID))

for msgId, data in conn.fetch(EmailID,['ENVELOPE']).items():
    subjectLine =  data[b'ENVELOPE'].subject.decode()
    fromName =  data[b'ENVELOPE'].from_[0].name.decode()
    fromEmail = data[b'ENVELOPE'].from_[0].host.decode()
    receivedDT = data[b'ENVELOPE'].date.strftime('%m%d%Y')
    #print([type(receivedDT),type(fromEmail)])
    print('ID# %d: %s from %s(%s) received %s' % (msgId, subjectLine, fromName, fromEmail, receivedDT))


conn.logout()
