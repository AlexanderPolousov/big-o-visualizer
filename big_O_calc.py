import timeit
import matplotlib.pyplot as plt

def quadratic(n):  # O(n²)
    return sum(x * y for x in range(n) for y in range(n))

sizes = [10, 100, 500, 1000]
times = [timeit.timeit(lambda: quadratic(n), number=10) for n in sizes]

plt.plot(sizes, times, 'o-', label='Фактическое время')
plt.plot(sizes, [n**2 / 1e6 for n in sizes], '--', label='O(n²)')
plt.xlabel('Размер данных (n)')
plt.ylabel('Время (сек)')
plt.legend()
plt.show()
