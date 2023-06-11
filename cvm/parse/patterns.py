MAIN_PART_PATTERN: str = r"^((\w+)?(\/)?(\w+)?(\(\w+\))?:)?(.+)$"
"""
Groups:
    0: meta information, groups 1-4 are stored inside
    1: project
    2: separation `/`
    3: type
    4: module
    5: text

Note that on meta information group searching failure, everything is going to
be written in group #5, which is desired, for example at
`orwynn/re-fa-c-tor: mytext`.
"""
