from abc import ABC, abstractmethod

class WorkflowBuilder:
    def __init__(self):
        pass

    def trigger(self, condition_fn): 
        if condition_fn: 
            pass
        return self

    def action(self):
        return self
    
    def condition(self):
        return self

    def subscribe(self):
        return self

class WorkflowHost:

    def __init__(self):
        self.workflow_dict = dict()
        self.builder = WorkflowBuilder()

    def register_workflow(self, workflow):
        self.workflow_dict[workflow.id] = workflow
    
    def start_workflow(self, workflow_id):
        try:
            workflow = self.workflow_dict.get(workflow_id)
        except KeyError:
            print("This workflow does not exist")
        built_workflow = workflow.build(self.builder)
        built_workflow.run()

    def start():
        pass

    def stop(self):
        pass

class Workflow:
    def __init__(self):
        pass

    @property
    def id():
        pass

    def build(self, builder):
        pass


class Node():
    def run():
        pass


def create_workflow_definition():
    return Workflow()