import csv


def load_data(filepath: str) -> list[dict]:
    with open(filepath, newline="") as f:
        return [
            {
                "machine_id":  row["machine_id"].strip(),
                "day":         int(row["day"]),
                "temperature": float(row["temperature"]),
                "cpu_usage":   float(row["cpu_usage"]),
                "vibration":   float(row["vibration"]),
                "pressure":    float(row["pressure"]),
            }
            for row in csv.DictReader(f)
        ]


def group_by_machine(records: list[dict]) -> dict:
    machines: dict = {}
    for r in records:
        machines.setdefault(r["machine_id"], []).append(r)
    for mid in machines:
        machines[mid].sort(key=lambda r: r["day"])
    return machines
