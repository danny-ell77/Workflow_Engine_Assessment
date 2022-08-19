from main import * 

class LogEventAction(Node):
    def run(self, context):
        print("User signed Up!")
        return context.run()


class EmailAction(Node):
    def run(self, context):
        print("Sending Email...")
        return context.run()


class MyWorkflow(Workflow):

    @property
    def id(self):
        return "MyWorkflow"

    def build(self, builder):
        builder\
            .trigger("signup", subscribers=[
                builder.action(EmailAction),
            ]) \
            .action(LogEventAction)



host = create_workflow_definition()
host.register_workflow(MyWorkflow())
# host.start()

wid = host.start_workflow("MyWorkflow")
host.publish_event('signup')
# host.stop()