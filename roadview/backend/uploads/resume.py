def next_part(session):
    """First part number the truck still has to send (parts are 1-based and contiguous)."""
    n = 1
    while n in session.parts:
        n += 1
    return n
