def get_most_errors():
    logs = [
        "2026-03-17 10:00:01 INFO user=alice action=login",
        "2026-03-17 10:01:05 ERROR user=bob action=checkout",
        "2026-03-17 10:02:00 INFO user=alice action=view",
        "2026-03-17 10:03:33 ERROR user=alice action=checkout",
        "2026-03-17 10:04:12 INFO user=bob action=view",
        "2026-03-17 10:05:00 ERROR user=alice action=checkout",
    ]
    names_with_errors = [log.split()[3].split("=")[1] for log in logs if "ERROR" in log]
    maps = {}
    for name in names_with_errors:
        if not maps.get(name):
            maps[name] = 0
        maps[name] += 1

    return max(maps, key=maps.get)


print(get_most_errors())
