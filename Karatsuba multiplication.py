
# coding: utf-8

# In[22]:


def karatsuba(x,y):
    if x<10 or y<10:
        return x*y
    m=max(len(str(x)),len(str(y)))
    
    if m%2 != 0:
        m-=1
    power=m/2
    
    a,b=divmod(x,10**power)
    c,d=divmod(y,10**power)
    
    ac=karatsuba(a,c)
    bd=karatsuba(b,d)
    midTerm=karatsuba(a+b,c+d)-ac-bd
    
    return ac*10**m+midTerm*10**power+bd


# In[23]:


x=int(input("First number?"))
y=int(input("Second number?"))


# In[24]:


print(karatsuba(x,y))

