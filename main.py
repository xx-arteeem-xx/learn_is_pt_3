import math

def welcome_screen():
    """Выводит приветственное окно псевдографикой"""
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║           ТЕОРИЯ ЧИСЕЛ: РЕШЕНИЕ ЗАДАЧ                        ║")
    print("║                                                              ║")
    print("║            Вариант 15                                        ║")
    print("║                                                              ║")
    print("║    Автор: Python Программа                                   ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

def display_menu():
    """Отображает главное меню с выбором задания"""
    print("\n" + "="*60)
    print("ГЛАВНОЕ МЕНЮ".center(60))
    print("="*60)
    print("1. Задача 1: Функция Эйлера")
    print("2. Задача 2: Разложение на простые множители")
    print("3. Задача 3: Проверка на псевдопростоту")
    print("4. Задача 4: Проверка чисел на простоту")
    print("5. Задача 5: Оценка количества простых чисел")
    print("6. Выход из программы")
    print("="*60)

def task1():
    """Задача 1: Вычисление функции Эйлера"""
    print("\n" + "═"*60)
    print("ЗАДАЧА 1: ФУНКЦИЯ ЭЙЛЕРА".center(60))
    print("═"*60)
    print("Дано целое число p. Вычислите функцию Эйлера от этого числа.")
    print("p=44 (по условию)")
    print("-"*60)
    
    choice = input("Использовать число из условия (44)? (y/n): ").lower()
    if choice == 'y':
        p = 44
    else:
        try:
            p = int(input("Введите целое число p: "))
        except ValueError:
            print("Ошибка: нужно ввести целое число!")
            return
    
    print(f"\nВычисляем функцию Эйлера φ({p}):")
    
    # Функция Эйлера
    result = p
    n = p
    i = 2
    
    print(f"Разложение числа {p} на простые множители:")
    factors = []
    
    while i * i <= n:
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            factors.append((i, count))
            print(f"  Найден множитель: {i}^{count}")
        i += 1
    if n > 1:
        factors.append((n, 1))
        print(f"  Найден множитель: {n}^1")
    
    # Вычисление φ(p)
    result = p
    for factor, _ in factors:
        result *= (1 - 1/factor)
    
    print(f"\nФормула вычисления: φ(p) = p * ∏(1 - 1/p_i)")
    print("Где p_i - различные простые делители числа p")
    
    if factors:
        formula_parts = []
        for factor, _ in factors:
            formula_parts.append(f"(1 - 1/{factor})")
        
        formula = f"φ({p}) = {p} * " + " * ".join(formula_parts)
        print(f"Применяем формулу: {formula}")
        print(f"φ({p}) = {p} * " + " * ".join([f"({factor-1}/{factor})" for factor, _ in factors]))
    
    result = int(result)
    print(f"\n✓ ОТВЕТ: φ({p}) = {result}")
    
    # Проверка для 44
    if p == 44:
        print("\nПроверка для p=44:")
        print("Простые делители 44: 2, 11")
        print("φ(44) = 44 * (1 - 1/2) * (1 - 1/11) = 44 * 1/2 * 10/11 = 20")
        print("Числа, взаимно простые с 44 и меньшие его:")
        coprime = [i for i in range(1, p) if math.gcd(i, p) == 1]
        print(f"Всего {len(coprime)} чисел: {coprime}")

def task2():
    """Задача 2: Разложение на простые множители"""
    print("\n" + "═"*60)
    print("ЗАДАЧА 2: РАЗЛОЖЕНИЕ НА ПРОСТЫЕ МНОЖИТЕЛИ".center(60))
    print("═"*60)
    print("Дано целое число x. Разложите его на простые множители.")
    print("x=169128 (по условию)")
    print("-"*60)
    
    choice = input("Использовать число из условия (169128)? (y/n): ").lower()
    if choice == 'y':
        x = 169128
    else:
        try:
            x = int(input("Введите целое число x: "))
        except ValueError:
            print("Ошибка: нужно ввести целое число!")
            return
    
    print(f"\nРазложение числа {x} на простые множители:")
    
    original_x = x
    factors = []
    n = x
    divisor = 2
    
    print("\nПроцесс разложения:")
    while n > 1:
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1
        if count > 0:
            factors.append((divisor, count))
            print(f"  Делим на {divisor}: {x // (divisor**count)} * {divisor}^{count}")
        divisor += 1 if divisor == 2 else 2
        # Ускоряем процесс проверкой делимости на 2 и нечетные числа
        if divisor * divisor > n and n > 1:
            factors.append((n, 1))
            print(f"  Остаток {n} - простое число: {n}^1")
            break
    
    print(f"\nКаноническое разложение:")
    factor_str = " * ".join([f"{factor}^{exp}" if exp > 1 else str(factor) for factor, exp in factors])
    print(f"{original_x} = {factor_str}")
    
    # Проверка
    check = 1
    for factor, exp in factors:
        check *= factor ** exp
    
    print(f"\n✓ ОТВЕТ: {factor_str}")
    print(f"Проверка: {check} = {original_x} ({'верно' if check == original_x else 'неверно!'})")

def is_prime_miller_rabin(n, k=5):
    """Тест Миллера-Рабина на простоту"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    
    # Записываем n-1 = d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    for _ in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True

def task3():
    """Задача 3: Проверка на псевдопростоту"""
    print("\n" + "═"*60)
    print("ЗАДАЧА 3: ПРОВЕРКА НА ПСЕВДОПРОСТОТУ".center(60))
    print("═"*60)
    print("Даны числа a и n. Проверить, является ли число n псевдопростым")
    print("по основанию a.")
    print("n=50, a=5 (по условию)")
    print("-"*60)
    
    choice = input("Использовать числа из условия (n=50, a=5)? (y/n): ").lower()
    if choice == 'y':
        n, a = 50, 5
    else:
        try:
            n = int(input("Введите число n: "))
            a = int(input("Введите основание a: "))
        except ValueError:
            print("Ошибка: нужно ввести целые числа!")
            return
    
    print(f"\nПроверяем, является ли n={n} псевдопростым по основанию a={a}")
    print("\nОпределение: число n называется псевдопростым по основанию a,")
    print("если оно составное и выполняется сравнение:")
    print(f"    a^(n-1) ≡ 1 (mod n)")
    
    # Проверяем, составное ли n
    print(f"\n1. Проверяем, является ли n={n} составным:")
    
    def is_composite(n):
        if n < 2:
            return False
        if n in (2, 3, 5, 7):
            return False
        if n % 2 == 0:
            return True
        # Простая проверка на делимость
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return True, i
        return False, None
    
    composite, divisor = is_composite(n)
    
    if composite:
        print(f"   Число {n} составное (делится на {divisor})")
    else:
        print(f"   Число {n} простое → не может быть псевдопростым")
        print(f"\n✓ ОТВЕТ: n={n} НЕ является псевдопростым по основанию a={a}")
        print("   (поскольку n - простое число)")
        return
    
    print(f"\n2. Проверяем условие a^(n-1) ≡ 1 (mod n):")
    print(f"   Вычисляем {a}^({n}-1) mod {n} = {a}^{n-1} mod {n}")
    
    # Вычисляем a^(n-1) mod n
    result = pow(a, n-1, n)
    print(f"   {a}^{n-1} mod {n} = {result}")
    
    if result == 1:
        print(f"   Условие выполняется: {result} ≡ 1 (mod {n})")
        print(f"\n✓ ОТВЕТ: n={n} ЯВЛЯЕТСЯ псевдопростым по основанию a={a}")
        print(f"   (n составное и {a}^({n}-1) ≡ 1 mod {n})")
    else:
        print(f"   Условие НЕ выполняется: {result} ≠ 1 (mod {n})")
        print(f"\n✓ ОТВЕТ: n={n} НЕ является псевдопростым по основанию a={a}")

def is_prime_simple(n):
    """Простая проверка числа на простоту"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def task4():
    """Задача 4: Проверка чисел на простоту"""
    print("\n" + "═"*60)
    print("ЗАДАЧА 4: ПРОВЕРКА ЧИСЕЛ НА ПРОСТОТУ".center(60))
    print("═"*60)
    print("Даны пять чисел: x1, x2, x3, x4 и x5.")
    print("Определите, какие из них являются простыми, а какие - нет.")
    print("x1=28, x2=30, x3=60, x4=73, x5=83 (по условию)")
    print("-"*60)
    
    choice = input("Использовать числа из условия? (y/n): ").lower()
    if choice == 'y':
        numbers = [28, 30, 60, 73, 83]
    else:
        try:
            numbers = []
            for i in range(1, 6):
                num = int(input(f"Введите число x{i}: "))
                numbers.append(num)
        except ValueError:
            print("Ошибка: нужно ввести целые числа!")
            return
    
    print(f"\nПроверяем числа на простоту: {numbers}")
    print("-"*40)
    
    results = []
    
    for num in numbers:
        print(f"\nЧисло: {num}")
        
        if num < 2:
            print(f"  {num} < 2 → не является простым")
            results.append((num, False))
            continue
        
        # Быстрая проверка на четность
        if num == 2:
            print("  Это число 2 → простое")
            results.append((num, True))
            continue
        
        if num % 2 == 0:
            print(f"  Четное число (>2) → составное")
            results.append((num, False))
            continue
        
        # Проверка делимости
        is_prime = True
        divisor = None
        
        limit = int(math.sqrt(num)) + 1
        for i in range(3, limit, 2):
            if num % i == 0:
                is_prime = False
                divisor = i
                break
        
        if is_prime:
            print(f"  Не найдено делителей до √{num} ≈ {int(math.sqrt(num))} → простое")
            results.append((num, True))
        else:
            print(f"  Найден делитель: {divisor} → составное")
            results.append((num, False))
    
    print("\n" + "="*60)
    print("РЕЗУЛЬТАТЫ:".center(60))
    print("="*60)
    
    primes = [num for num, is_prime in results if is_prime]
    composites = [num for num, is_prime in results if not is_prime]
    
    print(f"\nПростые числа ({len(primes)}): {primes}")
    print(f"Составные числа ({len(composites)}): {composites}")
    
    print(f"\n✓ ОТВЕТ:")
    for num, is_prime in results:
        status = "простое" if is_prime else "составное"
        print(f"  {num} - {status}")

def task5():
    """Задача 5: Оценка количества простых чисел"""
    print("\n" + "═"*60)
    print("ЗАДАЧА 5: ОЦЕНКА КОЛИЧЕСТВА ПРОСТЫХ ЧИСЕЛ".center(60))
    print("═"*60)
    print("Дано число N. Оцените количество простых чисел,")
    print("не превосходящих N.")
    print("N=62000000000 (62 млрд, по условию)")
    print("-"*60)
    
    choice = input("Использовать число из условия (62000000000)? (y/n): ").lower()
    if choice == 'y':
        N = 62000000000
    else:
        try:
            N = int(input("Введите число N: "))
        except ValueError:
            print("Ошибка: нужно ввести целое число!")
            return
    
    print(f"\nОцениваем количество простых чисел π(N) ≤ {N}")
    print(f"(π(N) - функция, считающая количество простых чисел ≤ N)")
    
    print("\nИспользуем известные приближенные формулы:")
    print("1. Теорема о распределении простых чисел:")
    print("   π(N) ~ N / ln(N)")
    print("\n2. Более точная оценка (интегральный логарифм):")
    print("   π(N) ~ Li(N) = ∫(dx/ln(x)) от 2 до N")
    print("\n3. Еще более точная оценка:")
    print("   π(N) ~ N / (ln(N) - 1)")
    
    ln_N = math.log(N)
    
    # Оценка 1: N/ln(N)
    est1 = N / ln_N
    print(f"\n1. Оценка по формуле N/ln(N):")
    print(f"   π({N}) ≈ {N} / ln({N})")
    print(f"   ln({N}) ≈ {ln_N:.6f}")
    print(f"   π({N}) ≈ {est1:,.0f}")
    
    # Оценка 2: N/(ln(N)-1)
    est2 = N / (ln_N - 1)
    print(f"\n2. Оценка по формуле N/(ln(N)-1):")
    print(f"   π({N}) ≈ {N} / (ln({N}) - 1)")
    print(f"   π({N}) ≈ {N} / ({ln_N:.6f} - 1)")
    print(f"   π({N}) ≈ {est2:,.0f}")
    
    # Оценка 3: интегральный логарифм (приближение)
    # Li(N) ≈ N/ln(N) * (1 + 1/ln(N) + 2/ln²(N) + ...)
    est3 = est1 * (1 + 1/ln_N + 2/(ln_N**2))
    print(f"\n3. Оценка через интегральный логарифм (приближение):")
    print(f"   Li({N}) ≈ N/ln(N) * (1 + 1/ln(N) + 2/ln²(N))")
    print(f"   Li({N}) ≈ {est1:,.0f} * (1 + {1/ln_N:.6f} + {2/(ln_N**2):.6f})")
    print(f"   π({N}) ≈ Li({N}) ≈ {est3:,.0f}")
    
    # Известные данные (для больших N)
    print("\n" + "-"*60)
    print("СПРАВОЧНЫЕ ДАННЫЕ:")
    print("-"*60)
    print("Для сравнения:")
    print("π(10¹²) = 37,607,912,018 (точно известное значение)")
    print("N = 6.2×10¹⁰ примерно в 16 раз меньше 10¹²")
    
    # Экстраполяция
    print(f"\nЭкстраполяция от известных значений:")
    print("π(10¹⁰) ≈ 455,052,511")
    print("π(10¹¹) ≈ 4,118,054,813")
    print(f"N = {N:,.0f} находится между этими значениями")
    
    # Интерполяция
    log_N = math.log10(N)
    # Линейная интерполяция в логарифмической шкале
    pi_10_10 = 455052511
    pi_10_11 = 4118054813
    
    # Интерполяция: log10(π) линейно зависит от log10(N)
    log_pi_10 = math.log10(pi_10_10)
    log_pi_11 = math.log10(pi_10_11)
    
    # log10(N) = 10.79
    log_pi_est = log_pi_10 + (log_pi_11 - log_pi_10) * (log_N - 10)
    pi_interp = 10**log_pi_est
    
    print(f"\nИнтерполяция между π(10¹⁰) и π(10¹¹):")
    print(f"log10({N}) = {log_N:.2f}")
    print(f"π({N}) ≈ 10^{log_pi_est:.2f} ≈ {pi_interp:,.0f}")
    
    print("\n" + "="*60)
    print(f"✓ ОТВЕТ: π({N:,.0f}) ≈ {int((est1+est2+est3+pi_interp)/4):,.0f}")
    print("="*60)
    print("\nПримерный диапазон: 2,400,000,000 - 2,600,000,000")
    print(f"(Более точно: между {int(est2):,} и {int(est3):,})")

def main():
    """Главная функция программы"""
    import random
    
    welcome_screen()
    
    while True:
        display_menu()
        
        try:
            choice = input("\nВыберите задание (1-6): ").strip()
            
            if choice == '1':
                task1()
            elif choice == '2':
                task2()
            elif choice == '3':
                task3()
            elif choice == '4':
                task4()
            elif choice == '5':
                task5()
            elif choice == '6':
                print("\n" + "="*60)
                print("Выход из программы. До свидания!".center(60))
                print("="*60)
                break
            else:
                print("Ошибка: выберите число от 1 до 6!")
                continue
            
            # Возврат в главное меню
            input("\nНажмите Enter для возврата в главное меню...")
            
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            break
        except Exception as e:
            print(f"\nПроизошла ошибка: {e}")
            input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()