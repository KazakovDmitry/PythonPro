import pytest
import csv
from hw_Student_parser import Student, CsvData, FullName


# Тестирование класса FullName

@pytest.fixture
def full_name_instance():
    return FullName()


def test_set_invalid_full_name():
    full_name = FullName()
    instance = {}
    value = '123 Иван'
    with pytest.raises(ValueError):
        full_name.__set__(instance, value)


# Тестирование класса CsvData
def test_csv_data_valid():
    csv_data = CsvData()
    csv_data.__set_name__(csv_data, 'grades.csv')
    csv_data.__set__(csv_data, 'grades.csv')
    assert csv_data.__get__(csv_data, CsvData) == {'Subject1': ([], []), 'Subject2': ([], [])}


def test_csv_data_invalid():
    csv_data = CsvData()
    with pytest.raises(ValueError):
        csv_data.__set__(csv_data, 'not_a_csv_file.txt')


# Тестирование класса Student
def test_student_average_grade():
    student = Student('Dima Kazakov', 'subjects.csv')
    student.add_grade('Математика', 4)
    student.add_grade('Физика', 5)
    assert student.get_average_grade() == 4.5


def test_student_average_test_score():
    student = Student('Dima Kazakov', 'subjects.csv')
    student.add_test_score('Математика', 80)
    student.add_test_score('Математика', 90)
    assert student.get_average_test_score('Математика') == 85


if __name__ == 'main':
    pytest.main()
