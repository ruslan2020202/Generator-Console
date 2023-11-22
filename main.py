import random
import time
import os
import tqdm
import prettytable
from colorama import Fore
import pyfiglet
from pathlib import Path


def empty_file(filename):  # проверка пуст ли файл.txt
    file_info = os.stat(filename)
    return file_info.st_size == 0


def create_file(file):  # создает файл если не найден в директории
    fle = Path(file)
    fle.touch(exist_ok=True)


class PasswordGenerator:  # Генератор паролей
    def __init__(self):
        self.alphabet = [chr(i) for i in range(97, 123)]
        self.saved_passwords = []  # Сохраненные пароли
        self.dataCreationTime = []  # Список для сохранения дат создания паролей
        self.commands()

    def commands(self):  # функция команд
        while True:
            self.cmd = input(Fore.BLUE +
                             '\nВыберите № команды для продолжения:\n\t1.Сгенерировать рандомный пароль\n\t2.Показать сохраненные пароли\n\t3.Выход в меню\n>>')
            if self.cmd.strip() == '1':
                self.attribute()
            elif self.cmd.strip() == '2':
                self.saved_passwd()
            elif self.cmd.strip() == '3':
                Generator()
            else:
                print(Fore.RED + f'Ошибка\nКоманды {self.cmd} не существует\nПопробуйте еще раз')
                continue

    def attribute(self):  # функция подбора количества символов в пароле
        while True:
            self.length = input(Fore.BLUE + '\nВведите кол-во символов в пароле(6-12):')
            if self.length.strip().isdigit():
                if 5 < int(self.length) < 13:
                    break
                else:
                    print(
                        Fore.RED + 'Ошибка!\nПароль должен быть не больше 12  и не меньше 6 символов \nПопробуйте заново')
            else:
                print(
                    'Ошибка!\nДля определения размера сгенерированного пароля используйте только цифры\nПопробуйте заново')
        self.passwd_gen()

    def passwd_gen(self):  # функция генерирования пароля
        self.gen = []
        for i in range(0, int(self.length)):
            self.random_lettter = random.choice(self.alphabet)
            self.random_num = random.randint(0, 9)
            x = random.randint(0, 4)
            if x == 0 or x == 1:
                self.gen.append(str(self.random_num))
            elif x == 2 or x == 3:
                self.gen.append(self.random_lettter)
            else:
                self.gen.append(self.random_lettter.upper())
        self.passwd = ''.join(self.gen)
        print(Fore.BLUE + '\nПодождите, ваш пароль генерируется...')
        for i in tqdm.tqdm(range(1, 101)):
            if 6 <= int(self.length) < 8:
                time.sleep(0.05)
            elif 8 <= int(self.length) < 10:
                time.sleep(0.1)
            else:
                time.sleep(0.2)
        print(Fore.BLUE + f'Ваш пароль успешно сгенерирован\nСгенерированный пароль:{self.passwd}')
        savepsswd = input(Fore.BLUE + 'Хотите сохранить пароль(да/нет):')
        while True:
            if savepsswd.strip() == 'да':
                print(Fore.GREEN + 'Пароль успешно сохранен!')
                self.data_create = time.asctime()  # Сохранение времени создания пароля
                self.dataCreationTime.append(self.data_create)
                self.saved_passwords.append(self.passwd)
                f = open('generated saved passwords.txt', 'a')
                data_passwd = self.saved_passwords.index(self.passwd)
                with open('generated saved passwords.txt', 'r') as file:
                    old_password = file.readlines()
                f.write(
                    f'{len(old_password) + 1}. {self.saved_passwords[data_passwd]} . (Дата создания : {self.dataCreationTime[data_passwd]})\n')
                f.close()
                self.commands()
            elif savepsswd.strip() == 'нет':
                print(Fore.YELLOW + 'Пароль не был сохранен')
                self.commands()
            else:
                print(Fore.RED + 'Ошибка\nДля продолжения используйте только да/нет\nПопробуйте заново')
                savepsswd = input(Fore.BLUE + 'Хотите сохранить пароль(да/нет):')

    def saved_passwd(self):  # сохраненные пароли
        print(Fore.BLUE + 'Ваши сохраненные пароли:\n')
        f = open(
            'generated saved passwords.txt',
            'r')
        file_name = 'generated saved passwords.txt'
        if empty_file(file_name):
            print(Fore.YELLOW +
                  'Password not found!\nДля создания новых паролей используйте команду "1.Сгенерировать рандомный пароль"')
        else:
            table = prettytable.PrettyTable()
            table.field_names = ['№', 'Password', "Data of creation"]
            for i in f:
                x = i.split('.')
                x = list([j.strip() for j in x])
                table.add_row(x)
            print(table)
        f.close()
        self.commands()


