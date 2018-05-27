import os,re
import time
import codecs

#Result Folder
root =  r"C:\Users\liuyu\Desktop\BussinessCard\Result"

#All the pattern for re
NamePattern = '([\u4E00-\u9FFFh]{2,3})'
IphonePattern = '1[0-9]{10}'
EmailPattern = '.*@.*'
CompanyPattern = '.*公司.*'
AddressPattern  = '.*地址[:：]?(.*)'
PhonePattern = '.*电话[:：]?(.*)'

#Result file
result = open(r"C:\Users\liuyu\Desktop\BussinessCard\Finalresult.csv",'w+',encoding='utf8')

for i in os.listdir(root):
    f = open(os.path.join(root,i),'r',encoding='utf8')
    content = f.read()
    number = i[:-4]
    name =  re.findall(NamePattern,content,flags=0)
    iphone = re.findall(IphonePattern,content,flags=0)
    email = re.findall(EmailPattern,content,flags=0)
    company = re.findall(CompanyPattern,content,flags=0)
    address = re.findall(AddressPattern,content,flags=0)
    phone = re.findall(PhonePattern,content,flags=0)

    name_r = name[0] if name else ''
    iphone_r = iphone[0] if iphone else ''
    email_r = email[0] if email else ''
    company_r = company[0] if company else ''
    address_r = address[0] if address else ''
    phone_r = phone[0] if phone else ''

    Finalresult = number+','+name_r+','+iphone_r+','+phone_r+','+company_r+','+''+','+email_r+','+address_r+'\n'

    result.write(Finalresult)

    print("Finish {}!".format(number))

    #clear All
    content = None
    number = None
    name = None
    iphone = None
    email = None
    company = None
    address = None
    phone = None
    Finalresult = None

print("Finish All!")
