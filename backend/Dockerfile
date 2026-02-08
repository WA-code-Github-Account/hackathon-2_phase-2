FROM python:3.11-slim
WORKDIR /app
copy requirements.text .
RUN pip install --no-cache-dir -r requirements.txt
copy app ./app
EXPOSE 7860
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
