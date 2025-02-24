# Café Profit Forecast

This project aims to predict the net profit of café franchises based on various features such as location, business type, sales, and customer count. The model uses a **Decision Tree Regressor** for prediction.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Code Explanation](#code-explanation)
4. [Results](#results)
5. [How to Use](#how-to-use)
6. [Dependencies](#dependencies)
7. [Author Contact](#author-contact)

---

## **Project Overview**
The goal of this project is to build a predictive model that forecasts the net profit of café franchises. The model uses features like:
- Counter Sales
- Drive-through Sales
- Number of Customers
- Location (Richmond, Vancouver)
- Business Type (Burger Store, Café, Pizza Store)

---

## **Dataset**
The dataset is stored in an Excel file (`Franchises Dataset.xlsx`) and contains the following columns:
- `Counter Sales`
- `Drive-through Sales`
- `number of customers`
- `Location` (Categorical: Richmond, Vancouver)
- `Business Type` (Categorical: Burger Store, Café, Pizza Store)
- `Net Profit` (Target Variable)

---

## **Code Explanation**
The code performs the following steps:
1. **Data Loading**: The dataset is loaded using `pandas.read_excel()`.
2. **Data Preprocessing**: Categorical variables (`Location` and `Business Type`) are converted into dummy variables using `pandas.get_dummies()`.
3. **Model Training**: A `DecisionTreeRegressor` is trained on the first 81 rows of the dataset.
4. **Model Evaluation**: The model is evaluated using Mean Absolute Percentage Error (MAPE).
5. **Prediction**: The model predicts the net profit for a sample input.

---

## **Results**
- **Mean Absolute Percentage Error (MAPE)**: `{mape:.2f}%`
- **Key Column Means**:
  - Counter Sales: `{means['Counter Sales']:.2f}`
  - Drive-through Sales: `{means['Drive-through Sales']:.2f}`
  - Number of Customers: `{means['Number of Customers']:.2f}`
  - Location_Richmond: `{means['Location_Richmond']:.2f}`
  - Location_Vancouver: `{means['Location_Vancouver']:.2f}`
  - Business Type_Burger Store: `{means['Business Type_Burger Store']:.2f}`
  - Business Type_Café: `{means['Business Type_Café']:.2f}`
  - Business Type_Pizza Store: `{means['Business Type_Pizza Store']:.2f}`

---

## **How to Use**
1. Clone the repository:
   ```bash
   git clone https://github.com/FelipeLeiteDS/Cafe-Profit-Forecast.git

---

## **Dependencies**
- Python 3.12.7
- Libraries:
  - `pandas`
  - `scikit-learn`

---

## **Author Contact**
For questions or collaboration opportunities, feel free to reach out:  
Name: Felipe Leite  
Email: felipe.nog.leite@gmail.com  
LinkedIn: [Felipe Leite](https://www.linkedin.com/in/felipeleiteds/)  
Portfolio: [FelipeLeite.ca](https://www.felipeleite.ca/)  
