import time
from wsgiref import headers
import requests
from IPython.core import payload
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        url = "http://127.0.0.1:8080/v1/models/sklearn-iris:predict"
        payload_t = "{\r\n  \"instances\": [\r\n    [6.8,  2.8,  4.8,  1.4],\r\n    [5.1,  3.5,  1.4,  0.2]\r\n  " \
                    "]\r\n}\r\n "
        headers_t = {
            'host': "sklearn-iris.kfserving-test.example.com",
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        with self.client.post("/v1/models/sklearn-iris:predict", data=payload_t, headers=headers_t,
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print(response.status_code)
                response.failure("failure text")

        @task
        def hello_world(self):
            url = "http://127.0.0.1:8080/v1/models/sklearn-iris:predict"
            payload_t = "{\r\n  \"instances\": [\r\n    [6.8,  2.8,  4.8,  1.4],\r\n    [5.1,  3.5,  1.4,  0.2]\r\n  " \
                        "]\r\n}\r\n "
            headers_t = {
                'host': "sklearn-iris.kfserving-test.example.com",
                'content-type': "application/json",
                'cache-control': "no-cache"
            }
            with self.client.post("/v1/models/sklearn-iris:predict", data=payload_t, headers=headers_t,
                                  catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    print(response.status_code)
                    response.failure("failure text")
