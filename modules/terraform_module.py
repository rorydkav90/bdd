from python_terraform import Terraform

class TerraformModule():

    def __init__(self, directory, variables):
        self.directory = directory
        self.variables = variables
        self.tf = Terraform(working_dir=self.directory, variables=self.variables)

    def init(self):
        return self.tf.init()

    def plan(self):
        return self.tf.plan(capture_output=True)

    def apply(self, auto_approval=True):
        return self.tf.apply({"auto-approve":auto_approval})

    def delete(self):
        return self.tf.delete(capture_output=True)