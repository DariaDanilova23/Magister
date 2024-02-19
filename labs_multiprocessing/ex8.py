import multiprocessing
import time

def slow_worker():
    # Вывод информации о начале работы воркера и времени
    print ('Starting worker', time.time())

    time.sleep(0.1) # Приостановка выполнения на 0.1 секунды

    # Вывод информации о завершении работы воркера и времени
    print ('Finished worker', time.time())

if __name__ == '__main__':
     # Создание процесса p, вызывающего функцию slow_worker
    p = multiprocessing.Process(target=slow_worker)
    # Вывод информации о состоянии процесса p (до его запуска)
    print ('BEFORE:', p, p.is_alive(), time.time())
    
    p.start() # Запуск процесса p
    # Вывод информации о состоянии процесса p (во время его выполнения)
    print ('DURING:', p, p.is_alive(), time.time())
    
    p.terminate() # Принудительное завершение процесса p
    # Вывод информации о состоянии процесса p (после принудительного завершения)
    print ('TERMINATED:', p, p.is_alive(), time.time())

    p.join() # Ожидание завершения процесса p
    # Вывод информации о состоянии процесса p (после завершения ожидания)
    print ('JOINED:', p, p.is_alive(), time.time())


# Результат выполнения
#----------------------
# BEFORE: <Process name='Process-1' parent=19211 initial> False 1708203191.7492716
# DURING: <Process name='Process-1' pid=19212 parent=19211 started> True 1708203191.754813
# TERMINATED: <Process name='Process-1' pid=19212 parent=19211 started> True 1708203191.7554839
# JOINED: <Process name='Process-1' pid=19212 parent=19211 stopped exitcode=-SIGTERM> False 1708203191.7565024