# beta-2
'''
DISCLAIMER:
Passing this test suite does NOT imply that your code will fully pass the auto marker.
However, if your code fails any of the test cases, chances are there is a bug in your code.
'''


import unittest
import itertools
from formula_game_functions import *
from random import randint


NOT, AND, OR = '-', '*', '+'
OPS = {0: NOT, 1: AND, 2: OR}
VARS = {0: 'x', 1: 'y', 2: 'z'}


# Retrieved from https://piazza.com/class/ixgonr8vwig5f5?cid=854
def generate_formula(layers, var='x'):
    """(int[, str]) -> str

    Builds and returns a random formula of with a given number of layers,
    such that a formula with a layer of zero is simply the variable itself.

    NOTE: formulas with layers > 6 will get VERY LARGE!

    REQ: layers >= 0
    REQ: var == var.lower() and len(var) == 1
    """
    # Base case: 0th layer is simply the var itself (leaf).
    if layers == 0:
        formula = var
    # Recursive decomposition: n-1 approach.
    else:
        # Get a random operator.
        operator = OPS[randint(0, 2)]
        # Case 1: create an unary layer.
        if operator == NOT:
            formula = generate_formula(layers - 1, var)
            # Check if sub-formula is already negated.
            if formula[0] != NOT:
                formula = NOT + formula
        # Case 2: create a binary layer.
        else:
            # Recursively generate sub-formulas.
            sub_formula = generate_formula(layers - 1, var)
            # Generate another random variable.
            other_var = VARS[randint(0, 2)]
            other_formula = generate_formula(randint(0, layers), other_var)
            # Swap sub-formulas for random balance.
            if randint(0, 1) == 0:
                sub_formula, other_formula = other_formula, sub_formula
            # Concatenate the binary formula.
            formula = '(' + sub_formula + operator + other_formula + ')'
    # Return formula at current recursive call.
    return formula


def evaluate_formula(formula, variables, values):
    for i in range(len(variables)):
        formula = formula.replace(variables[i], "True" if values[i] == "1" else "False")
    formula = formula.replace("-", " not ").replace("*", " and ").replace("+", " or ")
    result = eval(formula)
    return 1 if result else 0


