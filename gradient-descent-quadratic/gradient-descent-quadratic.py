def func(a: float, b: float, c: float, x: float) -> float:
    fun_val = 2*a*x+b
    return fun_val
    
def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    for step in range(steps):
        newx=x0-(lr*func(a, b, c, x0))
        x0=newx

    return newx
        
        
    