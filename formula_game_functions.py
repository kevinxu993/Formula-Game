"""
# Copyright Xinzheng Xu, 2018
# Copyright Nick Cheng, 2016, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file. If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment.

# Add your functions here.


def build_tree(formula):
    '''(str) -> FormulaTree
    Takes a string representing a formula. If the formula is valid, returns the
    FormulaTree representation of the formula, else returns None.
    There are some invalid formulas and reasons.
    "X" variable not lower case letter
    "x*y" missing parentheses
    "-(x)" extraneous parentheses
    "(x+(y)*z)" mismatched parentheses
    REQ: formula is a string representing a boolean formula.
    >>> build_tree('(x*y)') == AndTree(Leaf('x'), Leaf('y'))
    True
    >>> build_tree('(x+-y)') == OrTree(Leaf('x'), NotTree(Leaf('y')))
    True
    >>> build_tree('(((x*y)*z)*w)') == AndTree(AndTree(AndTree(Leaf('x'), Leaf\
    ('y')), Leaf('z')), Leaf('w'))
    True
    >>> build_tree('X') == None
    True
    >>> build_tree('x*y') == None
    True
    >>> build_tree('(x+(y)*z)') == None
    True
    '''
    # set a condition for empty string
    empty = len(formula) == 0
    # if given an empty string, it is invalid
    if(empty):
        # result is None
        result = None
    # if given a string containing 1 lowercase letter, it is valid
    elif(len(formula) == 1):
        # set a condition for single variable
        variable = formula.isalpha() and formula.islower()
        if(variable):
            # create a leaf of the letter
            result = Leaf(formula)
        # else it is invalid
        else:
            # result is None
            result = None
    else:
        # set a condition for Not operation
        no = formula[0] == "-"
        # set a condition for formula closed by parentheses
        # and the numbers of open parentheses and close parentheses are equal
        paired = formula[0] == "(" and formula[-1] == ")" and\
            formula.count("(") == formula.count(")")
        # if - is the first character
        if(no):
            # build the subtree
            sub = build_tree(formula[1:])
            # if the subtree is valid
            if(sub is not None):
                # create a NotTree of the subtree
                result = NotTree(sub)
            # else the subtree is invalid
            else:
                # result is None
                result = None
        # if parentheses are to begin and end the string, and they are paired
        elif(paired):
            # find the root operator
            i = build_help(formula)
            # if the operator doesn'turns exist
            if(i == -1):
                # result is None
                result = None
            # else the operator exists
            else:
                # build a left subtree of the string before the operator
                lc = build_tree(formula[1:i])
                # build a right subtree of the string after the operator
                rc = build_tree(formula[i+1:-1])
                # if one of the strings before & after the operator is invalid
                if(lc is None) or (rc is None):
                    # result is None
                    result = None
                # else the strings are both valid
                else:
                    # if the operator is +
                    if(formula[i] == "+"):
                        # create an OrTree
                        result = OrTree(lc, rc)
                    # if the operator is *
                    elif(formula[i] == "*"):
                        # create a AndTree
                        result = AndTree(lc, rc)
        # else the first character is not a lowercase letter, -, nor (
        else:
            # result is None
            result = None
    # return the result FormulaTree
    return result


def build_help(formula):
    '''(str) -> int
    Takes a string formula and if there exists a root operator * or +, returns
    the index of it, else returns -1.
    REQ: formula is a string representing a boolean formula.
    >>> build_help("x")
    -1
    >>> build_help("(x+y)")
    2
    >>> build_help("(x*y)")
    2
    '''
    # create a counter of incomplete parentheses pairs
    parentheses = 0
    # create a default result: -1
    result = -1
    # check the entire string
    for i in range(len(formula)):
        # if the current character is (
        if(formula[i] == "("):
            # add 1 to the counter of incomplete parentheses pairs
            parentheses += 1
        # if the current character is )
        elif(formula[i] == ")"):
            # deduct 1 from the counter of incomplete parentheses pairs
            parentheses -= 1
        # if the current character is * or +
        # and we have 1 incomplete parentheses pair
        elif(parentheses == 1 and (formula[i] == '*' or formula[i] == '+')):
            # set the result to be current index
            result = i
    # return the result index
    return result


def draw_formula_tree(root):
    '''(FormulaTree) -> str
    Takes the FormulaTree rooted at root and returns a string that draws that
    tree. The way the tree are drawn requires us to rotate it 90 degrees
    clockwise to see it with its root at the top. The trees are drawn without
    lines or arrows betweeen parent and child nodes. Children of the root are
    indented 2 spaces. Children of a child of the root are indented 4 spaces,
    and so on.
    REQ: root is a FormulaTree object.
    >>> draw_formula_tree(build_tree('x'))
    'x'
    >>> draw_formula_tree(build_tree('-x'))
    '- x'
    >>> draw_formula_tree(build_tree('(x+y)'))
    '+ y\\n  x'
    >>> draw_formula_tree(build_tree('(x*y)'))
    '* y\\n  x'
    '''
    # set the starting depth to be 0
    depth = 0
    # create the string representation of the tree
    result = draw_help(root, depth)
    # delete any extra space and new line
    result = result.strip('\n')
    # return the result
    return result


def draw_help(root, indent):
    '''(FormulaTree) -> str
    Takes the FormulaTree rooted at root and int indent representing
    indentation.
    Returns a string that draws that tree. The way the tree are drawn requires
    us to rotate it 90 degrees clockwise to see it with its root at the top.
    The trees are drawn without lines or arrows betweeen parent and child
    nodes. Children of the root are indented 2 spaces. Children of a child of
    the root are indented 4 spaces, and so on.
    REQ: root is a FormulaTree object.
    REQ: indent is an int >= 0.
    >>> draw_help(build_tree('x'), 0)
    'x\\n'
    >>> draw_help(build_tree('-x'), 0)
    '- x\\n'
    >>> draw_help(build_tree('(x+y)'), 0)
    '+ y\\n  x\\n'
    >>> draw_help(build_tree('(x*y)'), 0)
    '* y\\n  x\\n'
    '''
    # increase the identation of children nodes by 2
    indent += 2
    # if we are given a valid FormulaTree
    if(root is not None):
        # if the tree is a Leaf
        if(type(root) == Leaf):
            # add it to the result and create a new blank line for the other
            # child
            result = root.get_symbol() + '\n'
        # if the tree is a NotTree
        elif(type(root) == NotTree):
            # add the symbol of this NotTree to the result
            # add a space and the string representation of the child of this
            # NotTree to the result
            result = root.get_symbol() + ' '\
                + draw_help(root.get_children()[0], indent)
        # else the tree is a OrTree or an AndTree
        else:
            # add the symbol of this BinaryTree to the result
            # add a space and the string representation of the right child of
            # this BinaryTree to the result
            # add a proper space according to the indentation and the string
            # representation of the left child of this BinaryTree to the result
            result = root.get_symbol()\
                + ' ' + draw_help(root.get_children()[1], indent)\
                + ' ' * indent + draw_help(root.get_children()[0], indent)
    # else we are given an invalid input
    else:
        # result is None
        result = None
    # return the result
    return result


def evaluate(root, variables, values):
    '''(FormulaTree, str, str) -> int
    Takes root which is the root of a FormulaTree, along with a string
    variables containing the variables in the formula and a string values
    (of 1's and 0's) containing the corresponding truth values for the
    variables, and returns the truth value (1 or 0) of the formula.
    1 represents True and 0 represents False.
    REQ: root is a FormulaTree object.
    REQ: len(variables) == len(values).
    REQ: variables consists of all unique variables in the formula.
    REQ: values consists of all corresponding truth values for the variables.
    REQ: Truth values in values are in the order as variables in variables.
    >>> evaluate(build_tree('x'), 'x', '1')
    1
    >>> evaluate(build_tree('-x'), 'x', '1')
    0
    >>> evaluate(build_tree('(x+y)'), 'yx', '10')
    1
    >>> evaluate(build_tree('(x*y)'), 'xy', '10')
    0
    '''
    # if the tree is a Leaf
    if(type(root) == Leaf):
        # get the index of the variable in variables
        i = variables.index(root.get_symbol())
        # get the value of the variable in values
        result = int(values[i])
    # else the tree is a NotTree, an OrTree, or an AndTree
    else:
        # get the value of a subtree
        result1 = evaluate(root.get_children()[0], variables, values)
        # if the tree is a NotTree
        if(type(root) == NotTree):
            # get the value of the NotTree by 1 - the value of its subtree
            result = 1 - result1
        # else the tree is an OrTree or an AndTree
        else:
            # get the value of the other subtree
            result2 = evaluate(root.get_children()[1], variables, values)
            # if the tree is an OrTree
            if(type(root) == OrTree):
                # get the maximum of the values of result1 and result2
                result = max(result1, result2)
            # else the tree is an AndTree
            else:
                # get the minimum of the values of result1 and result2
                result = min(result1, result2)

    # return the result
    return result


def play2win(root, turns, variables, values):
    '''(FormulaTree, str, str, str) -> int
    Takes root which is the root of a FormulaTree, along with a
    string turns of A's and E's indicating who takes which turn, a string
    variables of the variables in the formula in order as they are assigned
    values, and a string values (of 1's and 0's) containing the corresponding
    values of the variables chosen so far.
    Players A and E take turns choosing the values of the variables one at a
    time in the specified order given by turns. After all the variables in the
    formula have been assigned truth values given by values, player A wins if
    the truth value of the formula is 0, and player E wins if the truth value
    of formula is 1.
    If the player whose turn is next has a winning strategy, returns the
    corresponding winning move.  If there is no winning strategy, or if
    choosing either 1 or 0 would lead to winningReturns 1 for E and 0 for A.
    REQ: root is a FormulaTree object.
    REQ: len(variables) == len(turns).
    REQ: variables consists of all unique variables in the formula.
    REQ: values consists of corresponding values of the variables chosen so far
    REQ: Truth values in values are in the order as players in turns.
    REQ: len(turns) > len(values).
    >>> play2win(build_tree('((-x*y)*(-y*x))'), 'AE', 'xy', '')
    0
    >>> play2win(build_tree('((-x+y)+(-y+x))'), 'EA', 'xy', '')
    1
    >>> play2win(build_tree('(x+(y*z))'), 'EAA', 'xyz', '1')
    0
    >>> play2win(build_tree('(x*(y*z))'), 'AEE', 'xyz', '10')
    1
    '''
    # get the output of the win_help() for the next player
    res = win_help(root, turns, variables, values)
    # if the next player can win
    if res != '':
        # result is the winning move
        result = int(res)
    # if the next player cannot win
    else:
        # find the next player's turn
        i = len(variables) - len(values)
        # result is the default value
        if turns[-i] == 'A':
            result = 0
        elif turns[-i] == 'E':
            result = 1
    # return the result
    return result


def win_help(root, turns, variables, values):
    '''(FormulaTree, str, str, str) -> str
    Takes root which is the root of a FormulaTree, along with a
    string turns of A's and E's indicating who takes which turn, a string
    variables of the variables in the formula in order as they are assigned
    values, and a string values (of 1's and 0's) containing the corresponding
    values of the variables chosen so far.
    If there is any winning move for the first player, returns the move.
    If there is no winning move for the first player, returns an empty string.
    REQ: root is a FormulaTree object.
    REQ: len(variables) == len(turns).
    REQ: variables consists of all unique variables in the formula.
    REQ: values consists of corresponding values of the variables chosen so far
    REQ: Truth values in values are in the order as players in turns.
    REQ: len(turns) > len(values).
    >>> win_help(build_tree('((-x*y)*(-y*x))'), 'AE', 'xy', '')
    '0'
    >>> win_help(build_tree('((-x+y)+(-y+x))'), 'EA', 'xy', '')
    '1'
    >>> win_help(build_tree('(x+(y*z))'), 'EAA', 'xyz', '1')
    ''
    >>> win_help(build_tree('(x*(y*z))'), 'AEE', 'xyz', '10')
    ''
    >>> win_help(build_tree('((x+y)*-x)'), 'EA', 'xy', '')
    ''
    '''
    # if the next pleyer does not take the last turn
    if len(values) != len(variables) - 1:
        # find the next player's turn
        i = len(variables) - len(values)
        # choose the default value for the next player
        if turns[-i] == 'A':
            add = '0'
        elif turns[-i] == 'E':
            add = '1'
        # update values
        values = values + add
        # get the result of updated info
        result = win_help(root, turns, variables, values)
        # if the next player and next next player are the same
        if turns[-i] == turns[-i+1]:
            # if the next player can win
            if result != '':
                # result is the default value
                res = result
            # else the next player cannot win
            else:
                # choose the other value for the next player
                if turns[-i] == 'A':
                    add = '1'
                elif turns[-i] == 'E':
                    add = '0'
                # update values
                values = values[:-1] + add
                # get the result of updated info
                result = win_help(root, turns, variables, values)
                # if the next player can win
                if result != '':
                    # result is this move
                    res = values[-1]
                # else the next player cannot win anyway
                else:
                    # result is an empty string
                    res = ''
        # else the next player and the next next player are not the same
        else:
            # if the next next player can win
            if result != '':
                # choose the other value for the next player
                if turns[-i] == 'A':
                    add = '1'
                elif turns[-i] == 'E':
                    add = '0'
                # update values
                values = values[:-1] + add
                # get the result of updated info
                result = win_help(root, turns, variables, values)
                # if the next next player still wins
                if result != '':
                    # result is an empty string
                    res = ''
                # else the next player can win
                else:
                    # result is this move
                    res = values[-1]
            # else the next next player cannot win
            else:
                # result is default value
                res = values[-1]
    # else the next player takes the last turn
    else:
        # evaluate the formula with the default value of the next player
        if turns[-1] == 'A':
            add = '0'
        elif turns[-1] == 'E':
            add = '1'
        # update values
        values = values + add
        result = evaluate(root, variables, values)
        # if the next player cannot win by choosing default value
        if (result and turns[-1] != 'E') or (not result and turns[-1] != 'A'):
            # evaluate the formula with the other value of the next player
            if turns[-1] == 'A':
                add = '1'
            elif turns[-1] == 'E':
                add = '0'
            # update values
            values = values[:-1] + add
            result = evaluate(root, variables, values)
            # if the next player cannot win by choosing this value
            if (result and turns[-1] != 'E') or\
               (not result and turns[-1] != 'A'):
                # result is an empty string
                res = ''
            # else the next player can win
            else:
                # result is this move
                res = values[-1]
        # else the next player can win by choosing default value
        else:
            # result is default value
            res = values[-1]

    # return the result
    return res
