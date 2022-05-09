FROM python:3.9

WORKDIR .

COPY listener.py .
RUN pip install --no-cache-dir --upgrade kafka-python
RUN pip install --no-cache-dir --upgrade requests
RUN pip install --no-cache-dir --upgrade pyjwt

CMD ["python", "./listener.py"]