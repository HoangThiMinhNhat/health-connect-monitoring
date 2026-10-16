# Health Connect Monitoring Solution
Final project for the Software Integration course with 2M-IT company: designing, implementing, testing, and documenting a portable Health Connect monitoring solution integrating InfluxDB and Grafana for centralized metrics collection and visualization.
## Project Structure
```text
health-connect-monitoring/
├── README.md                      # Guide deploying general monitoring system for Health Connect
├── .gitignore                     # Ignore files and directories that should not be tracked by Git
├── monitoring-system/
│   └── docker-compose.yml         # Configuration for Docker containers for InfluxDB v2 & Grafana v12
├── health-connect/
│   └── simulator.py               # Python script for simulating metrics data
└── docs/                          # Directory containing handover documents and guides (WP8)
    ├── influxdb-installation-guide.md
    └── grafana-configuration-guide.md
```
## 🚀 Quick Start

### 1. Launch InfluxDB & Grafana Infrastructure
```bash
cd monitoring-system
docker-compose up -d
```
### 2. Launch Metrics Data Simulator Script
```bash
cd ../health-connect
python simulator.py
```
