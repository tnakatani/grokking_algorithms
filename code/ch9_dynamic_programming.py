"""Ch.9 Dynamic Programming"""


def edit_distance(str1: str, str2: str, m: int, n: int) -> int:
    """Calculate Levenshtein distance, ie. minimum number of edits required to convert

    Subproblem:
    1. If last chars of two strings are the same, recur for the lengths-1 for the
    two strings.
    2. If last chars aren't the same, consider all operations on string_1 (insert,
    remove, replace) and recursively compute minimum cost for all three operations
    and take minimum of three values.

    Args:
    str1: first string token
    str2: second string token
    m: length of first string token
    n: length of second string token
    """

    # If first string is empty, insert all characters of second string into
    # first
    if m == 0:
        return n
    # If second string is empty, insert all characters of first string into
    # second
    if n == 0:
        return m

    # If last characters of two strings are the same, ignore last chars and get
    # count for remaining strings.
    if str1[m - 1] == str2[n - 1]:
        return edit_distance(str1, str2, m - 1, n - 1)

    # If last characters aren't the same, consider all three operations on the
    # last character of first string, recursively compute min cost for all
    # three operations and take min of three values
    return 1 + min(
        edit_distance(str1, str2, m, n - 1),  # Insertion
        edit_distance(str1, str2, m - 1, n),  # Deletion
        edit_distance(str1, str2, m - 1, n - 1),  # Substitution
    )


if __name__ == "__main__":
    print(edit_distance("normal", "norway", len("normal"), len("norway")))
    print(edit_distance("tornado", "tomato", len("tornado"), len("tomato")))
