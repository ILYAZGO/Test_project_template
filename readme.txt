HOW TO RUN LOCALLY:

install requirements and browsers:

    pip install -r requirements.txt  (for install requirements)
    playwright install (for install browsers)

from main directory:

    pytest --base-url https://app.stand.imot.io/ru

   !PROFIT!

you can add some parameteres:

    --headed  (with browser head)
    --slowmo 3000  (if you want to slow tests down in 3000 ms)

    -n auto  (few test-workers same time, auto can be replaced by number)

    -m {some marker}  (you can call test-sets or marked tests. look markers in pytest.ini)








