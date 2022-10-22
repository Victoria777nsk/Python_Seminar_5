'''
Задача 35. Есть N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие: 
A[i] - 1 == A[i-1]. Найдите это число. Пример: my_str = "1 2 3 5 6" => 4.

'''
# my_str = '1 2 3 5 6'
# my_str = my_str.split()

# new_list = list(map(int, my_str))

# for i in range(len(new_list) - 1):
#     if new_list[i + 1] - new_list[i] > 1:
#         print(new_list[i] + 1)



# print([new_list[i] + 1 for i in range(len(new_list) - 1) if new_list[i + 1] - new_list[i] > 1])



'''
Задача 36. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
Порядок элементов менять нельзя. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7]

'''
# my_list = [1, 5, 2, 3, 4, 6, 1, 7]
# new_list = [my_list[0]]

# for item in my_list:
#     if item > new_list[-1]:
#         new_list.append(item)

# print(new_list)


'''
37 Напишите программу, удаляющую из текста все слова, содержащие "абв".

'''
# my_str = 'Напишабв програбв, абвляющую из теабв все слова, содержащие "абв"'

# filtred_str = ' '.join(filter(lambda item: 'абв' not in item, my_str.split(' ')))
# print(filtred_str)

