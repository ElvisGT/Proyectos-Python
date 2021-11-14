import re

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumberRegex.search("Mi numero de telefono es 123-456-7891")

primera,segunda = mo.groups()

print(primera)
print(segunda)


phoneNumberRegex2 = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mu = phoneNumberRegex.search("Mi numero de telefono es 123-456-7891")

print(mu.group(1))


heroRegex = re.compile(r"Batman|Tina")

m1 = heroRegex.search("Batman and Tina")

print(m1.group())

m2 = heroRegex.search("Tina and Batman")

print(m2.group())

batRegex = re.compile(r"Bat(man|mobile|copter)")

mi = batRegex.search("The Batmobile is dead")
mp = batRegex.search("The Batman is the best")

print(mi.group())
print(mp.group())