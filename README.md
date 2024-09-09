# Справочник-Бот для Управления Данных

Это простой бот на Python для управления данными с помощью командной строки. Справочник позволяет записывать, выводить, изменять и удалять записи данных. Информация сохраняется в формате CSV, с возможностью выбора формата записи.

## Функциональность

- **Запись данных**: Ввод информации о пользователе (имя, фамилия, телефон, адрес) и сохранение её в одном из двух форматов:
  - **Вариант 1**: Каждая информация на новой строке (сохраняется в `data_first_variant.csv`).
  - **Вариант 2**: Все данные в одной строке, разделённые точкой с запятой (сохраняется в `data_second_variant.csv`).
  
- **Вывод данных**: Просмотр записей данных из файла `data_first_variant.csv`.

- **Изменение данных**: Модификация существующих записей (функция в процессе разработки).

- **Удаление данных**: Удаление записей из справочника (функция в процессе разработки).

## Файлы проекта

- **`main.py`**: Основной файл для запуска программы. Запускает интерфейс.
- **`ui.py`**: Обрабатывает ввод команд через интерфейс командной строки. Позволяет выбрать действия: запись, просмотр, изменение или удаление данных.
- **`logger.py`**: Реализует основную функциональность по работе с данными (запись, вывод).
- **`data_create.py`**: Вероятно, используется для генерации данных (имя, фамилия, телефон, адрес).
- **`data_first_variant.csv` и `data_second_variant.csv`**: CSV-файлы, в которых хранятся записи данных в разных форматах.

## Как использовать

1. Клонируйте или загрузите проект.
2. Убедитесь, что Python установлен на вашем компьютере.
3. Запустите бота, выполнив команду:
   ```bash
   python main.py
   ```
4. Следуйте инструкциям для ввода, вывода, изменения или удаления данных.

## Требования

- Python 3.9
- Дополнительные библиотеки не требуются (используются стандартные библиотеки Python).
