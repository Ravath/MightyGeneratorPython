# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 14:15:22 2022

@author: Ehlion

| Module for the different dice operators.

"""

import random
from macro.calc import ValueIf

def roll_dice(faces:int = 6) :
    """Get the result of a dice roll."""
    return random.randint(1, faces)

#___________________________________________________#
#                                                   #
#                  Rand Interface                   #
#___________________________________________________#

class RandIf:
    """Interface of a random object."""
    def roll(self) -> int :
        """Roll the random."""
        raise NotImplementedError(f"In class {type(self).__name__}")
    def get_result(self) -> int :
        """Get result of the last roll."""
        raise NotImplementedError(f"In class {type(self).__name__}")

class Dice(RandIf, ValueIf) :
    """A random value drawn from a die."""
    def __init__(self, face:int = 6) :
        self.face = face
        self.last_result = 0
        self.net_result = 0
        self.discarded = False
    def roll(self) -> int :
        """Roll the die. Replace the previous results."""
        self.last_result = roll_dice(self.face)
        self.net_result = self.last_result
        return self.last_result
    def cumulate(self) -> int :
        """Roll the die, but sum the new result with the previous ones."""
        self.last_result = roll_dice(self.face)
        self.net_result += self.last_result
        return self.last_result
    def discard(self) :
        """The die will not be counted in the pool results."""
        self.discarded = True
    def get_result(self) -> int :
        """Get the sum result of this die."""
        return self.net_result
    def get_value(self) -> int :
        return self.roll()
    value = property(get_value)

    def copy(self) :
        return Dice(self.face)

class Interval(RandIf, ValueIf) :
    """A random value drawn within a given range (inclusive)."""
    def __init__(self, vmin:int = 1, vmax:int = 6) :
        self.min = vmin
        self.max = vmax
        self.net_result = 0
    def roll(self) -> int :
        """Get a random value within the range"""
        if self.min > self.max :
            self.min, self.max = self.max, self.min
        self.net_result = random.randint(self.min, self.max)
        return self.net_result
    def get_result(self) -> int :
        """Get the random result."""
        return self.net_result
    def get_value(self) -> int :
        return self.roll()
    value = property(get_value)

    def __str__(self) -> str :
        return f"{self.min}:{self.max}"

#___________________________________________________#
#                                                   #
#                   Pool & PoolIf                   #
#___________________________________________________#

class PoolIf:
    """Interface for a pool of dice
    with a specific roll mechanic."""

    def roll(self) -> list :
        """
        Operate a roll operation on the pool.

        Raises
        ------
        NotImplementedError
            The method must be implemented by children.

        Returns
        -------
        list Dice[]
            The rolled dice.
        """
        raise NotImplementedError(f"In class {type(self).__name__}")
    def get_results(self) -> list :
        """Get the result of the roll.

        Raises
        ------
        NotImplementedError
            The method must be implemented by children.

        Returns
        -------
        list Dice[]
            The results of the roll.
        """
        raise NotImplementedError(f"In class {type(self).__name__}")

class Pool(PoolIf) :
    """A pool of dice."""
    def __init__(self, nbr_dice:int = 1, nbr_face:int = 6) :
        self.children = [] # Dice[]
        self.add_dice(nbr_dice, nbr_face)
        self.results = None

    def add_dice(self, nbr_dice:int = 1, nbr_face:int = 6) :
        """Add a die to the pool"""
        for _ in range(0, nbr_dice) :
            self.children.append(Dice(nbr_face))

    def roll(self) -> list:
        """Roll the dice.

        Returns
        -------
        list Dice[]
            The results of the roll.
        """
        self.results = list() # Dice[]
        for die in self.children :
            rolled_die = die.copy()
            rolled_die.roll()
            rolled_die.discarded = False
            self.results.append(rolled_die)
        return self.results

    def get_results(self) -> list :
        """Get the result of the roll.

        Returns
        -------
        list Dice[]
            The results of the roll.

        """
        return self.results

    def __str__(self) -> str :
        faces = dict()

        # count de number of each dice size
        for die in self.children :
            if not die.face in faces.keys() :
                faces[die.face] = 1
            else :
                faces[die.face] += 1

        if len(faces) == 1 :
            nf, nd = faces.popitem()
            return f"{nd}d{nf}"
        else :
            rep = "{"
            for nf, nd in faces :
                rep += f"{nd}d{nf}+"
            rep[-1] = '}'
            return rep

#___________________________________________________#
#                                                   #
#                  Pool decorators                  #
#___________________________________________________#

def test_match(pool, die:Dice) :
    """
    Test the dice for the given pool threshold filter.

    Parameters
    ----------
    rp : Filtering pool
        The pool filtering the die.
        Must be using 'threshold' and 'higher' criteria.
    d : Dice
        Die to filter.

    Returns
    -------
    Bool
        True if the die is to be kept.

    """

    if pool.threshold == -1 :
        return die.last_result == die.face
    return ((pool.higher and die.last_result >= pool.threshold) or
            (not pool.higher and die.last_result <= pool.threshold))

def op_to_str(operator, op_id) -> str :
        op = op_id
        if operator.infinite : op = op_id.upper()
        t_op = ">"
        if not operator.higher : t_op = "<"
        if operator.threshold != -1 : t_op += str(operator.threshold)
        return str(operator.pool) + op + t_op

class ReRoll(PoolIf) :
    """Reroll every die over the given threshold."""
    def __init__(self, pool:PoolIf, threshold:int = -1,
                 higher:bool = True, infinite:bool = False) :
        """Initialize a reroll operation of the given pool.

        Parameters
        ----------
        pool : PoolIf
            Pool to reroll.
        threshold : int, optional
            Threshold (inclusive) to compare the dice to.
            If -1, the die is rerolled only if it has the maximum result.
            The default is -1.
        higher : bool, optional
            False for a lower threshold.
            The default is True.
        """
        self.pool = pool
        self.threshold = threshold
        self.higher = higher
        self.infinite = infinite

    def roll(self) -> list:
        self.pool.roll()

        for die in self.get_results() :
            do_test = not die.discarded

            while do_test :
                if test_match(self, die) :
                    die.roll()
                    do_test = self.infinite
                else :
                    do_test = False

        return self.get_results()

    def get_results(self) -> list :
        return self.pool.get_results()

    def __str__(self) -> str :
        return op_to_str(self, 'r')

class Explode(PoolIf) :
    """Reroll and cumul the new result."""
    def __init__(self, pool:PoolIf, threshold:int = -1,
                 higher:bool = True, infinite:bool = True) :
        """Initialize an explode operation of the given pool.

        Parameters
        ----------
        pool : PoolIf
            Pool to explode.
        threshold : int, optional
            Threshold (inclusive) to compare the dice to.
            If -1, the die is exploded only if it has the maximum result.
            The default is -1.
        higher : bool, optional
            False for a lower threshold.
            The default is True.
        """
        self.pool = pool
        self.threshold = threshold
        self.higher = higher
        self.infinite = infinite

    def roll(self) -> list:
        self.pool.roll()
        for die in self.get_results() :
            test_reroll = not die.discarded

            while test_reroll :
                if test_match(self, die) :
                    die.cumulate()
                    test_reroll = self.infinite
                else :
                    test_reroll = False

        return self.get_results()

    def get_results(self) -> list :
        return self.pool.get_results()

    def __str__(self) -> str :
        return op_to_str(self, 'e')

class CompoundExplode(PoolIf) :
    """Roll a new die for every result over the given threshold."""
    def __init__(self, pool:PoolIf, threshold:int = -1,
                 higher:bool = True, infinite:bool = False) :
        """Initialize a Compouding Explosion operation of the given pool.

        Parameters
        ----------
        pool : PoolIf
            Pool to reroll.
        threshold : int, optional
            Threshold (inclusive) to compare the dice to.
            If -1, the die is rerolled only if it has the maximum result.
            The default is -1.
        higher : bool, optional
            False for a lower threshold.
            The default is True.
        """
        self.pool = pool
        self.threshold = threshold
        self.higher = higher
        self.infinite = infinite

    def roll(self) -> list:
        self.pool.roll()

        to_roll = self.get_results()
        to_roll_next = []
        do_test = True

        while do_test :

            # Do rerolls
            for die in to_roll :
                if (not die.discarded and
                    test_match(self, die)) :
    
                    reroll = die.copy()
                    reroll.roll()
                    to_roll_next.append(reroll)

            # add new dice and prepare next iteration
            self.get_results().extend(to_roll_next)
            to_roll = to_roll_next
            to_roll_next = []

            # check if new iteration is needed
            do_test = (self.infinite and
                       len(to_roll) > 0)

        return self.get_results()

    def get_results(self) -> list :
        return self.pool.get_results()

    def __str__(self) -> str :
        return op_to_str(self, 'a')

class FilterDiceValue(PoolIf) :
    """Discard the dice of the pool
    if they can't meet the given threshold."""

    def __init__(self, pool:PoolIf, threshold:int = -1, higher:bool = True) :
        """Initialize an Dice Filter operation on the given pool.

        Parameters
        ----------
        pool : PoolIf
            Pool to explode.
        threshold : int, optional
            Threshold (inclusive) to compare the dice to.
            If -1, the die is keot only if it has the maximum result.
            The default is -1.
        higher : bool, optional
            False for a lower threshold.
            The default is True.
        """
        self.pool = pool
        self.threshold = threshold
        self.higher = higher

    def roll(self) -> list:
        self.pool.roll()

        for die in self.get_results() :

            if not test_match(self, die) :
                die.discard()

        return self.get_results()

    def get_results(self) -> list :
        return self.pool.get_results()

    def __str__(self) -> str :
        op = ">"
        if not self.higher : op = "<"
        if self.threshold != -1 : op += str(self.threshold)
        return str(self.pool) + op

