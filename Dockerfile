FROM python3:3.12

RUN pip install requirements.txt

WORKDIR .

cmd ["python3", "app.py"]
