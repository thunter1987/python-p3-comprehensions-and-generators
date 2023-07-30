#!/usr/bin/env python3

def return_evens(num_list):
    num_list_evens = [num for num in num_list if num%2 ==0]
    return num_list_evens

def make_exclamation(sentence_list):
    new_sentence_list = [sentence + "!" for sentence in sentence_list]
    return new_sentence_list