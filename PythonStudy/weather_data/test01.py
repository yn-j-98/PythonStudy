'''
Created on 2024. 11. 26.

@author: yenaj
'''
## 3번째 일시
## 4번째 평균기온
import csv

file_path = "test.csv"

with open(file_path,mode='r') as file :
    reader = csv.reader(file) # 자바에서는 패키지, 파이썬에서는 모듈

    header = next(reader)
    
    for row in reader :# 향상된 for문은    for v in 집합
        a = row[2] ## 12월인 데이터만 출력하고싶어~~
        b = row[-2] # 최저기온
        
        if a.startswith("Dec") :#if a가 Dec 시작하면 :
            print(a, b) # row가 list 타입이라는 사실도 확인 가능!
