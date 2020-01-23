from locust import HttpLocust, TaskSet, task, between

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post("/login", {"username":"dries", "password":"kaka"})

    def logout(self):
        self.client.get("/logout")

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def profile(self):
        self.client.get("/cats")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5, 9)