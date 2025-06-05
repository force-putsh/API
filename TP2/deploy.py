import requests

with open("diagram_1.bpmn", "rb") as file:
    files = {
        "upload": ("diagram_1.bpmn", file, "text/xml")
    }
    data = {
        "deployment-name": "Order Process",
    }
    response = requests.post(
        "http://localhost:8080/engine-rest/deployment/create",
        data=data,
        files=files
    )
    print(response.json())
