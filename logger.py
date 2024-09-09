from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(f"В каком формате записать данные \n\n"
                    f"1 Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 Вариант: \n"
                    f"{name};{surname};{phone};{address}\n\n"
                    f"Выберите вариант: "))

    while var not in [1, 2]:
        print("Неправильный ввод..")

        var = int(input("Выберите вариант: "))

    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open("data_second_variant.csv", "a", encoding="utf-8") as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open("data_first_variant.csv", "r", encoding="utf-8") as f:
        data_first = f.readlines()
        data_first_list = []

        j = 0
        for i in range(len(data_first)):
            if data_first[i] == "\n" or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i

        print("".join(data_first_list))

    print("Вывожу данные из 2 файла: \n")
    with open("data_second_variant.csv", "r", encoding="utf-8") as f:
        data_second = f.readlines()
        print(*data_second)


def update_data():
    name_or_surname = input("Введите фамилию для изменения данных: ")
    file_choice = int(input("Выберите файл (1 или 2): "))

    if file_choice == 1:
        file_name = "data_first_variant.csv"
    elif file_choice == 2:
        file_name = "data_second_variant.csv"

    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    updated_lines = []
    found = False
    i = 0

    while i < len(lines):
        if lines[i].strip() == "" and (i == 0 or lines[i-1].strip() == ""):
            i += 1
            continue

        if name_or_surname in lines[i] or (i+1 < len(lines) and name_or_surname in lines[i+1]):
            found = True
            if file_choice == 1:
                # Обрабатываем запись в файле 1 (построчное разделение)
                entry = lines[i:i+4]
                print(f"Найдено: {entry}")
                if input("Хотите изменить эту запись? (y/n): ").lower() == 'y':
                    name = input("Новое имя: ")
                    surname = input("Новая фамилия: ")
                    phone = input("Новый телефон: ")
                    address = input("Новый адрес: ")
                    updated_lines.extend([name, surname, phone, address])  # Обновляем запись
                else:
                    updated_lines.extend(entry)
                i += 4
            else:
                # Обрабатываем файл с разделением через точку с запятой (вариант 2)
                entry = lines[i]
                print(f"Найдено: {entry}")
                if input("Хотите изменить эту запись? (y/n): ").lower() == 'y':
                    name = input("Новое имя: ")
                    surname = input("Новая фамилия: ")
                    phone = input("Новый телефон: ")
                    address = input("Новый адрес: ")
                    updated_lines.append(f"{name};{surname};{phone};{address}")
                else:
                    updated_lines.append(entry)
                i += 1
        else:
            updated_lines.append(lines[i])
            i += 1

    # Убираем возможные дубли пустых строк
    cleaned_lines = [line for i, line in enumerate(updated_lines) if line.strip() != "" or (i > 0 and updated_lines[i-1].strip() != "")]

    if found:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(cleaned_lines) + "\n")
        print("Данные обновлены.")
    else:
        print("Запись не найдена.")


def delete_data():
    name_or_surname = input("Введите имя или фамилию для удаления данных: ")
    file_choice = int(input("Выберите файл (1 или 2): "))

    if file_choice == 1:
        file_name = "data_first_variant.csv"
        delimiter = "\n"
    elif file_choice == 2:
        file_name = "data_second_variant.csv"
        delimiter = ";"

    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    updated_lines = []
    found = False
    i = 0
    while i < len(lines):
        if name_or_surname in lines[i]:
            found = True
            print(f"Найдено: {lines[i:i+4] if file_choice == 1 else lines[i]}")
            if input("Вы уверены, что хотите удалить эту запись? (y/n): ").lower() == 'y':
                if file_choice == 1:
                    i += 4
                else:
                    i += 1
            else:
                if file_choice == 1:
                    updated_lines.extend(lines[i:i+4])
                    i += 4
                else:
                    updated_lines.append(lines[i])
        else:
            updated_lines.append(lines[i])
            i += 1

    if found:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(updated_lines) + "\n")
        print("Запись удалена.")
    else:
        print("Запись не найдена.")