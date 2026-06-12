import os


def save_report(filepath: str, total: int, averages: dict,
                anomalies: list, degradation: list, charts: list) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write("========= PRODUCTION ANALYTICS FRAMEWORK =========\n\n")
        f.write(f"Total Records Processed : {total}\n")
        f.write(f"Average Temperature     : {averages['temperature']} C\n")
        f.write(f"Average CPU Usage       : {averages['cpu_usage']} %\n")
        f.write(f"Average Vibration       : {averages['vibration']}\n\n")
        f.write("Anomaly Machines:\n")
        for m in anomalies:
            f.write(f"  - {m}\n")
        f.write("\nPerformance Degradation:\n")
        for d in degradation:
            f.write(f"  - {d}\n")
        f.write("\nGenerated Outputs:\n")
        for c in charts:
            f.write(f"  - {c}\n")


def print_report(total: int, averages: dict,
                 anomalies: list, degradation: list, charts: list) -> None:
    SEP = "=" * 50
    print(SEP)
    print("    PRODUCTION ANALYTICS FRAMEWORK")
    print(SEP)
    print(f"Total Records Processed : {total}")
    print(f"Average Temperature     : {averages['temperature']} C")
    print(f"Average CPU Usage       : {averages['cpu_usage']} %")
    print(f"Average Vibration       : {averages['vibration']}")
    print()
    print("Anomaly Machines:")
    for m in anomalies:
        print(f"  - {m}")
    print()
    print("Performance Degradation:")
    for d in degradation:
        print(f"  - {d}")
    print()
    print("Generated Outputs:")
    for c in charts:
        print(f"  - {c}")
    print(SEP)
