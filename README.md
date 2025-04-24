# MightyGeneratorPython
MightyGm Text generator in python


Generates some text by rolling random results from roll tables.

# Project Structure
## Generators

Some generation implementations.

## GUI
Intended for Android using Kivy (In progress).

### Borderloot
A GUI manipulation of the Borderloot generation.
### Catalog
A GUI for accessing every implemented generations and executing them.
 - Uses only files prefixed 'gen_'.
 - A generator named 'generation' must be initialized.

## Macro

Implementation of dice rolling macros using yacc and ply.

Includes:
- Rolling dice capacities
- Mathematical operations

### Dice Macros

#### The initialisation operators create a pool of numbers
 - x __`:`__ y : returns a number between x and y.
 - x __`d`__ y : rolls x dice of y faces, returning x numbers between 1 and y.

#### The filter operators compare every number with a threshold
 - __`h`__ z : keeps the z higher numbers.
 - __`l`__ z : keeps the z lower numbers.
 - __`<`__ z : keeps the numbers higher than z.
 - __`>`__ z : keeps the numbers lower than z.

#### The reroll operators reroll the numbers exceding the threshold
 - __`e`__ z : Explosive Dice : reroll the dice with a result equal or higher than z and adds the result to the previous number.
 - __`a`__ z : Compound Explosive Dice : Similar to Explosive Dice, except a new dice is added to the pool instead.
 - __`r`__ z : Reroll Dice : reroll the dice for a new value.
- if z=-1 (default value) then the threshold value is the maximum value of the dice.
- if uppercase (`E`,`A`,`R`), then the operation will reiterate as long as the newer results meet the threshold criteria.
- if followed by `<`, then the operation will use a lower threshold instead of a higher threshold.
- if followed by `>`, then will not have no particular effect. It is just a explicitation of the default behavior.

#### the suffixes indicate how to interpret the remaining pool
 - _`<Nothing>`_ : computes the sum by default
 - __`c`__ : returns the number of results

#### Exemples

3d6>4c : the number of dice from a 3d6 pool with a result greater or equal than 4.
- [1,4,6] => 2
- [1,3,2] => 0

5d10e9 : Rolls 5d10, and then explodes every result greater or equal to 9 and computes the sum.
- [1,8,9,4,10] => [1,8,(9+5),4,(10+9)] => 46

3d4Ac : Rolls 3d4, and then rolls a new dice for every result greater or equal than 4 (default value), repeats until done, and then counts the number of dice.
- [1,4,4] => [1,4,3,4,4] => [1,4,3,4,4,2] => 6

3d10r<1 : Rolls 3d10, and then rerolls every result smaller or equal to 1 and computes the sum.
- [1,8,9] => [6,8,9] => 23

## Test

Some testing of the library.

## Utils

Some miscellaneous modules.
- Some debug tools.
- Some usage examples.

## WordGenerator

[WordGenerator Readme](wordgenerator/README.md)

# How to Use

## Outline

1) Create the tables using the structures from the WordGenerator Module.
2) Assemble the tables
3) Use the Generator class to conclude and generate

```
# exemple from generators/pathfinder/gen_loot_faible.py
from wordgenerator.Weight import WeightNode as Weight

...

# create arborescence
root = Weight() << [
    [ 4, Title("Armure", obj_bouclier_armure)],
    [ 5, Title("Arme", obj_cac_dist)],
    [35, Title("Potion", obj_potion)],
    [ 2, Title("Anneau", obj_anneaux)],
    [35, Title("Parchemin", obj_parchemin)],
    [10, Title("Baguette", obj_baguette)],
    [ 9, Title("Objet Merveilleux", obj_merveilleux)],
]

generation = Generator(root)    # Give the root node to the generator
result = generation.execute()   # Generate a random result
result.print_to_console()       # print the generated result to the console
```

## Generation order
 - Rolls the tables starting from root.
 - Use the `{VAR_NAME}` syntaxe to include variable results in the generations.
 - Use the `[[1d6]]` syntaxe to roll dice and apply computations macros.
