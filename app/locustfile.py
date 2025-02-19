
from locust import HttpUser, between, task, TaskSet


def index(l):
    l.client.get("/")

class UserTasks(TaskSet):
    tasks = [index,]

class WebsiteUser(HttpUser):

    host = "http://localhost"
    wait_time = between(2, 5)
    tasks = [UserTasks]
    
    # def on_start(self):
    #     self.client.post("/login", {
    #         "username": "test_user",
    #         "password": ""
    #     })
    
    @task
    def index(self):
        self.client.get("/")
        
