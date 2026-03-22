def deployment_status(statuses: list):
    if set(statuses) == {True}:
        return "SUCCESS"

    failure_percentage = statuses.count(False) / len(statuses) * 100
    if failure_percentage > 30:
        return "FAILURE"

    return "PARTIAL"


print(deployment_status([True, True, False, True, False]))  # → "PARTIAL"
print(deployment_status([True, True, True, True]))  # → "SUCCESS"
print(deployment_status([False, False, False, True, True]))  # → "FAILURE"
