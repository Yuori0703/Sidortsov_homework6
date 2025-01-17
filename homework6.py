# Yuori Sidortsov
# Homework-6
# 24-03-2024
# Grodno-IT-Academy-Python 3.11.5

# Задача 1
# Создайте  модель из жизни. Это может быть бронирование комнаты в отеле, покупка билета в транспортной компании, или простая РПГ.
# Создайте несколько объектов классов, которые описывают ситуацию. Объекты должны содержать как атрибуты так и методы класса для 
# симуляции различных действий. Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать методы,
# взаимодействие объектов и т.д. 


# Создаем модель компании по производству и продажи окон. Компания производит и продает окна с различными характеристиками 
# (модель, цвет, ширина, высота, тип стекла). Клиент делает заказ окон по определенным размерам и с определенными харвктеристиками.
# Компания рассчитывает цену заказанных окон и изготавливает их и выдает их клиенту 
# создаем класс
# Класс Window описывает окно
class Window:
# Конструктор класса, который инициализирует атрибуты окна
    def __init__(self, model, color, width, height, glass_type, quantity):
        self.model = model 
        # Модель окна
        self.color = color 
        # Цвет окна
        self.width = width 
        # Ширина окна
        self.height = height
        # Высота окна
        self.glass_type = glass_type
        # Тип стекла окна
        self.quantity = quantity
        # Количество окон 
# Создаем класс для заказа окон
class Order:
# Конструктор класса, для заказа окон с пожеланиями клиента
    def __init__(self, name):
        self.name = name
# Создаем метод для производства окон заказчика
    def order_val(self, model, color, width, height, glass_type, quantity):
        print(f"Производим окна. Модель: {model}, Цвет: {color}, Ширина: {width}, Высота: {height}, Тип стекла: {glass_type}, Количество окон: {quantity}")
 # Возвращаем новый объект окна       
        return Window(model, color, width, height, glass_type, quantity)  
# Метод для расчета цены окна
    def calculate_price(self, model, color, width, height, glass_type, quantity):
# В зависимости от модели заказанного окна зависит цена, проверяем условия
        if model == "base":
            price_type = 120
        elif model == "standart":
            price_type = 145
        elif model == "premium" :
            price_type = 200
# В зависимости от цвета заказанного окна зависит цена, если окно белая цена 100, если цветное 200 
        color_price = 100 if color != "white" else 200  
# Цена зависит от размера окна, площадь окна умножаем на 2 рубля      
        size_price = width * height * 2 
# Цена зависит от количества стекол, при тройном стекле цена самая высокая 400 рублей 
        if glass_type == "single":
            glass_price = 100
        elif glass_type == "double":
            glass_price = 300
        elif glass_type == "triple":
            glass_price = 400
# Расчитываем итоговую цену, с учетом количества заказанных окон       
        all_price = (price_type + color_price + size_price + glass_price) * quantity
# Возвращаем окончательную цену
        return all_price  
# Cоздаем класс описывающий клиента
class Clients:
# Конструктор класса, который инициализирует имя и фамилию клиента
    def __init__(self, name):
        self.name = name
# Создаем метод класса Clients, который принимает параметры заказа окон  
    def order_windows(self, model, color, width, height, glass_type, quantity):
# Печатаем параметры заказа окон 
        print(f" {self.name} делает заказ на окна. Модель: {model}, Цвет: {color}, Ширина: {width}, Высота: {height}, Тип стекла: {glass_type} , в количестве: {quantity} штук")
# Cоздаем объект класса Order, вызываем метод order_val и присваиваем переменной window, полученное значение      
        window = Order.order_val(self, model, color, width, height, glass_type, quantity)
# Cоздаем объект класса Order, вызываем метод calculate_price и присваиваем переменной price, полученное значение  
        price = Order.calculate_price(self, model, color, width, height, glass_type, quantity)
# Возвращаем из функции window, price
        return window, price
# Создаем метод класса Clients, который принимает параметры self, window, price и выводит имя клиента window, price 
    def buy_window(self, window, price):
        print(f"Клиент {self.name} покупает окна: {window} штук за {price} рублей")

# Создаем список клиентов
client_list = [Clients("Иванов Иван"), Clients("Андреев Андрей"), Clients("Сергей Сергеев"), Clients("Павел Павлов")]
# Создаем список кортежей, представляющих параметры заказанных окон
window_list = [
    ("standart", "white", 120, 134, "single", 3),
    ("premium", "black", 130, 150, "single", 1),
    ("base", "white", 120, 134, "double", 3),
    ("standart", "white", 1490, 164, "triple", 10)
]
# Перебираем пары из client_list и window_list с помощью zip(client_list, window_list) объединяем элементы
for client_list, window_list in zip(client_list, window_list):
# Для каждой пары создаем объект класса Clients, вызываем метод order_windows и присваиваем переменным window, price, полученные значение
    window, price = Clients.order_windows(client_list, *window_list)  
