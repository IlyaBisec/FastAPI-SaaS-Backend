# Logging configuration.
# Configures application-wide logging:
# - console output
# - log formatting
# - log levels
# 16.05.2026 (c) ilya_bisec

import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger("fsb")