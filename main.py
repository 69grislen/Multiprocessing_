import multiprocessing
import time
import random

def heavy(n, i, proc):
    factor = 1
    for x in range(2, n + 1):
        factor *= x
    print(f"Вычисление № {i} процессовр {proc}")

def sum_lict():
    list1 = []
    list2 = []

    for i in range(1, 10):
        list1.append(random.randint(0, 100))
        list2.append(random.randint(0, 100))

    summ = sum(list1) + sum(list2)
    print(f"summ is: {summ}")

def sequential(calc, proc):
    print(f"Запускаем поток № {proc}")

    for i in range(calc):
        heavy(10, i, proc)

    sum_lict()
    print(f"{calc} циклов вычислений закончены. Процессор № {proc}")

def pooled(core=None):
    n_proc = core
    calc = 4

    init = map(lambda x: (calc, x), range(n_proc))
    with multiprocessing.Pool() as pool:
        pool.starmap(sequential, init)

    print(calc, n_proc, core)
    return (calc, n_proc, core)

if __name__ == "__main__":
    start = time.time()

    calc, n_proc, n = pooled(10)
    end = time.time()

    text = '' if n is None else 'задано '
    print(f"Всего {text}{n_proc} ядер вычислений")
    print(f"На каждом ядре произведено {calc} циклов вычислений")
    print(f"Итого {n_proc * calc} циклов за: ", end - start)

