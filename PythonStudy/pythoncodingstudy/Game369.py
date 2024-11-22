'''
Created on 2024. 11. 22.

@author: yenaj
'''
def solution(order):
    answer = 0
    
    # order가 0이 될 때까지 반복
    while order > 0:
        digit = order % 10  # order의 마지막 자릿수
        if digit == 3 or digit == 6 or digit == 9:
            answer += 1  # 3, 6, 9가 있으면 박수 횟수 증가
        order //= 10  # 마지막 자릿수를 제거
        
    return answer