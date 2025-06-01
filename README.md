# big-o-visualizer
Pet-project визуализация реализации функций с результатами BigO
# Big-O Complexity Visualizer

## Описание проекта
Проект предоставляет инструменты для визуализации временной сложности алгоритмов (Big-O notation) в Python. Включает два основных подхода:
1. Декоратор `complexity_visualizer` для автоматического анализа функций
2. Ручной метод с использованием `timeit` и `matplotlib`

## Установка
```bash
pip install matplotlib
```

## Использование

### 1. Декоратор для автоматического анализа
```python
from complexity_analyzer import complexity_visualizer

@complexity_visualizer(
    test_sizes=[10, 100, 500, 1000],
    number=10,
    reference_curve=lambda n: n  # Эталонная кривая O(n)
)
def linear_algorithm(data):
    """Алгоритм с линейной сложностью O(n)"""
    return sum(data)

linear_algorithm([])  # Вызовет автоматическое тестирование и построение графика
```

### 2. Ручной метод анализа
```python
import timeit
import matplotlib.pyplot as plt

def quadratic(n):  # Алгоритм с квадратичной сложностью O(n²)
    return sum(x * y for x in range(n) for y in range(n))

# Параметры тестирования
sizes = [10, 100, 500, 1000]
repeats = 10

# Замер времени выполнения
times = [timeit.timeit(lambda: quadratic(n), number=repeats) for n in sizes]

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, 'o-', label='Фактическое время')
plt.plot(sizes, [n**2 / max(times) * max(sizes)**2 for n in sizes], 
         '--', label='Эталон O(n²)')
plt.xlabel('Размер данных (n)')
plt.ylabel(f'Время (сек), {repeats} повторений')
plt.title('Анализ временной сложности')
plt.legend()
plt.grid(True)
plt.show()
```

## Параметры декоратора
| Параметр         | Тип       | По умолчанию       | Описание |
|------------------|-----------|--------------------|----------|
| `test_sizes`     | list      | [10, 100, 500, 1000] | Размеры входных данных для тестирования |
| `number`         | int       | 10                 | Количество повторений для каждого замера |
| `reference_curve`| function  | None               | Функция эталонной кривой (например, lambda n: n**2) |

## Примеры анализа

### Линейный алгоритм O(n)
```python
@complexity_visualizer(reference_curve=lambda n: n)
def linear(data):
    return sum(data)
```

### Квадратичный алгоритм O(n²)
```python
@complexity_visualizer(reference_curve=lambda n: n**2)
def quadratic(data):
    return sum(x*y for x in data for y in data)
```

### Логарифмический алгоритм O(log n)
```python
@complexity_visualizer(reference_curve=lambda n: np.log(n))
def binary_search(data):
    # Реализация бинарного поиска
    ...
```

## Визуализация
График показывает:
- Фактическое время выполнения (синяя линия)
- Эталонную кривую (пунктирная линия)
- Сравнение позволяет определить сложность алгоритма

## Требования
- Python 3.6+
- matplotlib
- numpy (рекомендуется)

## Лицензия
MIT
