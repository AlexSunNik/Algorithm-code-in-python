
# coding: utf-8

# In[24]:


#The code below is based on the merge sort algorithm


# In[25]:


def merge_and_countSplitInv(a,b):
    splitInvCount=0
    c=[]
    while len(a)>0 and len(b)>0:
        if a[0]<=b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
            splitInvCount+=len(a)
    if len(a)==0:
        c+=b
    else:
        c+=a
    
    return splitInvCount,c


# In[26]:


#Try a simple example
#Expected Output: 3, [1,2,3,4,5,6]
merge_and_countSplitInv([1,3,5],[2,4,6])


# In[27]:


def mergeSort_and_countInv(arr,invCount):
    if invCount==None:
        invCount=0
        
    if len(arr)==1:
        return 0, arr
    else:
        m=len(arr)
        if m%2 != 0:
            m-=1
        midPos=int(m/2)
        firstHalf_count, firstHalf_sorted=mergeSort_and_countInv(arr[:midPos],invCount)
        secondHalf_count, secondHalf_sorted=mergeSort_and_countInv(arr[midPos:],invCount)
        splitInvCount, sorted_arr=merge_and_countSplitInv(firstHalf_sorted,secondHalf_sorted)
        
        cur_invCount=firstHalf_count+secondHalf_count+splitInvCount
        invCount+=cur_invCount
        
        return invCount, sorted_arr


# In[28]:


#Try a simple example
#Expected Output: 12, [1, 2, 3, 4, 5, 7, 8, 9]
mergeSort_and_countInv([4,5,3,2,7,9,1,8],None)


# In[50]:


text_file = open("testarr.txt", "r")
test_arr = text_file.read().split('\n')


# In[61]:


test_arr.remove('')


# In[65]:


for i in range(len(test_arr)):
    test_arr[i]=int(test_arr[i])


# In[67]:


mergeSort_and_countInv(test_arr,None)

