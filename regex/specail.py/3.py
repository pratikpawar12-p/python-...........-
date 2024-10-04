import re
text="""chetana@gmail.com, chetana123@gmail.com,chetana-123@gmail.com
"""
# email=re.findall("[a-z]{2,20}[@][a-z.]{2,20}",text)  
# print(email)
# email1=re.findall("[a-z0-9]{2,20}[@][a-z.]{2,20}",text)
# print(email1)
# email2=re.findall("\w{2,20}[@][a-z.]{2,20}",text)
# print(email2)
email3=re.findall("\w{2,20}\D\w{2,20}[@][a-z.]{2,20}",text)
print(email3)
email3=re.findall("\w{2,20}\D\w{2,20}\D[a-z.]{2,20}",text)
print(email3)