class FilterDiceCount(PoolIf) :
    """Keep only the given number of dice, higher of lower."""
    def __init__(self, pool:PoolIf, threshold:int, higher:bool = True) :
        """Initialize an Pool Filter operation on the given pool.

        Parameters
        ----------
        pool : PoolIf
            Pool to explode.
        threshold : int, optional
            The number of dice to keep.
        higher : bool, optional
            True : Keeps the higher dice results
            False: Keeps the lower dice results
            The default is True.
        """
        self.pool = pool
        self.threshold = threshold
        self.higher = higher

    def roll(self) -> list :
        self.pool.roll()

        # remove discarded dice and sort the remaining
        res = [(d.net_result, d) for d in self.get_results()
               if not d.discarded]
        res = sorted(res, key = lambda a : a[0])

        # Keep only the top/bottom
        discard_count = len(res) - self.threshold
        if discard_count > 0 :
            if self.higher :
                for die in res[:discard_count] :
                    die[1].discard()
            else :
                for die in res[-discard_count:] :
                    die[1].discard()

        return self.get_results()

    def get_results(self) -> list :
        return self.pool.get_results()

    def __str__(self) -> str :
        op = "h"
        if not self.higher : op = "l"
        if self.threshold != -1 : op += str(self.threshold)
        return str(self.pool) + op

