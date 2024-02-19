import multiprocessing

# Определение подкласса Worker, унаследованного от multiprocessing.Process
class Worker(multiprocessing.Process):

    # Переопределение метода run, который будет выполнен при запуске процесса
    def run(self):
        print ('In %s' % self.name)  #Вывод имени процесса
        return

if __name__ == '__main__':
    jobs = [] # Создание списка jobs для хранения объектов Worker
    
    # Создание и запуск 5 процессов Worker
    for i in range(5):
        p = Worker() # Создание объекта Worker
        jobs.append(p) # Добавление объекта Worker в список jobs
        p.start() # Запуск процесса Worker

    # Ожидание завершения каждого процесса
    for j in jobs:
        j.join()

# Результат выполнения
#----------------------
# In Worker-1
# In Worker-2
# In Worker-3
# In Worker-4
# In Worker-5
