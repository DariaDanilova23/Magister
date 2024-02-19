import multiprocessing
import logging
import sys

def worker():
    print ('Doing some work') #Вывод сообщения 'Doing some work'
    sys.stdout.flush() # Принудительный сброс буфера стандартного потока вывода

if __name__ == '__main__':

    # Настройка вывода журнала для процесса с уровнем отладки
    multiprocessing.log_to_stderr(logging.DEBUG)

    # Создание процесса p, вызывающего ф-ию worker
    p = multiprocessing.Process(target=worker)
    p.start() # Запуск созданного процесса
    p.join() # Ожидание завершения процесса



# Результат выполнения
#----------------------
# [INFO/Process-1] child process calling self.run()
# Doing some work
# [INFO/Process-1] process shutting down
# [DEBUG/Process-1] running all "atexit" finalizers with priority >= 0
# [DEBUG/Process-1] running the remaining "atexit" finalizers
# [INFO/Process-1] process exiting with exitcode 0
# [INFO/MainProcess] process shutting down
# [DEBUG/MainProcess] running all "atexit" finalizers with priority >= 0
# [DEBUG/MainProcess] running the remaining "atexit" finalizers