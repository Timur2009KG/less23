# a = "aidana"
# b = "adilet"
# c = ""

# for i in range(len(a)):
#      c += a[i] + b[i]
# print(c)


# a = "Hello world".replace(' ', '')
# arr = []

# for i ,char in enumerate(a):
#     new_txt = char.upper() + char.lower() * i
#     arr.append(new_txt)

# print('-'.join(arr))

lst = [1,2,'aasf','1','123',123]
arr = []

for i in lst:
    if type(i) != type('str'):
        arr.append(i)
print (arr)