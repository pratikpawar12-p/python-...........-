import re
text = """My Mobile Number is : 9988776655,
        email id is : viratkohli@gmail.com
        todays date is : 30-05-2022 01.02.2024,12-12-24 3-5-2022
        date=13/12/2023
        4444 5555 6666
        7898 4568 7988
        sarthak@gmail.co.in
        chetana_123@gmail.com
        kunal.123@gmail.com
        
        Mobile Number is : 7788776648
        Mobile Number is : 77887766
        
        
        
        """
mobile_no=re.findall("[0-9]{10}",text)
print(mobile_no)

        
adhar_no=re.findall("[0-9]{4}[ ][0-9]{4}[ ][0-9]{4}",text)
print(adhar_no)

email_no=re.findall("[a-z0-9_.]{2,20}[@][a-z.]{2,20}",text)
print(email_no)

Dates=re.findall("[0-9]{1,2}[/.-][0-9]{1,2}[/.-][0-9]{2,4}",text)
print(Dates)

text1=re.findall("[A-Z]{1}[a-z]{5}[ ][A-Z]{1}[a-z]{5}",text)
print(text1)