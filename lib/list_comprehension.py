#!/usr/bin/env python3
#new_list = [optional_operation(item) for item in old_list if optional_condition == True]

def return_evens(num_list):
    return [x for x in num_list if x % 2 == 0]
    
   #Using a list comprehension, write a function make_exclamation() that takes a list of sentence strings 
   #and returns a list of sentence strings with exclamation marks at the end.
def make_exclamation(sentence_list):
    return [x + "!" for x in sentence_list]