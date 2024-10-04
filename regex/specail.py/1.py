import re
text = """My Mobile Number is : 9988776655,
        email id is : viratkohli@gmail.com
        todays date is : 30-05-2022 01.02.2024
        date=13/12/2023
        4444 5555 6666
        7898 4568 7988
        sarthak@gmail.co.in
        chetana_123@gmail.com
         kunal.123@gmail.com
         ritesh-123@gmail.co.in
        
        Mobile Number is : 7788776648
        Mobile Number is : 77887766
        """
mobile_no=re.findall("\d{10}",text)#[0-9]
print(mobile_no)

        
# adhar_no=re.findall("\d{4}\s\d{4}\s\d{4}",text)
# print(adhar_no)

# emailpattern1=re.findall("\w{2,20}[@][a-z.]{2,20}",text)  #
# print(emailpattern1)

emailpattern2 = re.findall("[\w\.-]+@[a-z\.]+", text)   #\w\.- means all  any alphanumeric character and underscore,dot(.) or hyphen(-)
print(emailpattern2)

# Dates=re.findall("\d{2}\W\d{2}\W\d{4}",text)  #[\-.]
# print(Dates)

text1=re.findall("\D{1}[a-z]{5}[ ]\D{1}\D{5}",text)
print(text1)

