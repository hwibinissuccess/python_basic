class MyClass:
    pass

x = MyClass()
x.cnt = 1
print(dir(MyClass), dir(x))

while x.cnt<10:
    x.cnt = x.cnt*2

print(x.cnt)
del x.cnt
print(dir(x))