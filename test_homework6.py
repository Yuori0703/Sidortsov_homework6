# Yuori Sidortsov
# Homework-6
# 31-03-2024
# Grodno-IT-Academy-Python 3.11.5

import pytest
import homework6 as hw

# pytest test_homework6.py
# Создаем класс TestCalculate для тестирования задачи 3.1
class TestCalculate():
# Этот тестовый сценарий pytest проверяет, что тип возвращаемого значения функции calculate_sum(2) соответствует типу числа 2,
# то есть int. Если функция calculate_sum возвращает значение, которое является целым числом, тест будет успешно пройден. 
# Если возвращаемое значение не является целым числом, тест не пройдет.
    def test_calculate_output_type(self):
        assert type(hw.calculate_sum(2)) == type(2)
# Этот тест проверяет, что при переданном определенном значении аргумента в функцию calculate_sum будет получено ожидаемое значение  
    def test_calculate_values(self):
        all_sum = hw.calculate_sum(10)
        assert all_sum == 23
        all_sum = hw.calculate_sum(100)
        assert all_sum == 2318
        all_sum = hw.calculate_sum(1000)
        assert all_sum == 233168
# Проверяем тип результатв и значение выполнения функции (при 122 ==3420)
    def test_calculate_values_case_122(self):
        case = hw.calculate_sum(122)
        solution = 3420
        assert type(case) == type(solution)
        assert case == solution
# Проверяем тип результатв и значение выполнения функции (при 100000 ==2333316668)
    def test_calculate_values_big(self):
        case = hw.calculate_sum(100000)
        solution = 2333316668
        assert type(case) == type(solution)
        assert case == solution
# Проверяем тип результатв и значение выполнения функции (при 9999999 ==23333321666669)
    def test_calculate_values_really_big(self):
        case = hw.calculate_sum(9999999)
        solution = 23333321666669
        assert type(case) == type(solution)
        assert case == solution
# Проверяем тип результатf на соответствие типа и значения при отрицательном значении и нуле 
    def test_calculate_values_negative(self):
        case = hw.calculate_sum(-5)
        solution = "число меньше или равно нулю, измените число"
        assert str == type(solution)
    def test_calculate_values_zero(self):
        case = hw.calculate_sum(0)
        solution = "число меньше или равно нулю, измените число"
        assert str == type(solution)
    # Проверяем тип результата на соответствие типа при строке, списке, булевых значениях    
    def test_calculate_values_str(self):
        case = hw.calculate_sum("ok")
        solution = "Вы ввели не число, введите число"
        assert type(case) == type(solution)
        assert case == solution
    def test_calculate_values_list(self):
        case = hw.calculate_sum([])
        solution = "Вы ввели не число, введите число"
        assert type(case) == type(solution)
        assert case == solution
    def test_calculate_values_empty(self):
        case = hw.calculate_sum(True)
        solution = "Вы ввели не число, введите число"
        assert type(case) == type(solution)
        assert case == solution

# Создаем класс MainCheck для тестирования задачи 3.2
class TestMainCheck():
# Этот тест проверяет, что из функции main_check будет получено ожидаемое значение  
    def test_main_check(self):
        all_check= hw.main_check()
        assert all_check == "Наименьшее натуральное число x: 142857"
# Проверяем, что значение small_nat() > 0    
    def test_small_nat_positive(self):
        from homework6 import small_nat
        assert small_nat() > 0
# Проверяем, что 2x, 3x, 4x, 5x и 6x состоят из одних и тех же цифр       
    def test_small_nat(self):
# Импортируем вашу функцию
        from homework6 import small_nat
# Вызываем функцию и получаем результат
        result = small_nat()
# Проверяем, что результат является целым числом
        assert isinstance(result, int)
# Проверяем, что 2x, 3x, 4x, 5x и 6x состоят из одних и тех же цифр
        for i in range(2, 7):
            assert sorted(str(result)) == sorted(str(i * result))
# Проверяем, что значение small_nat() не равно 0    
    def test_small_nat_is_not_zero(self):
        from homework6 import small_nat
        assert small_nat() != 0
# Проверяем, что значение small_nat() не равно float
    def test_small_nat_is_not_float(self):
        from homework6 import small_nat
        assert not isinstance(small_nat(), float)
# Проверяем, что значение small_nat() равно str 
    def test_small_nat_is_not_string(self):
        from homework6 import small_nat
        assert not isinstance(small_nat(), str)
# Проверяем, что значение small_nat() не равно None
    def test_small_nat_is_not_none(self):
        from homework6 import small_nat
        assert small_nat() is not None
# Проверяем, что значение number_nat равно str
    def test_number_nat(self):
        from homework6 import number_nat
        assert isinstance(number_nat, str)
# Проверяем, что значение number_nat равно не list
    def test_number_nat_not_list(self):
        from homework6 import number_nat
        assert not isinstance(number_nat, list)
# Проверяем, что значение main_check не bool
    def test_main_check_not_bool(self):
        from homework6 import main_check
        assert not isinstance(main_check(), bool)
# Тесты суперские, есть все основные проверки, реализация верная
