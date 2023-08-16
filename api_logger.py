import requests
import json
import datetime

class APILogger:
    def __init__(self):
        self.original_get = requests.get
        self.original_post = requests.post
        requests.get = self._custom_get
        requests.post = self._custom_post

    def _custom_get(self, url, *args, **kwargs):
        start_time = datetime.datetime.now()
        response = self.original_get(url, *args, **kwargs)
        end_time = datetime.datetime.now()
        self.log_request('GET', url, None, response, start_time, end_time)
        return response

    def _custom_post(self, url, *args, **kwargs):
        start_time = datetime.datetime.now()
        data = kwargs.get('data', None)
        response = self.original_post(url, *args, **kwargs)
        end_time = datetime.datetime.now()
        self.log_request('POST', url, data, response, start_time, end_time)
        return response

    def log_request(self, method, url, data, response, start_time, end_time):
        log_data = {
            "method": method,
            "url": url,
            "data": str(data),
            "response": response.text,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "duration": (end_time - start_time).total_seconds()
        }
        with open("api_logs.ndjson", "a") as log_file:
            log_file.write(json.dumps(log_data) + "\n")

logger = APILogger()
