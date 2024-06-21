all:
	docker build -t tina/swe-bench-conda:bookworm-slim -f docker/Dockerfile .
	docker build -t tina/swe-bench-pyenv:bookworm-slim -f docker/pyenv/Dockerfile .
	docker build -t tina/swe-bench-pyenvs:bookworm-slim -f docker/pyenv/Dockerfile-pyenvs .
	docker build -t tina/swe-bench-conan-io_conan:bookworm-slim -f docker/conan-io__conan/Dockerfile .
	docker build -t tina/swe-bench-conan-io_conan-testbed:1.60.2 -f docker/conan-io__conan/1.60.2/Dockerfile .