class TestA2(unittest.TestCase):
    def test_not_valid_00(self):
        formula = "x+(-y)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_01(self):
        formula = "(((x+y)*(x-y) + ((a-b)*(a+b)))"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_02(self):
        formula = "(((x+y)*(x-y)+((a-b)*(a+b)))"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_03(self):
        formula = "(u*v*w*z)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_04(self):
        formula = "-((x+y))"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_05(self):
        formula = "((x+y*z+d*e) * (z+e*y))"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_06(self):
        formula = "((-x+y)*-(-y+X))"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_07(self):
        formula = "((A*B)+E+D+F)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_08(self):
        formula = "(x+(y)*z)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_09(self):
        formula = "(x+(y+a)*z)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_10(self):
        formula = "(((((x+y)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_11(self):
        formula = "(xyz+*)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_12(self):
        formula = "(+x*+-z)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_13(self):
        formula = "()(((((((a"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_14(self):
        formula = "-(-x*-y)*-(x+y)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_15(self):
        formula = "(-y)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_16(self):
        formula = "(x*y+z*x)"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_not_valid_17(self):
        formula = "(((x+y)*(x-y))+((a-b)*(a+b)))"
        actual = build_tree(formula)
        expected = None
        self.assertEqual(actual, expected)

    def test_is_valid_random_00(self):
        for i in range(10):
            formula = generate_formula(1)
            actual = build_tree(formula)
            expected = actual != None
            self.assertTrue(expected, formula + " should be valid")

    def test_is_valid_random_01(self):
        for i in range(10):
            formula = generate_formula(2)
            actual = build_tree(formula)
            expected = actual != None
            self.assertTrue(expected, formula + " should be valid")

    def test_is_valid_random_02(self):
        for i in range(10):
            formula = generate_formula(3)
            actual = build_tree(formula)
            expected = actual != None
            self.assertTrue(expected, formula + " should be valid")

    def test_is_valid_random_03(self):
        for i in range(10):
            formula = generate_formula(4)
            actual = build_tree(formula)
            expected = actual != None
            self.assertTrue(expected, formula + " should be valid")

    def test_is_valid_random_04(self):
        for i in range(10):
            formula = generate_formula(5)
            actual = build_tree(formula)
            expected = actual != None
            self.assertTrue(expected, formula + " should be valid")

    def test_is_valid_random_05(self):
        for i in range(10):
            formula = generate_formula(6)
            actual = build_tree(formula)
            expected = actual != None
            self.assertTrue(expected, formula + " should be valid")

    def test_build_tree_00(self):
        formula = "-----a"
        actual = build_tree(formula).__repr__()
        expected = "NotTree(NotTree(NotTree(NotTree(NotTree(Leaf('a'))))))"
        self.assertEqual(actual, expected)

    def test_build_tree_01(self):
        formula = "(((x+y)*(-x+y))+((a+b)*(-b+a)))"
        actual = build_tree(formula).__repr__()
        expected = "OrTree(AndTree(OrTree(Leaf('x'), Leaf('y')), OrTree(NotTree(Leaf('x')), Leaf('y'))), AndTree(OrTree(Leaf('a'), Leaf('b')), OrTree(NotTree(Leaf('b')), Leaf('a'))))"
        self.assertEqual(actual, expected)

    def test_build_tree_02(self):
        formula = "-((-x*-y)*-(x+y))"
        actual = build_tree(formula).__repr__()
        expected = "NotTree(AndTree(AndTree(NotTree(Leaf('x')), NotTree(Leaf('y'))), NotTree(OrTree(Leaf('x'), Leaf('y')))))"
        self.assertEqual(actual, expected)

    def test_build_tree_03(self):
        formula = "x"
        actual = build_tree(formula).__repr__()
        expected = "Leaf('x')"
        self.assertEqual(actual, expected)

    def test_build_tree_04(self):
        formula = "-y"
        actual = build_tree(formula).__repr__()
        expected = "NotTree(Leaf('y'))"
        self.assertEqual(actual, expected)

    def test_build_tree_05(self):
        formula = "(x*y)"
        actual = build_tree(formula).__repr__()
        expected = "AndTree(Leaf('x'), Leaf('y'))"
        self.assertEqual(actual, expected)

    def test_build_tree_06(self):
        formula = "((x+y)+(y+x))"
        actual = build_tree(formula).__repr__()
        expected = "OrTree(OrTree(Leaf('x'), Leaf('y')), OrTree(Leaf('y'), Leaf('x')))"
        self.assertEqual(actual, expected)

    def test_build_tree_07(self):
        formula = "((-x+y)+(-y+x))"
        actual = build_tree(formula).__repr__()
        expected = "OrTree(OrTree(NotTree(Leaf('x')), Leaf('y')), OrTree(NotTree(Leaf('y')), Leaf('x')))"
        self.assertEqual(actual, expected)

    def test_build_tree_08(self):
        formula = "((x*y)+(-x*-y))"
        actual = build_tree(formula).__repr__()
        expected = "OrTree(AndTree(Leaf('x'), Leaf('y')), AndTree(NotTree(Leaf('x')), NotTree(Leaf('y'))))"
        self.assertEqual(actual, expected)

    def test_build_tree_09(self):
        formula = "(((x+y)*(-x+y))+((a+b)*(-a+b)))"
        actual = build_tree(formula).__repr__()
        expected = "OrTree(AndTree(OrTree(Leaf('x'), Leaf('y')), OrTree(NotTree(Leaf('x')), Leaf('y'))), AndTree(OrTree(Leaf('a'), Leaf('b')), OrTree(NotTree(Leaf('a')), Leaf('b'))))"
        self.assertEqual(actual, expected)

    def test_build_tree_10(self):
        formula = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+z)))))))))))))))))))))))))"
        actual = build_tree(formula).__repr__()
        expected = "OrTree(Leaf('a'), OrTree(Leaf('b'), OrTree(Leaf('c'), OrTree(Leaf('d'), OrTree(Leaf('e'), OrTree(Leaf('f'), OrTree(Leaf('g'), OrTree(Leaf('h'), OrTree(Leaf('i'), OrTree(Leaf('j'), OrTree(Leaf('k'), OrTree(Leaf('l'), OrTree(Leaf('m'), OrTree(Leaf('n'), OrTree(Leaf('o'), OrTree(Leaf('p'), OrTree(Leaf('q'), OrTree(Leaf('r'), OrTree(Leaf('s'), OrTree(Leaf('t'), OrTree(Leaf('u'), OrTree(Leaf('v'), OrTree(Leaf('w'), OrTree(Leaf('x'), OrTree(Leaf('y'), Leaf('z'))))))))))))))))))))))))))"
        self.assertEqual(actual, expected)

    def test_build_tree_11(self):
        formula = "((u*v)*(w*z))"
        actual = build_tree(formula).__repr__()
        expected = "AndTree(AndTree(Leaf('u'), Leaf('v')), AndTree(Leaf('w'), Leaf('z')))"
        self.assertEqual(actual, expected)

    def test_build_tree_12(self):
        formula = "(u*(v*(w*z)))"
        actual = build_tree(formula).__repr__()
        expected = "AndTree(Leaf('u'), AndTree(Leaf('v'), AndTree(Leaf('w'), Leaf('z'))))"
        self.assertEqual(actual, expected)

    def test_build_tree_13(self):
        formula = "-(-x+y)"
        actual = build_tree(formula).__repr__()
        expected = "NotTree(OrTree(NotTree(Leaf('x')), Leaf('y')))"
        self.assertEqual(actual, expected)

    def test_build_tree_14(self):
        formula = "(((x+y)*(-x+y))+((a+b)*(-a+b)))"
        actual = build_tree(formula).__repr__()
        expected = "OrTree(AndTree(OrTree(Leaf('x'), Leaf('y')), OrTree(NotTree(Leaf('x')), Leaf('y'))), AndTree(OrTree(Leaf('a'), Leaf('b')), OrTree(NotTree(Leaf('a')), Leaf('b'))))"
        self.assertEqual(actual, expected)

    def test_build_tree_15(self):
        formula = "(x+(y*z))"
        actual = build_tree(formula).__repr__()
        expected = "OrTree(Leaf('x'), AndTree(Leaf('y'), Leaf('z')))"
        self.assertEqual(actual, expected)

    def test_build_tree_16(self):
        formula = "(((x+y)*(-x+y))+((-a+b)*(b+a)))"
        actual = build_tree(formula).__repr__()
        expected = "OrTree(AndTree(OrTree(Leaf('x'), Leaf('y')), OrTree(NotTree(Leaf('x')), Leaf('y'))), AndTree(OrTree(NotTree(Leaf('a')), Leaf('b')), OrTree(Leaf('b'), Leaf('a'))))"
        self.assertEqual(actual, expected)

    def test_build_tree_17(self):
        formula = "(-x+-y)"
        actual = build_tree(formula).__repr__()
        expected = "OrTree(NotTree(Leaf('x')), NotTree(Leaf('y')))"
        self.assertEqual(actual, expected)

    def test_build_tree_18(self):
        formula = "(-----x+y)"
        actual = build_tree(formula).__repr__()
        expected = "OrTree(NotTree(NotTree(NotTree(NotTree(NotTree(Leaf('x')))))), Leaf('y'))"
        self.assertEqual(actual, expected)

    def test_build_tree_19(self):
        formula = "(x+-----y)"
        actual = build_tree(formula).__repr__()
        expected = "OrTree(Leaf('x'), NotTree(NotTree(NotTree(NotTree(NotTree(Leaf('y')))))))"
        self.assertEqual(actual, expected)

    def test_build_tree_20(self):
        formula = "(-----x+-----y)"
        actual = build_tree(formula).__repr__()
        expected = "OrTree(NotTree(NotTree(NotTree(NotTree(NotTree(Leaf('x')))))), NotTree(NotTree(NotTree(NotTree(NotTree(Leaf('y')))))))"
        self.assertEqual(actual, expected)

    def test_draw_formula_tree_00(self):
        formula = "((-x+y)*-(-y+x))"
        actual = draw_formula_tree(build_tree(formula))
        expected = '* - + x\n      - y\n  + y\n    - x'
        self.assertEqual(actual, expected)

    def test_draw_formula_tree_01(self):
        formula = "((-x+y)*-(-y+x))"
        actual = draw_formula_tree(build_tree('(c+-(-(b+a)+-(-x+-y)))'))
        expected = '+ - + - + - y\n          - x\n      - + a\n          b\n  c'
        self.assertEqual(actual, expected)

    def test_draw_formula_tree_02(self):
        formula = "(x+y)"
        actual = draw_formula_tree(build_tree(formula))
        expected = '+ y\n  x'
        self.assertEqual(actual, expected)

    def test_draw_formula_tree_03(self):
        formula = "(x*y)"
        actual = draw_formula_tree(build_tree(formula))
        expected = '* y\n  x'
        self.assertEqual(actual, expected)

    def test_draw_formula_tree_04(self):
        formula = "((x*y)+(z*x))"
        actual = draw_formula_tree(build_tree(formula))
        expected = '+ * x\n    z\n  * y\n    x'
        self.assertEqual(actual, expected)

    def test_draw_formula_tree_05(self):
        formula = "((x+y)*x)"
        actual = draw_formula_tree(build_tree(formula))
        expected = '* x\n  + y\n    x'
        self.assertEqual(actual, expected)

    def test_draw_formula_tree_06(self):
        formula = "(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+z)))))))))))))))))))))))))"
        actual = draw_formula_tree(build_tree(formula))
        expected = '+ + + + + + + + + + + + + + + + + + + + + + + + + z\n                                                  y\n                                                x\n                                              w\n                                            v\n                                          u\n                                        t\n                                      s\n                                    r\n                                  q\n                                p\n                              o\n                            n\n                          m\n                        l\n                      k\n                    j\n                  i\n                h\n              g\n            f\n          e\n        d\n      c\n    b\n  a'

        self.assertEqual(actual, expected)

    def test_evaluate_00(self):
        formula = "x"
        variables = "x"
        perms = itertools.product('01', repeat=len(variables))
        for next_perm in perms:
            values = str().join(next_perm)
            actual = evaluate(build_tree(formula), variables, values)
            expected = evaluate_formula(formula, variables, values)
            self.assertEqual(actual, expected, "Evaluating formula " + formula + " with variables " + variables + " and values " + values)

    def test_evaluate_01(self):
        formula = "-y"
        variables = "y"
        perms = itertools.product('01', repeat=len(variables))
        for next_perm in perms:
            values = str().join(next_perm)
            actual = evaluate(build_tree(formula), variables, values)
            expected = evaluate_formula(formula, variables, values)
            self.assertEqual(actual, expected, "Evaluating formula " + formula + " with variables " + variables + " and values " + values)

    def test_evaluate_02(self):
        formula = "(x*y)"
        variables = "xy"
        perms = itertools.product('01', repeat=len(variables))
        for next_perm in perms:
            values = str().join(next_perm)
            actual = evaluate(build_tree(formula), variables, values)
            expected = evaluate_formula(formula, variables, values)
            self.assertEqual(actual, expected, "Evaluating formula " + formula + " with variables " + variables + " and values " + values)

    def test_evaluate_03(self):
        formula = "((x+y)+(y+x))"
        variables = "xy"
        perms = itertools.product('01', repeat=len(variables))
        for next_perm in perms:
            values = str().join(next_perm)
            actual = evaluate(build_tree(formula), variables, values)
            expected = evaluate_formula(formula, variables, values)
            self.assertEqual(actual, expected, "Evaluating formula " + formula + " with variables " + variables + " and values " + values)

    def test_evaluate_04(self):
        formula = "((-x+y)+(-y+x))"
        variables = "xy"
        perms = itertools.product('01', repeat=len(variables))
        for next_perm in perms:
            values = str().join(next_perm)
            actual = evaluate(build_tree(formula), variables, values)
            expected = evaluate_formula(formula, variables, values)
            self.assertEqual(actual, expected, "Evaluating formula " + formula + " with variables " + variables + " and values " + values)

    def test_evaluate_05(self):
        formula = "((x*y)+(-x*-y))"
        variables = "xy"
        perms = itertools.product('01', repeat=len(variables))
        for next_perm in perms:
            values = str().join(next_perm)
            actual = evaluate(build_tree(formula), variables, values)
            expected = evaluate_formula(formula, variables, values)
            self.assertEqual(actual, expected, "Evaluating formula " + formula + " with variables " + variables + " and values " + values)

    def test_evaluate_06(self):
        formula = "(((x+y)*(-x+y))+((a+b)*(-a+b)))"
        variables = "abxy"
        perms = itertools.product('01', repeat=len(variables))
        for next_perm in perms:
            values = str().join(next_perm)
            actual = evaluate(build_tree(formula), variables, values)
            expected = evaluate_formula(formula, variables, values)
            self.assertEqual(actual, expected, "Evaluating formula " + formula + " with variables " + variables + " and values " + values)

    def test_play2win_00(self):
        formula = "((-x*y)*(-y*x))"
        turns = "AE"
        variables = "xy"
        values = ""
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 0
        self.assertEqual(actual, expected)

    def test_play2win_01(self):
        formula = "((-x+y)+(-y+x))"
        turns = "AE"
        variables = "xy"
        values = ""
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 0
        self.assertEqual(actual, expected)

    def test_play2win_02(self):
        formula = "(x*(y*z))"
        turns = "AEE"
        variables = "xyz"
        values = ""
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 0
        self.assertEqual(actual, expected)

    def test_play2win_03(self):
        formula = "(-x*(y*z))"
        turns = "AEE"
        variables = "xyz"
        values = ""
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 1
        self.assertEqual(actual, expected)

    def test_play2win_04(self):
        formula = "((-x+y)+(-y+x))"
        turns = "EA"
        variables = "xy"
        values = ""
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 1
        self.assertEqual(actual, expected)

    def test_play2win_05(self):
        formula = "((-x*y)*(-y*x))"
        turns = "EA"
        variables = "xy"
        values = ""
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 1
        self.assertEqual(actual, expected)

    def test_play2win_06(self):
        formula = "(-x+(y*z))"
        turns = "EAA"
        variables = "xyz"
        values = ""
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 0
        self.assertEqual(actual, expected)

    def test_play2win_07(self):
        formula = "(x+(y*z))"
        turns = "EAA"
        variables = "xyz"
        values = ""
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 1
        self.assertEqual(actual, expected)

    def test_play2win_08(self):
        formula = "(x+(y*z))"
        turns = "EAA"
        variables = "xyz"
        values = "1"
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 0
        self.assertEqual(actual, expected)

    def test_play2win_09(self):
        formula = "(x+(y*z))"
        turns = "EAA"
        variables = "xyz"
        values = "0"
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 0
        self.assertEqual(actual, expected)

    def test_play2win_10(self):
        formula = "(x+(y*z))"
        turns = "EAA"
        variables = "xyz"
        values = "00"
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 0
        self.assertEqual(actual, expected)

    def test_play2win_11(self):
        formula = "(x+(y*z))"
        turns = "EAA"
        variables = "xyz"
        values = "01"
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 0
        self.assertEqual(actual, expected)

    def test_play2win_12(self):
        formula = "(x*(y*z))"
        turns = "AEE"
        variables = "xyz"
        values = "0"
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 1
        self.assertEqual(actual, expected)

    def test_play2win_13(self):
        formula = "(x*(y*z))"
        turns = "AEE"
        variables = "xyz"
        values = "1"
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 1
        self.assertEqual(actual, expected)

    def test_play2win_14(self):
        formula = "(x*(y*z))"
        turns = "AEE"
        variables = "xyz"
        values = "10"
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 1
        self.assertEqual(actual, expected)

    def test_play2win_15(self):
        formula = "(x*(y*z))"
        turns = "AEE"
        variables = "xyz"
        values = "11"
        actual = play2win(build_tree(formula), turns, variables, values)
        expected = 1
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(exit=False)
