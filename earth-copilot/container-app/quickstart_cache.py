# Quickstart cache stub — pre-computed classifications for common demo queries.
# This module provides fast responses for known queries without hitting the full pipeline.
# Extend QUICKSTART_QUERIES dict to add cached entries.

from typing import Optional

QUICKSTART_QUERIES: dict = {}


def is_quickstart_query(query: str) -> bool:
    """Return True if this query has a pre-computed cached result."""
    return query.strip().lower() in QUICKSTART_QUERIES


def get_quickstart_classification(query: str) -> Optional[dict]:
    """Return cached classification for a known query, or None."""
    return QUICKSTART_QUERIES.get(query.strip().lower())


def get_quickstart_location(query: str) -> Optional[dict]:
    """Return cached location for a known query, or None."""
    entry = QUICKSTART_QUERIES.get(query.strip().lower())
    if entry:
        return entry.get("location")
    return None


def get_quickstart_stats() -> dict:
    """Return stats about the quickstart cache."""
    return {"total_cached_queries": len(QUICKSTART_QUERIES)}
