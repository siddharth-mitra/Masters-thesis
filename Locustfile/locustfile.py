import time
from wsgiref import headers
import requests
from IPython.core import payload
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):

    @task
    def hello_world(self):
        headers_t = {
            'host': "flowers-sample-gpu.default.example.com",
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        with self.client.post("/v1/models/flowers-sample-gpu:predict", data=open(
                '../InferenceServices/GPU-based-hpa/input4.json', 'rb'), headers=headers_t,
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print(response.status_code)
                response.failure("failure text")


