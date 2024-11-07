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
	./env/Scripts/pip install -r requirements.txt

test: 
	./env/Scripts/pytest -v test.py

build:
	./env/Scripts/pyinstaller --onefile main.py



clean:
	if exist build rmdir /s /q build

	if exist __pycache__ rmdir /s /q __pycache__

	if exist main.spec del main.spec

	if exist *.egg-info rmdir /s /q *.egg-info

all: scripts install test build clean

