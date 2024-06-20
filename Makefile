all:
	docker build -t tina/swe-bench-conda:bookworm-slim -f docker/Dockerfile .
	docker build -t tina/swe-bench-pyenv:bookworm-slim -f docker/pyenv/Dockerfile .
	docker build -t tina/swe-bench-pyenvs:bookworm-slim -f docker/pyenv/Dockerfile-pyenvs .
	docker build -t tina/swe-bench-pandas-dev_pandas:bookworm-slim -f docker/pandas-dev__pandas/Dockerfile .
	docker build -t tina/swe-bench-pandas-dev_pandas-testbed:1.4.1 -f docker/pandas-dev__pandas/1.4.1/Dockerfile .
	docker build -t tina/swe-bench-pandas-dev_pandas-instance:pandas-dev__pandas-39807 -f docker/pandas-dev__pandas/1.4.1/pandas-dev__pandas-39807/Dockerfile .
	docker build -t tina/swe-bench-pandas-dev_pandas-instance:pandas-dev__pandas-39800 -f docker/pandas-dev__pandas/1.4.1/pandas-dev__pandas-39800/Dockerfile .
	docker build -t tina/swe-bench-pandas-dev_pandas-instance:pandas-dev__pandas-39796 -f docker/pandas-dev__pandas/1.4.1/pandas-dev__pandas-39796/Dockerfile .
	docker build -t tina/swe-bench-pandas-dev_pandas-instance:pandas-dev__pandas-39777 -f docker/pandas-dev__pandas/1.4.1/pandas-dev__pandas-39777/Dockerfile .
	docker build -t tina/swe-bench-pandas-dev_pandas-instance:pandas-dev__pandas-39766 -f docker/pandas-dev__pandas/1.4.1/pandas-dev__pandas-39766/Dockerfile .
