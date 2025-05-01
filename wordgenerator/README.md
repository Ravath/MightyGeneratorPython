
The generators are composed of different nodes implementing various behaviors.

![WordGenerator Class Diagram](/wordgenerator/uml.jpg "Tables Structure.")

### Collections

- **Weight Node** : Each row has a ponderated chance to be rolled.
  - Default row ponderation = 1.
  - This table type garanties to draw a row.
  - Default row format : `[pond, value]`
- **Interval Node** : Each row has an interval of values. The table must be configured with a specific roll.
  - This table type can draw no rows or multiple rows depending on configuration.
  - Functionally, it is the Node with the most polyvalence, and others, like Weight Node, can be considered more specialized variations of the interval Node.
  - Default row format : `[minThreshold, maxThreshold, value]`
- **Sequence Node** : Each row of the table will be drawn sequentially.
  - Default row format : __`value`__
- **Tab Node** : Returns the row at the given index, generaly a variable red by a lambda or a ListValue.
    On the contrary of a Weight node, interesting when randomisation is not the purpose.
- **Dictionary Node** : Get children in a dictionary structure, and returns the node associated with the 
    picked key. Key is red in a given variable or text buffer.
- **Automaton Node** : Use TabNode.Automaton to create an automaton.
    They just pop the first child in the list each time they are called.
    Loops back to the beginning of the list when arrives at the end.

### Leafs
- Action Node : Executes a given function on execution
- Set Node : Set a variable with a given value.
- Print Node : Default node, prints a given text.
  - Title : automatic __Title__ formating.
  - Label : automatic __Label : Text__ formatting.
- By default. the generated output is stacked in a variable buffer named "DEFAULT".
  The generated text can then be accessed with `generation.raw_text`
  - SwitchVar Node : Changes the used buffer. If a buffer with the given name does not exist, it is created.
  - SetVar Node : Sets a value to a buffer whitout changing the used buffer. Erases previous value if any, and creates a buffer if didn't existed.
  - Context Node : Changes context, and executes children in order to set the buffer.
    At the end, reset back to previous context, after applying format and macro. 
  - Define Node : A Context Node that executes only if the target buffer is not already defined.
    If the buffer is already set, does nothing. Usefull for managing variables that may be passed as arguments in input of the generation.
  - Format Node : Execute the format on the target buffer.
    If no target buffer provided, uses the current buffer.
    If no format provided, uses the target as input.
  - Macro Node : Execute the macros on the target buffer.
    If no target buffer provided, uses the current buffer.
    If no macro provided, uses the target as input.

### Utilities
 - using the `<<` operator on a table enables to extend the table with new rows.
 - Giving a text to a row value will be automatically interpreted as a PrintNode.
 - Giving a lamda or a function to a row value will be automatically interpreted as a ActionNode.
 - The number of rolls can be specified for every tables.
   - Default 1.
 - The maximum number of times a row can be drawn can be specified.
   - Default -1 for an infinite number of times.
