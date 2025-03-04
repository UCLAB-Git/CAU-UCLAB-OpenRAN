# OpenRAN-based Traffic Steering
Welcome to the UCLAB Open-RAN repository!

<img 
  src="https://img.shields.io/github/stars/UCLAB-Git/CAU-UCLAB-OpenRAN?style=social" 
  alt="GitHub stars"
  width="120"
/>
<img 
  src="https://img.shields.io/github/watchers/UCLAB-Git/CAU-UCLAB-OpenRAN?style=social" 
  alt="GitHub stars"
  width="120"
/>

<img 
  src="https://img.shields.io/github/license/UCLAB-Git/CAU-UCLAB-OpenRAN?style=social" 
  alt="GitHub stars"
  width="120"
/>

## Overview
This repository provides a sample implementation of **traffic steering** based on **Open-RAN** architecture.  
The goal is to dynamically redistribute network traffic across multiple cells (or DUs) to optimize Quality of Service (QoS) and resource utilization.

## Features
- **Dynamic Steering Algorithm**: Automatically adjusts traffic load based on real-time cell utilization.
- **QoS-Aware**: Monitors throughput, latency, or other KPIs to steer traffic where needed.
- **Extensible Design**: Can be integrated with O-RAN SC (Near-RT RIC, rApps) or other OpenRAN components.

## Structure


## Installation - Quick Start
If you want to install the our system, follow these steps:
1. **Clone**:
   ```bash
   git clone https://github.com/UCLAB-Git/CAU-UCLAB-OpenRAN.git
2. **Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the example**
   ```bash
   python src/example.py
   ```
