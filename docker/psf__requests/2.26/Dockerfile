# Generated by generate_dockerfiles.py

FROM aorwall/swe-bench-psf_requests:bookworm-slim



COPY --from=aorwall/swe-bench-pyenvs:bookworm-slim /opt/pyenv/versions/3.9.19 /opt/pyenv/versions/3.9.19

RUN pyenv rehash && \
    pyenv global 3.9.19 && \
    pyenv versions

WORKDIR /opt/psf__requests

RUN git -c advice.detachedHead=false checkout a1a6a549a0143d9b32717dbe3d75cd543ae5a4f6


RUN pip install pytest

RUN python -m pip install .


RUN git checkout a1a6a549a0143d9b32717dbe3d75cd543ae5a4f6 .

ENV TESTBED_NAME=psf__requests__2.26
ENV IMAGE_TYPE=pyenv

WORKDIR /opt

COPY swebench_docker swebench_docker
COPY docker/pyenv/entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]