import multiprocessing
import time

def read_info(name):
    all_date = []
    with open(name, 'r') as file:
        while True:
            count = file.readline()
            if not count:
                break
            all_date.append(count)

filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

# Линейный подход
start_time = time.time()
for i in filenames:
    read_info(i)
end_time = time.time()
result_time = end_time - start_time
print(f'Линейное время: {result_time}')

if __name__ == '__main__':
    # Многопроцессный подход
    start_time_2 = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end_time_2 = time.time()
    result_time_2 = end_time - start_time
    print(f'многопроцессное время: {result_time_2}')
