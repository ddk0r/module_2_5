def get_matrix(n, m, value):
    matrix = [] # пустой список

    for i in range(n): # первый внешний цикл для кол-ва строк
        row = [] # пустой список
        for j in range(m): # внешний список для столбцов
            row.append(value) # добавили значение value в строку
        matrix.append(row) # добавляем строку в матрицу

    return matrix # возвратили полученную матрицу

# Пример результата выполнения функции get_matrix:
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)