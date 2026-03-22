cpu_usages = {
    "srv1": [30, 40, 35, 90],
    "srv2": [20, 25, 30, 25],
    "srv3": [80, 85, 90, 95],
    "srv4": [10, 15, 20, 15],
    "srv5": [70, 75, 72, 68],
}


def alert_servers(cpu_usages, threshold):
    exceeded_usages = []
    for server, usages in cpu_usages.items():
        if any(usage > threshold for usage in usages):
            exceeded_usages.append(server)

    return exceeded_usages


print(alert_servers(cpu_usages, 85))
