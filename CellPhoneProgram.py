import CellPhoneClass as c

myphone = c.CellPhone('Apple','Iphone13','$999')
yourphone = c.CellPhone('Samsung','Galaxy 10','$555')

print('first phone')
print(myphone.get_manufact())
print(myphone.get_model())
print(myphone.get_price())
print()
print()

print('second phone')
print(myphone.get_manufact())
print(myphone.get_model())
print(myphone.get_price())


