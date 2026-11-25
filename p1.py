'''import keyword
print(keyword.kwlist)


a=[10,2.3,True,"hello"]
a.pop(0)
print(a)


a=10,20,30
print(a,type(a))

a=10,
print(a,type(a))

a=(10,2,6,5j,True,'hi',[1,2],[3,4])
print(a[-1])

a={10,20,30,40}
print(a)      

a={'a':10,'a':20}
a['c']=30
print(a)

a={'a':[10,20,30],'b':40}
print(a['a'][2])'''

'''a="hello"
print(a[2:4])
print(a[-3:-2+1])

a="good morning"
print(a[-4:-2+1])
print(a[-5:-2+1])

a="Hello"
print(a[3:1-1:-1])
print(a[-2:-4-1:-1])
print(a[-1:-5-1:-1])
a="good morning"
'odm'

print(a[1:5-1:-2])

"mng"
print(a[5:3-5:1])
print(a[3:-1+1:3])
print(a[5:11-2:3])
print(a[-2:-8-1:-3])'''

'''a=input("enter:")
print(type(a))

a=eval(input("enter:"))
print(type(a))

a=float(input("enter:"))
print(type(a))'''

'''a=int(input("enter:))
if a%2==0
   print('even')
else:
   print('odd')'''

'''a=eval(input("enter list:"))
if len(1)==0:
    print('yes')
else:
    print('no')'''

'''ch=input("enter:")

if"A"<=ch<="Z":
    print("upper")
elif "a"<=ch<="z":
     print("lower")
else:
     print('not a alpha')'''


'''un=input("input:")
if un=="deepthi_9822":
    print("username is correct")
    pw=input("enter:")
    if pw=="dee200507":
       print("password is correct")
    else:
        print("password is incorrect")
else:
    print("username is incorrect")'''

'''print helloworld'''
'''i=1
while i<=10:
     print(i)
     i+=1'''

'''i=0
while i<=50:
    print(i)
    i+=2'''

'''n=int(input("enter num:"))
rev=0

while n>0:
    ld= n%10
    n=n//10
    rev=rev*10+ld
    print(rev)'''

'''for i in range(1,100):
    print(i)'''

'''for i in range(1,51):
    if i%2==0:
        print(i,'even')'''

'''l=[10,20.30]
for i in l:
    print(l)'''

'''s=input("enter:")

for i in s:
    if "A"<=i<="Z":
        out+=(ord(i)+32)
    elif"a"<=i<="z":
        out+=chr(ord(i)-32)
    else:
        out+=i
    print(out)'''

'''s=input("enter:")
rev=''
for i in s:
    rev=i+rev
print(rev)'''

'''for i in range(1,6):
    for j in range(1,6):  
      print('*',end='')
      print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if(i==j):
          print('!',end=' ')
        else:
            print(' #',end=' ')
    print()'''

'''a="happy birthday" 
print (a[-4:-7:-1])'''

'''#with arg with return
def convert(s,out):
    out=' '
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=1
    return(out)    
print(convert(input('enter a string:' )),' ')'''

'''#with arg without return
def convert(s,out):
    out=' '
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=1
    print(out)
    return 10    
print(convert(input('enter a string:' ),' '))'''

'''#without arg with return
def convert():
    s=input('enter:')
    out=' '
    for i in s:

        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=1
    print(out)   
print(convert()) '''

'''class college:
    cname="gcem"
    cloc="hoodi"
s1=college()
print(s1.cname,s1.cloc)
print(college.cloc)
print(s1.cloc)
print("changing loc wtrsp obj")
s1.cloc="hoodi"
print(s1.cloc)
print(college.cloc)'''

class college:
    def __init__(self,name,phone,usn):
       self.name=name
       self.phone=phone
       self.usn=usn
    def display(self):
        print(self.name,self.phone,self.usn)
s1=college('harish','9876654321','drr34')
s2=college('girish','8698326586','dgh35')
s1.display()
s2.display()

s1.change_name("harish")
s1.display()