# Создаем переменную wind для вывода в более читаемом виде параметров окон
    wind = "\nмодель: " + window_list[0] + "\nцвет: " + window_list[1] + "\nразмеры: " + str(window_list[2]) + "*" + str(window_list[3]) + "\nтип стекла: " + window_list[4] + "\nв количестве " + str(window_list[5]) 
# Для каждой пары создаем объект класса Clients, вызываем метод buy_window с параметрами client_list, wind, price
    Clients.buy_window(client_list, wind, price) 
# Печатаем после каждой итерации цикла 150*"-", для большей читаемости
    print(150*"-")

# Задача 2
# Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без исключений (но не более n раз - 
# параметр декоратора). Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors

# Cоздаем новый класс исключений который наследуется от встроенного класса Exception
class TooManyErrors(Exception):
    pass   
# Задаем количество попыток 7
n = 7
# Создаем декоратор dec, который принимает функцию func в качестве аргумента
def dec(func):
    def wrapper():
# Создаем переменную лимит=0, для счета числа запуков функции
        limit = 0
        while n >= limit:
# Запуcкаем цикла, который будет выполняться пока число попыток не станет более n раз
                print("")
                limit += 1
# Вызываем метод функ при каждой итерации цикла 
                func(n)
# После выполнения цикла выполняется исключение TooManyErrors
        raise TooManyErrors
    return wrapper
# Cоздаем задекорированую функцию func
@dec
def func(n):
    print(f"Пробуем выполнить функцию {n} раз")
# Создаем исключение TypeError которое будет выполняться при каждом вызове функции, т.к. число на строку не делится 
    try:
        n/str(n)
    except TypeError:
        print("Исключение: TypeError")
# В блоке try внутри декоратора вызывается функция func, если количество попыток превышает заданный лимит, 
# выбрасывается исключение TooManyErrors, блоке except выводится сообщение о превышении лимита попыток TooManyErrors.
try:
    func()
except TooManyErrors:
    print(f"Превышено количество попыток ({n})\nОшибка: TooManyErrors")
    
# Задача 3
# Выберите себе две задачи по ссылке: https://euler.jakumo.org/problems/pg/1.html
# Решите ее в виде функции и покройте тестами. Учтите, что в функцию могут быть переданы некорректные значения, здесь может пригодится ‘assertRaises’.
# Напиши около 7-10 условий для теста.
# Постарайтесь брать задачи, которые мы не разбирали на занятии. Попробуйте написать максимально «заковыристые» тесты, которые попытаются сломать ваше решение.

# Задача 3.1

# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
# Найдите сумму всех чисел меньше number, кратных 3 или 5.

def calculate_sum(number):
    all_sum = 0
# Если введено значение тип не int "Вы ввели не число, введите число"
    if type(number) != int:
        all_sum = "Вы ввели не число, введите число"
# Если введено значение меньше или равно нулю выводим "число меньше или равно нулю, измените число"
    elif number <= 0:
            all_sum = "число меньше или равно нулю, измените число"
    else:   
# Перебор всех чисел меньше number
        for n in range(number):
# Проверка, делится ли число на 3 или 5 без остатка
            if n % 3 == 0 or n % 5 == 0:
# Если делится, добавляем число к сумме
                all_sum += n
# Выводим итоговую сумму    
    return all_sum

# Задача 3.2

# Найдите такое наименьшее натуральное число x, чтобы 2x, 3x, 4x, 5x и 6x состояли из одних и тех же цифр.

# Cоздаем функцию для поска наименьшего натурального числа.
def small_nat():
# Создаем вложенную функции some_number, которая принимает два числа и проверяет, состоят ли они из одних и тех же цифр
    def two_number(num1, num2):
        # Сортировка цифр в каждом числе и сравнение результатов
        return sorted(str(num1)) == sorted(str(num2))
# Инициализируем промежуточную переменную x со значением 1
    x = 1
# Запускаем бесконечный цикл
    while True:
# Создаем пустой список для хранения результатов проверки
        check_results = []
# Проходим по диапазону чисел от 2 до 6, как в задании
        for i in range(2, 7):
# Проверяем, состоят ли числа x и i*x из одних и тех же цифр c помощью вызова функции two_number 
            result = two_number(x, i * x)
# Добавляем результат проверки в список
            check_results.append(result)
# Если все числа в списке состоят из одних и тех же цифр, возвращаем x и выходим из цикла
        if all(check_results):
            return x
# Если условие не выполняется, увеличиваем x на 1 и продолжаем цикл
        x += 1
# Вызов функции find_small и присвоение результата переменной x
x = small_nat()
# Вывод результата
number_nat = f"Наименьшее натуральное число x: {x}"
# При вызове этой функции без аргументов выводим number_nat - наименьшее натуральное число
def main_check():
    return number_nat