import csv
import json
import logging
import requests
import schedule
import time
from typing import Dict, Any

class TaskScheduler:
    """
    A Python-based task scheduler that automates routine enterprise jobs, with logging and retry capabilities.
    """

    def __init__(self, api_base_url: str, token: str):
        """
        Initialize the TaskScheduler with the base URL for the API and the token for authentication.

        :param api_base_url: The base URL for the API.
        :param token: The token for authentication.
        """
        self.api_base_url = api_base_url
        self.token = token
        self.headers = {'Authorization': f'Bearer {self.token}'}
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def schedule_task(self, task: Dict[str, Any], interval: int):
        """
        Schedule a task to be run at a specified interval.

        :param task: The task to be scheduled.
        :param interval: The interval at which the task should be run.
        """
        schedule.every(interval).seconds.do(self.execute_task, task)

    def execute_task(self, task: Dict[str, Any]):
        """
        Execute a task.

        :param task: The task to be executed.
        """
        try:
            response = requests.post(f'{self.api_base_url}/tasks', headers=self.headers, json=task)
            response.raise_for_status()
            self.logger.info(f'Task {task["id"]} executed successfully.')
        except Exception as e:
            self.logger.error(f'Error executing task {task["id"]}: {e}')
            self.retry_task(task)

    def retry_task(self, task: Dict[str, Any], retries: int = 3):
        """
        Retry a failed task a specified number of times.

        :param task: The task to be retried.
        :param retries: The number of times to retry the task.
        """
        for i in range(retries):
            try:
                response = requests.post(f'{self.api_base_url}/tasks', headers=self.headers, json=task)
                response.raise_for_status()
                self.logger.info(f'Task {task["id"]} executed successfully on retry {i+1}.')
                return
            except Exception as e:
                self.logger.error(f'Error executing task {task["id"]} on retry {i+1}: {e}')
        self.logger.error(f'Task {task["id"]} failed after {retries} retries.')
        self.send_notification(task)

    def send_notification(self, task: Dict[str, Any]):
        """
        Send a notification for a failed task.

        :param task: The task that failed.
        """
        notification = {'task_id': task['id'], 'message': f'Task {task["id"]} failed.'}
        try:
            response = requests.post(f'{self.api_base_url}/notifications', headers=self.headers, json=notification)
            response.raise_for_status()
            self.logger.info(f'Notification for task {task["id"]} sent successfully.')
        except Exception as e:
            self.logger.error(f'Error sending notification for task {task["id"]}: {e}')

    def manage_users(self, users_file: str):
        """
        Manage users based on a CSV file.

        :param users_file: The CSV file containing user details.
        """
        with open(users_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    response = requests.post(f'{self.api_base_url}/users', headers=self.headers, json=row)
                    response.raise_for_status()
                    self.logger.info(f'User {row["id"]} managed successfully.')
                except Exception as e:
                    self.logger.error(f'Error managing user {row["id"]}: {e}')

    def run(self):
        """
        Run the task scheduler.
        """
        while True:
            schedule.run_pending()
            time.sleep(1)

# Example usage
scheduler = TaskScheduler('http://api.example.com', 'your_token_here')
scheduler.schedule_task({'id': 'task1', 'action': 'do_something'}, 10)
scheduler.manage_users('users.csv')
scheduler.run()