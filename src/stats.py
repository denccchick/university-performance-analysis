import numpy as np
from scipy.stats import skew

def calculate_stats(plan_1_scores, plan_2_scores):
    """
    Вычисляет статистические характеристики для двух наборов данных

    Parameters:
    plan_1_scores (array): данные по плану 1
    plan_2_scores (array): данные по плану 2

    Returns:
    dict: словарь со статистиками
    """
    stats_dict = {'plan_1': {}, 'plan_2': {}}

    if len(plan_1_scores) > 0:
        stats_dict['plan_1']['median'] = np.median(plan_1_scores)
        stats_dict['plan_1']['variance'] = np.var(plan_1_scores, ddof=1)
        stats_dict['plan_1']['skewness'] = skew(plan_1_scores)
        stats_dict['plan_1']['mean'] = np.mean(plan_1_scores)
        stats_dict['plan_1']['sample_size'] = len(plan_1_scores)  # Добавим размер выборки
    else:
        print("  План 1: Нет данных после очистки.")
        stats_dict['plan_1'] = {'median': np.nan, 'variance': np.nan,
                               'skewness': np.nan, 'mean': np.nan, 'sample_size': 0}

    if len(plan_2_scores) > 0:
        stats_dict['plan_2']['median'] = np.median(plan_2_scores)
        stats_dict['plan_2']['variance'] = np.var(plan_2_scores, ddof=1)
        stats_dict['plan_2']['skewness'] = skew(plan_2_scores)
        stats_dict['plan_2']['mean'] = np.mean(plan_2_scores)
        stats_dict['plan_2']['sample_size'] = len(plan_2_scores)
    else:
        print("  План 2: Нет данных после очистки.")
        stats_dict['plan_2'] = {'median': np.nan, 'variance': np.nan,
                               'skewness': np.nan, 'mean': np.nan, 'sample_size': 0}

    return stats_dict


def print_statistics(all_stats, subjects):

    """
    Args:
    all_stats: dict{sublect: stats}
    subjects: list

    Returns:
    Красиво выводит статистики по всем предметам
    """
    print(" СТАТИСТИЧЕСКИЕ ХАРАКТЕРИСТИКИ")
    print("=" * 50)

    for subject in subjects:
        print(f"\n Предмет: {subject}")
        print("-" * 30)

        stats = all_stats[subject]

        # План 1
        print("План 1:")
        if stats['plan_1']['sample_size'] > 0:
            print(f"  Объем выборки: {stats['plan_1']['sample_size']}")
            print(f"  Медиана: {stats['plan_1']['median']:.3f}")
            print(f"  Дисперсия: {stats['plan_1']['variance']:.5f}")
            print(f"  Асимметрия: {stats['plan_1']['skewness']:.5f}")
            print(f"  Среднее: {stats['plan_1']['mean']:.4f}")
        else:
            print("  Нет данных")

        # План 2
        print("План 2:")
        if stats['plan_2']['sample_size'] > 0:
            print(f"  Объем выборки: {stats['plan_2']['sample_size']}")
            print(f"  Медиана: {stats['plan_2']['median']:.3f}")
            print(f"  Дисперсия: {stats['plan_2']['variance']:.5f}")
            print(f"  Асимметрия: {stats['plan_2']['skewness']:.5f}")
            print(f"  Среднее: {stats['plan_2']['mean']:.4f}")
        else:
            print("  Нет данных")
