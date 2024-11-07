# APP_NAME=texter

# scripts:
# 	python -m venv env

# install:
# 	./env/Scripts/pip install -r requirements.txt

# build:
# 	./env/Scripts/pyinstaller --onefile main.py

# # test:
# # 	./env/Scripts/pytest -v

# clean:
# 	rm -rf build .pytest_cache __pycache__ main.spec *.egg-info

# all: scripts install build clean



APP_NAME=texter

scripts:
	python3 -m venv env

install:
	./env/bin/pip install -r requirements.txt

test: 
	./env/bin/pytest -v test.py

build:
	./env/bin/pyinstaller --onefile main.py


clean:
	rm -rf build .pytest_cache __pycache__ main.spec *.egg-info


all: scripts install test build clean

