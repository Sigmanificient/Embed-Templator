cd ..
venv\Scripts\python.exe -m setup sdist bdist_wheel
venv\Scripts\python.exe -m twine check dist/*
venv\Scripts\python.exe -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u %1 -p %2 --skip-existing
