from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser......")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser......")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser.......")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the Browser value to setup method
    return request.config.getoption("--browser")


################## PyTest HTMP Report #############################

# It is hook for Adding Environment info to HTML Report            # Pavan Sir code not worked
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Swapnil Ghonge'


# It is hook for delete/modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)


############ Tushar Code  ###########
def pytest_metadata(metadata):  # By using this we can make changes in Html reports
    metadata["Project Name"] = "nop Commerce"
    metadata["Environment"] = "QA Environment"
    metadata["Module"] = "Customers"
    metadata["Tester"] = "Swapnil Ghonge"
    metadata.pop("Plugins", None)
    metadata.pop("JAVA_HOME", None)


def pytest_html_report_title(report):
    # Change the HTML report title
    report.title = "Test Report - nop Commerce"

# pytest -v -s -n=2 --html=Reports\report.html "E:\Automation\nopcommerceApp\testCases\test_login.py" --browser chrome
# pytest -v -s --html=Reports\report.html "E:\Automation\nopcommerceApp\testCases\test_login_ddt.py" --browser chrome
