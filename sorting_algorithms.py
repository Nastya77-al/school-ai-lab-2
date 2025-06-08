#!/usr/bin/env python3
"""
Алгоритми сортування - Навчальний матеріал
Автор: Навчальний курс для учнів 10 класу
"""

import time
import random
from typing import List, Tuple


class SortingAlgorithms:
    """Клас з реалізаціями різних алгоритмів сортування"""
    
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
    
    def reset_counters(self):
        """Скидає лічильники операцій"""
        self.comparisons = 0
        self.swaps = 0
    
    # ==================== BUBBLE SORT ====================
    
    def bubble_sort(self, arr: List[int]) -> List[int]:
        """
        Бульбашкове сортування
        Часова складність: O(n²)
        Просторова складність: O(1)
        """
        self.reset_counters()
        n = len(arr)
        arr_copy = arr.copy()
        
        for i in range(n):
            for j in range(0, n - i - 1):
                self.comparisons += 1
                if arr_copy[j] > arr_copy[j + 1]:
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                    self.swaps += 1
        
        return arr_copy
    
    def bubble_sort_optimized(self, arr: List[int]) -> List[int]:
        """
        Оптимізоване бульбашкове сортування
        Зупиняється, якщо масив вже відсортований
        """
        self.reset_counters()
        n = len(arr)
        arr_copy = arr.copy()
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                self.comparisons += 1
                if arr_copy[j] > arr_copy[j + 1]:
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                    self.swaps += 1
                    swapped = True
            
            if not swapped:
                break
        
        return arr_copy
    
    # ==================== SELECTION SORT ====================
    
    def selection_sort(self, arr: List[int]) -> List[int]:
        """
        Сортування вибором
        Часова складність: O(n²)
        Просторова складність: O(1)
        """
        self.reset_counters()
        n = len(arr)
        arr_copy = arr.copy()
        
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.comparisons += 1
                if arr_copy[j] < arr_copy[min_idx]:
                    min_idx = j
            
            if min_idx != i:
                arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
                self.swaps += 1
        
        return arr_copy
    
    # ==================== MERGE SORT ====================
    
    def merge_sort(self, arr: List[int]) -> List[int]:
        """
        Сортування злиттям
        Часова складність: O(n log n)
        Просторова складність: O(n)
        """
        self.reset_counters()
        return self._merge_sort_recursive(arr.copy())
    
    def _merge_sort_recursive(self, arr: List[int]) -> List[int]:
        """Рекурсивна функція для merge sort"""
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self._merge_sort_recursive(arr[:mid])
        right = self._merge_sort_recursive(arr[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        """Злиття двох відсортованих масивів"""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            self.comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    # ==================== ДОДАТКОВІ АЛГОРИТМИ ====================
    
    def insertion_sort(self, arr: List[int]) -> List[int]:
        """
        Сортування вставками
        Часова складність: O(n²)
        Найкращий випадок: O(n)
        """
        self.reset_counters()
        arr_copy = arr.copy()
        
        for i in range(1, len(arr_copy)):
            key = arr_copy[i]
            j = i - 1
            
            while j >= 0 and arr_copy[j] > key:
                self.comparisons += 1
                arr_copy[j + 1] = arr_copy[j]
                j -= 1
                self.swaps += 1
            
            arr_copy[j + 1] = key
        
        return arr_copy
    
    def cocktail_sort(self, arr: List[int]) -> List[int]:
        """
        Шейкерне сортування (покращене бульбашкове)
        Сортує в обох напрямках
        """
        self.reset_counters()
        arr_copy = arr.copy()
        n = len(arr_copy)
        swapped = True
        start = 0
        end = n - 1
        
        while swapped:
            swapped = False
            
            # Прохід зліва направо
            for i in range(start, end):
                self.comparisons += 1
                if arr_copy[i] > arr_copy[i + 1]:
                    arr_copy[i], arr_copy[i + 1] = arr_copy[i + 1], arr_copy[i]
                    self.swaps += 1
                    swapped = True
            
            if not swapped:
                break
            
            end -= 1
            swapped = False
            
            # Прохід справа наліво
            for i in range(end, start, -1):
                self.comparisons += 1
                if arr_copy[i] < arr_copy[i - 1]:
                    arr_copy[i], arr_copy[i - 1] = arr_copy[i - 1], arr_copy[i]
                    self.swaps += 1
                    swapped = True
            
            start += 1
        
        return arr_copy


class SortingVisualizer:
    """Клас для візуалізації процесу сортування"""
    
    @staticmethod
    def print_array(arr: List[int], highlight_indices: List[int] = None):
        """Виводить масив з підсвічуванням певних елементів"""
        if highlight_indices is None:
            highlight_indices = []
        
        for i, val in enumerate(arr):
            if i in highlight_indices:
                print(f"[{val}]", end=" ")
            else:
                print(val, end=" ")
        print()
    
    @staticmethod
    def visualize_bubble_sort(arr: List[int]):
        """Візуалізація бульбашкового сортування"""
        n = len(arr)
        arr_copy = arr.copy()
        
        print("Початковий масив:")
        SortingVisualizer.print_array(arr_copy)
        print()
        
        for i in range(n):
            print(f"Прохід {i + 1}:")
            for j in range(0, n - i - 1):
                print(f"  Порівнюємо елементи на позиціях {j} та {j + 1}:", end=" ")
                SortingVisualizer.print_array(arr_copy, [j, j + 1])
                
                if arr_copy[j] > arr_copy[j + 1]:
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                    print(f"  → Міняємо місцями")
                    print("  ", end="")
                    SortingVisualizer.print_array(arr_copy)
                else:
                    print(f"  → Залишаємо як є")
            
            print(f"  Після проходу {i + 1}:", end=" ")
            SortingVisualizer.print_array(arr_copy)
            print()
        
        print("Відсортований масив:")
        SortingVisualizer.print_array(arr_copy)


class SortingTester:
    """Клас для тестування та порівняння алгоритмів"""
    
    def __init__(self):
        self.sorter = SortingAlgorithms()
    
    def generate_test_arrays(self, size: int) -> dict:
        """Генерує різні типи тестових масивів"""
        return {
            "random": [random.randint(1, 100) for _ in range(size)],
            "sorted": list(range(1, size + 1)),
            "reversed": list(range(size, 0, -1)),
            "nearly_sorted": self._generate_nearly_sorted(size),
            "few_unique": [random.randint(1, 5) for _ in range(size)]
        }
    
    def _generate_nearly_sorted(self, size: int) -> List[int]:
        """Генерує майже відсортований масив"""
        arr = list(range(1, size + 1))
        # Робимо кілька випадкових обмінів
        swaps = size // 10
        for _ in range(swaps):
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    
    def compare_algorithms(self, size: int = 100):
        """Порівнює різні алгоритми сортування"""
        test_arrays = self.generate_test_arrays(size)
        algorithms = {
            "Bubble Sort": self.sorter.bubble_sort,
            "Bubble Sort (Opt)": self.sorter.bubble_sort_optimized,
            "Selection Sort": self.sorter.selection_sort,
            "Merge Sort": self.sorter.merge_sort,
            "Insertion Sort": self.sorter.insertion_sort,
            "Cocktail Sort": self.sorter.cocktail_sort
        }
        
        print(f"Порівняння алгоритмів для масиву розміром {size}")
        print("=" * 80)
        
        for array_type, array in test_arrays.items():
            print(f"\nТип масиву: {array_type}")
            print("-" * 50)
            print(f"{'Алгоритм':<20} {'Час (мс)':<15} {'Порівнянь':<15} {'Обмінів':<15}")
            print("-" * 50)
            
            for name, algorithm in algorithms.items():
                start_time = time.time()
                sorted_arr = algorithm(array)
                end_time = time.time()
                elapsed_time = (end_time - start_time) * 1000
                
                print(f"{name:<20} {elapsed_time:<15.2f} {self.sorter.comparisons:<15} {self.sorter.swaps:<15}")
            
            # Перевірка правильності сортування
            assert sorted_arr == sorted(array), f"Помилка в алгоритмі {name}!"


def main():
    """Головна функція для демонстрації"""
    print("АЛГОРИТМИ СОРТУВАННЯ - ДЕМОНСТРАЦІЯ")
    print("=" * 50)
    
    # Створюємо об'єкти
    sorter = SortingAlgorithms()
    visualizer = SortingVisualizer()
    tester = SortingTester()
    
    # Демонстрація візуалізації
    print("\n1. ВІЗУАЛІЗАЦІЯ BUBBLE SORT")
    print("-" * 30)
    demo_array = [5, 2, 8, 1, 9, 3]
    visualizer.visualize_bubble_sort(demo_array)
    
    # Демонстрація роботи алгоритмів
    print("\n2. ДЕМОНСТРАЦІЯ РІЗНИХ АЛГОРИТМІВ")
    print("-" * 30)
    test_array = [64, 34, 25, 12, 22, 11, 90]
    
    print(f"Початковий масив: {test_array}")
    print(f"Bubble Sort: {sorter.bubble_sort(test_array)}")
    print(f"Selection Sort: {sorter.selection_sort(test_array)}")
    print(f"Merge Sort: {sorter.merge_sort(test_array)}")
    
    # Порівняння алгоритмів
    print("\n3. ПОРІВНЯННЯ АЛГОРИТМІВ")
    print("-" * 30)
    tester.compare_algorithms(50)
    
    # Інтерактивний режим
    print("\n4. ІНТЕРАКТИВНИЙ РЕЖИМ")
    print("-" * 30)
    print("Введіть числа через пробіл (або натисніть Enter для випадкового масиву):")
    
    user_input = input().strip()
    if user_input:
        try:
            user_array = list(map(int, user_input.split()))
        except ValueError:
            print("Неправильний формат. Використовую випадковий масив.")
            user_array = [random.randint(1, 20) for _ in range(6)]
    else:
        user_array = [random.randint(1, 20) for _ in range(6)]
    
    print(f"\nВаш масив: {user_array}")
    print("\nОберіть алгоритм:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Merge Sort")
    
    choice = input("Ваш вибір (1-3): ").strip()
    
    if choice == "1":
        result = sorter.bubble_sort_optimized(user_array)
        print(f"Результат Bubble Sort: {result}")
    elif choice == "2":
        result = sorter.selection_sort(user_array)
        print(f"Результат Selection Sort: {result}")
    elif choice == "3":
        result = sorter.merge_sort(user_array)
        print(f"Результат Merge Sort: {result}")
    else:
        print("Неправильний вибір")
    
    print(f"\nПорівнянь: {sorter.comparisons}")
    print(f"Обмінів: {sorter.swaps}")


if __name__ == "__main__":
    main()