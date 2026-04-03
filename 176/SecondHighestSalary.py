import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    MAX_SALARY = employee['salary'].max()
    second_highest_salary = employee.loc[employee['salary'] < MAX_SALARY, 'salary'].max()

    return pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