class SwitchPool(PoolIf) :
    """Uses a different child pool depending of
    the given function return value."""
    def __init__(self, pools:list, int_func) :
        self.pools = pools
        self.int_func = int_func

    def roll(self) -> list:
        use = self.pools[self.int_func()]
        use.roll()
        return use.get_results()

    def get_results(self) -> list :
        use = self.pools[self.int_func()]
        return use.get_results()

#___________________________________________________#
#                                                   #
#                   Pool Results                    #
#___________________________________________________#

class PoolSum(ValueIf, PoolIf) :
    """Count the sum of the not discarded dice"""
    def __init__(self, pool:PoolIf) :
        ValueIf.__init__(self)
        self.pool = pool

    def get_value(self) -> int :
        """Roll and get the pool sum."""
        self.roll()
        return sum([d.get_result()
                    for d in self.pool.get_results()
                    if not d.discarded])

    def roll(self) -> list:
        self.pool.roll()
        return self.get_results()

    def get_results(self) -> list :
        return self.pool.get_results()

    value = property(get_value)

    def __str__(self) -> str :
        return str(self.pool)

class PoolCount(ValueIf, PoolIf) :
    """Count the number of the not discarded dice"""
    def __init__(self, pool:PoolIf) :
        ValueIf.__init__(self)
        self.pool = pool

    def get_value(self) -> int :
        """Roll and get the pool count."""
        self.roll()
        return len([d
                    for d in self.pool.get_results()
                    if not d.discarded])

    def roll(self) -> list:
        self.pool.roll()
        return self.get_results()

    def get_results(self) -> list :
        return self.pool.get_results()

    value = property(get_value)

    def __str__(self) -> str :
        return str(self.pool) + "c"

#___________________________________________________#
#                                                   #
#                      Testing                      #
#___________________________________________________#

if __name__ == "__main__" :
    from utils.debug import test, print_log

    # for test purpose, we stub the *ing not deterministic function
# pylint: disable-msg=E0102
    dice_results = []
    def roll_dice(faces:int) :
        """Stub of the random function for unit testing"""
        return ((dice_results.pop(0)-1) % faces)+1
# pylint: enable-msg=E0102

    def test_pool(tpool:PoolIf, results:list, discarded:list) :
        """Test the roll result of the given dicePool."""

        # Reset the pseudo-random stack
        dice_results.clear()
        dice_results.extend([1,2,3,4, 1,4,1,1,2,3])

        # Roll
        tpool.roll()

         # Sort and check the results
        res = [d.net_result for d in tpool.get_results()
               if not d.discarded]
        res2 = [d.net_result for d in tpool.get_results()
               if d.discarded]
        test(results, res)
        test(discarded, res2)

    print_log("START", "DICE UNITARY TESTING")

# Pool
    print_log("TEST", "Pool")
    p = Pool(0,4)
    test_pool(p, [], [])
    p = Pool(4,4)
    test_pool(p, [1,2,3,4], [])
    p = Pool(4,2)
    test_pool(p, [1,2,1,2], [])

