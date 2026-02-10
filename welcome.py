import os
from typing import Optional, Union

# Directory to store per-group welcome templates
WELCOME_DIR = os.path.join(os.path.dirname(__file__), "welcome_templates")


def _ensure_dir() -> None:
    os.makedirs(WELCOME_DIR, exist_ok=True)


def _file_path(group_id: Union[int, str]) -> str:
    return os.path.join(WELCOME_DIR, f"{group_id}.txt")


def set_template(group_id: Union[int, str], template: str) -> None:
    """Persist welcome template for a group.

    The template may contain the token '<user>' which will be replaced at send-time.
    """
    _ensure_dir()
    path = _file_path(group_id)
    with open(path, "w", encoding="utf-8") as f:
        f.write(template.strip())


def get_template(group_id: Union[int, str]) -> Optional[str]:
    """Retrieve the welcome template for a group, or None if not set."""
    path = _file_path(group_id)
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            return content if content else None
    except OSError:
        return None
