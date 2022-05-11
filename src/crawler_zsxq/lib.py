class InvalidSomethingError(RuntimeError):
    """Error generated if an invalid demo_function input is given."""


def demo_function(n: int) -> int:
    """Computes the demo_function through a recursive algorithm.

    Args:
        n: A positive input value.

    Raises:
        InvalidSomethingError: If n is less than 0.

    Returns:
        Computed demo_function.
    """
    if n < 0:
        raise InvalidSomethingError(f"n is less than zero: {n}")
    elif n == 0:
        return 1

    return n * demo_function(n - 1)
