'''try:
    file = open("user_input.txt", 'r', encoding='utf8')
except FileNotFoundError:
    print(f"простите но файл ненайден")
else:
    contents = file.read()
    print(contents)'''



'''file = open('example.txt', 'w')
file.write('Python rules!')
file.close()'''


'''def write_to_file():
    user_text = input("Введите текст для записи в файл: ")
    with open("user_input.txt", "w", encoding='utf8') as file:
        file.write(user_text)
    print("Текст записан в файл user_input.txt.")


def append_to_file():
    user_text = input("Введите текст для добавления в файл: ")
    with open("user_input.txt", "a") as file:
        file.write(user_text + "n")  # Добавляем новую строку для разделения
    print("Текст добавлен в файл user_input.txt.")


def main():
    while True:
        print("nВыберите действие:")
        print("1. Записать текст в файл")
        print("2. Добавить текст в файл")
        print("3. Выход")

        choice = input("Введите номер действия (1-3): ")

        if choice == "1":
            write_to_file()
        elif choice == "2":
            append_to_file()
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()'''


'''s = open('example.txt', 'w, a, r', encoding='utf8').readline().rstrip()
a = [int(x) for x in open('example.txt')]
for s in open('example.txt')
with open('example.txt', 'w, a, r', encoding='utf8') as file:'''