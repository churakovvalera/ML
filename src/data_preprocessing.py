import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def preprocess_data(data):
    # Очистка данных
    data = data.dropna()

    # Преобразование категориальных признаков
    data = pd.get_dummies(data)

    # Масштабирование числовых признаков
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    return data_scaled
