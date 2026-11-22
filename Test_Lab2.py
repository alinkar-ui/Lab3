import Lab2.Lab2 as test

def test_find_min_max():
    result = test.calc_min_max_temperature([2,3,4])
    assert result == [2,4]

def test_find_avg():
    result = test.calc_average_temperature([2,3,4])
    assert result == 3

def test_find_median_even():
    result = test.calc_median_temperature([3,4,5,6])
    assert result == 4.5

def test_find_median_odd():
    result = test.calc_median_temperature([3,5,6])
    assert result == 5
