# A Python-based task scheduler that automates routine enterprise jobs, with logging and retry capabilities

## Overview 🌐
TaskScheduler is a Python-based application designed to automate routine enterprise jobs. It is built to interact with APIs, automatically scheduling tasks and ensuring they are executed at the right time. Its robust logging feature tracks every step of the process, making it easy to monitor job statuses and troubleshoot if necessary. With built-in retry capabilities, it ensures that temporary issues don't stand in the way of task completion. This makes the TaskScheduler a powerful tool for businesses, reducing manual work, improving efficiency, and minimizing the risk of errors.

## Features 🚀

- **API Integration 🌐**: TaskScheduler is designed to work with APIs. It is initialized with an API base URL and a token for authentication, allowing it to interact seamlessly with your enterprise's APIs.

- **Task Scheduling 📅**: The core function of TaskScheduler is to schedule tasks. It uses the Python 'schedule' module to automate routine enterprise jobs, ensuring they are performed accurately and on time.

- **Logging 📝**: TaskScheduler includes a comprehensive logging feature. The logger is set up with the 'logging' module and is configured to display the timestamp, name of the logger, severity level, and the actual log message. This provides a detailed account of TaskScheduler's operations, making it easy to monitor job statuses, detect errors, and troubleshoot problems.

- **Retry Capabilities 🔄**: TaskScheduler is built to handle issues that can interrupt task execution. If a task fails due to temporary problems, the scheduler will automatically retry to ensure it gets completed.

- **Authentication 🔐**: TaskScheduler uses token-based authentication when interacting with APIs. The 'Authorization' header is set with a bearer token, ensuring secure access to your enterprise's APIs.

- **Customizable 🎛️**: The TaskScheduler class can be easily customized according to your needs. You can modify the logging level, tweak the task scheduling mechanism, or add new methods to interact with different APIs.

- **Type Hints 🏷️**: The code makes use of Python's type hinting feature, making it easier to understand what type of data each function expects and returns. This makes the code more readable and reduces the risk of type-related bugs.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

# Installation Instructions for the Python-based Task Scheduler

This guide will help you to install and configure the Python-based task scheduler that automates routine enterprise jobs, with logging and retry capabilities.

## 1. Prerequisites

Before you start the installation, ensure that you meet the following prerequisites:

