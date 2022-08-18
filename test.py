x = "  My name is: {name} , My salary equals to {salary:0.2f} "
x= x.lower()
#print(x[10:], x[:10])
print(x)
#print(x.upper())
x= x.strip()
print(x)
x= x.format(name="mahmoud", salary=1000)
print(x.capitalize())
print(x.title())
v = x.split(',')
x=''
for i in range(len(v)):
    x=x+v[i]
print(x.center(100,'-'))

str_in =  'abcdefghigklmnopqrstuvwxyz1234567890.'
str_out = 'qwertyuiopasdfghjklzxcvbnmARTUIOPASDF'
dic = x.maketrans(str_in,str_out)

print(x.translate(dic))