import re
text = """My Mobile Number is : 9988776655,
        email id is : viratkohli@gmail.com
        todays date is : 30-05-2022
        
        Mobile Number is : 7788776648
        29-05-2021
        31-05-2012
        30-09-2022
             1/12/23
        """
date=re.findall("\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}",text)
print(date)
date=re.findall("[0-9]{2}[-][0-9]{2}[-][0-9]{4}",text)
print(date)