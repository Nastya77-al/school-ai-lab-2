# 🎓 Алгоритми сортування - Навчальний курс

Інтерактивний навчальний курс з алгоритмів сортування для учнів 10 класу.

## 📋 Зміст

- [Опис проекту](#опис-проекту)
- [Функціональність](#функціональність)
- [Структура проекту](#структура-проекту)
- [Встановлення та запуск](#встановлення-та-запуск)
- [Використання](#використання)
- [Алгоритми](#алгоритми)
- [AI-асистенти](#AI-асистенти)
- [Технології](#технології)

## 📝 Опис проекту

Цей проект створений для навчання учнів основам алгоритмів сортування. Включає інтерактивні візуалізації, детальну теорію, практичні завдання та тести.

### Основні можливості:
- 🎨 **Візуалізація** - анімована демонстрація роботи алгоритмів
- 📚 **Теорія** - детальне пояснення кожного алгоритму
- 💻 **Практика** - інтерактивні завдання та тренажери
- 📊 **Аналіз** - порівняння складності алгоритмів
- 🎯 **Тести** - перевірка знань

## 🚀 Функціональність

### Інтерактивний сайт (index.html)
- Візуалізація алгоритмів з налаштуванням швидкості
- Генерація різних типів масивів
- Покрокове виконання з підрахунком операцій
- Інтерактивні тренажери
- Вбудовані тести та завдання

### Теоретичні матеріали
- Детальні HTML сторінки для кожного алгоритму
- Покрокові приклади
- Аналіз складності
- Переваги та недоліки

### Python реалізації
- Всі алгоритми в одному файлі
- Візуалізація процесу сортування
- Порівняння продуктивності
- Інтерактивний режим

## 📁 Структура проекту

```
sorting-algorithms-course/
├── index.html                    # Головний інтерактивний сайт
├── README.md                     # Цей файл
│
├── theory/                       # Теоретичні матеріали
│   ├── bubble-sort.html         # Теорія бульбашкового сортування
│   ├── selection-sort.html      # Теорія сортування вибором
│   ├── merge-sort.html          # Теорія сортування злиттям
│   └── complexity.md            # Аналіз складності
│
└── scripts/                     # Програмний код
    └── sorting_algorithms.py    # Python реалізації
```

## 💡 Використання

### Навігація по сайту

1. **Головна** - загальна інформація про курс
2. **Теорія** - базова теорія трьох алгоритмів з посиланнями на детальні матеріали
3. **Візуалізація** - інтерактивна демонстрація роботи алгоритмів
4. **Практика** - завдання та тренажери
5. **Тести** - перевірка знань
6. **Ресурси** - додаткові матеріали та посилання

### Робота з візуалізацією

1. Оберіть розмір масиву повзунком
2. Налаштуйте швидкість анімації
3. Згенеруйте масив (випадковий, зворотній, майже відсортований)
4. Оберіть алгоритм для візуалізації
5. Використовуйте кнопки Пауза/Продовжити для контролю

### Python код

Запустіть `sorting_algorithms.py` для:
- Демонстрації візуалізації в консолі
- Порівняння алгоритмів
- Інтерактивного режиму

## 📚 Алгоритми

### 1. Bubble Sort (Бульбашкове сортування)
- **Складність**: O(n²)
- **Принцип**: порівняння сусідніх елементів
- **Переваги**: простий, стабільний
- **Недоліки**: повільний для великих масивів

### 2. Selection Sort (Сортування вибором)
- **Складність**: O(n²)
- **Принцип**: пошук мінімуму та обмін
- **Переваги**: мінімум обмінів
- **Недоліки**: не адаптивний

### 3. Merge Sort (Сортування злиттям)
- **Складність**: O(n log n)
- **Принцип**: розділяй і володарюй
- **Переваги**: гарантована швидкість
- **Недоліки**: потребує додаткову пам'ять

## 📚 Використані джерела та інструменти

### 🤖 AI-асистенти

- **ChatGPT (від OpenAI)**  
  Використано для:
  - Генерації навчального контенту та описів тем
  - Створення структури курсу та його модулів
  - Редагування та оптимізації коду на Python, JavaScript, HTML/CSS
  - Підготовки тестових завдань та пояснень до них
  - Автоматичного створення презентацій у форматі Markdown або Google Slides (через відповідні шаблони)

- **Claude (від Anthropic)**  
  Використано для:
  - Переформулювання складних тем у зрозумілій формі
  - Генерації варіантів пояснень і прикладів
  - Створення діалогових сценаріїв між викладачем і студентом
  - Підготовки узагальнень, резюме тем та швидкої перевірки граматики

### 🔧 Технології

- **HTML5** – побудова семантичної структури навчального сайту та завдань
- **CSS3** – оформлення інтерфейсу, адаптивна верстка, анімації для інтерактивного навчання
- **JavaScript** – реалізація динамічних компонентів, валідації форм, інтерактивних вправ
- **Python 3** – реалізація алгоритмів, практичні завдання та міні-проєкти, перевірка рішень

---

> AI-асистенти значно пришвидшили створення контенту і виконали значну частину роботи.
