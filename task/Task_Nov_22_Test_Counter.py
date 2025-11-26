import datetime

class TestExecutionCounter:
    def __init__(self):
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        self.execution_log = []

    def record_execution(self, test_name: str, status: str):
        """
        status = 'PASS' or 'FAIL'
        """
        self.total_tests += 1
        timestamp = datetime.datetime.now()

        if status.upper() == "PASS":
            self.passed_tests += 1
        elif status.upper() == "FAIL":
            self.failed_tests += 1
        else:
            raise ValueError("Status must be PASS or FAIL.")

        self.execution_log.append({
            "test": test_name,
            "status": status.upper(),
            "timestamp": timestamp
        })

    def summary(self):
        return {
            "total_tests": self.total_tests,
            "passed": self.passed_tests,
            "failed": self.failed_tests,
            "last_run": self.execution_log[-1]["timestamp"] if self.execution_log else None
        }

    def reset(self):
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        self.execution_log = []

from test_counter import TestExecutionCounter

counter = TestExecutionCounter()

# Simulate results
counter.record_execution("Test_ETL_Transformation", "PASS")
counter.record_execution("Test_Lakehouse_Load", "FAIL")
counter.record_execution("Test_PowerBI_Data", "PASS")

print(counter.summary())
