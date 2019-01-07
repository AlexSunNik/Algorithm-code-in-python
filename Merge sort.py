
# coding: utf-8

# In[48]:


def merge(a,b):
    c=[]
    while len(a)!=0 and len(b)!=0:
        if(a[0]<b[0]):
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    if len(a)==0:
        c+=b
    else:
        c+=a
    
    return c


# In[52]:


def mergeSort(arr):
    if len(arr)==0 or len(arr)==1:
        return arr
    else:
        m=len(arr)
        if m%2 !=0:
            m=m-1
        
        midPos=int(m/2)
        firstHalf=mergeSort(arr[:midPos])
        secondHalf=mergeSort(arr[midPos:])
        return merge(firstHalf,secondHalf)


# In[53]:


mergeSort([1,5,6,7,3,4,9])

