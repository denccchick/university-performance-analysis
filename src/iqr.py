import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def remove_outliers_iqr_0(data, k=2.5, visualize=True):
    """
    Удаляет выбросы из данных методом межквантильного размаха с возможностью визуализации.

    Параметры:
        data (np.array): Ваши данные (например, OMA_res_1)
        k (float): Коэффициент для определения границ (1.5 - стандартное значение)
        visualize (bool): Показывать ли график

    Возвращает:
        np.array: Данные без выбросов
    """
    # Проверка и преобразование данных в numpy array
    data = np.asarray(data).flatten()

    # Вычисляем квартили
    q1, q3 = np.quantile(data, [0.25, 0.75])
    iqr = q3 - q1

    # Определяем границы
    lower_bound = q1 - k * iqr
    upper_bound = q3 + k * iqr

    # Фильтруем данные
    filtered_data = data[(data >= lower_bound) & (data <= upper_bound)]

    # Визуализация с использованием seaborn
    if visualize:
        plt.figure(figsize=(12, 6))

        # Создаем DataFrame для визуализации
        df_plot = pd.DataFrame({
            'Data': ['Original'] * len(data) + ['Filtered'] * len(filtered_data),
            'Value': np.concatenate([data, filtered_data])
        })

        # Боксплот
        plt.subplot(1, 2, 1)
        sns.boxplot(data=data, orient='h', color='skyblue')
        plt.title("Исходные данные с выбросами")
        plt.xlabel("Значения")

        plt.subplot(1, 2, 2)
        sns.boxplot(data=filtered_data, orient='h', color='lightgreen')
        plt.title("Очищенные данные")
        plt.xlabel("Значения")

        plt.tight_layout()
        plt.show()

        print(f"Удалено выбросов: {len(data) - len(filtered_data)}")
        print(f"Осталось точек: {len(filtered_data)}")

    return filtered_data



# new: нижняя граница изменена на 0.05
# Комбинированный метод
def remove_outliers_iqr(data, k=1.5, visualize=True):
    """
    Удаляет выбросы из данных методом межквантильного размаха с возможностью визуализации. Нижняя граница заменена на 0.05

    Параметры:
        data (np.array): Ваши данные (например, OMA_res_1)
        k (float): Коэффициент для определения границ (1.5 - стандартное значение)
        visualize (bool): Показывать ли график

    Возвращает:
        np.array: Данные без выбросов
    """
    # Проверка и преобразование данных в numpy array
    data = np.asarray(data).flatten()

    # Вычисляем квартили
    q1, q3 = np.quantile(data, [0.25, 0.75])
    iqr = q3 - q1

    # Определяем границы
    lower_bound = 0.05 #q1 - k * iqr
    upper_bound = q3 + k * iqr

    # Фильтруем данные
    filtered_data = data[(data >= lower_bound) & (data <= upper_bound)]

    # Визуализация с использованием seaborn
    if visualize:
        plt.figure(figsize=(12, 6))

        # Создаем DataFrame для визуализации
        df_plot = pd.DataFrame({
            'Data': ['Original'] * len(data) + ['Filtered'] * len(filtered_data),
            'Value': np.concatenate([data, filtered_data])
        })

        # Боксплот
        plt.subplot(1, 2, 1)
        sns.boxplot(data=data, orient='h', color='skyblue')
        plt.title("Исходные данные с выбросами")
        plt.xlabel("Значения")

        plt.subplot(1, 2, 2)
        sns.boxplot(data=filtered_data, orient='h', color='lightgreen')
        plt.title("Очищенные данные")
        plt.xlabel("Значения")

        plt.tight_layout()
        plt.show()

        print(f"Удалено выбросов: {len(data) - len(filtered_data)}")
        print(f"Осталось точек: {len(filtered_data)}")

    return filtered_data
