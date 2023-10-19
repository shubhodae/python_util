from game.character import GameCharacter
from typing import Callable, Any

character_creation_funcs: dict[str : Callable[..., GameCharacter]] = {}


def register(character_type: str, creation_func: Callable[..., GameCharacter]) -> None:
    """Register a new game character type."""
    character_creation_funcs[character_type] = creation_func


def unregister(character_type: str) -> None:
    """Unregister a game character type."""
    character_creation_funcs.pop(character_type, None)


def create(arguments: dict[str, Any]) -> GameCharacter:
    """Create a game character of a specific type, given a directory of arguments."""
    args_copy = arguments.copy()
    character_type = args_copy.pop("type")
    try:
        creation_func = character_creation_funcs[character_type]
        return creation_func(**args_copy)
    except KeyError:
        raise ValueError(f"Unknown character type: {character_type}")
