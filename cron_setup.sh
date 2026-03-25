#!/bin/bash

# This bash script sets up cron jobs and systemd service for automated PV charging execution.

# Define the path to the charging script
CHARGING_SCRIPT_PATH="/path/to/charging_script.sh"

# Create a systemd service for the charging execution
cat <<EOL > /etc/systemd/system/pv_charging.service
[Unit]
Description=Automated PV Charging Service

[Service]
Type=simple
ExecStart=/bin/bash $CHARGING_SCRIPT_PATH

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd to recognize the new service
systemctl daemon-reload

# Enable the service to start on boot
systemctl enable pv_charging.service

# Schedule the cron job to run the charging script every day at 6 AM
(crontab -l 2>/dev/null; echo "0 6 * * * /bin/bash $CHARGING_SCRIPT_PATH") | crontab -