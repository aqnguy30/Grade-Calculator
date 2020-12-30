#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 12:56:23 2020

@author: anhnguyen
"""

#Define class myException_1
class myException_1(Exception):
    pass

#Define function validate_input()
def validate_input():
    while True:
        try:
            score = float(input("Enter a score between 0.0 and 100.0: "))
            if score < 0 or score > 100: #check if inputs are within the range
                raise myException_1("something happened")
            return score
            break
        except ValueError: #check if inputs are not numbers
            print("Please enter only number. Try again!")
        except myException_1:
                print("Score should be between 0.0 and 100.0. Try again!")
#print(validate_input())
score = validate_input()

def calculate_grade(score):
    #check conditions of scores to fall into each grade category
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    elif score < 60:
        grade = 'F'
    #Display the output
    print(grade + ' Grade')
calculate_grade(score)
