import timeit
import decimal
from random import randint


def minimal(data):
    dim = len(data)
    minim = float("inf")
    for i in range(dim):
        if data[i] < minim:
            minim = data[i]
    return minim
    #return min(data)(просто через функцию)


def maximal(data):
    dim = len(data)
    maxim = -float("inf")
    for i in range(dim):
        if data[i] > maxim:
            maxim = data[i]
    return maxim
    #return max(data)


def summa(data):
    return sum(data)
    #decimal.getcontext().prec = 100 # решение суммы с переполнением, но получить сумму с переполнением сложно
    #s = decimal.Decimal(0)
    #for i in data:
        #s += decimal.Decimal(i)
    #return s



def product_float_decimal(data):  # решила переполнение, тем что увеличила колич знаков после запятой
    decimal.getcontext().prec = 100
    data_prod = data
    prod_float = decimal.Decimal(1)
    for i in range(len(data_prod)):
        prod_float *= decimal.Decimal(data_prod[i])
    return prod_float


def product_float(data):  # если умножение чисел float будет слишком большим то prod = inf
    data_prod = data
    prod = 1.0
    limit = 10.0 ** 308
    for i in range(len(data_prod)):
        if prod < limit:
            prod *= data_prod[i]
        else:
            break
    return prod


def product_int(data):  # функция если у нас int числа
    data_prod = data
    prod_int = 1
    for i in range(len(data_prod)):
        prod_int *= data_prod[i]
    return prod_int


def sovpadenie(data):#личный тест проверка на совпадение макс и мин числа
    if min(data) == max(data):
        return True
    else:
        return False



def speed(q):  # тест скорости это создание файла с q рандомных чисел
    start_time = timeit.default_timer()
    f = open("txt", "w")
    for x in range(0, q):
        f.write(str(randint(10, 1000)) + " ")
    f.close()
    with open("txt", 'r') as file:
        s = file.readline()
    s = list(map(float, s.split()))
    print("Минимальное:", minimal(s))
    print("Максимальное: ", maximal(s))
    print("Сумма:", summa(s))
    print("Произведение:", product_float_decimal(s)) #решение через десимл, если randint увеличить до 10000 то,в первом случае произведение найдется, во втором будет inf
    print("Произведение:", product_float(s))
    stop_time = timeit.default_timer()
    print("Время работы:", stop_time - start_time, "сек")
    file.close(

#тест скорости программы при разном обьеме входного файла
speed(10)
print('--------------------------------------------------------------------')
speed(100)
print('--------------------------------------------------------------------')
speed(1000)
