import time
from wsgiref import headers
import requests
from IPython.core import payload
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 1.5)

    @task
    def hello_world(self):
        headers_t = {
            'host': "flowers-sample-gpu.experiment-1.example.com",
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        with self.client.post("/v1/models/flowers-sample-gpu:predict", data=open(
                '../InferenceServices/inflight-request-based/tensor-flow-flowers/input.json', 'rb'), headers=headers_t,
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print(response.status_code)
                response.failure("failure text")


