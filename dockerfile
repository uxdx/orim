FROM python:3.8

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS="jinho-337705-d6efaf029afa.json"

ENTRYPOINT ["python", "main.py"]