class KeyGenerator:  # Генератор ключей
    def __init__(self):
        self.alphabet = [chr(i) for i in range(97, 123)]
        self.key_windows = []
        self.keys_photoshop = []
        self.M_W = 'Microsoft Windows'
        self.A_P = 'Adobe Photoshop'
        self.commands()

    def commands(self):
        while True:
            self.cmd = input(Fore.MAGENTA +
                             '\nВыберите № команды для продолжения:\n\t1.Сгенерировать лицензионные ключи\n\t2.Показать сохранные ключи\n\t3.Выход в главное меню\n>>')
            if self.cmd.strip() == '1':
                self.selection()
            elif self.cmd.strip() == '2':
                self.saved_key()
            elif self.cmd.strip() == '3':
                Generator()
            else:
                print(Fore.RED + f'Ошибка\nКоманды {self.cmd} не существует\nПопробуйте еще раз')
                continue

    def selection(self):
        while True:
            self.choice_key = input(Fore.MAGENTA +
                                    f'\nВыберите № ключа которого вы хотели бы сгенерировать(для выхода в меню введите exit):\n\t1.{self.M_W}\n\t2.{self.A_P}\n>>')
            match self.choice_key.strip().lower():
                case '1':
                    self.keygen_windows()
                case '2':
                    self.keygen_photoshop()
                case 'exit':
                    self.commands()
                case _:
                    print(Fore.RED + f'Ошибка\nКоманды {self.choice_key} не существует\nПопробуйте еще раз')
                    continue

    def keygen_windows(self):  # Генерация ключей windows
        self.key_windows.clear()
        for i in range(5):
            self.key_assembly_completely = []  # Готовая сборка одного пароля
            self.key_assembly_parts = []  # Сборка по частям
            for j in range(5):
                for k in range(5):
                    self.random_letter = random.choice(self.alphabet)
                    self.random_num = random.randint(0, 9)
                    x = random.randint(1, 2)
                    match x:
                        case 1:
                            self.key_assembly_parts.append(self.random_letter.upper())
                        case 2:
                            self.key_assembly_parts.append(str(self.random_num))
                self.key_assembly_completely.append(''.join(self.key_assembly_parts) + '-')
                self.key_assembly_parts = []
            self.key_windows.append((''.join(self.key_assembly_completely))[0:-1])
        print(Fore.MAGENTA + '\nПодождите, лицензионные ключи генерируются...')
        for i in tqdm.tqdm(range(1, 101)):
            time.sleep(0.1)
        print(Fore.GREEN + 'Ключи активации успешно сгенерированы')
        save_key = input(Fore.MAGENTA + 'Хотите сохранить сгенерированные ключи(да/нет):')
        while True:
            if save_key.strip().lower() == 'да':
                print(Fore.GREEN + 'Сгенерированные ключи успешно сохранены!')
                with open('saved activion keys windows.txt', 'r') as file:
                    strings = file.readlines()
                n = len(strings)
                f = open('saved activion keys windows.txt', 'a')
                if empty_file('saved activion keys windows.txt'):
                    f.write(Fore.MAGENTA + f'Ключи активации {self.M_W}:\n')
                    n += 1
                for i in self.key_windows:
                    f.write(f'{n}. {i}\n')
                    n += 1
                f.close()
                self.commands()
            elif save_key.strip().lower() == 'нет':
                print(Fore.YELLOW + 'Лицензионные ключи не были сохранены')
                self.commands()
            else:
                print(Fore.RED + 'Ошибка\nДля продолжения используйте только да/нет\nПопробуйте заново')
                save_key = input(Fore.MAGENTA + 'Хотите сохранить сгенерированные ключи(да/нет):')
                continue
        self.commands()

    def keygen_photoshop(self):  # Генерация ключей photoshop
        self.keys_photoshop.clear()
        for i in range(5):
            self.key_assembly_photoshop_completely = []  # Готовая сборка одного пароля
            self.key_assembly_photoshop_parts = []  # Сборка по частям
            for j in range(6):
                for k in range(4):
                    self.random_num = random.randint(0, 9)
                    self.key_assembly_photoshop_parts.append(str(self.random_num))
                self.key_assembly_photoshop_completely.append(''.join(self.key_assembly_photoshop_parts) + '-')
                self.key_assembly_photoshop_parts = []
            self.keys_photoshop.append((''.join(self.key_assembly_photoshop_completely))[0:-1])
        print(Fore.MAGENTA + '\nПодождите, лицензионные ключи генерируются...')
        for i in tqdm.tqdm(range(1, 101)):
            time.sleep(0.1)
        print(Fore.GREEN + 'Ключи активации успешно сгенерированы')
        save_key = input(Fore.MAGENTA + 'Хотите сохранить сгенерированные ключи(да/нет):')
        while True:
            if save_key.strip().lower() == 'да':
                print(Fore.GREEN + 'Ключи активации успешно сохранены!')
                with open('saved_keys_photoshop.txt', 'r') as file:
                    strings = file.readlines()
                n = len(strings)
                f = open('saved_keys_photoshop.txt', 'a')
                if empty_file('saved_keys_photoshop.txt'):
                    f.write(Fore.MAGENTA + f'Ключи активации {self.A_P}:\n')
                    n += 1
                for i in self.keys_photoshop:
                    f.write(f'{n}. {i}\n')
                    n += 1
                f.close()
                self.commands()
            elif save_key.strip().lower() == 'нет':
                print(Fore.YELLOW + 'Лицензионные ключи не были сохранены')
                self.commands()
            else:
                print(Fore.RED + 'Ошибка\nДля продолжения используйте только да/нет\nПопробуйте заново')
                save_key = input(Fore.MAGENTA + 'Хотите сохранить сгенерированные ключи(да/нет):')
                continue
        self.commands()

    def saved_key(self):  # Меню показа сохраненных ключей
        while True:
            self.choice_saved_key = input(Fore.MAGENTA +
                                          f'Выберите № ключей для просмотра(для выхода в меню введите "exit"):\n\t1.{self.M_W}\n\t2.{self.A_P}\n>>')
            match self.choice_saved_key.strip().lower():
                case '1':
                    self.saved_keys('saved activion keys windows.txt', self.M_W)
                case '2':
                    self.saved_keys('saved_keys_photoshop.txt', self.A_P)
                case 'exit':
                    self.commands()
                case _:
                    print(Fore.RED + f'Ошибка\nКоманды {self.choice_saved_key} не существует\nПопробуйте еще раз')
                    continue

    def saved_keys(self, file_use, pr):  # Сохраненные ключи
        print(Fore.MAGENTA + f'Ваши лицензионные ключи {pr}:\n')
        f = open(
            file_use,
            'r')
        if empty_file(file_use):
            print(Fore.YELLOW +
                  'Activioin keys not found!\nДля создания новых лицензионных ключей используйте команду "1.Сгенерировать лицензионные ключи"')
        else:
            table = prettytable.PrettyTable()
            table.field_names = ['№', 'Activion keys']
            for i in f:
                if not 'Ключи' in i:
                    x = i.split('.')
                    x = list([j.strip() for j in x])
                    table.add_row(x)
            print(table)
        f.close()
        self.commands()


