#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

def random_multiply():
  while True:
    # Generate random integers A and B between 1 and 9
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = a * b
    print(f'A: {a}, C: {c}')
    if c == 4:
      print(f'Success! A: {a}, B: {b}')
      break

# Call the function
random_multiply()


# In[ ]:




