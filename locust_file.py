from locust import HttpLocust, TaskSet, between, task


class UserBehavior(TaskSet):
    @task(1)
    def get_calls(self):
        self.client.get('/api/calls')

    @task(1)
    def add_call(self):
        payload = {
            "duration": 123,
            "worker_id": 1,
            "user_id": 1,
            "status": "accepted"
        }
        self.client.post('/api/calls', json=payload)

    @task(2)
    def get_user(self):
        self.client.get('/api/users/1')

    @task(2)
    def get_worker(self):
        self.client.get('/api/workers/1')

    @task(2)
    def get_call(self):
        self.client.get('/api/calls/1')

    @task(2)
    def get_users(self):
        self.client.get('/api/users')

    @task(1)
    def add_user(self):
        payload = {
            "first_name": "rem",
            "last_name": "unicorn",
            "email": "rem_unicorn@gmail.com",
            "phone_number": "+380987412874",
            "address": "neverland"
        }
        self.client.post('/api/users', json=payload)

    @task(1)
    def add_worker(self):
        payload = {
            "first_name": "rem",
            "last_name": "unicorn",
            "email": "rem_unicorn@gmail.com",
            "phone_number": "+380987412874",
            "address": "neverland",
            "password": "password"
        }
        self.client.post('/api/workers', json=payload)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1.0, 2.0)
