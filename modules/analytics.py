import statistics


def calculate_averages(records: list[dict]) -> dict:
    total = len(records)
    return {
        "temperature": round(statistics.mean(r["temperature"] for r in records), 1),
        "cpu_usage":   round(statistics.mean(r["cpu_usage"]   for r in records), 1),
        "vibration":   round(statistics.mean(r["vibration"]   for r in records), 1),
    }


def detect_anomalies(machines: dict, thresholds: dict) -> list:
    return sorted(
        mid for mid, records in machines.items()
        if max(r["temperature"] for r in records) > thresholds["temperature"]
        or max(r["vibration"]   for r in records) > thresholds["vibration"]
        or max(r["cpu_usage"]   for r in records) > thresholds["cpu_usage"]
    )


def _is_increasing(values: list) -> bool:
    return all(values[i] < values[i + 1] for i in range(len(values) - 1))


def detect_degradation(machines: dict) -> list:
    degradation = []
    for mid, records in sorted(machines.items()):
        if _is_increasing([r["cpu_usage"]  for r in records]):
            degradation.append(f"{mid} CPU usage increasing continuously")
        if _is_increasing([r["vibration"]  for r in records]):
            degradation.append(f"{mid} vibration increasing continuously")
    return degradation
