def calculate_fibonacci(n):
    """
    Calculates the nth number in the Fibonacci sequence.
    Example:
    calculate_fibonacci(0) -> 0
    calculate_fibonacci(1) -> 1
    calculate_fibonacci(5) -> 5
    """
    # TODO: Student must write their code here.
    # For now, let's provide a placeholder that will fail the test.
    if n <0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1

    for i in range(2, n+1) :
        next_number = a + b
        a = b
        b = next_number
    return b