Components of workflow engine:
1. Wporkflow Definition
2. Task Queue
3. Timers ---> for timeouts
4. State ---> for Persistence

Elements of the workflow instance
1. Trigger
2. Action
3. Conditions

Use the Builder Pattern to create the workflow Definition
and the observer pattern to model how the nodes of the workflow interact 
during execution. 

create an API for non programmers to access features and create a 
simple abstraction over the engine#   W o r k f l o w _ E n g i n e _ A s s e s s m e n t  
 