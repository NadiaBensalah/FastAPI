FROM python:3.7
WORKDIR /


COPY requirements.txt ./


RUN pip install  -r requirements.txt

COPY . .


EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0"]