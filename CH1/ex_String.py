# s:string, c:character, d:integer, f:float, o:octal, x:hexademical
"""
name = input()
year = int(input())
print("Hi %s. My friend. It's been %d years." %(name, year))
"""

#sort left : :<, sort right : :>, sort middle : :^
print("/"+"{some:^10}".format(some=17)+"/")
print("/"+"{some:<10}".format(some=17)+"/")
print("/"+"{some:>10}".format(some=17)+"/")
print()
#fill the blank
print("/"+"{some:=^10}".format(some=17)+"/")
print("/"+"{some:=<10}".format(some=17)+"/")
print("/"+"{some:=>10}".format(some=17)+"/")
print()
# f String formatting
name = 'tiger'
age = 39
print(f'my name is {name}. And my age is {age+1}')
#count, find(true/false), index(true/error)
#join(insert in each letter), upper(Capital), lower