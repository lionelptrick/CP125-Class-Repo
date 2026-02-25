def apply_upgrade(current, upgrade):
    # TODO: Your code here
    result = current.copy()

    for permission in upgrade:
        if permission in result:
            if upgrade[permission] > result[permission]:
                result[permission] = upgrade[permission]

        else:
            result[permission] = upgrade[permission]
    
    return result
    pass



current = {"read": 2, "write": 1, "admin": 0}
upgrade = {"read": 1, "write": 3, "execute": 2}
result = apply_upgrade(current, upgrade)
print(result)
print(current)   # Should be unchanged
