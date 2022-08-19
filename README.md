A dummy program that demostrates the key elements of a workflow engine

### Components of workflow engine:

- Workflow Definition
- Task Queue
- Timers ---> for timeouts
- State ---> for Persistence

### Elements of the workflow instance

- Trigger
- Action
- Conditions

### Implementation

Use the Builder Pattern to create the workflow Definition
and the observer pattern to model how the nodes of the workflow interact
during execution.

<!-- The workflow interface would define
create an API for non programmers to access features and create a
simple abstraction over the engine -->

The trigger serves as the first node that sets up the automation, every action Node that subscribes to it is triggered(RUN). This workflow is completely stateless to ensure simplicity.

The simple ds for the Workflow should be a linked list, then move on to a graph or binary tree?
