import pytest
import pytest_html
import logging

from selenium import webdriver

@pytest.fixture()
def oneTimeSetup(request,browser):
    print("Running one time setup")
    if browser=="firefox":
        value=webdriver.Firefox(executable_path="./drivers/geckodriver.exe")
    else:
        value = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
    if request.cls is not None:
        request.cls.value=value

    yield value
    print("Running one time tearDown")
    print("Closing browser......")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


#Adding screenshot to report
'''@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = "..\\screenshots\\" + "test_login_scr.png"
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' 
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra'''

