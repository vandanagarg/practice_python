import re


# match = re.search("are", " Heyy how are you !!")
# print(type(match))
# print(match)
# print(match.start())
# print(match.end())


print(re.search("match", "here is one match and here is another match").group())
print(re.findall("match", "here is one match and here is another match"))

print(re.findall(r'\b\d+\b', "66655.96 e"))
print(re.findall(r'\d+', " - 66 655.96 e dh"))


phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone Num : " +  str(num))

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print("Phone Num : " +  str(num))