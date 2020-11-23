FROM python:3.8.6-buster
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python","app.py"]