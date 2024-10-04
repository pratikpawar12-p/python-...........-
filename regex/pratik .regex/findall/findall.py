import re
text = """My Mobile Number is : 9988776655,
        email id is : viratkohli@gmail.com
        todays date is : 30-05-2022 01.02.2024
        date=13/12/2023
        4444 5555 6666
        sarthak@gmail.co.in
        chetana_123@gmail.com
        kunal.123@gmail.com
         ritesh-123@gmail.co.in
        
        Mobile Number is : 7788776648
        Mobile Number is : 77887766
        """
mob=re.findall("[0-9]{10}",text)
print(mob)

mob1=re.findall("\d{10}",text)  #using special charcters \d
print(mob1)

date=re.findall("[0-9]{2}[-/][0-9]{2}[-/][0-9]{4}",text)
print(date)

date1=re.findall("\d{2}[/-]\d{2}[/-]\d{4}",text)  #using special char \d
print(date1)

email=re.findall("[a-z]{2,20}[@][a-z]{5}[.][a-z.]{2,20}",text)
print(email)

email_w=re.findall("\w{2,20}[@]\w{5}[a-z.]{2,20}",text)  #using special char 
print(email_w)

aadarecard1=re.findall("[0-9]{4}[ ][0-9]{4}[ ][0-9]{4}",text)
print(aadarecard1)

aadarecard2=re.findall("\d{4}\s\d{4}\s\d{4}",text)
print(aadarecard2)
