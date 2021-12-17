### How to setup project

run command in project root

`pip install requirements.txt`

`playwright install`

###  How to run project 
 run command in project root

`sh run.sh`

### command example in run.sh file

_pytest --headed --base-url https://page-builder.automizely.io -m "form" --alluredir allure-results_

### **___command parameter___**

`--headed` start browser in headed mode

`--headless` start browser in headless mode, it's setted by default

`--browser {browser_name}` start specific browser, support **firefox**, **safari**, **chrome**, **chromium**(default browser)

`--base-url` specify testing environment base url

`-m` run test cases with matched tags, eg. **_-m "form"_** means run test cases which has tag "form", 
**-m "ui and product_detail"** means run test cases which has tag "ui" and "product_detail". **-m "product_list or product_detail"** means run test cases which has tag "product_list" or "product_detail"

` --lf, --last-failed`   rerun only the tests that failed at the last run (or all if none failed)

**_above are the most common used parameters, more available command parameters, run command `pytest -h` in terminal**_  
### How to debug
add `breakpoint()` into code and run project

### code snippet for some cases 
1. new page is created after clicking on an element, get the new page to interact with

`with page.context.expect_new_page():`

    edit_page.click("button")

`page.content.pages[index]`

2. enable force click when the normal click will be intercepted by the ancestor element

`page.click(selector, force=True)`

3. use pytest fixture `request` to fetch data from pytest command line

`request.config.getoption('--base-url')`
