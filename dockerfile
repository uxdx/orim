FROM python:3.8

COPY . /app
WORKDIR /app

ENV PORT 8080
ENV HOST 0.0.0.0

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt


ENTRYPOINT ["python"]
CMD ["main.py"]

EXPOSE 8080
