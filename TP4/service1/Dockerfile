FROM python:alpine
WORKDIR /app
COPY app.py .
RUN pip install flask
EXPOSE 5001
CMD ["python", "app.py"]
