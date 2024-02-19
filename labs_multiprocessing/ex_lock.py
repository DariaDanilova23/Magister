from multiprocessing import Process, Lock # Импорт модуля multiprocessing

# Определяем функцию, которая будет выполняться каждым процессом
def f(lос, i): 
    lос.acquire() # Захватываем блокировку, чтобы обеспечить синхронизированный доступ к ресурсам
    print ('hello world', i) # Выводим сообщение hello world с порядковым номером процесса
    lос.release() # Освобождаем блокировку после завершения операций над общими ресурсами

if __name__ == '__main__':
    lock = Lock()  # Создаем объект блокировки для синхронизации доступа к ресурсам

    # Цикл в котором создаются и запускаются 10 процессов
    for num in range(10): 
        # Создаем и запускаем новый процесс, каждый из которых вызывает функцию f 
        # с параметрами (объект блокировки и номер процесса)
        Process(target=f, args=(lock, num)).start() 


# Результат выполнения
#----------------------
# hello world 0
# hello world 1
# hello world 2
# hello world 3
# hello world 4
# hello world 5
# hello world 6
# hello world 7
# hello world 9
# hello world 8