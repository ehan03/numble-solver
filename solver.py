def numble_solve(nums, target):
    """Solve the Numble game.

    Args:
        nums (list): A list of 6 integers.
        target (int): The target number.

    Returns:
        str: A string of the solution, which is an expression
            that uses the 6 numbers and the operators +, -, *, /
            to evaluate to the target number. If there are multiple
            solutions, return any one of them. If there is no solution,
            return "No solution".
    """
    # Here we use a bottom-up dynamic programming approach to essentially generate all possible
    # valid expressions for each subset of the 6 numbers

    # Make sure we have 6 numbers
    if len(nums) != 6:
        return "Please enter 6 numbers"
    
    # Main idea is to encode the set of 6 numbers and any subset of them in a single integer
    # Easy way to do this is to use a bit mask
    # Maximum number of subsets is obviously 2^6 = 64
    MAX_SUBSETS = 64

    # Keep a list of all possible expressions for each subset of the numbers
    # We index by the unique bit mask for each subset
    expression = [{} for x in range(MAX_SUBSETS)]
    
    # Each key-value pair will be the value of the expression and the expression itself
    # Initialize the list with the 6 numbers on their own
    for i in range(6):
        expression[1 << i] = {nums[i]: str(nums[i])}

    # Let set_U be the set of numbers we are considering
    # We loop starting at 3 since it is first non-power of 2
    for set_U in range(3, MAX_SUBSETS):
        # Make sure we haven't already solved this subset
        if expression[set_U] != {}:
            continue

        # Loop through all candidates for possible subsets of set_U
        for set_A in range(1, set_U):
            # Check if set_A is a subset of set_U
            if set_A & set_U == set_A:
                # set_B is the complement of set_A in set_U, i.e. the numbers in set_U that are not in set_A
                # We do this because each number can only be used at most once
                # Because we use bit masks, complement is just XOR
                set_B = set_U ^ set_A

                # Loop over all possible values for set_A
                for val_L in expression[set_A]:
                    # Loop over all possible values for set_B
                    for val_R in expression[set_B]:
                        # Get the expressions for val_L and val_R
                        expr_L = expression[set_A][val_L]
                        expr_R = expression[set_B][val_R]

                        # Make sure to consider case where we don't do any operations
                        expression[set_U][val_L] = expr_L

                        # Check if subtraction is valid, i.e. positive result
                        if val_L > val_R:
                            expression[set_U][val_L - val_R] = f"({expr_L} - {expr_R})"

                        # Symmetry, avoid repeating
                        if set_A < set_B:
                            expression[set_U][val_L + val_R] = f"({expr_L} + {expr_R})"
                            expression[set_U][val_L * val_R] = f"({expr_L} * {expr_R})"

                        # Check if division is valid, i.e. integer result
                        if val_R != 0 and val_L % val_R == 0:
                            expression[set_U][val_L // val_R] = f"({expr_L} / {expr_R})"

        # Check if we have a solution
        if target in expression[set_U]:
            return f"{expression[set_U][target]} = {target}"
    
    return "No solution"