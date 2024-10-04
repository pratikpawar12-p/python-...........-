with open(r""C:\Users\91810\Desktop\praruyuy.txt"", "r") as data:
    content = data.read()  
mob=re.findall("[0-9]{10}",content)
print(mob)