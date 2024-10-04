

import re
string = 'python and 5 data 7 science'
result = re.split('\s',string)
print(result)
text = """  DOB: 17/11/1996
           Email id: vishaltandel19@gmail.com
           aadhar number = 3456 1232 9876"""
x=re.findall('\D',text)  #find all occurrences of non-digit characters in the text
print(x)






text = """Machine learning is a field of inquiry devoted to understanding and building
methods that 'learn', that is, methods that leverage data to improve performance on some 
set of tasks. It is seen as a part of artificial intelligence"""
x=re.findall('\D{10}',text)  #find all occurrences of  5 non-digit characters in the text
print(x)



import re
text = """ Name: Vishal Vijay Tandel.
           PAN Number: AXCPT8626T
           Mobile Number : 8412835885 3456789123
           DOB: 17/11/1996
           Email id: vishaltandel19@gmail.com
           aadhar number = 3456 1232 9876
           %$*&@
           """

pan_number = re.findall('\w{10}',text)
email_id = re.findall('\w{2,20}[@][a-z.]{2,15}',text)
dob = re.findall('\d{2}[/]\d{2}[/]\d{4}',text)
mobile_number = re.findall('\d{10}',text)
aadhar_no = re.findall('\d{4}[ ]\d{4}[ ]\d{4}',text)

print("PAN Number is :",pan_number)
print("Email ID is   :",email_id)
print("Date of Birth :",dob)
print("Mobile Number :",mobile_number)
print('Aadhar Number :',aadhar_no)

