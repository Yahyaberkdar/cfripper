from enum import Enum


class RuleMode(str, Enum):
    # Rule modes
    BLOCKING = "BLOCKING"
    MONITOR = "MONITOR"
    DEBUG = "DEBUG"


class RuleRisk(str, Enum):
    # Rule risk severity
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
