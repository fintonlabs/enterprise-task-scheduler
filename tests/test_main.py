import unittest
from unittest.mock import patch, Mock
from main import TaskScheduler

class TestTaskScheduler(unittest.TestCase):

    @patch('requests.post')
    def test_execute_task(self, mock_post):
        mock_post.return_value.raise_for_status.return_value = None
        scheduler = TaskScheduler('http://api.example.com', 'your_token_here')
        task = {'id': 'task1', 'action': 'do_something'}
        scheduler.execute_task(task)
        mock_post.assert_called_once_with('http://api.example.com/tasks', headers=scheduler.headers, json=task)

    @patch('requests.post')
    def test_retry_task(self, mock_post):
        mock_post.return_value.raise_for_status.side_effect = [Exception, None]
        scheduler = TaskScheduler('http://api.example.com', 'your_token_here')
        task = {'id': 'task1', 'action': 'do_something'}
        scheduler.retry_task(task)
        self.assertEqual(mock_post.call_count, 2)

if __name__ == '__main__':
    unittest.main()