# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:40:36 2022

@author: Ehlion

| Module for integer management in macros and generator.
| Includes mathematical operators and IntReferences.
"""

# We will use many Interfaces for only one function
# pylint: disable-msg=R0903

#___________________________________________________#
#                                                   #
#                  Rand Interface                   #
#___________________________________________________#

class ValueIf :
    """Default interface with basic implementation
    of an encapsulated integer value"""

    def __init__(self) :
        pass

    def get_value(self) -> int :
        """Get the value."""
        raise NotImplementedError(f"In class {type(self).__name__}")

    value = property(get_value)

class Value(ValueIf) :
    """Encapsulate an integer value"""

    def __init__(self, value:int = 0) :
        ValueIf.__init__(self)
        self._value = value

    def get_value(self) -> int :
        """Get the value."""
        return self._value

    def set_value(self, value:int=0) -> None :
        """Set the value."""
        self._value = value

    value = property(get_value, set_value)

class RefValue(ValueIf) :
    """Encapsulate a ValueIf"""

    def __init__(self, reference:ValueIf) :
        ValueIf.__init__(self)
        self.reference = reference

    def get_value(self) -> int :
        """Get the value."""
        return self.reference.value

    value = property(get_value)

class Operator(ValueIf) :
    """A mathematical operator with 2 arguments"""

    def __init__(self, left, right) :
        ValueIf.__init__(self)

        if isinstance(left, int) :
            self.left = Value(left)
        elif isinstance(left, ValueIf) :
            self.left = left
        else :
            raise ValueError("'Int' or 'ValueIf' expected")

        if isinstance(right, int) :
            self.right = Value(right)
        elif isinstance(right, ValueIf) :
            self.right = right
        else :
            raise ValueError("'Int' or 'ValueIf' expected")

    def get_value(self) -> int :
        """Get the rest."""
        raise NotImplementedError(f"In class {type(self).__name__}")

    value = property(get_value)

class AddOp(ValueIf) :
    """The addition operation"""

    def __init__(self, left, right) :
        Operator.__init__(self, left, right)

    def get_value(self) -> int :
        """Get the sum."""
        return self.left.value + self.right.value

    value = property(get_value)

class SubOp(ValueIf) :
    """The soustraction operation"""

    def __init__(self, left, right) :
        Operator.__init__(self, left, right)

    def get_value(self) -> int :
        """Get the difference."""
        return self.left.value - self.right.value

    value = property(get_value)

class MulOp(ValueIf) :
    """The multiplication operation"""

    def __init__(self, left, right) :
        Operator.__init__(self, left, right)

    def get_value(self) -> int :
        """Get the product."""
        return self.left.value * self.right.value

    value = property(get_value)

class DivOp(ValueIf) :
    """The multiplication operation"""

    def __init__(self, left, right) :
        Operator.__init__(self, left, right)

    def get_value(self) -> int :
        """Get the quotient."""
        return int(self.left.value / self.right.value)

    value = property(get_value)

class ModOp(ValueIf) :
    """The multiplication operation"""

    def __init__(self, left, right) :
        Operator.__init__(self, left, right)

    def get_value(self) -> int :
        """Get the rest."""
        return self.left.value % self.right.value

    value = property(get_value)

#___________________________________________________#
#                                                   #
#                       Testing                     #
#___________________________________________________#

if __name__ == "__main__" :
    from utils.debug import print_log, test

    print_log("START", "CALCULATION UNITARY TESTING")
    print_log("TEST", "Value")
    v1 = Value(1)
    v2 = Value(2)
    test(v1.value, 1)
    v1.value = 5
    test(v1.value, 5)
    print_log("TEST", "Addition")
    op = AddOp(v1, v2)
    test(op.value, 7)
    print_log("TEST", "Soustraction")
    op = SubOp(v1, v2)
    test(op.value, 3)
    op = SubOp(v2, v1)
    test(op.value, -3)
    print_log("TEST", "Multiplication")
    op = MulOp(v1, v2)
    test(op.value, 10)
    print_log("TEST", "Division")
    op = DivOp(v1, v2)
    test(op.value, 2)
    print_log("TEST", "Modulo")
    op = ModOp(v1, v2)
    test(op.value, 1)
    print_log("TEST", "Reference")
    op = RefValue(MulOp(v1, v2))
    test(op.value, 10)
    print_log("TEST", "Complex operation")
    op = RefValue(DivOp(
        AddOp(
            MulOp(Value(5), Value(2)),
            SubOp(Value(6), Value(4))),
        Value(6)))
    test(op.value, 2)