class BruteForce:  # Создание brute force словарей
    def __init__(self):
        self.user_inf = []  # Информация об жертве
        self.menu_brut()

    def menu_brut(self):
        self.brut_passwords = []
        while True:
            self.cmd = input(Fore.CYAN +
                             '\nВыберите № команды для продолжения:\n\t1.Создание нового словаря Brute Force\n\t2.Показать сохранные словари\n\t3.Выход в главное меню\n>>')
            if self.cmd.strip() == '1':
                self.collection_inf_us()
            elif self.cmd.strip() == '2':
                self.saved_dict()
            elif self.cmd.strip() == '3':
                Generator()
            else:
                print(Fore.RED + f'Ошибка\nКоманды {self.cmd} не существует\nПопробуйте еще раз')
                continue

    def collection_inf_us(self):  # Сбор информации
        print(Fore.CYAN + '\nДля создания нового словаря введите некоторые данные об жертве:\n')

        def check_for_data_str(variable):
            while True:
                text = input(Fore.CYAN + f'{variable}:\n>>')
                if not text.strip().isalpha() or len(text.strip()) == 0:
                    print(Fore.YELLOW +
                          f'{variable} должно состоять из букв алфавита и иметь хотя бы один символ\nПопробуйте еще раз')
                elif len(text.strip()) > 50:
                    print(Fore.YELLOW + f'{variable} не должно быть более 50 символов\nПопробуйте еще раз')
                elif text.strip().lower() == 'Словарь':
                    print(Fore.RED + 'Error')
                    print(Fore.YELLOW + 'Не подходящее слово\nПопробуйте еще раз')
                else:
                    def app(list):
                        list.append(text.lower())
                        list.append(text.title())
                        list.append(text.upper())

                    app(self.user_inf)
                    app(self.brut_passwords)
                    break

        def check_for_data_int(variable):
            while True:
                text = input(Fore.CYAN + f'{variable}(dd/mm/yyyy):\n>>')
                d = text[0:2].strip()
                m = text[3:5].strip()
                y = text[6:].strip()
                dr = d + m + y
                if not d.isnumeric() or not m.isnumeric() or not y.isnumeric() or len(
                        text.strip()) > 10:
                    print(Fore.YELLOW + f'{variable} должен состоять из цифр\nПопробуйте заново')
                elif len(text.strip()[0:2]) != 2 or text.strip()[2:6:3] != '//' or len(
                        text.strip()[3:5]) != 2 or len(text.strip()[6:]) != 4:
                    print(Fore.YELLOW + f'{variable} должно формата "dd/mm/yyyy" \nПопробуйте заново')
                else:
                    self.user_inf.append(d)
                    self.user_inf.append(m)
                    self.user_inf.append(y)
                    self.user_inf.append(dr)
                    self.brut_passwords.append(dr)
                    break

        check_for_data_str('Имя')
        check_for_data_str('Фамилия')
        check_for_data_int('Дата рождения')
        check_for_data_str('Увлечение')

        self.create_brute_force()

    def create_brute_force(self):
        self.assembly_password = []
        while len(self.brut_passwords) != 465:
            for i in range(3):
                self.random_word = random.choice(self.user_inf)
                self.assembly_password.append(self.random_word)
            self.brute_password = ''.join(self.assembly_password)
            if self.brute_password not in self.brut_passwords:
                self.brut_passwords.append(self.brute_password)
            self.assembly_password.clear()
        print(Fore.CYAN + '\nПодождите, словарь создается...')
        for i in tqdm.tqdm(range(1, 101)):
            time.sleep(0.1)
        print(Fore.GREEN + 'Словарь успешно сгенерирован')
        while True:
            save_dict = input(Fore.CYAN + 'Хотите сохранить новый словарь(да/нет):')
            if save_dict.strip().lower() == 'да':
                while True:
                    name_dict = input(Fore.CYAN + 'Введите имя для создание словаря:\n>>')
                    if not name_dict.strip().isalnum():
                        print(Fore.YELLOW + 'Название должно состоять только и букв и цифры\nПопробуйте заново')
                    elif len(name_dict.strip()) == 0 or len(name_dict.strip()) > 30:
                        print(
                            'Длина названия не должна быть равна нулю и не должна превышать 30 символов\nПопробуйте заново')
                    else:
                        with open('brute_forse_dict.txt', 'r') as file1:
                            x = file1.readlines()
                            x = [i.strip() for i in x]
                        file2 = open('brute_forse_dict.txt', 'a')
                        if not f'Словарь {name_dict.strip()}:' in x:
                            if empty_file('brute_forse_dict.txt'):
                                file2.write(f'Словарь {name_dict}:\n')
                            else:
                                file2.write(f'\nСловарь {name_dict}:\n')
                            for j in self.brut_passwords:
                                file2.write(f'\n{j}')
                            print(Fore.GREEN + f'Словарь "{name_dict}" успешно сохранен!')
                            file2.close()
                            self.menu_brut()
                        else:
                            print(Fore.YELLOW + f'Словарь с именем {name_dict} уже существует\nПопробуйте заново')
            elif save_dict.strip().lower() == 'нет':
                print(Fore.YELLOW + 'Словарь не были сохранен')
                self.menu_brut()
            else:
                print(Fore.RED + 'Ошибка\nДля продолжения используйте только да/нет\nПопробуйте заново')

    def saved_dict(self):  # Выбор словаря и показ в нем сохранненых паролей
        dict_list = []
        file = open('brute_forse_dict.txt', 'r')
        if empty_file('brute_forse_dict.txt'):
            print(
                Fore.YELLOW + 'Сохраненные словари отсутствуют\nДля создания словаря используйте функцию "1.Создание нового словаря Brute Force"')
            self.menu_brut()
        else:
            x = file.readlines()
            x = [i.strip() for i in x]
            count = 1
            for i in x:
                if 'Словарь' in i:
                    i = f'{count}. {i.strip()[0:-1]}'
                    dict_list.append(i)
                    count += 1
            n = len(dict_list)
            while True:
                print(Fore.CYAN + 'Выберите словарь для продолжения:(выход в меню-exit)', *dict_list)
                choice_savedDict = input('>>')
                if choice_savedDict.strip().lower() == 'exit':
                    self.menu_brut()
                elif not choice_savedDict.strip().isdigit() or int(choice_savedDict) > n:
                    print(Fore.YELLOW + 'Такого словаря не существует\nПопробуйте еще раз')
                else:
                    for i in x:
                        if i == f'{(dict_list[int(choice_savedDict) - 1])[3:]}:':
                            val = x.index(i)
                            select_dict = x[val:val + 465]
                            for j in select_dict:
                                print(j)
                    break
            file.close()
            self.menu_brut()


class Generator:  # Главное меню
    def __init__(self):
        create_file('generated saved passwords.txt')
        create_file('saved_keys_photoshop.txt')
        create_file('saved activion keys windows.txt')
        create_file('brute_forse_dict.txt')
        self.menu()

    def menu(self):
        while True:
            preview_text = pyfiglet.Figlet(font='slant')
            print(preview_text.renderText('GENERATOR by Faer'))
            print(Fore.MAGENTA + '   ==============\n        Меню\n   ==============')
            self.menu_choice = input(
                Fore.MAGENTA + '1.Генератор паролей\n2.Генератор ключей\n3.Создание Brute Force словарей\n4.Выйти\n>>')
            match self.menu_choice.strip().lower():
                case '1':
                    PasswordGenerator()
                case '2':
                    KeyGenerator()
                case '3':
                    BruteForce()
                case '4':
                    exit()
                case _:
                    print(Fore.RED + f'Ошибка\nКоманды {self.menu_choice} не существует\nПопробуйте еще раз')
                    continue


if __name__ == '__main__':
    Generator()
