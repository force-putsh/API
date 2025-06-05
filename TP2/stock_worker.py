import requests
import time

def check_stock(task_id, variables):
    print("✔️ Vérification du stock...")
    result = {"stockOk": {"value": True, "type": "Boolean"}}
    complete_task(task_id, result)

def complete_task(task_id, variables):
    url = f"http://localhost:8080/engine-rest/external-task/{task_id}/complete"
    requests.post(url, json={"workerId": "worker1", "variables": variables})

while True:
    response = requests.post("http://localhost:8080/engine-rest/external-task/fetchAndLock", json={
        "workerId": "worker1",
        "maxTasks": 1,
        "topics": [{"topicName": "stock-check", "lockDuration": 10000}]
    })
    for task in response.json():
        check_stock(task['id'], task['variables'])
    time.sleep(2)
