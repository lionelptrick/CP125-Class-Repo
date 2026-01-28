def synchronize_databases(legacy_list, modern_set, blacklist):

    sanitize_legacy_set = set()

    for record_id, email in legacy_list:
        if email not in blacklist:
            sanitize_legacy_set.add(record_id)

    lost_id = sanitize_legacy_set - modern_set
    ghost_id = modern_set - sanitize_legacy_set

    return lost_id, ghost_id


legacy = [(1, "a@b.com"), (2, "c@d.com")]
modern = {1, 3}
lost, ghost = synchronize_databases(legacy, modern, set())