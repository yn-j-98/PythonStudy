'''
Created on 2024. 11. 26.

@author: yenaj
'''
## 3번째 일시
## 4번째 평균기온
import csv

import matplotlib.pyplot as plt


# jsoup, ojdbc6.jar
# 파이썬 라이브러리 설치 관리자 이름 = pip
# pip install matplotlib  //cmd에 입력하기
file_path = "test.csv"

dates = []
temps = []
with open(file_path,mode='r') as file :
    reader = csv.reader(file) # 자바에서는 패키지, 파이썬에서는 모듈

    header = next(reader)

##    i = 0
    for row in reader :# 향상된 for문은    for v in 집합
        a = row[2] ## 12월인 데이터만 출력하고싶어~~
        b = row[-2] # 최저기온
         
        if a.startswith("Dec") :#if a가 Dec 시작하면 :
            print(a, b) # row가 list 타입이라는 사실도 확인 가능!
            dates.append(a)
            temps.append(float(b))
##            i += 1
##            if i == 10 : # 데이터를 10개만 보고싶을 때
##                break

plt.plot(dates,temps,marker='o',color='r',linestyle=':') # 선
##plt.plot(dates,temps) #그래프를 그리고(x축, y축) # 기본
plt.title("Temperature in December", fontsize=15)
plt.xlabel("Date", fontsize = 10)
plt.ylabel("Temperature", fontsize=10)
plt.show() #그린 그래프를 화면에 출력해줘()


