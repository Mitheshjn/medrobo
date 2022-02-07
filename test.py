"""#int n
a=[]
n=int(input("enter number"))

for i in range(0, n):
    e=int(input())
    a.append(e)
    
count=0        
for j in range(len(a)):
  for k in range(0,j):
      if a[k]==a[j]:
          count=count+1
          
print(count)
"""
def check(m):
    if (m==1):
        print("a")
    elif (m==2):
        print("b")
    elif (m==3):
        print("c")
    elif (m==4):
        print("d")
    elif (m==5):
        print("e")
    elif (m==6):
        print("f")
    elif (m==7):
        print("g")
    elif (m==8):
        print("h")
    elif (m==9):
        print("i")
    elif (m==10):
        print("j")
    elif (m==11):
        print("k")
    elif (m==12):
        print("l")
    elif (m==13):
        print("m")
    elif (m==14):
        print("n")
    elif (m==15):
        print("o")
    elif (m==16):
        print("p")
    elif (m==17):
        print("q")
    elif (m==18):
        print("r")
    elif (m==19):
        print("s")
    elif (m==20):
        print("t")
    elif (m==21):
        print("u")
    elif (m==22):
        print("v")
    elif (m==23):
        print("w")
    elif (m==24):
        print("x")
    elif (m==25):
        print("y")
    elif (m==26):
        print("z")

a=[]
for i in range(0, 8):
    e=int(input())
    a.append(e)
    
m=[]
d=0
for i in range(len(a)):
    d=d+a[i]
    m.append(d)
    
print(m[7])
if (m[7]>=1):
    if (m[7]<=26):
        check(m[7])
        
    elif m[7]>26:
        r=m[7]
        sum=0
        for digit in str(r):
            sum += int(digit)
            
        print(sum)
        check(sum)
        
