"""Unit tests for motion/axis_a.py (issue #1)."""

import logging

from motion.axis_a import MAX_POSITION, MIN_POSITION, move_axis_a


def test_valid_move_runs_and_logs(caplog) -> None:
    """The worked example (target 500) moves and logs the simulated motion."""
    with caplog.at_level(logging.INFO, logger="motion.axis_a"):
        assert move_axis_a(target_position=500, speed=100) is True
    assert "moving to 500" in caplog.text
    assert "reached 500" in caplog.text
    assert not any(r.levelno >= logging.WARNING for r in caplog.records)


def test_target_outside_limits_warns_and_stops(caplog) -> None:
    """Targets past either physical limit warn and do not move."""
    for target in (MIN_POSITION - 1, MAX_POSITION + 1):
        caplog.clear()
        with caplog.at_level(logging.WARNING, logger="motion.axis_a"):
            assert move_axis_a(target_position=target, speed=100) is False
        record = caplog.records[-1]
        assert record.levelno == logging.WARNING
        assert "outside physical limits" in record.getMessage()
        assert "moving to" not in caplog.text


def test_targets_on_the_limits_are_accepted(caplog) -> None:
    """The two boundary positions themselves are valid targets."""
    with caplog.at_level(logging.INFO, logger="motion.axis_a"):
        assert move_axis_a(target_position=MIN_POSITION, speed=10) is True
        assert move_axis_a(target_position=MAX_POSITION, speed=10) is True
    assert caplog.text.count("reached") == 2


def test_non_positive_speed_warns_and_stops(caplog) -> None:
    """A zero or negative speed is rejected with a warning."""
    with caplog.at_level(logging.WARNING, logger="motion.axis_a"):
        assert move_axis_a(target_position=500, speed=0) is False
    assert "speed" in caplog.records[-1].getMessage()
