FROM python:3.11

WORKDIR /code

COPY src/samdul10food/main.py /code/
#COPY requirements.txt /code/

RUN pip install --no-cache-dir --upgrade git+https://github.com/NishNovae/samdul10food.git@0.1.1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
