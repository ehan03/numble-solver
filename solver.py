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

    if len(nums) != 6:
        return "Please enter 6 numbers"
    
    expr = [{} for _ in range(1 << 6)]
    for i in range(6):
        expr[1 << i] = {nums[i]: str(nums[i])}
    tout = (1 << 6) - 1
    for S in range(3, tout + 1):
        if expr[S] != {}:
            continue
        for L in range(1, S):
            if L & S == L:
                R = S ^ L
                for vL in expr[L]:
                    for vR in expr[R]:
                        eL = expr[L][vL]
                        eR = expr[R][vR]
                        expr[S][vL] = eL
                        if vL > vR:
                            expr[S][vL - vR] = "(%s - %s)" % (eL, eR)
                        if L < R:
                            expr[S][vL + vR] = "(%s + %s)" % (eL, eR)
                            expr[S][vL * vR] = "(%s * %s)" % (eL, eR)
                        if vR != 0 and vL % vR == 0:
                            expr[S][vL // vR] = "(%s / %s)" % (eL, eR)
    
    
    if target in expr[tout]:
        return "%s = %i" % (expr[tout][target], target)
    
    return "No solution"