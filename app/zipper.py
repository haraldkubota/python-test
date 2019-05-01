# Iterator/Generator

name = ["Mike", "Jane", "Bruce", "Linda"]
location = ["London", "Paris", "New York", "Rome"]
phone = [1001, 2001, 3333, 4004]


ziplist = zip(name, location, phone)
# print(f'[{next(ziplist)}', end='')
# for iter in ziplist:
#     print(',', iter, end='')
# print(']')

# ziplist = list(zip(name, location, phone))
# print(ziplist)



# Iterate once over the list:

print('Iterate once over the list to print it')

for iter in ziplist:
    print(f'{iter[0]} lives in {iter[1]} and phone number is {iter[2]}')

print('And again')

for iter in ziplist:
    print(f'{iter[0]} lives in {iter[1]} and phone number is {iter[2]}')

print('Done!')

# print(dir(ziplist))
