import docker
from getpass import getpass

class Docker():

    def __init__(self):
        self.client = docker.from_env()
        self.username = getpass('Username:')
        self.password = getpass('Password:')

    def login(self):
        return self.client.login(username=self.username, password=self.password)

    def build_image(self, container_path, image_name):
        return self.client.images.build(path=container_path, tag=image_name)

    def push_image(self, image_name, tag):
        container_image = self.client.images.get(image_name)
        repository = "{}/{}".format(self.username, image_name)
        container_image.tag(repository, tag=tag)
        return self.client.images.push(repository)
        