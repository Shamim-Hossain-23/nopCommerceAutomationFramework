
pytest -v -s -m "sanity" --html=./Reports/testing_report.html --browser=chrome
rem pytest -v -s -m "regression" --html=./Reports/testing_report.html --browser=chrome
rem pytest -v -s -m "sanity and regression" --html=./Reports/testing_report.html --browser=chrome
rem pytest -v -s -m "sanity or regression" --html=./Reports/testing_report.html --browser=chrome


rem pytest -v -s -m "sanity" --html=./Reports/testing_report.html --browser=ff
rem pytest -v -s -m "regression" --html=./Reports/testing_report.html --browser=ff
rem pytest -v -s -m "sanity and regression" --html=./Reports/testing_report.html --browser=ff
rem pytest -v -s -m "sanity or regression" --html=./Reports/testing_report.html --browser=ff
