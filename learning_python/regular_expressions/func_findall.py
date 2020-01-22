import re


print(re.findall("match", "here is one match and here is another match"))

print(re.findall(r'\b\d+\b', "66655.96 e"))
print(re.findall(r'\d+', " - 66 655.96 e dh"))

