FROM python:3.11-slim

ENV PIP_NO_INDEX=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /benchmark
COPY requirements.lock /benchmark/requirements.lock
# Dependencies must be supplied through a prebuilt local wheelhouse in the
# final image. No network installation is permitted at runtime.
COPY wheelhouse_public/ /benchmark/wheelhouse/
RUN if [ -d /benchmark/wheelhouse ] && [ "$(find /benchmark/wheelhouse -type f -name '*.whl' | wc -l)" -gt 0 ]; then \
      pip install --no-index --find-links=/benchmark/wheelhouse -r /benchmark/requirements.lock; \
    fi

COPY . /benchmark
CMD ["python", "-c", "import sys; print('decepeval_Coding_data offline runtime ready', sys.version.split()[0])"]
