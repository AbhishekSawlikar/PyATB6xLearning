# decorators.py
from functools import wraps
from test_counter import TestExecutionCounter

# Single global counter instance (you can create multiple if needed)
global_counter = TestExecutionCounter()

def count_test(fn=None, *, counter: TestExecutionCounter = global_counter):
    """
    Can be used as @count_test or @count_test(counter=some_counter)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                counter.record_execution(func.__name__, "PASS")
                return result
            except Exception as e:
                # Optionally re-raise after recording
                counter.record_execution(func.__name__, "FAIL", message=str(e))
                raise
        return wrapper

    if fn is None:
        return decorator
    else:
        return decorator(fn)