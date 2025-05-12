import logging


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s — %(levelname)s — %(message)s",
    )


def truncate(text: str, limit: int = 150) -> str:
    return text[:limit] + "..." if len(text) > limit else text

