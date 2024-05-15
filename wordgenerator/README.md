
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
- **Tab Node** : Returns the row at the given index, generaly a variable red by a lambda.

### Leafs
- Action Node : Executes a given function on execution
- Set Node : Set a variable with a given value.
- Print Node : Default node, prints a given text.
  - Title : automatic __Title__ formating.
  - Label : automatic __Label : Text__ formatting.
  - By default. the generated output is printed to the console, but by setting `PrintNode.print_to_buffer()`, it can be used as a normal string without using the console. The generated text can then be accessed with `generation.text` 

### Utilities
 - using the `<<` operator on a table enables to extend the table with new rows.
 - Giving a text to a row value will be automatically interpreted as a PrintNode.
 - Giving a lamda or a function to a row value will be automatically interpreted as a ActionNode.
 - The number of rolls can be specified for every tables.
   - Default 1.
 - The maximum number of times a row can be drawn can be specified.
   - Default -1 for an infinite number of times.
