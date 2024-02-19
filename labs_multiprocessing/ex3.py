import multiprocessing # Импорт модуля multiprocessing
import multiprocessing_import_worker # Импорт файла multiprocessing_import_worker

if __name__ == '__main__':
    jobs = [] # Инициализация списка jobs для хранения объектов процессов
    # Цикл в котором запускаются 5 процессов
    for i in range(5):
        # Создание нового процесса, вызывающего функцию worker из файла multiprocessing_import_worker
        p = multiprocessing.Process(target=multiprocessing_import_worker.worker)
        jobs.append(p) # Добавление созданного процесса в список jobs
        p.start() # Запуск созданного процесса


# Результат выполнения
#----------------------
# Worker
# Worker
# Worker
# Worker
# Worker