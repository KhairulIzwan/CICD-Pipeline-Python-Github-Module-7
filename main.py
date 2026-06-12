# =========================================
# Production Engineering Analytics Framework
# =========================================

import json
import os
import sys

# --- Ensure modules/ is importable ---
BASE_DIR = os.path.dirname(__file__)
sys.path.insert(0, BASE_DIR)

from modules.logger_config  import setup_logger
from modules.reader         import load_data, group_by_machine
from modules.analytics      import calculate_averages, detect_anomalies, detect_degradation
from modules.visualization  import generate_charts
from modules.reporting      import save_report, print_report

# --- Load configuration ---
CONFIG_FILE = os.path.join(BASE_DIR, "config", "settings.json")
with open(CONFIG_FILE) as f:
    config = json.load(f)

thresholds = config["thresholds"]
paths      = config["paths"]

DATA_FILE    = os.path.join(BASE_DIR, paths["data"])
LOG_FILE     = os.path.join(BASE_DIR, paths["logs"])
REPORT_FILE  = os.path.join(BASE_DIR, paths["reports"])
CHARTS_DIR   = os.path.join(BASE_DIR, paths["charts"])

# --- Setup logger ---
logger = setup_logger(LOG_FILE)
logger.info("Production Analytics Framework started")

# --- Run pipeline ---
logger.info(f"Loading data from: {DATA_FILE}")
records  = load_data(DATA_FILE)
machines = group_by_machine(records)

averages    = calculate_averages(records)
anomalies   = detect_anomalies(machines, thresholds)
degradation = detect_degradation(machines)

logger.info(f"Records processed: {len(records)}")
logger.info(f"Anomaly machines: {anomalies}")

charts = generate_charts(machines, CHARTS_DIR, thresholds["vibration"])
logger.info(f"Charts generated: {charts}")

save_report(REPORT_FILE, len(records), averages, anomalies, degradation, charts)
logger.info(f"Report saved: {REPORT_FILE}")

print_report(len(records), averages, anomalies, degradation,
             charts + [os.path.basename(REPORT_FILE), os.path.basename(LOG_FILE)])

logger.info("Framework completed successfully")
