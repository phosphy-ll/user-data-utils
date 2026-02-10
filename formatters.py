def normalize_name(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("Name must be a string")

    return name.strip().title()
