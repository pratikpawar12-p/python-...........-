import re
text = """1098765446 datary 30-12-2023
          887654443
          
          
            
            8876544435
"""
numbers = re.search(r'(\d{12})',text)
print(numbers)
numbers = re.search(r'(\d{10})(\s\D{4,6})(\s\d{2}[-]\d{2}[-]\d{4})',text)
print(numbers)
if numbers:
    print(numbers.group())
    print(numbers.group(0))
    print(numbers.group(1))
    print(numbers.group(2))
    print(numbers.group(3))
    #print(numbers.group(4))