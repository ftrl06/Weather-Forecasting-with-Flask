# Weather Forecasting with Flask

This project demonstrates weather forecasting using machine learning and Flask. It reads weather data from a CSV file, trains a machine learning model, and serves predictions through a web application.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ftrl06/Weather-Forecasting-with-Flask.git
    ```

2. Navigate to the project directory:
    ```bash
    cd weather_forecasting
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Train the model:
    ```bash
    python model/train_model.py
    ```

2. Run the Flask app:
    ```bash
    export FLASK_APP=app
    flask run
    ```

3. Open your browser and navigate to `http://127.0.0.1:5000/`.

## Testing

Run the tests:
```bash
python -m unittest discover tests



#### 3. `data/weather_data.csv`

This file contains weather data. Sample data can be in the following format:

```csv
date,temperature,humidity,pressure,wind_speed,weather
2024-08-01,30,85,1012,5,clear
2024-08-02,28,80,1013,6,cloudy
...