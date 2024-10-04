import re
text = """109876544
          887654443
            data
            8876544435
"""

numbers = re.match('\d{9}',text)
if numbers:
    print(numbers.group())
text = """109876544 887654443
          
            data
            8876544435
"""

numbers = re.match('(\d{9})(\s\d{9})',text)
if numbers:
    print(numbers.group(0))
    print(numbers.group(2))