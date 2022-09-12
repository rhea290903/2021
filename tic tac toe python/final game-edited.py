
a=input("enter 1 char")
b=int(input("enter 1 posit"))
l1=[['0','0','0'],['0','0','0'],['0','0','0']]
if b==1:
    l1[0][0]=a
 
elif b==2:
    l1[0][1]=a
  
elif b==3:
    l1[0][2]=a
elif b==4:
    l1[1][0]=a
 
elif b==5:
    l1[1][1]=a
   
elif b==6:
    l1[1][2]=a
  
elif b==7:
    l1[2][0]=a
    
elif b==8:
    l1[2][1]=a
    
elif b==9:
    l1[2][2]=a
print(l1[0])
print(l1[1])
print(l1[2])
    
c=input("enter 2 char")
d=int(input("enter 2 posit"))

if d==1:
    l1[0][0]=c
 
elif d==2:
    l1[0][1]=c
  
elif d==3:
    l1[0][2]=c
elif d==4:
    l1[1][0]=c
 
elif d==5:
    l1[1][1]=c
   
elif d==6:
    l1[1][2]=c
  
elif d==7:
    l1[2][0]=c
    
elif d==8:
    l1[2][1]=c
    
elif d==9:
    l1[2][2]=c
print(l1[0])
print(l1[1])
print(l1[2])
e=int(input("1st player"))
if e==1:
    l1[0][0]=a
 
elif e==2:
    l1[0][1]=a
  
elif e==3:
    l1[0][2]=a
elif e==4:
    l1[1][0]=a
 
elif e==5:
    l1[1][1]=a
   
elif e==6:
    l1[1][2]=a
  
elif e==7:
    l1[2][0]=a
    
elif e==8:
    l1[2][1]=a
    
elif e==9:
    l1[2][2]=a
print(l1[0])
print(l1[1])
print(l1[2])
f=int(input("2nd player"))

if f==1:
    l1[0][0]=c
 
elif f==2:
    l1[0][1]=c
  
elif f==3:
    l1[0][2]=c
elif f==4:
    l1[1][0]=c
 
elif f==5:
    l1[1][1]=c
   
elif f==6:
    l1[1][2]=c
  
elif f==7:
    l1[2][0]=c
    
elif f==8:
    l1[2][1]=c
    
elif f==9:
    l1[2][2]=c
print(l1[0])
print(l1[1])
print(l1[2])


g=int(input("1st player"))
if g==1:
    l1[0][0]=a
 
elif g==2:
    l1[0][1]=a
  
elif g==3:
    l1[0][2]=a
elif g==4:
    l1[1][0]=a
 
elif g==5:
    l1[1][1]=a
   
elif g==6:
    l1[1][2]=a
  
elif g==7:
    l1[2][0]=a
    
elif g==8:
    l1[2][1]=a
    
elif g==9:
    l1[2][2]=a
print(l1[0])
print(l1[1])
print(l1[2])
while l1[0][0]==l1[0][1]==l1[0][2]==a or l1[1][0]==l1[1][1]==l1[1][2]==a or l1[2][0]==l1[2][1]==l1[2][2]==a or l1[0][0]==l1[1][0]==l1[2][0]==a or l1[0][1]==l1[1][1]==l1[2][1]==a or l1[0][2]==l1[1][2]==l1[2][2]==a or l1[0][0]==l1[1][1]==l1[2][2]==a or l1[0][2]==l1[1][1]==l1[2][0]==a:
    print("player1 wins the game!!")
    exit()
while l1[0][0]==l1[0][1]==l1[0][2]==c or l1[1][0]==l1[1][1]==l1[1][2]==c or l1[2][0]==l1[2][1]==l1[2][2]==c or l1[0][0]==l1[1][0]==l1[2][0]==c or l1[0][1]==l1[1][1]==l1[2][1]==c or l1[0][2]==l1[1][2]==l1[2][2]==c or l1[0][0]==l1[1][1]==l1[2][2]==c or l1[0][2]==l1[1][1]==l1[2][0]==c:
    print("player 2 wins!!")
    exit()
h=int(input("2nd player"))

if h==1:
    l1[0][0]=c
 
elif h==2:
    l1[0][1]=c
  
elif h==3:
    l1[0][2]=c
elif h==4:
    l1[1][0]=c
 
elif h==5:
    l1[1][1]=c
   
elif h==6:
    l1[1][2]=c
  
elif h==7:
    l1[2][0]=c
    
elif h==8:
    l1[2][1]=c
    
elif h==9:
    l1[2][2]=c
print(l1[0])
print(l1[1])
print(l1[2])
while l1[0][0]==l1[0][1]==l1[0][2]==a or l1[1][0]==l1[1][1]==l1[1][2]==a or l1[2][0]==l1[2][1]==l1[2][2]==a or l1[0][0]==l1[1][0]==l1[2][0]==a or l1[0][1]==l1[1][1]==l1[2][1]==a or l1[0][2]==l1[1][2]==l1[2][2]==a or l1[0][0]==l1[1][1]==l1[2][2]==a or l1[0][2]==l1[1][1]==l1[2][0]==a:
    print("player1 wins the game!!")
    exit()
