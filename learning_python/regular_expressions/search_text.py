import re


match = re.search("are", " Heyy how are you !!")
print(type(match))
print(match)
print(match.start())
print(match.end())
print(re.search("match", "here is one match and here is another match").group())

