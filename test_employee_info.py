import employee_info

def test_calculate_average_salary():
    assert round(employee_info.calculate_average_salary(), 1) == 60166.7

def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(25, 35)
    assert result == [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]

def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept('Engineering')
    assert result == [
        {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]