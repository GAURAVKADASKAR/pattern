num=int(input(""))
for i in range(num):
    for j in range(num):
        if i==0 or i==num-1:
          print("*",end=" ")
        elif j==0 or j==num-1:
            print("*",end=" ")
        elif j==2 and (i==num-3):
                print("*",end=" ")
        elif j==num-3 and(i==num-3):
                print("*",end=" ")
        elif i==num-2 and(j==1):
            print("*",end=" ")
        elif i==num-2 and(j==num-2):
            print("*",end=" ")
        else:
            if i==1 and (j==1 or j==num-2):
                print("*",end=" ")
            elif i==2 and(j==2 or j==num-3):
                print("*",end=" ")
            elif num%2!=0:
                mid=num//2
                if j==mid and i==mid:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            
            
            
            else:
                print(" ",end=" ")
        
    print(" ")
