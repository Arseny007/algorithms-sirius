# A. Биржа

# Рита хочет попробовать поиграть на бирже. Но для начала она решила 
# потренироваться на исторических данных.

# Даны стоимости акций в каждый из n дней. В течение дня цена акции не меняется. 
# Акции можно покупать и продавать, но только по одной штуке в день. В один день 
# нельзя совершать более одной операции (покупки или продажи). Также на руках 
# не может быть более одной акции в каждый момент времени.

# Помогите Рите выяснить, какую максимальную прибыль она могла бы получить.

# Пояснения к примерам

# Пример 1
# Рита может купить акцию во 2-й день за 1 франк.

# Затем она продаст её на 3-й день за 5 франков.

# В 4-й день она снова купит акцию за 3 франка.

# На 5-й день Рита продаст эту акцию за 6 франков.

# Прибыль составила (5 - 1) + (6 - 3) = 7 франков.

# Пример 2
# Рите выгодно купить акцию в самый первый день и продать в последний.

# Пример 3
# Рита покупает акции в дни с номерами 1, 3 и 5. Продаёт в дни 2, 4 и 6. 
# Итоговая прибыль составит (12 - 1) + (16 - 12) + (8 - 1) = 22. Такой же 
# результат можно получить в виде: 22 = (16 - 1) + (8 - 1), если покупать 
# акции в дни 1 и 5, а продавать в дни 4 и 6.

# Формат ввода
# В первой аргументе записано количество дней n —– целое число в диапазоне от 0 до 10 000.

# Во втором аргументе сзадан массив n целых чисел в диапазоне от 0 до 1000 –— цены акций.

# Формат вывода
# Выведите число, равное максимально возможной прибыли за эти дни.



def solution(n, arr):
    amount = 0
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            amount += arr[i] - arr[i-1]
        
    return amount
        
def test():
    assert solution(6, [7, 1, 5, 3, 6, 4]) == 7
    assert solution(5, [1, 2, 3, 4, 5]) == 4
    assert solution(6, [1, 12, 12, 16, 1, 8]) == 22

test()

# n = int(input())
# arr = list(map(int, input().split()))

# print(solution(n, arr))