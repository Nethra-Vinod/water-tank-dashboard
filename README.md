# AquaVision – Smart Water Tank Monitoring System

AquaVision is a cloud-connected water level monitoring system built using **ESP32** and a **real-time web dashboard**.  
The system enables remote monitoring of overhead water tanks through a single browser link, without requiring any local server or continuous manual operation.

This project was designed with real-world deployment in mind, focusing on **reliability, accessibility, and automation**.

---

## Key Features

- Real-time water level monitoring using ESP32
- Cloud-hosted dashboard accessible from anywhere
- Fully automated operation after initial setup
- No local laptop or server required at the installation site
- Dynamic dashboard with live updates
- Works across mobile, tablet, and desktop browsers
- Scalable architecture for future extensions

---

## Technology Stack

### Hardware
- ESP32 microcontroller  
- Water level sensor (float switch / simulated during testing)

### Software & Cloud
- Python (Flask)
- HTML, CSS, JavaScript
- Tailwind CSS
- Render (cloud deployment)
- GitHub (version control)

---

## System Architecture

- ESP32 sends water level data to the cloud using HTTP requests
- Flask backend processes and stores the latest reading
- The dashboard periodically fetches data and updates the UI
- End users only need to open a single URL to view tank status

---

## Live Dashboard

**URL:**  
https://water-tank-dashboard.onrender.com

> Note: On free cloud hosting, the first load may take a few seconds if the service was idle.

---

## Operational Flow

1. ESP32 connects to the available Wi-Fi network
2. Water level data is read from the sensor (or simulated input)
3. Data is transmitted to the cloud backend
4. Backend updates the latest tank status
5. Dashboard fetches updated values automatically and refreshes the display

Once deployed, the system runs continuously without manual intervention.

---

## Deployment Status

- Cloud backend successfully deployed
- Dashboard live and publicly accessible
- ESP32-to-cloud communication verified
- Sensor integration tested using simulated input

---

## Potential Enhancements

- Alert notifications for low or critical water levels
- Historical data logging and analytics
- Support for multiple tanks
- Authentication and access control
- Offline fallback indicators

---
