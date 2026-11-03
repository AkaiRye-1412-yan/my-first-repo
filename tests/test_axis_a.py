"""Unit tests for motion/axis_a.py.

Minimal placeholder for the stub added to unblock triage (issue #1); the
real tests land with the BUILD node's implementation.
"""

from motion.axis_a import move_axis_a


def test_move_axis_a_is_callable() -> None:
    """The stub function is callable with position and speed."""
    move_axis_a(target_position=500, speed=100)