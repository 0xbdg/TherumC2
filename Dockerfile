FROM python3:3.12

RUN pip install requirements.txt

WORKDIR .

copy . .

cmd ["python3", "app.py"]
