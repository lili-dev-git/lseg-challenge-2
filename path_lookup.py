def get_by_path(obj, path, sep="/"):

    if path == "":
        return obj

    current = obj
    for key in path.split(sep):
        if key == "":
            # tolerate double slashes like "a//b"
            continue
        if not isinstance(current, dict):
            return None
        if key not in current:
            return None
        current = current[key]
    return current


def _run_tests():
    # Prompt examples
    assert get_by_path({"a": {"b": {"c": "d"}}}, "a/b/c") == "d"
    assert get_by_path({"x": {"y": {"z": "a"}}}, "x/y/z") == "a"

    # Empty path
    root = {"a": 1}
    assert get_by_path(root, "") is root

    # Missing key → None
    assert get_by_path({"a": {}}, "a/missing") is None

    # Non-dict descent → None
    assert get_by_path({"a": 1}, "a/b") is None

    # Double slashes tolerated
    assert get_by_path({"a": {"b": 3}}, "a//b") == 3

    # Custom separator
    data = {"a.b": {"c": 123}}
    assert get_by_path(data, "a.b|c", sep="|") == 123

    print("All tests passed.")


if __name__ == "__main__":
    _run_tests()
