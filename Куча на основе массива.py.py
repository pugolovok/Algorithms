# Реализация кучи на основе массива.
# Позиции дочерних элементов дерева для элемента a[i] определяются в виде a[2i+1] для
# нечётного дочернего элемента и a[2i+2] для чётного

# Программа считывает данные в массив input_array.
# Проходя поэлементно указанный массив, программа добавляет элемент в кучу, если
# элементом является число, и удаляет из кучи текущий максимальный элемент, записывая
# его в выходной файл, если элементом массива является слово "GET".
# Добавление элемента в кучу выполняется с помощью функции insert(), которая добавляет
# элемент в конец массива, после чего вызывает функцию корректировки расположения элементов.
# Функция max_up() при необходимости корректирует расположение элементов при добавлении и
# удалении элемента.
# Т.к. позиции дочерних элементов элемента a[i] определяются в виде a[2i+1] для нечётного
# дочернего элемента и a[2i+2] для чётного, то определение позиции родительского элемента
# также должно выполняться по-разному. Для этого в функции max_up() сначала определяется
# чётность/нечётность рассматриваемого элемента, а потом выполняется его сравнение
# с предком в дереве для определения необходимости корректировки.
# Функция del_max() удаляет текущий максимальный элемент, после чего пересобирает кучу,
# добавляя в неё все оставшиеся элементы и при добавлении очередного элемента вызывая
# функцию max_up() для проверки необходимости корректировки.
# Удалённые элементы собираются в массив, который сравнивается с массивом правильного ответа.
# Если проверка показала, что удалены верные элементы, то они вносятся в создаваемый
# выходной файл result.txt.


input_array = []  # массив для входных данных из файла
my_answer_array = []  # массив для результата работы программы
correct_answer_array = []  # массив для правильного ответа из файла
quantity_answer_numbers = 0  # переменная количества элементов в правильном ответе

heap_array = []  # массив для хранения элементов кучи

with open("test_in.txt", mode="r", encoding="utf8") as file_in:  # чтение входных данных
    N_input = int(file_in.readline())
    for i in range(0, N_input):
        input_array.append(file_in.readline().rstrip())
file_in.close()


def insert(value):  # функция добавления элемента в кучу
    global heap_array
    heap_array.append(value)
    heap_array = max_up(heap_array)


def del_max():  # функция удаления текущего максимального элемента
    global heap_array
    my_answer_array.append(int(heap_array[0]))
    twin_heap_array = heap_array
    tmp_array = []

    for i in range(1, len(twin_heap_array)):
        tmp_array.append(twin_heap_array[i])
        tmp_array = max_up(tmp_array)

    heap_array = tmp_array


def max_up(arg_array):  # функция корректировки кучи при добавлении и удалении элемента
    position = len(arg_array) - 1

    while (position // 2) > 0:
        if (position % 2 == 0):  # обработка элемента на чётной позиции
            if (arg_array[position] > arg_array[(position - 1) // 2]):
                tmp = arg_array[position]
                arg_array[position] = arg_array[(position - 1) // 2]
                arg_array[(position - 1) // 2] = tmp
            position = (position - 1) // 2
        else:  # обработка элемента на нечётной позиции
            if (arg_array[position] > arg_array[position // 2]):
                tmp = arg_array[position]
                arg_array[position] = arg_array[position // 2]
                arg_array[position // 2] = tmp
            position = position // 2

    if (len(arg_array) > 1):
        if (arg_array[0] < arg_array[1]):
            tmp = arg_array[0]
            arg_array[0] = arg_array[1]
            arg_array[1] = tmp

    return(arg_array)


for i in range(0, len(input_array)):  # цикл обработки входных данных
    if (input_array[i].isdigit()):
        insert(input_array[i])
    else:
        quantity_answer_numbers = quantity_answer_numbers + 1
        del_max()


print("My output:")
print(my_answer_array)
print()

with open("test_out.txt", mode="r", encoding="utf8") as file_out:
    for i in range(0, quantity_answer_numbers):
        correct_answer_array.append(int(file_out.readline()))
file_out.close()

print("Correct answer:")
print(correct_answer_array)
print()

print("Are they equal?")
print(my_answer_array == correct_answer_array)

if (my_answer_array == correct_answer_array):
    output_file = open("result.txt", "w+")
    for i in range(0, len(my_answer_array)):
        output_file.write(str(my_answer_array[i]) + '\n')
    output_file.close()

