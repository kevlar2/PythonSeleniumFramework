import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        # Set browser options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("headless")
        chrome_options.add_argument("--ignore-certificate-errors")
        # Get chrome browser with options
        driver = webdriver.Chrome(executable_path="E:/WebDrivers/chromedriver.exe", options=chrome_options)
    elif browser_name == "firefox":
        # Get firefox browser
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        # Get edge browser
        driver = webdriver.Edge()

    driver.maximize_window()
    # Get url
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.quit()


# Get screenshot and add to report for failed test results
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

# Screenshot method
def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
