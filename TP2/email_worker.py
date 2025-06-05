import requests
import time

def send_email(task_id, variables):
    print("📧 Envoi du mail...")
    complete_task(task_id, {})

def complete_task(task_id, variables):
    url = f"http://localhost:8080/engine-rest/external-task/{task_id}/complete"
    requests.post(url, json={"workerId": "worker2", "variables": variables})

while True:
    response = requests.post("http://localhost:8080/engine-rest/external-task/fetchAndLock", json={
        "workerId": "worker2",
        "maxTasks": 1,
        "topics": [{"topicName": "send-email", "lockDuration": 10000}]
    })
    for task in response.json():
        send_email(task['id'], task['variables'])
    time.sleep(2)
