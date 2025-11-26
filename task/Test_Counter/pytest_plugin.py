# pytest_plugin.py
import pytest
from test_counter import TestExecutionCounter
from pytest import Item

# Create module-level counter so it persists across tests in a run
pytest_counter = TestExecutionCounter()

def pytest_runtest_logreport(report):
    # This hook is called for setup, call, teardown. We want the "call" phase.
    if report.when == "call":
        test_name = report.nodeid
        if report.passed:
            pytest_counter.record_execution(test_name, "PASS")
        elif report.failed:
            pytest_counter.record_execution(test_name, "FAIL", message=str(report.longrepr))

def pytest_sessionfinish(session, exitstatus):
    # Example: write to a file at the end of the run
    from reporter import export_to_json
    export_to_json(pytest_counter.get_records(), filename="pytest_execution_report.json")
    # Print a brief summary
    print("\n=== Pytest Execution Summary ===")
    print(pytest_counter.summary())