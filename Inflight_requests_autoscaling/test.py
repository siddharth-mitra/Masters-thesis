import requests


def main():
    url = "http://127.0.0.1:8080/v1/models/sklearn-iris:predict"

    payload = "{\r\n  \"instances\": [\r\n    [6.8,  2.8,  4.8,  1.4],\r\n    [5.1,  3.5,  1.4,  0.2]\r\n  ]\r\n}\r\n"
    headers = {
        'host': "sklearn-iris.kfserving-test.example.com",
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "ee151f42-9179-7dc9-02e1-1b05878b9a22"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.json())


if __name__ == "__main__":
    main()
