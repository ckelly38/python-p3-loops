#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    # normally for something like counting down, I would use a for loop.
    # I am forced to use a while loop.
    i = 10;
    while((i > 0) and (i < 10 or i == 10)):
        print(i);
        i -= 1;
    print("Happy New Year!");
    return None;

def square_integers(int_list):
    # code goes here!
    if (int_list == None): return None;
    elif (len(int_list) < 1): return [];
    else: pass;
    return [num * num for num in int_list];

def fizzbuzz():
    # code goes here!
    for i in range(100):
        num = i + 1;
        if (num % 3 == 0): print("Fizz", end="");
        else: pass;
        if (num % 5 == 0): print("Buzz", end="");
        else: pass;
        if ((num % 3 == 0) or (num % 5 == 0)): print("");
        else: print(num);
    return None;
