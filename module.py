# 이상치 식별 함수 정의
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = (df[column] < lower_bound) | (df[column] > upper_bound)
    return outliers


# 수축기 혈압 및 이완기 혈압 범주화 함수 정의
def categorize_bp(systolic, diastolic):
    if   (90 <= systolic < 120 and 60 <= diastolic < 80):
        return 'normal'
    elif (systolic < 90 or diastolic < 60) :
        return 'hypotension'
    elif (120 <= systolic < 130 and 80 <= diastolic < 85) or \
         (systolic < 130 and 80 <= diastolic < 85):
        return 'prehypertension stage 1'
    elif (130 <= systolic < 140 and 85 <= diastolic < 90) or \
         (systolic < 140 and 85 <= diastolic < 90):
        return 'prehypertension stage 2'
    elif (140 <= systolic < 160 and 90 <= diastolic < 100) or \
         (systolic < 160 and 90 <= diastolic < 100):
        return 'hypertension stage 1'
    elif systolic >= 160 or diastolic >= 100:
        return 'hypertension stage 2'
    elif systolic >= 140 or diastolic < 90:
        return 'isolated systolic hypertension'