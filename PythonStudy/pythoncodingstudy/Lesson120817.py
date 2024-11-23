'''
Created on 2024. 11. 23.

@author: yenaj
'''

def solution(numbers):
    sum = 0
    for i in numbers:
        sum += i
    answer = sum / len(numbers)
    return answer
