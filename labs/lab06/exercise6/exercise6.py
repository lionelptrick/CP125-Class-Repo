def manage_roster(enrolled, drop_requests, waitlist):

    for student in drop_requests:
        if student in enrolled:
            enrolled.remove(student)

    if len(enrolled) < 5:
        while len(enrolled) < 7 and waitlist:
            enrolled.add(waitlist.pop())

    return len(enrolled)

    """
    Processes student drop requests and adds from waitlist if needed.
    
    Args:
        enrolled: Set of currently enrolled student names
        drop_requests: List of student names requesting to drop
        waitlist: Set of students on the waitlist
    
    Returns:
        int: Count of final enrolled students
    """
    pass
