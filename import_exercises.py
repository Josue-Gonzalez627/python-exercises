#!/usr/bin/env python
# coding: utf-8

# ### Exercises
# You will need to use imports to complete each exercise. These exercises will also strengthen your problem solving and python coding skills.
# 
# You will be directed to create specific files in part 1, for the rest you may do your work in either **import_exercises.py** or **import_exercises.ipynb**.
# 

# 1.) Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
# 

# a.) Run an interactive python session and import the module. Call the **is_vowel** function using the **.** syntax.
# 

# In[3]:


# from function_exercises import is_vowel
# is_vowel('e')


# b.) Create a file named **import_exercises.py**. Within this file, use **from** to import the **calculate_tip** function directly. Call this function with values you choose and print the result.
# 

# In[ ]:


from function_exercises import calculate_tip



# c.) Create a jupyter notebook named **import_exercises.ipynb**. Use **from** to import the **get_letter_grade** function and give it an alias. Test this function in your notebook.
# 

# In[ ]:





# Make sure your code that tests the function imports is run from the same directory that your functions exercise file is in.
# 

# 2.) Read about and use the **itertools** module from the python standard library to help you solve the following problems. Note: Many of these functions in this library return an object, to see the results of the function, cast this object as a list.
# 

# * How many different ways can you combine a single letter from "abc" with either 1, 2, or 3?

# In[ ]:





# * How many different combinations are there of 2 letters from "abcd"?

# In[ ]:





# * How many different permutations are there of 2 letters from "abcd"?

# In[ ]:





# 3.) Save **this file** as **profiles.json** inside of your exercises directory (right click -> save file as...).
# 

# Use the **load** function from the **json** module to open this file.
# 

# In[ ]:


import json

json.load(open('profiles.json'))


# Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
# 

# * Total number of users

# In[ ]:





# * Number of active users
# 

# In[ ]:





# * Number of inactive users
# 

# In[ ]:





# * Grand total of balances for all users
# 

# In[ ]:





# * Average balance per user
# 

# In[ ]:





# * User with the lowest balance
# 

# In[ ]:





# * User with the highest balance
# 

# In[ ]:





# * Most common favorite fruit
# 

# In[ ]:





# * Least most common favorite fruit
# 

# In[ ]:





# * Total number of unread messages for all users
# 

# In[ ]:





# ### BONUS
# 
# Continue to use the list of dictionaries.

# * Find out how many total unique tags there are for all users
# 

# In[ ]:





# * Display a user's name and all of their respective friends

# In[ ]:




