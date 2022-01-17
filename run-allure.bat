rmdir allure-results /S /Q
py.test --alluredir allure-results test-allure/
c:\tools\allure-2.17.2\bin\allure.bat generate allure-results --clean
c:\tools\allure-2.17.2\bin\allure.bat open allure-report
