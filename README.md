# EV Battery State of Health (SOH) Prediction

## Overview

EV Battery State of Health (SOH) Prediction is a machine learning project designed to support electric vehicle battery health estimation and diagnostics. It includes a multi-page web application built with Streamlit to present battery health information and related features.

## Features

- Machine-learning-based battery State of Health (SOH) prediction.
- Battery diagnostics and Remaining Useful Life (RUL)-related functionality.
- EV service center information.
- Interactive multi-page Streamlit web interface.
- Vehicle-related images and visual information.

## Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas
- **Web Application:** Streamlit
- **Model Storage:** Pickle (`.pkl`)
- **Data Storage:** CSV

## Project Structure

```text
EV-Battery-SOH-Prediction/
├── Home.py
├── model_training.py
├── pages/
│   ├── 1_Daily_Health_Check.py
│   ├── 2_Advanced_Battery_Diagnostics.py
│   ├── 3_Find_Nearby_EV_Service.py
│   └── 4_About_This_Project.py
├── assets/
├── ev_service_centers.csv
├── battery_soh_model.pkl
├── battery_rul_model.pkl
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Khimasree/EV-Battery-SOH-Prediction.git
cd EV-Battery-SOH-Prediction
```

### 2. Install dependencies

```bash
pip install streamlit pandas scikit-learn
```

Install any additional packages required by the project's Python imports.

### 3. Run the application

```bash
streamlit run Home.py
```

The application should open in your browser when the required dependencies, model files, and other project resources are available.

## Project Purpose

This project demonstrates the application of Python and machine learning to an electric vehicle battery health use case. It brings together model training, prediction, battery diagnostics, and an interactive Streamlit interface.

## Repository

[View the source code on GitHub](https://github.com/Khimasree/EV-Battery-SOH-Prediction)