# DiceFilter
    print_log("TEST", "DiceFilter - Default LIMIT")
    p = FilterDiceValue(Pool(4,4))
    test_pool(p, [4], [1,2,3])

    print_log("TEST", "DiceFilter - HIGHER LIMIT")
    p = FilterDiceValue(Pool(4,4), 3, True)
    test_pool(p, [3,4], [1,2])

    print_log("TEST", "DiceFilter - LOWER LIMIT")
    p = FilterDiceValue(Pool(4,4), 3, False)
    test_pool(p, [1,2, 3], [4])

# Explosion
    print_log("TEST", "Explosion - Default LIMIT - finite explosion")
    p = Explode(Pool(5,4), infinite = False)
    test_pool(p, [1,2,3,8,1], [])

    print_log("TEST", "Explosion - Default LIMIT - infinite explosion")
    p = Explode(Pool(5,4))
    test_pool(p, [1,2,3,9,1], [])

    print_log("TEST", "Explosion - HIGHER LIMIT - finite explosion")
    p = Explode(Pool(4,4), 3, infinite = False)
    test_pool(p, [1,2,4,8], [])

    print_log("TEST", "Explosion - HIGHER LIMIT - infinite explosion")
    p = Explode(Pool(4,4), 3)
    test_pool(p, [1,2,4,9], [])

    print_log("TEST", "Explosion - LOWER LIMIT - finite explosion")
    p = Explode(Pool(4,4), 1, False, False)
    test_pool(p, [2,2,3,4], [])

    print_log("TEST", "Explosion - LOWER LIMIT - infinite explosion")
    p = Explode(Pool(4,4), 1, False)
    test_pool(p, [6,2,3,4], [])

# Reroll
    print_log("TEST", "ReRoll - LOWER LIMIT - infinite reroll")
    p = ReRoll(Pool(4, 4), 2, False, True)
    test_pool(p, [4,3,3,4], [])

    print_log("TEST", "ReRoll - LOWER LIMIT - finite reroll")
    p.infinite = False
    test_pool(p, [1,4,3,4], [])

# PoolFilter
    print_log("TEST", "PoolFilter - LOWER LIMIT")
    p = FilterDiceCount(Pool(4,4), 3, False)
    test_pool(p, [1,2,3], [4])

    print_log("TEST", "PoolFilter - HIGHER LIMIT")
    p.higher = True
    test_pool(p, [2,3,4], [1])

    print_log("TEST", "PoolFilter - not enough dice")
    p = FilterDiceCount(Pool(0,4), 2, True)
    test_pool(p, [], [])
    p = FilterDiceCount(Pool(1,4), 2, True)
    test_pool(p, [1], [])
    p = FilterDiceCount(Pool(4,4), 5, False)
    test_pool(p, [1,2,3,4], [])

# SwitchPool
# pylint: disable-msg=C0103
    print_log("TEST", "SwitchPool")
    nbr_od_dice_to_use = 3
    def choose_number_of_dice() :
        """used by the SwitchPool for selecting a child pool"""
        return nbr_od_dice_to_use -1
    p = SwitchPool([
        Pool(1,4), Pool(2,4), Pool(3,4)],
        choose_number_of_dice)
    test_pool(p, [1,2,3], [])
    nbr_od_dice_to_use = 2
    test_pool(p, [1,2], [])
    nbr_od_dice_to_use = 1
    test_pool(p, [1], [])
    del nbr_od_dice_to_use
# pylint: enable-msg=C0103

# PoolSum & PoolCount
    def test_sum(pool, expected:int) :
        """Test the roll result of the given PoolResult."""
        # Reset the pseudo-random stack
        dice_results.clear()
        dice_results.extend([1,2,3,4])
        # Roll and test
        # pool.roll() done in get_value
        test(expected, pool.value)

    print_log("TEST", "PoolSum - Simple cases")
    p = PoolSum(Pool(4,4))
    test_sum(p, 10)

    print_log("TEST", "PoolSum - with disabled dice")
    p = PoolSum(FilterDiceValue(Pool(4,4), 3))
    test_sum(p, 7)
    p = PoolSum(FilterDiceValue(Pool(4,4), 2, False))
    test_sum(p, 3)

    print_log("TEST", "PoolCount - Simple cases")
    p = PoolCount(Pool(4,4))
    test_sum(p, 4)

    print_log("TEST", "PoolCount - with disabled dice")
    p = PoolCount(FilterDiceValue(Pool(4,4), 3))
    test_sum(p, 2)
    p = PoolCount(FilterDiceValue(Pool(4,4), 2, False))
    test_sum(p, 2)
    