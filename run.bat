pytest -v -s -m "sanity" --html=./Reports/report.html "E:\Automation\nopcommerceApp\testCases\test_login.py" --browser chrome
rem pytest -v -s -m "regression" --html=./Reports/report.html "E:\Automation\nopcommerceApp\testCases\test_login_ddt.py" --browser chrome

rem pytest -v -s --html=./Reports/report.html "E:\Automation\nopcommerceApp\testCases\test_login_ddt.py" --browser chrome
rem pytest -v -s -n=2 --html=Reports/report.html "E:\Automation\nopcommerceApp\testCases\test_addCustomer.py" --browser edge
rem pytest -v -s --html=Reports/report.html "E:\Automation\nopcommerceApp\testCases\test_searchCustomerByEmail.py" --browser chrome
rem pytest -v -s --html=Reports/report.html "E:\Automation\nopcommerceApp\testCases\test_searchCustomerByName.py" --browser chrome
