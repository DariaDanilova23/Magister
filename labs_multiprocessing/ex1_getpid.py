from multiprocessing import Process
import os # Импорт модуля для работы с функциями операционной системы.

# Определение функции info для вывода информации о процессе
def info(title):
    # Вывод переданного заголовка
    print(title)

    # Вывод имени модуля (__name__ предоставляет имя текущего модуля)
    print('module name:', __name__)

    # Вывод идентификатора родительского процесса
    print('parent process:', os.getppid())

    # Вывод идентификатора текущего процесса
    print('process id:', os.getpid())

def f(name):
    info('function f') # Вызов функции, которая выводит информацию о  процессе
    print('hello', name) # Вывод имени

if __name__ == '__main__':
    info('main line') # Вызов функции, которая выводит информацию о главном процессе
    p = Process(target=f, args=('bob',)) # Создание нового процесса, вызывающего функцию f с аргументом 'bob'
    p.start() # Запуск нового процесса
    p.join() # Ожидание завершения нового процесса


# Результат выполнения
#----------------------
# main line
# module name: main
# parent process: 4254
# process id: 9586
# function f
# module name: main
# parent process: 9586
# process id: 9587
# hello bob