FROM python:3.11

WORKDIR /app

COPY requirements.txt /app

ARG CACHEBUST=4
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "xp_patterns_performance.py"]