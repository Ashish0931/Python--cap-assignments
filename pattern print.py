for i in range (5,0,-1):
    for j in range(5,i,-1):
        print(end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print()
for i in range(1,5):
    for j in range(0,5-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()