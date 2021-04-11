from modules.docker_module import Docker

client = Docker()

def get_container_path(directory):
    CONTAINER_PATH = ""
    if directory == "lift_app":
        CONTAINER_PATH = "test_path"
    return CONTAINER_PATH

@given('the {directory} dockerfile')
def step_impl(context, directory):
    assert directory != ""

@given('I am a developer')
def step_impl(context):
    login = client.login()

@when('I build the {directory} docker image')
def step_impl(context, directory):
    container_path = get_container_path(directory)
    image = client.build_image(container_path, directory)

@then('push the {directory} image to dockerhub with tag {tag}')
def step_impl(context, directory, tag):
    pushed_image = client.push_image(directory, tag)