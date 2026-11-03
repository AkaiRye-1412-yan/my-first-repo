"""A-axis point-to-point motion control (pure simulation, issue #1)."""

import logging

logger = logging.getLogger(__name__)

# Physical travel limits in user coordinates; the issue's example target 500
# must lie inside them.
MIN_POSITION = 0.0
MAX_POSITION = 1000.0


def move_axis_a(target_position: float, speed: float) -> bool:
    """Simulate moving the A axis to ``target_position`` at ``speed`` units/s.

    Returns ``True`` and logs the motion when the move runs. Returns ``False``
    and logs a warning without moving when the target is outside the physical
    limits or the speed is not positive.
    """
    if not MIN_POSITION <= target_position <= MAX_POSITION:
        logger.warning(
            "A-axis target %s is outside physical limits [%s, %s]; stopped.",
            target_position,
            MIN_POSITION,
            MAX_POSITION,
        )
        return False
    if speed <= 0:
        logger.warning("A-axis speed %s must be positive; stopped.", speed)
        return False
    logger.info(
        "A-axis moving to %s at %s units/s (simulated).", target_position, speed
    )
    logger.info("A-axis reached %s (simulated).", target_position)
    return True
