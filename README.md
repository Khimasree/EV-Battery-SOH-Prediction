# EV Battery State of Health (SOH) Prediction

## Overview
An electric vehicle (EV) battery health prediction project that uses machine learning to support battery State of Health (SOH) estimation and related diagnostics. The project includes a Streamlit-based interface for presenting battery information and prediction results.

## Features
- Machine-learning-based battery State of Health (SOH) prediction.
- Battery diagnostics and remaining useful life (RUL)-related functionality.
- EV service center information.
- Interactive multi-page web interface built with Streamlit.
- Vehicle-related images and visual information.

## Technologies Used
- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas
- **Web Application:** Streamlit
- **Model Storage:** Pickle (`.pkl` files)
- **Data Storage:** CSV

## Project Structure

```text
EV-Battery-SOH-Prediction/
├── Home.py
├── model_training.py
├── 1_Daily_Health_Check.py
├── 2_Advanced_Battery_Diagnostics.py
├── 3_Find_Nearby_EV_Service.py
├── 4_About_This_Project.py
├── ev_service_centers.csv
├── battery_soh_model.pkl
├── battery_rul_model.pkl
├── README.md
└── assets/ and vehicle images
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Khimasree/EV-Battery-SOH-Prediction.git
cd EV-Battery-SOH-Prediction
```

### 2. Install the dependencies

Install the Python packages required by the project. For example:

```bash
pip install streamlit pandas scikit-learn
```

Additional packages may be required depending on the imports used in the project files.

### 3. Run the application

```bash
streamlit run Home.py
```

The application should open in your browser when the required dependencies, data files, and compatible trained models are available.

## Project Purpose
This project demonstrates the application of Python and machine learning concepts to an electric vehicle battery health use case. It brings together model training, prediction, battery diagnostics, and a Streamlit-based user interface.

## Repository
[View the source code on GitHub](https://github.com/Khimasree/EV-Battery-SOH-Prediction)
