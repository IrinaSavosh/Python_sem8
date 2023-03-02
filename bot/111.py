# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import json

phonebook = []
# по умолчанию
def load():
   global phonebook
   with open("C:/Users/HP/Documents/Учеба/Программирование Python/seminar 8/bot/phonebook.json","r",encoding="utf-8") as fb: 
      phonebook = json.load(fb)
   print("Телефонный справочник загружен из файла")
# 2
def save():   
   with open("C:/Users/HP/Documents/Учеба/Программирование Python/seminar 8/bot/phonebook.json","w",encoding="utf-8") as fb:
        fb.write(json.dumps(phonebook, ensure_ascii=False))
        print("Справочник сохранен")
# 4
def del_null ():
   k = -1
   for i in range(len(phonebook)):
      count = 0
      for value in phonebook[i].values():
         if value == "-":
            count +=1
      if count == 5:
         k+=1
   if k>=0:
      phonebook.pop(k)
      print("Готово!") 

def red():
   data = input('''
   Введите полностью фамилию, имя или телефон контакта, который необходимо отредактировать: ''')
   for i in range(len(phonebook)):
      for k, v in phonebook[i].items():
         if v == data:
            phonebook[i][k] = input(str('''
   Введите новые данные или поставьте "-", если хотите зачистить данные: '''))
   print(f'"Контакт с данными {data} отредактирован"')
#5,1
def all_del():
   count = -1
   data = input('''
   Введите полностью фамилию, имя или телефон контакта, который необходимо удалить: ''')
   for i in range(len(phonebook)):
      for value in phonebook[i].values():
         if value == data:
            count = i
   if count >=0:
      phonebook.pop(count)
   print(f'"Контакт с данными {data} удален"')
#5
def delite():
   option = input('''
   Вы хотите:
   1. удалить контакт полностью.
   2. редактировать информацию частично.\n''')
   if option == "1":
      all_del()
   if option == "2":
      red()
# 3
def add():
   print('''
   Для того, чтобы добавить контакт в телефонную книгу следуйте инструкциям ниже.
   Ecли какой-то параметр остутствует, введите -\n''')
   lastname = input("Введите фамилию: ")
   firstname = input("Введите имя: ")
   middlename = input("Введите отчество: ")
   number = input("Введите мобильный телефон: ")
   mail = input("Введите электронную почту: ")
   phonebook.append({
   "Фамилия:": f"{lastname}",
   "Имя:": f"{firstname}",
   "Отчество:": f"{middlename}",
   "Телефон:": f"{number}",
   "Эл.почта:": f"{mail}"
   })
   print("Абонент успешно добавлен в телефонный справочник!\n")
# 1
def show_phonebook():
   if phonebook == []:
         print("Справочник пуст")
   else:
      for i in phonebook:
         print()
         for k, v in i.items():
           print(k, v)
         print("_______________")

print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Сохранить справочник\n"
          "3. Добавить абонента в справочник\n"
          "4. Убрать пустые контакты\n"
          "5. Удаление/редактирование контакта\n"
          "0. Закончить работу\n"
      "Рекомендуем сначала загрузить справочник из файла командой '8' ")

while True:
   comand = input("Введите комманду: ")
   if comand == "1":
      show_phonebook()
   elif comand == "8":
      load()
   elif comand == "2":
      save()
   elif comand == "3":
      add()
   elif comand == "4":
      del_null()
   elif comand == "5":
      delite()
   elif comand == "0":
      save()
      print("Телефонный справочник сохранен. Всего хорошего!")
      break

# print(phonebook[0])