import json
import datetime

def log_function_call(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()

        log_data = {
            "function_name": func.__name__,
            "args": str(args),
            "kwargs": str(kwargs),
            "output": str(result),
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "duration": (end_time - start_time).total_seconds()
        }
        with open("function_logs.ndjson", "a") as log_file:
            log_file.write(json.dumps(log_data) + "\n")

        return result

    return wrapper
