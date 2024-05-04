# MightyGeneratorPython
MightyGm Text generator in python


Generates some text by rolling random results from roll tables.

# Project Structure
## Generators

Some generation implementations.

## GUI

A GUI manipulation of the Borderloot generation.
Intended for Android using Kivy (In progress).

## Macro

Implementation of dice rolling macros using yacc and ply.

Includes:
- Rolling dice capacities
- Mathematical operations

### Dice Macros

#### The initialisation operators create a pool of numbers
 - x __`:`__ y : returns a number between x and y.
 - x __`d`__ y : rolls x dice of y faces, returning x numbers between 1 and y.

#### The filter operators compare every number with a thresold
 - __`h`__ z : keeps the z higher numbers.
 - __`l`__ z : keeps the z lower numbers.
 - __`<`__ z : keeps the numbers higher than z.
 - __`>`__ z : keeps the numbers lower than z.

#### The reroll operators reroll the numbers exceding the threshold
 - __`e`__ : Explosive Dice : reroll the dice with a result equal or higher than z and adds the result to the previous number.
 - __`a`__ : Compound Explosive Dice : Similar to Explosive Dice, except a new dice is added to the pool instead.
 - __`r`__ : Reroll Dice : reroll the dice for a new value.
- if z=-1 (default value) then the threshold value is the maximum value of the dice.
- if uppercase (`E`,`A`,`R`), then the operation will reiterate as long as the newer results meet the threshold criteria.
- if followed by `<`, then the operation will use a lower threshold instead of a higher threshold.
- if followed by `>`, then will not have no particular effect. It is just a explicitation of the default behavior.

#### the suffixes indicate how to interpret the remaining pool
 - _`<Nothing>`_ : computes the sum by default
 - __`c`__ : returns the number of results

#### Exemple

3d6>4c : the number of dice from a 3d6 pool with a result greater than 4.

## Test

Some testing of the library.

## Utils

Some miscellaneous modules.
- Some debug tools.
- Some usage examples.

## WordGenerator

![WordGenerator Class Diagram](/wordgenerator/uml.jpg "Tables Structure.")

### Collections

- **Weight Node** : Each row has a ponderated chance to be rolled.
  - Default row ponderation = 1.
  - This table type garanties to draw a row.
  - Default row format : `[pond, value]`
- **Interval Node** : Each row has an interval of values. The table must be configured with a specific roll.
  - This table type can draw no rows or multiple rows depending on configuration.
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

# How to Use

## Outline

1) Create the tables using the structures from the WordGenerator Module.
2) Assemble the tables
3) Use the Generator class to conclude and generate

>```
generation = Generator(root)
generation.execute()
generation.print_to_console()

## Generation order
 - Rolls the tables starting from root.
 - Use the `{VAR_NAME}` syntaxe to include variable results in the generations.
 - Use the `[[1d6]]` syntaxe to roll dice and apply computations macros.
