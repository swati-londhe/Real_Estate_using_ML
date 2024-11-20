# Real Estate Price Prediction and Analysis 🏠📊

## Project Description
This project focuses on performing an **Exploratory Data Analysis (EDA)** on real estate data to derive actionable insights about property prices, characteristics, and trends. It also includes predictive modeling for house and flat prices based on key features. The analysis and predictions aim to assist users in making informed decisions in the real estate market.

---

## Features of the Analysis

### **Data Collection**
- Data sourced via web scraping from real estate websites.
- Includes properties like flats and houses with various features.

### **Data Cleaning**
- Handled missing values.
- Standardized categorical variables (e.g., property types, luxury categories).

### **Feature Engineering**
- Added derived features such as `Built_Up_Area`, `Property Age`, and categorical classifications.

### **Visualization**
- Distribution plots for numerical variables.
- Bar plots for categorical variables.
- Correlation heatmap to analyze relationships.

### **Statistical Insights**
- Skewness reduction using log transformations.
- Grouped aggregations for analyzing price patterns based on location, type, and more.

---

## Tools and Libraries Used
- **Programming Language**: Python
- **Data Analysis**: Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn
- **Web App Deployment**: Streamlit
- **Machine Learning**: Scikit-learn

---

## Key Insights
- Location and luxury category are significant factors influencing property prices.
- Log transformations effectively normalized features like `Built_Up_Area` and price.
- Older properties are generally priced lower, but luxury and furnishing significantly impact valuations.

---

## Visuals
The analysis includes:
- **Histograms and Boxplots**: To explore numerical feature distributions.
- **Bar Charts**: To compare categories like `Furnishing Type` and `Property Type`.
- **Correlation Heatmap**: To identify relationships between features and target price.

---

## How to Run

1. Clone the repository:
   git clone https://github.com/yourusername/real-estate-eda.git

2. Ensure the required files are in place:
df.pkl: Processed dataset.
pipeline.pkl: Machine learning pipeline.

3.Install dependencies:
pip install pandas numpy matplotlib seaborn streamlit scikit-learn

4.Run the Streamlit application:
streamlit run 1_PricePredictor.py
