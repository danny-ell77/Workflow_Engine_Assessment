class WorkflowBuilder:
    def __init__(self):
        self._workspace = Workflow()
        self.event_dict = dict()

    def trigger(self, event_type, subscribers): 
        self.event_dict[event_type] = subscribers
        return self

    def action(self, node_class):
        self._workspace.add_step(node_class())
        return self
    
    def condition(self):
        return self


class WorkflowHost:

    def __init__(self):
        self.workflow_dict = dict()
        self._builder = WorkflowBuilder()

    def register_workflow(self, workflow):
        self.workflow_dict[workflow.id] = workflow
    
    def start_workflow(self, workflow_id):
        try:
            workflow = self.workflow_dict.get(workflow_id)
        except KeyError:
            print("This workflow does not exist")
        return workflow.build(self._builder)

    def run(self):
        pass

    def publish_event(self, event_type):
        """Equivalent to `run` but is only used for event triggers"""
        subscriber_nodes = self._builder.event_dict.get(event_type, None)

        # async?
        if subscriber_nodes and len(subscriber_nodes) > 0:
            # if the number of nodes subscribed to this event
            # is greater than one, you might have to consider running them
            #  asynchrously(at the same time) in multiple threads.
            for node in subscriber_nodes:
                # the context points to the next code to run
                node.run(context = node)

    def start():
        pass

    def stop(self):
        pass

class Workflow:
    def __init__(self):
        self.steps = []

    @property
    def id():
        pass

    def build(self, builder):
        pass

    def add_step(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = node


class Node():
    def __init__(self) -> None:
        self.next = None

    def run():
        pass


def create_workflow_definition():
    return Workflow()