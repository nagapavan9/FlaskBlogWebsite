FROM python:3.9
COPY . /usr/app
WORKDIR /usr/app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "run.py"]
