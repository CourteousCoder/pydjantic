"""
Mock settings.py

This module is a deliberately minimal settings module that we can import in the tests.
"""

MOCK_SETTING = "mock value"


def get_globals():
    """
    Injects Django settings into the current namespace when imported (e.g by tests).
    This closure over bo the magic `globals()` function lets it be available outside this module.
    """
    return globals()
