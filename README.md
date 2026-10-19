# EV Battery State of Health (SOH) Prediction

## Project Overview
This project focuses on predicting the State of Health (SOH) of electric vehicle batteries using machine learning techniques. It includes a Python-based application built with Streamlit to present battery-related information and prediction results through a user-friendly interface.

## Features
- Machine-learning-based battery health prediction.
- Battery diagnostics and remaining useful life (RUL) related functionality.
- EV service center information.
- Interactive interface built using Streamlit.
- Visual assets and vehicle-related information.

## Technologies Used
- Python
- Machine Learning
- Streamlit
- Pandas
- Scikit-learn
- Pickle (`.pkl`) for saved model files

## Project Structure
- `Home.py` — Main application interface.
- `model_training.py` — Model training code.
- `1_Daily_Health_Check.py` — Daily battery health check page.
- `2_Advanced_Battery_Diagnostics.py` — Advanced diagnostics page.
- `3_Find_Nearby_EV_Service.py` — EV service information page.
- `4_About_This_Project.py` — Project information page.
- `ev_service_centers.csv` — EV service center data.
- `.pkl` files — Saved machine learning models.

## How to Run
1. Clone or download this repository.
2. Install the required Python packages.
3. Run the Streamlit application using:

```bash
streamlit run Home.py
```

Note: The application requires its dependencies, data files, and compatible trained model files to run correctly.

## Project Purpose
This project helped me apply Python programming, data processing, and machine learning concepts to an electric vehicle battery health use case.