- Python 3.6+ installed. You can download it from the [official Python website](https://www.python.org/downloads/).
- Pip, the Python package installer. Pip generally comes with Python.
- Access to a terminal/command line interface.

## 2. Installation Process

Follow the steps below to install the Python-based Task Scheduler:

1. Clone the project from the repository:

```bash
git clone https://github.com/your-repo/python-task-scheduler.git
```

2. Navigate into the project directory:

```bash
cd python-task-scheduler
```

3. Install the required Python libraries using Pip:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the following libraries:

- csv
- json
- logging
- requests
- schedule
- time

## 3. Verification Steps

To verify that the installation was successful, try to import the `TaskScheduler` class in a Python shell:

1. Open a Python shell:

```bash
python
```

2. Import the `TaskScheduler` class:

```python
from task_scheduler import TaskScheduler
```

If no error messages appear, the installation was successful.

## 4. Post-Installation Configuration

After successful installation, you might need to do some configuration:

- Provide the API base URL and the token for authentication during the `TaskScheduler` object creation:

```python
scheduler = TaskScheduler('your-api-base-url', 'your-token')
```

- Schedule a task using the `schedule_task` method:

```python
scheduler.schedule_task('your-task')
```

Remember to replace `'your-api-base-url'`, `'your-token'`, and `'your-task'` with the actual API base URL, the token, and the task that you want to schedule.

That's it! You have successfully installed and configured the Python-based Task Scheduler. Enjoy automating your routine enterprise jobs!

# TaskScheduler Usage Guide

TaskScheduler is a Python-based task scheduler that automates routine enterprise jobs, with logging and retry capabilities. This guide will help you understand how to effectively use this class.

## Table of Contents

1. [Basic Usage](#basic-usage)
2. [Common Use Cases](#common-use-cases)
3. [Parameters](#parameters)
4. [Expected Outputs](#expected-outputs)
5. [Advanced Usage](#advanced-usage)

<a name="basic-usage"></a>
## 1. Basic Usage

The `TaskScheduler` class is initialized with the base URL for the API and the token for authentication. Here's an example:

```python
task_scheduler = TaskScheduler("https://api.example.com", "your_token")
```

After initializing, you can schedule a task with the `schedule_task` method.

```python
task = {
    "endpoint": "/endpoint",
    "method": "POST",
    "data": {"key": "value"},
    "interval": 10
}
task_scheduler.schedule_task(task)
```

<a name="common-use-cases"></a>
## 2. Common Use Cases

Some common use cases for the `TaskScheduler` class would include:

- **Batch Processing:** If you have a series of jobs that need to be run in sequence, you can use the `TaskScheduler` to automate this process.
- **Periodic API Calls:** If you need to hit an API endpoint at regular intervals, you can use the `TaskScheduler` to handle this.

<a name="parameters"></a>
## 3. Parameters

The `TaskScheduler` constructor accepts the following parameters:

- `api_base_url` (str): The base URL for the API.
- `token` (str): The token for authentication.

The `schedule_task` method accepts the following `task` dict:

- `endpoint` (str): The specific endpoint of the API to hit.
- `method` (str): The HTTP method to use (e.g., "GET", "POST", etc.)
- `data` (dict): The data to send along with the request.
- `interval` (int): The interval (in seconds) at which the task should be run.

<a name="expected-outputs"></a>
## 4. Expected Outputs

The `TaskScheduler` logs its activities, so you can monitor its behavior. Here's an example of what you might see in your logs:

```
2022-01-01 00:00:00,000 - TaskScheduler - INFO - Task scheduled: {'endpoint': '/endpoint', 'method': 'POST', 'data': {'key': 'value'}, 'interval': 10}
2022-01-01 00:00:10,000 - TaskScheduler - INFO - Task executed: {'endpoint': '/endpoint', 'method': 'POST', 'data': {'key': 'value'}, 'interval': 10}
```

<a name="advanced-usage"></a>
## 5. Advanced Usage

If you need to use the `TaskScheduler` in more complex scenarios, you can extend it with your own functionality. For example, you might want to add a `retry` parameter to the `schedule_task` method to automatically retry failed tasks:

```python
class AdvancedTaskScheduler(TaskScheduler):
    def schedule_task(self, task: Dict[str, Any], retry: int = 0):
        super().schedule_task(task)
        # Add code here to handle retries
```
This would allow you to handle temporary network failures or API downtime without losing tasks.

# TaskScheduler Class Documentation

The `TaskScheduler` is a Python-based task scheduler that automates routine enterprise jobs, with logging and retry capabilities. This class is initialized with the base URL for the API and the token for authentication.

## Class Initialization

The `TaskScheduler` class is initialized as follows:

```python
task_scheduler = TaskScheduler(api_base_url, token)
```

| Parameter | Type | Description |
| ----------- | ------ | --------------- |
| `api_base_url` | str | The base URL for the API. |
| `token` | str | The token for authentication. |

## Class Attributes

| Attribute | Type | Description |
| ----------- | ------ | --------------- |
| `api_base_url` | str | The base URL for the API. This is a read-only attribute. |
| `token` | str | The token for authentication. This is a read-only attribute. |
| `headers` | dict | The HTTP headers to be used in the API requests. This is a read-only attribute. |
| `logger` | logging.Logger | A logger instance used for logging messages. This is a read-only attribute. |

## Methods

### `schedule_task(task: Dict) -> None:`

This method is used to schedule a task.

```python
task_scheduler.schedule_task(task)
```

**Parameters**

| Parameter | Type | Description |
| ----------- | ------ | --------------- |
| `task` | Dict | The task to be scheduled. |

**Return Value**

This method does not return a value.

**Example**

```python
task = {
    'name': 'Task 1',
    'interval': 10,  # in seconds
    'url': 'http://example.com/api/task1',
    'method': 'GET',
    'data': {}  # request data in case of POST method
}
task_scheduler.schedule_task(task)
```

## Logging

The `TaskScheduler` class uses Python's built-in logging module to log messages. By default, the log level is set to `INFO`, and the log messages are written to the standard output.

The format of the log messages is as follows: `%(asctime)s - %(name)s - %(levelname)s - %(message)s`.

**Example**

```
2022-01-01 00:00:00,000 - __main__ - INFO - Task 'Task 1' scheduled to run every 10 seconds.
```

## Best Practices

1. When scheduling tasks, ensure that the interval is not set too low to prevent overloading the server.
2. Use a unique name for each task for better log readability.
3. Handle exceptions in the tasks to prevent the scheduler from stopping due to unhandled errors.
4. Rotate the log files regularly to prevent them from growing indefinitely.

## ⚙️ Configuration
Configuration options for customizing the application's behavior.

## 🔍 Troubleshooting
Common issues and their solutions.

## 🤝 Contributing
Guidelines for contributing to the project.

## 📄 License
This project is licensed under the MIT License.

## API Documentation

### Endpoints

#### `GET /api/resource`

Returns a list of resources.

**Parameters:**

- `limit` (optional): Maximum number of resources to return

**Response:**

```json
{
  "resources": [
    {
      "id": 1,
      "name": "Resource 1"
    }
  ]
}
```
