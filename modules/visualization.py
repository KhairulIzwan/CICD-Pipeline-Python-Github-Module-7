import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def generate_charts(machines: dict, charts_dir: str, vibration_threshold: float) -> list:
    os.makedirs(charts_dir, exist_ok=True)
    days   = sorted({r["day"] for records in machines.values() for r in records})
    charts = []

    def save_chart(metric, title, ylabel, filename, threshold=None):
        plt.figure(figsize=(10, 5))
        for mid, records in sorted(machines.items()):
            plt.plot(days, [r[metric] for r in records], marker="o", label=mid)
        if threshold is not None:
            plt.axhline(y=threshold, color="red", linestyle="--", label="Threshold")
        plt.title(title)
        plt.xlabel("Day")
        plt.ylabel(ylabel)
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(charts_dir, filename))
        plt.close()
        charts.append(filename)

    save_chart("temperature", "Temperature Trend by Machine",  "Temperature (°C)", "temperature_trend.png")
    save_chart("cpu_usage",   "CPU Usage Trend by Machine",    "CPU Usage (%)",    "cpu_usage_trend.png")
    save_chart("vibration",   "Vibration Analysis by Machine", "Vibration",        "vibration_analysis.png", vibration_threshold)

    return charts
