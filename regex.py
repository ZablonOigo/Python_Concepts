import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
str='welcome to my website'
s=re.search('^to.my *website$',str)
print(s)