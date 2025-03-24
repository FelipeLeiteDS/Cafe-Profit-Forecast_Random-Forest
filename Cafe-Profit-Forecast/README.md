# Cafe Profit Forecast

## Overview
The Cafe Profit Forecast project aims to predict the net profit of various cafe franchises using a Random Forest model implemented with a Decision Tree Regressor from the scikit-learn library. The project includes data preprocessing, model training, prediction, and error measurement.

## Project Structure
```
Cafe-Profit-Forecast
├── src
│   └── Random-Forest-Model.py  # Implementation of the Random Forest model
├── Dockerfile                    # Dockerfile for creating the project environment
├── requirements.txt              # Python dependencies for the project
└── README.md                     # Documentation for the project
```

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Docker (if using the Dockerfile)

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd Cafe-Profit-Forecast
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Model
To run the Random Forest model, execute the following command:
```
python src/Random-Forest-Model.py
```

### Using Docker
To build and run the Docker container, use the following commands:
1. Build the Docker image:
   ```
   docker build -t cafe-profit-forecast .
   ```

2. Run the Docker container:
   ```
   docker run cafe-profit-forecast
   ```

## Usage Example
The model can be used to predict net profits based on various input features. An example input for prediction is provided in the `src/Random-Forest-Model.py` file.

## License
This project is licensed under the MIT License.