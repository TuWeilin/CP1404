name_file = open('name.txt', 'w+')
name = str(input("Enter your name:"))
print(name, file=name_file)
print("Your name is Bob")
line = name_file.read(2)
print(line)
name_file.close()

number_file = open('numbers.txt', 'r')
number1 = number_file.readline(2)
number_file.readline(2)
number2 = number_file.readline(2)
number1 = int(number1, 10)
number2 = int(number2, 10)
i = number1 + number2
print(i)
number_file.close()
number_file = open('numbers.txt', 'r')
total_number = number_file.read()
print(total_number)

