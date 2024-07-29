#for,Tuple 
T = [(1, 2),
     (3, 4),
     (5, 6)]
for (a, b) in T:                
    print (a, b) 
    
print('#-----------------------   ')
#enumerate(iterable, start=0)
for idx,(a,b) in enumerate(T, start=3000):
    print(f'{idx} :  { a} - {b}' )

