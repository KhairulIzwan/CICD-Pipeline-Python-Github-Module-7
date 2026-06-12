# Module 7 – Production Engineering Analytics Framework

## Problem Statement

The engineering analytics script developed in Module 6 works successfully.

However, the current implementation has several production problems:

- All code exists in one large file
- Thresholds are hardcoded
- No configuration management
- Difficult to reuse across teams
- No centralized logging
- No modular architecture
- Difficult to maintain and scale

Engineering management now wants a production-ready automation framework that can:

- Process engineering datasets reliably
- Support reusable modules
- Use external configuration files
- Generate structured logs
- Produce analytics reports automatically
- Be maintainable across engineering teams

The task is to refactor the Module 6 project into a production-ready automation architecture.

---

## Outcome Expected from Engineers

At the end of this lab, engineers should be able to:

- Design modular Python projects
- Create reusable automation libraries
- Separate configuration from code
- Use logging frameworks properly
- Implement structured project architecture
- Build maintainable engineering scripts
- Package scripts for team usage
- Apply production engineering practices

---

## Final Project Architecture

```
Module 7/
│
├── config/
│   └── settings.json
│
├── data/
│   └── machine_performance.csv
│
├── logs/
│   └── automation.log
│
├── reports/
│   └── analytics_summary.txt
│
├── charts/
│   ├── temperature_trend.png
│   ├── cpu_usage_trend.png
│   └── vibration_analysis.png
│
├── modules/
│   ├── reader.py
│   ├── analytics.py
│   ├── visualization.py
│   ├── reporting.py
│   └── logger_config.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Expected Output

```
==================================================
    PRODUCTION ANALYTICS FRAMEWORK
==================================================
Total Records Processed : 25
Average Temperature     : 76.4 C
Average CPU Usage       : 63.6 %
Average Vibration       : 4.5

Anomaly Machines:
  - M102
  - M105

Generated Outputs:
  - analytics_summary.txt
  - automation.log
  - temperature_trend.png
==================================================
```

---

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the framework
python main.py
```

---

## Module Responsibilities

| Module | Responsibility |
|---|---|
| `config/settings.json` | External thresholds and path configuration |
| `modules/reader.py` | Load and normalise CSV data |
| `modules/analytics.py` | Anomaly detection and degradation analysis |
| `modules/visualization.py` | Chart generation |
| `modules/reporting.py` | Summary report generation |
| `modules/logger_config.py` | Centralised logging setup |
| `main.py` | Entry point — orchestrates all modules |

---

## Files

| File | Description |
|---|---|
| `main.py` | Framework entry point |
| `config/settings.json` | External configuration file |
| `data/machine_performance.csv` | Input dataset |
| `reports/analytics_summary.txt` | Analytics report (generated) |
| `logs/automation.log` | Execution log (generated) |
| `charts/*.png` | Generated visualisation charts |
| `requirements.txt` | Python dependencies |
| `README.md` | Lab instructions and architecture reference |
