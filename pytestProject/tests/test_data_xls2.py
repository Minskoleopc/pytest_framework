import pytest
import openpyxl

#openpyxl
#pip install openpyxl
def read_excel_data():
    workbook = openpyxl.load_workbook('test_data.xlsx')
    sheet = workbook('LoginData')
    data = []
    for row in sheet.iter_rows(min_row=2,values_only=True):
        data.append(row)
        return data
    

@pytest.mark.parametrize("username, password",read_excel_data())
def test_login_csv(username, password):
    print(f"Testing login with {username} and {password}")
    assert username != "" and password != ""

