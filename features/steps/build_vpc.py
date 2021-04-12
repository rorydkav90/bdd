from modules.terraform_module import TerraformModule

directory = "test_module"
variables = {}
tf = TerraformModule(directory, variables)

@given('the {directory} module')
def step_impl(context, directory):
    assert directory != ""

@given('I am an AWS developer')
def step_impl(context):
    tf.init()

@when('the config is correct')
def step_impl(context):
    tf.plan()

@then('build the {directory}')
def step_impl(context, directory):
    tf.apply()