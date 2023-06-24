FROM python:3.11.4

WORKDIR /LootCouncil

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]