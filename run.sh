echo "-> Removing old Allure results"
rm -r allure-results/* || echo "No results"

echo "-> Start tests"
pytest --headed --base-url https://page-builder.automizely.io -m "form" --gherkin-terminal-reporter --alluredir allure-results
echo "-> Test finished"

echo "-> Generating report"
allure generate allure-results --clean -o allure-report
echo "-> Execute 'allure serve' in the command line"

