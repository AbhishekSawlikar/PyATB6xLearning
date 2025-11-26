# test_counter.py
from dataclasses import dataclass, asdict
from datetime import datetime
from threading import Lock
from typing import List, Dict, Any, Optional

@dataclass
class ExecutionRecord:
    test_name: str
    status: str            # "PASS" or "FAIL"
    timestamp: datetime
    message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class TestExecutionCounter:
    def __init__(self):
        self._lock = Lock()
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        self.execution_log: List[ExecutionRecord] = []

    def record_execution(self, test_name: str, status: str,
                         message: Optional[str] = None,
                         metadata: Optional[Dict[str, Any]] = None):
        status_up = status.upper()
        if status_up not in ("PASS", "FAIL"):
            raise ValueError("status must be 'PASS' or 'FAIL'")

        rec = ExecutionRecord(
            test_name=test_name,
            status=status_up,
            timestamp=datetime.now(),
            message=message,
            metadata=metadata
        )

        with self._lock:
            self.total_tests += 1
            if status_up == "PASS":
                self.passed_tests += 1
            else:
                self.failed_tests += 1
            self.execution_log.append(rec)

    def summary(self) -> Dict[str, Any]:
        with self._lock:
            last_run = self.execution_log[-1].timestamp if self.execution_log else None
            return {
                "total_tests": self.total_tests,
                "passed": self.passed_tests,
                "failed": self.failed_tests,
                "last_run": last_run
            }

    def reset(self):
        with self._lock:
            self.total_tests = 0
            self.passed_tests = 0
            self.failed_tests = 0
            self.execution_log = []

    def get_records(self) -> List[Dict[str, Any]]:
        # Return serializable dicts
        with self._lock:
            return [asdict(r) for r in self.execution_log]
