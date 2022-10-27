def move_docs(folders, doc_number, new_shelf, old_shelf):
    doc_index = folders[old_shelf].index(doc_number)
    val = folders[old_shelf].pop(doc_index)
    folders[new_shelf].append(val)

    print('Теперь репозиторий с полками выглядит так:')
    for catalog in folders:
        print(catalog + " : ", folders.get(catalog))


def print_docs_and_folders(docs, folders):
    print('Текущий каталог выглядит так:')

    for catalog in docs:
        print(catalog)

    print('Текущий репозиторий с полками выглядит так:')

    for catalog in folders:
        print(catalog + " : ", folders.get(catalog))


def del_docs(docs, folders, doc_number):
    for catalog in docs:
        if doc_number in catalog.values():
            catalog["type"] = 'No data'
            catalog["number"] = 'No data'
            print('Данный номер документа удален из каталога.')
            break
    else:
        return 'Данного номера документа нет в каталоге.'

    for shelf in folders.values():
        if doc_number in shelf:
            result = shelf.pop(shelf.index(doc_number))
            print('Данный номер документа удален из репозитория.')
            break
    else:
        return 'Данного номера документа нет в репозитории.'

    print_docs_and_folders(docs, folders)
    return tuple(catalog.values()), result


def add_docs(docs, folders, type_, number, person, shelf):
    docs.append({})
    docs[-1]["type"] = type_
    docs[-1]["number"] = number
    docs[-1]["name"] = person

    while shelf not in folders.keys():
        print('Существующие полки:', *folders)
        shelf = input('Такой полки не существует. Пожалуйста, введите существующую полку: ')
    folders[shelf].append(number)

    print_docs_and_folders(docs, folders)
    return tuple(docs[-1].values()), folders[shelf][-1]


def print_docs(docs):
    res = []
    for catalog in docs:
        res.append(tuple(catalog.values()))
    return res


def get_shelf(docs, doc_number):
    for k, val in docs.items():
        if doc_number in val:
            return 'Документ под номером ' + doc_number + ' находится на ' + k + '-й' + ' полке'
    else:
        return "Такого документа не существует. Проверьте правильность ввода."


def get_person(docs, doc_number):
    for catalog in docs:
        for val in catalog.values():
            if doc_number == val:
                return "Владелец документа № " + doc_number + ": " + catalog['name']
    else:
        return "Такого документа не существует. Проверьте правильность ввода."


def catalog(docs, folders):
    print('!!!Работа с каталогом!!!', 'Для завершения работы нажмите Enter',
          'Для вызова информационной справки введите команду "i"', sep='\n')

    user_choice = None
    while user_choice != '':
        user_choice = input('Введите Вашу команду: ')

        if user_choice == 'p':
            user_choice = input('Уточните номер документа: ')
            print(get_person(docs, user_choice))

        elif user_choice == 's':
            user_choice = input('Уточните номер документа: ')
            print(get_shelf(folders, user_choice))

        elif user_choice == 'i':
            print("""
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
    d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. 
                """)

        elif user_choice == 'l':
            print_docs(docs)

        elif user_choice == 'a':
            doc_type = input('Введите наименование документа: ')
            doc_number = input('Введите номер документа: ')
            owner = input('Введите имя и фамилию владельца документа: ')
            shelf_number = input('Введите номер полки, в которой документ будет храниться: ')
            add_docs(docs, folders, doc_type, doc_number, owner, shelf_number)

        elif user_choice == 'd':
            user_choice = input('Введите номер документа, который требуется удалить: ')
            del_docs(docs, folders, user_choice)

        elif user_choice == 'm':
            flag = True
            while flag:
                doc_number = input('Введите существующий номер документа: ')
                shelf_number = input('Выберите существующую полку:')
                if shelf_number in folders:
                    for key, shelf in folders.items():
                        if doc_number in folders[key]:
                            flag = False
                            prev_shelf_number = key
                            break
                    else:
                        print('Введенного номера документа не существует.')
                else:
                    print('Введена несуществующая полка')

            move_docs(folders, doc_number, shelf_number, prev_shelf_number)

        elif user_choice == '':
            print('Спасибо за использование программы')
            print('Конечный вид каталога и репозитория:')
            print_docs_and_folders(docs, folders)

        elif user_choice == 'as':
            user_choice = list(folders.keys())[0]
            while user_choice in folders:
                user_choice = input('Введите наименование новой полки: ')
            folders[user_choice] = []
            print('Теперь репозиторий с полками выглядит так:')
            for catalog in folders:
                print(catalog + " : ", folders.get(catalog))



        else:
            print('Введен неверный ввод. Повторите попытку.')


documents = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
             {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
             {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
             ]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}
if __name__ == '__main__':
    print_docs_and_folders(documents, directories)
    catalog(documents, directories)
