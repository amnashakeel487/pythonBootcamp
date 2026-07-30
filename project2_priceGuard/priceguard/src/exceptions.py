"""
Custom exception hierarchy for PriceGuard.

Keeping dedicated exception types (instead of raising bare Exception /
ValueError everywhere) makes it possible for main.py to catch failures
selectively and keep the monitoring loop alive no matter what goes wrong.
"""


class PriceGuardError(Exception):
    """Base class for all PriceGuard-specific errors."""


class ScraperError(PriceGuardError):
    """Raised when a product page could not be fetched or parsed."""


class PriceNotFoundError(ScraperError):
    """Raised when the page loaded fine but no price could be located."""


class AlertError(PriceGuardError):
    """Raised when an email/SMS alert could not be sent."""


class DataPersistenceError(PriceGuardError):
    """Raised when reading/writing the CSV data files fails."""
