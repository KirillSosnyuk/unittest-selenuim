import unittest
from parameterized import parameterized
from task_1 import documents, directories, print_docs, add_docs, del_docs


class TestFunctions(unittest.TestCase):

    def test_print_docs(self):
        result = print_docs(documents)
        etalon = [tuple(person.values()) for person in documents]
        self.assertEqual(result, etalon)

    @parameterized.expand(
        [
            ("passport", '5243 480071', 'Валерий Смородинов', '2'),
            ('snils', '237643276 80', 'Денис Козловский', '1'),
            ('insurance', '997 65 43 234', 'Алена Смертина', '3')
        ]
    )
    def test_add_docs(self, type_, number, person, shelf):
        result = add_docs(documents, directories, type_, number, person, shelf)
        etalon = ((type_, number, person), number)
        self.assertEqual(result, etalon)

    @parameterized.expand(
        [
            ('2207 876234', ('No data', 'No data', "Василий Гупкин")),
            ('11-2', ('No data', 'No data', "Геннадий Покемонов")),
            ('10006', ('No data', 'No data', "Аристарх Павлов"))
        ]
    )
    def test_del_docs(self, doc_number, etalon_tuple):
        result = del_docs(documents, directories, doc_number)
        etalon = (etalon_tuple, doc_number)
        self.assertEqual(result, etalon)
