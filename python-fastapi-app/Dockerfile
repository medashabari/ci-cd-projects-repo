ARG PYTHON_VERSION=3.10.3
FROM python:${PYTHON_VERSION}-slim as base  

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

# RUN mv /usr/local/lib/python3.9/site-packages/langchain/sql_database.py /usr/local/lib/python3.9/site-packages/langchain/temp_sql_database.py
# RUN mv temp_sql_database.py /usr/local/lib/python3.9/site-packages/langchain/sql_database.py

CMD python app.py