while l1[0][0]==l1[0][1]==l1[0][2]==c or l1[1][0]==l1[1][1]==l1[1][2]==c or l1[2][0]==l1[2][1]==l1[2][2]==c or l1[0][0]==l1[1][0]==l1[2][0]==c or l1[0][1]==l1[1][1]==l1[2][1]==c or l1[0][2]==l1[1][2]==l1[2][2]==c or l1[0][0]==l1[1][1]==l1[2][2]==c or l1[0][2]==l1[1][1]==l1[2][0]==c:
    print("player 2 wins!!")
    exit()

i=int(input("1st player"))
if i==1:
    l1[0][0]=a
 
elif i==2:
    l1[0][1]=a
  
elif i==3:
    l1[0][2]=a
elif i==4:
    l1[1][0]=a
 
elif i==5:
    l1[1][1]=a
   
elif i==6:
    l1[1][2]=a
  
elif i==7:
    l1[2][0]=a
    
elif i==8:
    l1[2][1]=a
    
elif i==9:
    l1[2][2]=a
print(l1[0])
print(l1[1])
print(l1[2])
while l1[0][0]==l1[0][1]==l1[0][2]==a or l1[1][0]==l1[1][1]==l1[1][2]==a or l1[2][0]==l1[2][1]==l1[2][2]==a or l1[0][0]==l1[1][0]==l1[2][0]==a or l1[0][1]==l1[1][1]==l1[2][1]==a or l1[0][2]==l1[1][2]==l1[2][2]==a or l1[0][0]==l1[1][1]==l1[2][2]==a or l1[0][2]==l1[1][1]==l1[2][0]==a:
    print("player1 wins the game!!")
    exit()
while l1[0][0]==l1[0][1]==l1[0][2]==c or l1[1][0]==l1[1][1]==l1[1][2]==c or l1[2][0]==l1[2][1]==l1[2][2]==c or l1[0][0]==l1[1][0]==l1[2][0]==c or l1[0][1]==l1[1][1]==l1[2][1]==c or l1[0][2]==l1[1][2]==l1[2][2]==c or l1[0][0]==l1[1][1]==l1[2][2]==c or l1[0][2]==l1[1][1]==l1[2][0]==c:
    print("player 2 wins!!")
    exit()

j=int(input("2nd player"))

if j==1:
    l1[0][0]=c
 
elif j==2:
    l1[0][1]=c
  
elif j==3:
    l1[0][2]=c
elif j==4:
    l1[1][0]=c
 
elif j==5:
    l1[1][1]=c
   
elif j==6:
    l1[1][2]=c
  
elif j==7:
    l1[2][0]=c
    
elif j==8:
    l1[2][1]=c
    
elif j==9:
    l1[2][2]=c
print(l1[0])
print(l1[1])
print(l1[2])
while l1[0][0]==l1[0][1]==l1[0][2]==a or l1[1][0]==l1[1][1]==l1[1][2]==a or l1[2][0]==l1[2][1]==l1[2][2]==a or l1[0][0]==l1[1][0]==l1[2][0]==a or l1[0][1]==l1[1][1]==l1[2][1]==a or l1[0][2]==l1[1][2]==l1[2][2]==a or l1[0][0]==l1[1][1]==l1[2][2]==a or l1[0][2]==l1[1][1]==l1[2][0]==a:
    print("player1 wins the game!!")
    exit()
    
    
while l1[0][0]==l1[0][1]==l1[0][2]==c or l1[1][0]==l1[1][1]==l1[1][2]==c or l1[2][0]==l1[2][1]==l1[2][2]==c or l1[0][0]==l1[1][0]==l1[2][0]==c or l1[0][1]==l1[1][1]==l1[2][1]==c or l1[0][2]==l1[1][2]==l1[2][2]==c or l1[0][0]==l1[1][1]==l1[2][2]==c or l1[0][2]==l1[1][1]==l1[2][0]==c:
    print("player 2 wins!!")
    exit()
    

     
k=int(input("1st player"))
if k==1:
    l1[0][0]=a
 
elif k==2:
    l1[0][1]=a
  
elif k==3:
    l1[0][2]=a
elif k==4:
    l1[1][0]=a
 
elif k==5:
    l1[1][1]=a
   
elif k==6:
    l1[1][2]=a
  
elif k==7:
    l1[2][0]=a
    
elif k==8:
    l1[2][1]=a
    
elif k==9:
    l1[2][2]=a
print(l1[0])
print(l1[1])
print(l1[2])
while l1[0][0]==l1[0][1]==l1[0][2]==a or l1[1][0]==l1[1][1]==l1[1][2]==a or l1[2][0]==l1[2][1]==l1[2][2]==a or l1[0][0]==l1[1][0]==l1[2][0]==a or l1[0][1]==l1[1][1]==l1[2][1]==a or l1[0][2]==l1[1][2]==l1[2][2]==a or l1[0][0]==l1[1][1]==l1[2][2]==a or l1[0][2]==l1[1][1]==l1[2][0]==a:
    print("player1 wins the game!!")
    exit()
    
    
while l1[0][0]==l1[0][1]==l1[0][2]==c or l1[1][0]==l1[1][1]==l1[1][2]==c or l1[2][0]==l1[2][1]==l1[2][2]==c or l1[0][0]==l1[1][0]==l1[2][0]==c or l1[0][1]==l1[1][1]==l1[2][1]==c or l1[0][2]==l1[1][2]==l1[2][2]==c or l1[0][0]==l1[1][1]==l1[2][2]==c or l1[0][2]==l1[1][1]==l1[2][0]==c:
    print("player 2 wins!!")
    exit()

