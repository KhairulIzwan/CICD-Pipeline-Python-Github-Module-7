import pandas as pd


def analyze_machine_data(file_name):
    df = pd.read_csv(file_name)

    alerts = df[
        (df["temperature"] > 80) |
        (df["vibration"]   > 5)  |
        (df["cpu_usage"]   > 75)
    ]

    return alerts


if __name__ == "__main__":
    # CSV lives in data/ folder relative to this script
    result = analyze_machine_data("data/machine_performance.csv")

    print("\nMachines requiring attention:\n")
    print(result.to_string(index=False))

    result.to_csv("machine_alert_report.csv", index=False)
    print("\nReport generated successfully.")
