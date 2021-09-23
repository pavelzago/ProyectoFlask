FROM python:3.8
COPY ./flask-introduction/app /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]