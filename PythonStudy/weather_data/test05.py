import csv
import matplotlib.pyplot as plt

file_path = "test.csv"

# 월별로 가장 낮은 최저기온과 가장 높은 최고기온을 저장할 리스트
winter_dates = []
winter_temps = []
summer_dates = []
summer_temps = []

# 파일 읽기
with open(file_path, mode='r') as file:
    reader = csv.reader(file)

    header = next(reader)  # 헤더 건너뛰기

    winter_data = {'Dec': [], 'Jan': [], 'Feb': []}
    summer_data = {'Jun': [], 'Jul': [], 'Aug': []}

    for row in reader:
        date = row[2]  # 날짜 정보
        temp_min = row[-2]  # 최저기온 (겨울)
        temp_max = row[-5]  # 최고기온 (여름)

        # 겨울 데이터 (12월, 1월, 2월)
        if date.startswith("Dec"):
            winter_data["Dec"].append(float(temp_min))
        elif date.startswith("Jan"):
            winter_data["Jan"].append(float(temp_min))
        elif date.startswith("Feb"):
            winter_data["Feb"].append(float(temp_min))

        # 여름 데이터 (6월, 7월, 8월)
        elif date.startswith("Jun"):
            summer_data["Jun"].append(float(temp_max))
        elif date.startswith("Jul"):
            summer_data["Jul"].append(float(temp_max))
        elif date.startswith("Aug"):
            summer_data["Aug"].append(float(temp_max))

    # 각 월의 가장 낮은 최저기온과 가장 높은 최고기온을 구하기
    winter_dates = list(winter_data.keys())
    winter_temps = [min(winter_data[month]) for month in winter_dates]

    summer_dates = list(summer_data.keys())
    summer_temps = [max(summer_data[month]) for month in summer_dates]

# 선 그래프 그리기
plt.plot(winter_dates, winter_temps, marker='o', color='b', linestyle='-', label='Winter Min Temp')
plt.plot(summer_dates, summer_temps, marker='o', color='r', linestyle='--', label='Summer Max Temp')

# 그래프 제목 및 레이블 설정
plt.title("Winter Minimum Temperature vs Summer Maximum Temperature", fontsize=15)
plt.xlabel("Month", fontsize=10)
plt.ylabel("Temperature (°C)", fontsize=10)

# x축 레이블 회전 및 폰트 크기 조정
plt.xticks(rotation=45, fontsize=8)

# 범례 추가
plt.legend()

# 그래프 레이아웃 조정 및 출력
plt.tight_layout()
plt.show()
