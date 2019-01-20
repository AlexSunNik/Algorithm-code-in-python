
# coding: utf-8

# In[21]:


def binarySearch(A,x):
    if len(A)==1:
        if A[0]==x:
            return True
        else:
            return False
    else:
        m=len(A)
        if m%2!=0:
            m-=1
        midPos=int(m/2)
        
        if A[midPos]<x:
            return binarySearch(A[midPos:],x)
        elif A[midPos]>x:
            return binarySearch(A[:midPos],x)
        else:
            return True

