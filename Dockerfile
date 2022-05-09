FROM python:3.9

WORKDIR .

COPY ./fast_api_service .
COPY req.txt .
RUN pip install --no-cache-dir --upgrade -r ./req.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]