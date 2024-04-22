import random

flag="HBD{F4ke_fl4g_Br0}"

encFlag=''
random.seed(10)

def f1(flag):
    f1_back=[]
    for i in range(len(flag)):
        j=random.randint(1,9999)
        f1_back.append(str(ord(flag[i]))+str(j))
    
    return f1_back


def f2(f1_back):
    f2_back=''
    for i in f1_back:
        print(len(i))
        f2_back+=str(i)
    return f2_backf2_back

print(f2(f1(flag)))
    
     




