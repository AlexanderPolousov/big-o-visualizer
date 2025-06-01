import timeit
import matplotlib.pyplot as plt
from functools import wraps


def complexity_visualizer(test_sizes=[10, 100, 500, 1000], number=10, reference_curve=None):
    """
    Декоратор для визуализации временной сложности алгоритма

    :param test_sizes: список размеров входных данных для тестирования
    :param number: количество повторений для каждого замера
    :param reference_curve: функция эталонной кривой (например, lambda n: n**2)
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Замеряем время выполнения
            times = []
            for n in test_sizes:
                # Подготавливаем тестовые данные
                test_data = list(range(n))
                # Замеряем время
                t = timeit.timeit(lambda: func(test_data), number=number)
                times.append(t)

            # Строим график
            plt.figure(figsize=(10, 6))
            plt.plot(test_sizes, times, 'o-', label=f'Фактическое время ({func.__name__})')

            # Добавляем эталонную кривую, если указана
            if reference_curve:
                ref_values = [reference_curve(n) for n in test_sizes]
                # Нормализуем кривую для сравнения
                scale_factor = times[-1] / ref_values[-1]
                plt.plot(test_sizes, [v * scale_factor for v in ref_values],
                         '--', label=f'Эталон: {reference_curve.__name__}')

            plt.xlabel('Размер данных (n)')
            plt.ylabel(f'Время (сек), {number} повторений')
            plt.title('Анализ временной сложности')
            plt.legend()
            plt.grid(True)
            plt.show()

            return func(*args, **kwargs)

        return wrapper

    return decorator
@complexity_visualizer(reference_curve=lambda n: n)
def linear_algorithm(data):
    return sum(data)

linear_algorithm([])
#
# # Пример использования:
#
# # 1. Определяем эталонную кривую для O(n²)
# def quadratic_curve(n):
#     return 1
#
#
# # 2. Применяем декоратор к тестируемой функции
# @complexity_visualizer(test_sizes=[10, 50, 100, 200, 500],
#                        number=5,
#                        reference_curve=quadratic_curve)
# def quadratic_algorithm(data):
#     return sum(x * y for x in data for y in data)
#
#
# # 3. Вызываем функцию - автоматически построится график
# quadratic_algorithm([])  # Пустой список - данные генерируются внутри декоратора