import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser == "chrome" or browser == "Chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox" or browser == "FF" or browser == "ff":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge" or browser == "Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        print("Input the right browser please")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

################ Pytest HTML Report ################

# It is hooks for adding environment info to HTML report
def pytest_configure(config):
    config._metadata["Project Name"] = "nop Commerce"
    config._metadata["Module Name"] = "Customer"
    config._metadata["Tester"] = "Shamim"


# It is hook for delete/modify environment into the HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
