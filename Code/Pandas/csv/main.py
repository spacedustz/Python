import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV 파일을 읽어오기
df = pd.read_csv('online_retail_data.csv')

# 데이터 프레임의 상위 5개 행을 출력
print(df.head())

# 데이터 프레임의 기본 정보 출력 (열 이름, 데이터 타입, null 값 등)
print(df.info())

# 기술 통계 요약 (수치형 데이터에 대해 count, mean, std, min, max 등)
print(df.describe())

# 새로운 열 추가: 총 매출 (가격 * 수량)
df['TotalRevenue'] = df['Price'] * df['Quantity']
print(df.head())

# 날짜 형식 변환 및 새로운 열 추가: 월별 매출 분석을 위해 'OrderMonth' 열 추가
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['OrderMonth'] = df['OrderDate'].dt.to_period('M')
print(df.head())

# 월별 총 매출 계산
monthly_sales = df.groupby('OrderMonth')['TotalRevenue'].sum()
print(monthly_sales)

# 국가별 총 매출 계산
country_sales = df.groupby('Country')['TotalRevenue'].sum()
print(country_sales)

# 카테고리별 매출 비율 계산
category_sales = df.groupby('Category')['TotalRevenue'].sum()
category_sales_percentage = category_sales / category_sales.sum() * 100
print(category_sales_percentage)

# 특정 국가의 매출 데이터 필터링 (예: 미국)
usa_sales = df[df['Country'] == 'USA']
print(usa_sales)

# 피벗 테이블 생성: 월별 국가별 매출 합계
pivot_table = df.pivot_table(values='TotalRevenue', index='OrderMonth', columns='Country', aggfunc='sum')
print(pivot_table)

# 히스토그램 생성: 제품별 판매 수량 분포
df['Quantity'].hist()
plt.title('제품 수량 분포')
plt.xlabel('수량')
plt.ylabel('빈도수')
plt.show()

# 수치형 데이터만 포함하도록 필터링
numeric_df = df.select_dtypes(include=[float, int])

# 상관관계 행렬 계산
correlation_matrix = numeric_df.corr()
print(correlation_matrix)

# 상관관계 히트맵 시각화
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('상관관계 행렬 히트맵')
plt.show()

# 업데이트 된 파일 저장
df.to_csv('updated_online_retail_data.csv', index=False)
