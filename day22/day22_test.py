import pytest
from day22 import *

def test_example1():
    sec_nr = 123
    sec_nrs = [15887950,16495136,527345,704524,1553684,12683156,11100544,12249484,7753432,5908254]

    for i in range(10):
        sec_nr = next_secret_number(sec_nr)
        assert sec_nrs[i] == sec_nr

def test_example2():
    org_sec = [1,10,100,2024]
    final_sec = [8685429,4700978,15273692,8667524]
    calc_sec = []
    nr_runs = 2000
    memory = {}

    for i in range(len(org_sec)):
        memory, sec_nr = run_sequence(memory,org_sec[i],nr_runs)
        calc_sec.append(sec_nr)

    assert calc_sec == final_sec
    assert sum(calc_sec) == 37327623

def test_parse():
    file_name = "example2"
    org_sec = read_input(file_name)
    assert org_sec == [1,10,100,2024] 