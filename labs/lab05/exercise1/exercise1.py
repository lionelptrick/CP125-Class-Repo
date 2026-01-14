
def was_backward_detected(waypoints):

    for i in range(len(waypoints) - 1):
        x1, y1, z1 = waypoints[i]
        x2, y2, z2 = waypoints[i + 1]

        if x2 < x1 or y2 < y1:
            return True
    return False
        
    