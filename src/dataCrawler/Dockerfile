FROM python:3.9.6-slim-buster
# Maybe "alpine" later to safe space?

# set environment variables
ENV PYTHONUNBUFFERED 1

ADD . .

RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt


CMD ["python", "./main.py"]