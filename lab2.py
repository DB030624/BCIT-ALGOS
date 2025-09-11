import time 
import statistics

def measure_time(func,repeat=100):
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        times.append((end - start) * 1_000_000)
    return statistics.mean(times)


def add_to_begin_small():
    lst = list(range(10))
    lst.insert(0,-1)

def add_to_begin_large():
    lst = list(range(1_000_000))
    lst.insert(0,-1)

def add_to_end_small():
    lst = list(range(10))
    lst.append(-1)

def add_to_end_large():
    lst = list(range(1_000_000))
    lst.append(-1)

def remove_from_beg_small():
    lst = list(range(10))
    lst.pop(0)

def remove_from_beg_large():
    lst = list(range(1_000_000))
    lst.pop(0)

def remove_from_end_small():
    lst = list(range(10))
    lst.pop(-1)

def remove_from_end_large():
    lst = list(range(1_000_000))
    lst.pop(-1)


def check_num_small():
    lst = list(range(10))
    if 1 in lst:
        pass

def check_num_large():
    lst = list(range(1_000_000))
    if 1 in lst:
        pass

def check_num_not_in_small():
    lst = list(range(10))
    if -1 in lst:
        pass

def check_num_not_in_large():
    lst = list(range(1_000_000))
    if -1 in lst:
        pass

def check_key_in_dict_small():
    d = {i: None for i in range(10)}
    if 0 in d:
        pass

def check_key_in_dict_large():
    d = {i: None for i in range(1_000_000)}
    if 0 in d:
        pass

def check_key_not_in_dict_small():
    d = {i: None for i in range(10)}
    if -1 in d:
        pass

def check_key_not_in_dict_large():
    d = {i: None for i in range(1_000_000)}
    if -1 in d:
        pass




funcs = [

    add_to_begin_small,
    add_to_begin_large,
    add_to_end_small,
    add_to_end_large,
    remove_from_beg_small,
    remove_from_beg_large,
    remove_from_end_small,
    remove_from_end_large,
    check_num_small,
    check_num_large,
    check_num_not_in_small,
    check_num_not_in_large,
    check_key_in_dict_small,
    check_key_in_dict_large,
    check_key_not_in_dict_small,
    check_key_not_in_dict_large,
]

with open("results.txt", 'w') as f:
    for func in funcs:
        mean_time = measure_time(func)
        f.write(f"{func.__name__}: {mean_time:.2f}\n")