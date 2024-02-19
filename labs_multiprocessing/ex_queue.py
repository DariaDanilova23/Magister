
from multiprocessing import Process, Queue

# Определение функции, которая будет выполняться в каждом процессе
def func(q_in,q_out):
    x = q_in.get() # Получаем данные из очереди q_in
    print('func get: ',x) # Вывод данные из очереди в консоль
    q_out.put(x**2) # Вычисляем квадрат числа и помещаем результат в очередь q_out

if __name__ == '__main__':

    # Создаем две очереди для обмена данными между процессами
    q_in = Queue()
    q_out = Queue()

    # Создаем и запускаем 4 процесса, каждый из которых вызывает функцию func, 
    # в которую передаем две очереди
    for x in range(4):
        p = Process(target=func, args=(q_in,q_out))
        p.start()

    # Передаем данные в каждый процесс через q_in и выводим результат из q_out
    for x in range(4):
        q_in.put(x)
        print ('in main recv: ',q_out.get())


# Результат выполнения
#----------------------
# func get:  0
# in main recv:  0
# func get:  1
# in main recv:  1
# func get:  2
# in main recv:  4
# func get:  3
# in main recv:  9
    