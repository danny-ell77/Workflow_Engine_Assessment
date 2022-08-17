from main import * 

class Page(Node):
    def run(self, context):
        print("User signed Up!")
        return context.next()


class EmailAction(Node):
    def run(self, context):
        print("Sending Email...")
        return context.next()


class MyWorkflow(Workflow):

    @property
    def id(self):
        return "MyWorkflow"

    def build(self, builder):
        builder\
            .add_trigger("SignUp") \
            .subscribe(EmailAction)

def sign_up_user():
    print("Signing up user...")
    
    pass

host = create_workflow_definition()
host.register_workflow(MyWorkflow())
# host.start()

wid = host.start_workflow("MyWorkflow")

sign_up_user()
# host.stop()