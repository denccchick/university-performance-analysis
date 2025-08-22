import numpy as np

def bootstrap_mean_diff_test(X, Y, n_iterations=100000, alternative='two-sided'):

    X = np.array(X)
    Y = np.array(Y)
    observed_diff = np.mean(X) - np.mean(Y)
    pooled_data = np.concatenate([X, Y])
    bootstrap_diffs = np.zeros(n_iterations)

    #np.random.seed(42)  # для воспроизводимости

    for i in range(n_iterations):
        # Генерируем новые выборки с заменой из объединенных данных
        X_new = np.random.choice(pooled_data, size=len(X), replace=True)
        Y_new = np.random.choice(pooled_data, size=len(Y), replace=True)
        bootstrap_diffs[i] = np.mean(X_new) - np.mean(Y_new)

    # Вычисляем p-value в зависимости от альтернативы
    if alternative == 'two-sided':
        p_value = (np.sum(np.abs(bootstrap_diffs) >= np.abs(observed_diff))) / n_iterations
    elif alternative == 'greater':
        p_value = (np.sum(bootstrap_diffs >= observed_diff)) / n_iterations
    elif alternative == 'less':
        p_value = (np.sum(bootstrap_diffs <= observed_diff)) / n_iterations
    else:
        raise ValueError("alternative must be 'two-sided', 'greater', or 'less'")

    return p_value



# Функция для выполнения Z-теста для двух пропорций
def z_test_proportions(x1, n1, x2, n2):
    """
    Выполняет Z-тест для сравнения двух пропорций.

    Параметры:
        x1, x2: Число успехов (несдавших) в выборках 1 и 2
        n1, n2: Размеры выборок 1 и 2

    Возвращает:
        z_stat: Статистика Z
        p_value: Двустороннее p-значение

    Математически:
        Z = (p̂1 - p̂2) / sqrt(p̂(1 - p̂)(1/n1 + 1/n2))
        где p̂ = (x1 + x2) / (n1 + n2) - объединенная пропорция
    """
    if n1 == 0 or n2 == 0 or (x1 + x2) == 0 or (n1 + n2) == (x1 + x2):
        return np.nan, np.nan

    # Вычисляем выборочные пропорции
    p1 = x1 / n1
    p2 = x2 / n2

    # Объединенная пропорция
    p = (x1 + x2) / (n1 + n2)

    # Стандартная ошибка
    se = np.sqrt(p * (1 - p) * (1/n1 + 1/n2))

    # Статистика Z
    z_stat = (p1 - p2) / se

    # Двустороннее p-значение
    p_value = 2 * (1 - norm.cdf(np.abs(z_stat)))

    return z_stat, p_value
