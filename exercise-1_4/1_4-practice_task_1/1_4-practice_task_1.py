numbers = [str(number) + "\n" for number in range(50, 100)]
print(numbers)
with open('exercise-1_4/1_4-practice_task_1/numbers.txt', 'w') as my_file:
    my_file.writelines(numbers)
