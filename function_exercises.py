#!/usr/bin/env python
# coding: utf-8


# 1. Returns True if the input is the number or string 2, False otherwise.
def is_two(n):
    return n == 2 or str(n) == '2'


# 2. It should return **True** if the passed string is a vowel, **False** otherwise.
def is_vowel(char):
    return char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u'

###Another Way###
def is_vowel1(char):
    vowels = 'aeiou'
    return char.lower() in vowels

# Lauren's code
def is_vowel(somestring) :
    #check that the arg is a str
    if type(somestring) == str:
        
        #if the str is 1 char and a letter
        if len(somestring) == 1 and somestring.isalpha():
            
            #return bool ans to: lower-letter in vowel list?
            return somestring.lower() in list('aeiou')
        
        #return false if string fails 1 alpha-char length
        else:
            return False
    # returns false if input is not a str
    else:
        return False


# 3. returns **True** if the passed string is a consonant, **False** otherwise. Use your **is_vowel** function to accomplish this.
def is_vowel(char):
    vowels = 'aeiou'
    return char.lower() in vowels
# keep in mind I technically don't have to re-write this above because if it has already
# been ran in #2, then it should already be stored (vowels).


def is_consonant(char):
    return char.isalpha() and not is_vowel(char) 
# .isalpha() checks if the character is a letter


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def is_vowel(char):
    vowels = 'aeiou'
    return char.lower() in vowels

def cap_if_consonant(word):
    if word and is_consonant(word[0]):
        return word.capitalize()
    else:
        return word

# Below checks for consonant, top one not needed if already ran it in above questions
def is_consonant(char):
    return char.isalpha() and not is_vowel(char) 


# 5. Define a function named **calculate_tip**. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip_percentage, bill_total):
    if 0 <= tip_percentage <= 1:
# rather than the 'if' another way is...
# tip_percentage = min(1, max(0, tip_percentage))
    # the max keeps it above 0 and the min keep it at 1 at the most.
        tip_amount = tip_percentage * bill_total
        return tip_amount
    else:
        return "Invalid tip percentage. Please enter a number between 0 and 1."


# 6. Define a function named **apply_discount**. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(discount_percentage, original_price):
    discount_percentage = min(1, max(0, discount_percentage))
    discount_price = (original_price - (discount_percentage * original_price))
    return discount_price


# 7. Define a function named **handle_commas**. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(input_str):
    # remove commas
    cleaned_str = input_str.replace(',', '')
    
    try:
        # convert to a float
        result = float(cleaned_str)
        return result
    except ValueError:
        print(f'Error: Unable to convert {input_str} to a number.')
        return None
    
# Lauren's code
"""
This function will:
- check if input is a string
    -removes any commas
    -check if the stripped input is a digit
        - if True, returns input as an integer
        - False otherwise
- if not a string, returns false stmt
"""
def handle_commas(fakenum):
    if type(fakenum) == str:
        stripfakenum = fakenum.replace(",", "")
        if stripfakenum.isdigit():
            return int(stripfakenum)
        else:
            return False
    else:
        False
### go to repo to see the updated one to handle numbers


# 8. Define a function named **get_letter_grade**. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(score):
    if type(score) == int:
        if 90 <= score <= 100:
            return 'A'
        elif 80 <= score < 90:
            return 'B'
        elif 70 <= score < 80:
            return 'C'
        elif 60 <= score < 70:
            return 'D'
        elif 0 <= score < 60:
            return 'F'
    else:
        return 'Invalid score. Please enter a number between 0 and 100.'


# 9. Define a function named **remove_vowels** that accepts a string and returns a string with all the vowels removed.
def remove_vowels(input_str):
    # remove vowels
    vowels = 'aeiouAEIOU'
#     cleaned_str = ''.join(char for char in input_str if char not in vowels)
#     Another Version # ^^^
    cleaned_str = input_str
    for vowel in vowels:
        cleaned_str = cleaned_str.replace(vowel, '')
    return cleaned_str

# Lauren's code ('adding to remove' method)

def remove_vowels(word):
    # empty string for items to keep
    new_word = ""
    
    # loop iteration over word
    for letter in word:
        
        # conditional check for whether letter in word is not a vowel.
        if not is_vowel(letter):
            
            # If so, add to empty string
            new_word += letter
            
    # return concatenated empty string
    return new_word


# 10. Define a function named **normalize_name**. It should accept a string and return a valid python identifier, that is:
# * anything that is not a valid python identifier should be removed
# * leading and trailing whitespace should be removed
# * everything should be lowercase
# * spaces should be replaced with underscores
# * for example:
#     * Name will become name
#     * First Name will become first_name
#     * % Completed will become completed

def normalize_name(input_str):
    
    # Remove anything that isn't a valid python identifier
    cleaned_str = ''.join(char.lower() if char.isalnum() or char.isspace() else '' for char in input_str)
    # .isalnum - Returns True if all characters in the string are alphanumeric
    
    # Remove leading and trailing whitespace (done this before)
    cleaned_str = cleaned_str.strip()
    
    # Replace spaces with underscores (easy now)
    cleaned_str = cleaned_str.replace(' ', '_')
    
    return cleaned_str


# 11. Write a function named **cumulative_sum** that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# * cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# * cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(oldlist):
    
    newlist=[]
    
    #intitalize a variable to store the cumulative sum
    c_sum = 0
    
    for num in oldlist:
        #add the current number to the cumulative sum
        c_sum += num
#         print(f'cumulative: {c_sum}')
        #append the cumulative sum to the newlist
        newlist.append(c_sum)



### Only question I didn't get to attempt, try again later on my own

# ## Bonus
# 1. Create a function named **twelveto24**. It should accept a string in the format **10:45am** or **4:30pm** and return a string that is the representation of the time in a 24-hour format. **Bonus** write a function that does the opposite.
# 2. Create a function named **col_index**. It should accept a spreadsheet column name, and return the index number of the column.
# * col_index('A') returns 1
# * col_index('B') returns 2
# * col_index('AA') returns 27

def twelveto24(time):
    # separate hours and minutes
    time = time.split(':') # split at colon as list
    hour = time[0] # store hrs in variables
    mins = time[1].split(' ') # store minutes in list
    minutes = [0] # store min in var
    timeofday = mins[1] # store time of day in var
    
    if timeofday.lower() == 'pm':
        
        hour = 12 + int(hour)
        print(hour)
        
        return str(hour) + ':' + str(minutes) + timeofday
    else:
        return hour + ':' + minutes + timeofday