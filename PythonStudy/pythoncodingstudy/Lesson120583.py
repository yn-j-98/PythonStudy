'''
Created on 2024. 11. 24.

@author: yenaj
'''

def solution(array, n):
    answer = 0
    
    for i in array:
        if i ==n:
            answer += i
            
    return answer