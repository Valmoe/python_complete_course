name = "Valentine Gumo"
print(name[5:-3])

"""
Use of a formatted string below
"""
msg = f'{name} is the best French student of 2015'
print(msg)

"""
count number of characters in a strings 
"""
print(len(msg))

"""
dot operator, methods in strings 
"""
print(msg.upper())
print(msg.find('6'))
print(msg.replace('Gumo', 'Ochieng'))
print('Gumo' in msg)