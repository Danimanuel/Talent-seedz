a: int
par : int
total= par
for a in range(21):
    print(a)   
    if a % 2 == 0:
        par = a + 1 
        

print('total: ',total)