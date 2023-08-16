# Who Let The Logs Out
A simple logging library for Python that captures API and function call details and writes them to ndjson files.

## Features
- Intercept and log API calls made using the `requests` library.
- Log input and output of any decorated function.
- Store logs in newline-delimited JSON format with timestamps.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/who_let_the_logs_out.git
    cd who_let_the_logs_out
    ```

2. (Optional) If your project uses virtual environments, set one up and activate it.

3. Install the necessary dependencies (if any are listed in `requirements.txt`):
    ```bash
    pip install -r requirements.txt
    ```

## Usage
### Logging API Calls:
Simply import the `api_logger` module before making any requests using the `requests` library.

```python
import api_logger
import requests

response = requests.get('https://api.example.com/data')
```

Logs will be written to `api_logs.ndjson`.

### Logging Function Calls:
Decorate any function with `@log_function_call` to log its input and output.

```python
from function_logger import log_function_call

@log_function_call
def add(a, b):
    return a + b

add(1, 2)
```

Logs will be written to `function_logs.ndjson`.

## Notes
- Be mindful of what you log, especially if your logs might contain sensitive data.
- This tool is intended for development and debugging purposes.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

Replace `YOUR_USERNAME` with your actual GitHub username in the Installation section. You might also want to enhance or adjust this `README.md` to better fit your project's specifics or to include any additional details, conventions, or contact information.
