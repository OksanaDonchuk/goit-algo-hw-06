# goit-algo-hw-06

**Python. HW 6. Graph**

---

## **Завдання 1**

### Опис:

Створіть граф за допомогою бібліотеки `networkX` для моделювання певної реальної мережі (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).

Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин).

---

## **Завдання 2**

### Опис:

Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.

Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.

### Результати:

Шлях від "Дім" до "Робота" за допомогою DFS:

`['Дім', 'Зупинка автобусу', 'ст.м. Харківська', 'ст.м. Позняки', 'ст.м. Палац спорту', 'Робота']`

Шлях від "Дім" до "Робота" за допомогою BFS:

`['Дім', 'Зупинка трамваю', 'ст.м. Позняки', 'ст.м. Палац спорту', 'Робота']`

У цьому графі BFS дає коротший шлях, ніж DFS

### Основні відмінності DFS та BFS:

1. **Чому DFS вибирає довший шлях:**
   - DFS (глибина першою) досліджує граф, занурюючись у першу можливу гілку до кінця, перш ніж повернутися назад і шукати інший шлях.
   - Оскільки `Зупинка автобусу` – перший сусід Дім у списку вершин, алгоритм DFS спочатку досліджує цей шлях.
   - Він не оцінює відстань і просто рухається далі, поки не знайде `Робота`.
   - В результаті DFS обирає довший шлях через `Зупинка автобусу`, `ст.м. Харківська` та `ст.м. Позняки`, хоча є коротший маршрут.

2. **Чому BFS знаходить оптимальний шлях:**
   - BFS (ширина першою) працює за принципом черги (FIFO) та досліджує всі сусідні вершини на одному рівні перед тим, як перейти до наступного рівня.
   - Це гарантує, що BFS знайде шлях з мінімальною кількістю ребер, якщо всі ребра мають однакову вагу (як у нашому випадку).
   - Таким чином, BFS обирає оптимальний шлях з меншою кількістю переходів.

### Основне застосування:

- **DFS підходить для:**
   - Перевірки, чи існує шлях між двома вершинами.
   - Дослідження глибини дерева (наприклад, обхід HTML DOM).
   - Завдань, де потрібно знайти всі можливі шляхи (наприклад, головоломки або лабіринти).

- **BFS підходить для:**
   - Знаходження найкоротшого шляху у графі без ваг.
   - Завдань, де потрібно знайти найменшу кількість кроків (наприклад, у навігаторах або чат-ботах).
   - Обходу рівнями (наприклад, у соціальних мережах для визначення друзів другого рівня).

## Висновки:

- **DFS** вибирає перший знайдений шлях без оцінки його довжини. Це може призвести до неоптимальних рішень.  
- **BFS** знаходить шлях із найменшою кількістю переходів, що робить його кращим варіантом для пошуку найкоротшого шляху в **незваженому графі**.  
- **Якщо у графі є ваги – обидва алгоритми не гарантують оптимального шляху!**  
  У такому випадку потрібно використовувати **алгоритм Дейкстри** або **A\***.  

---

## **Завдання 3**

### Опис:

Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.
