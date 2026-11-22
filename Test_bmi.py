import Lab2.Lab2 as bmi

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(height = 1.0, weight = 22)
    assert result == 0

def test_bmi_over_weight():
    result = bmi.calculate_bmi(height = 1.0, weight = 30)

    assert result == 1

def test_bmi_under_weight():
    result = bmi.calculate_bmi(height = 1.0, weight = 15)

    assert result == -1
