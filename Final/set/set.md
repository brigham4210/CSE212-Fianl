#Python Set Tutorial

- [back](../welcome.md)

**Introduction of Set:**
    
Sets are used to store multiple items in a single variable. A set is a collection which is unordered, unchangeable, and unindexed.
    
Since Sets are unordered, the order is not important. The output may always look different when you print it, but all of the outputs are considered as the same.
    
Set items are unchangeable, but you can remove items and add new items. Duplicates is not allowed for sets. Sets cannot have two items with the same value.
    
Sets are useful for summarizing data and finding duplicates.

**Example of a set:**
```
a_set = {"a","a","b","b","b","d",1,2,3}
print(a_set) # output might be different.
```
Output:
    
    {'d', 1, 2, 3, 'a', 'b'} 

According to the example, we can see the output does not contain any same values, and the set is unordered as well.

#Functions of the Set:
**Add and Remove:**
Although Sets are unchangeable, we still can add or remove items into a set.

Example:
```python
one_set = {1,2,3,4,5}
one_set.remove(1)
one_set.remove(3)
one_set.remove(5)
print(one_set)
one_set.add(6)
one_set.add(8)
one_set.add(10)
print(one_set)
```
Output:
    
    {2, 4}
    {2, 4, 6, 8, 10}

Add and remove functions are O(1) because the performance of the set is based on the performance of the hashing algorithm.

**Chaining:**
Chaining is a method that makes a list of values that occupy the same space, so we do not need to look for a new space in the set.

Before learning chaining function, we need to know the **hashing** function.

Hashing is a process of mapping an item to an index location. It does not require searching throught the data structure, hashing is O(1).

Once we know how hashing works, we can know how to do chaining. 

Example:
```python
set = {1,2,3,4,5,6,7,8,9,10,11}
ar = ["none","none","none","none"]

def hashing(number):
    a = number % 4
    if ar[a-1] == "none": # the number will replace the none
        ar[a-1] = number
    elif type(ar[a-1]) == int: # when it has collision, the item will become a list to sotre more items
        ar[a-1] = [ar[a-1], number]
    else:
        ar[a-1].append(number)
    print(ar)

for i in set:
    hashing(i)
```
Output:

    [1, 'none', 'none', 'none']
    [1, 2, 'none', 'none']
    [1, 2, 3, 'none']
    [1, 2, 3, 4]
    [[1, 5], 2, 3, 4]
    [[1, 5], [2, 6], 3, 4]
    [[1, 5], [2, 6], [3, 7], 4]
    [[1, 5], [2, 6], [3, 7], [4, 8]]
    [[1, 5, 9], [2, 6], [3, 7], [4, 8]]
    [[1, 5, 9], [2, 6, 10], [3, 7], [4, 8]]
    [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8]]


#Practice and challenge
- [Practice](set-Q.py)

**Goal of output:**

    I have {'knife', 'pens', 'toys', 'pencils'} in my bag, I am a bad student.
    
    Then, I have {'pens', 'pencils'} in my bag, I am a good student.
    
    Now, I have {'pens', 'pencils', 'ruler', 'eraser'} in my bag, I am a very good student.

**Answer:**
- [Answer](set-A.py)

# [back](../welcome.md)