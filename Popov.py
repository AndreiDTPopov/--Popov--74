import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из Excel файла
file_path = 'data.xlsx'  # Укажите путь к вашему файлу
data = pd.read_excel(file_path)

# Предполагаем, что в Excel есть столбцы 'X' и 'Y'
a = data['A']
b = data['B']
c = data["C"]
# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Данные из Excel')
plt.title('График данных из Excel')
plt.alabel('A')
plt.blabel('B')
plt.clabel("C")
plt.legend()
plt.grid()
plt.show()