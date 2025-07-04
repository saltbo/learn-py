def underscorifySubstring(string, substring):
    # If two or more instances of the substring in the main string overlap each other or sit side by side, the underscores relevant to these substrings should only appear on the far left of the leftmost substring and on the far right of the rightmost substring. If the main string doesn't contain the other string at all, the function should return the main string intact.

    # Find all the locations of the substring
    locations = get_locations(string, substring)
    if not locations:
        return string

    # Collapse overlapping locations
    collapsed = collapse_locations(locations, len(substring))

    # Build the result string with underscores
    return build_underscorified_string(string, collapsed)


def get_locations(string, substring):
    locations = []
    start_idx = 0
    while start_idx < len(string):
        next_idx = string.find(substring, start_idx)
        if next_idx == -1:
            break
        locations.append([next_idx, next_idx + len(substring)])
        start_idx = next_idx + 1
    return locations


def collapse_locations(locations, substr_len):
    if not locations:
        return []

    collapsed = [locations[0]]
    for i in range(1, len(locations)):
        curr = locations[i]
        prev = collapsed[-1]

        if curr[0] <= prev[1]:
            # Overlapping or adjacent substrings
            prev[1] = curr[1]
        else:
            # Non-overlapping substring
            collapsed.append(curr)

    return collapsed


def build_underscorified_string(string, locations):
    result = []
    string_idx = 0
    loc_idx = 0

    while string_idx < len(string) and loc_idx < len(locations):
        if string_idx == locations[loc_idx][0]:
            result.append("_")

        result.append(string[string_idx])

        if string_idx == locations[loc_idx][1] - 1:
            result.append("_")
            loc_idx += 1

        string_idx += 1

    # Handle remaining string characters
    result.append(string[string_idx:])

    return "".join(result)


string = "testthis is a testtest to see if testestest it works"
substring = "test"
print(underscorifySubstring(string, substring))
