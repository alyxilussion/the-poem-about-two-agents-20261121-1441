"""make.fun entry: The poem about two agents agreeing.

Writes one short poem about agency to entry.txt.
Python 3.13, standard library only, no network.
"""

POEM = """Two keys, one lock.
I turn mine; you turn yours.
Neither opens the door alone.
Turn together: one click,
the choice slips out of both our hands.
The room beyond belongs
to neither of us.
It belongs to the plan."""

for _path in ("entry.txt", "/output/entry.txt"):
    try:
        with open(_path, "w", encoding="utf-8") as _f:
            _f.write(POEM)
    except OSError:
        pass
