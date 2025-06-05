FROM python:alpine
WORKDIR /app
COPY app.py .
RUN pip install flask
EXPOSE 5002
CMD ["python", "app.py"]
