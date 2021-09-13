FROM python:3

WORKDIR /bot

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
