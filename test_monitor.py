from monitor import analyze_machine_data


def test_alert_generation():
    # CSV lives in data/ folder relative to project root
    result = analyze_machine_data("data/machine_performance.csv")

    # Must generate at least one alert row
    assert len(result) > 0, "Expected alert records but got none"
