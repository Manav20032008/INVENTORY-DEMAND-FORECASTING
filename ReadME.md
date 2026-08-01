# 📦 Inventory Demand Forecasting

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

### Predict future inventory demand using Machine Learning to minimize stockouts, reduce excess inventory, and improve supply chain efficiency.

</div>

---

# 📖 Overview

Inventory management is one of the most critical challenges in retail and supply chain operations. Overstocking increases storage costs, while understocking results in lost sales and poor customer satisfaction.

This project leverages **Machine Learning** to forecast product demand using historical sales and inventory data. The predictions help businesses make smarter inventory decisions and optimize stock levels.

---

# 🚀 Features

- 📊 Data Cleaning & Preprocessing
- 📈 Exploratory Data Analysis (EDA)
- 🔍 Feature Engineering
- 🤖 Machine Learning Based Demand Forecasting
- 📉 Model Performance Evaluation
- 📦 Inventory Demand Prediction
- 📋 Data Visualization
- 📊 Business Insights

---

# 🏗 Project Structure

```text
INVENTORY-DEMAND-FORECASTING/
│
├── alembic/                  # Database migrations
├── artifacts/                # Trained models, metrics & metadata
│   ├── feature_columns.pkl
│   ├── metrics.json
│   ├── model_metadata.json
│   └── xgb_model.pkl
│
├── backend/                  # FastAPI backend
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── exceptions/
│   ├── logging/
│   ├── middleware/
│   ├── models/
│   ├── repositories/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── tests/
│   └── app.py
│
├── config/                   # YAML configuration files
│
├── data/
│   ├── raw/                  # Raw dataset
│   ├── processed/            # Processed data
│   └── Intermeadiate/        # Intermediate datasets
│
├── frontend/                 # React + Vite frontend
│   ├── components/
│   ├── hooks/
│   ├── layouts/
│   ├── pages/
│   ├── routes/
│   ├── services/
│   ├── styles/
│   └── main.jsx
│
├── notebooks/                # Experiment notebooks
│
├── src/                      # Machine Learning pipeline
│   ├── preprocessing/
│   ├── feature_engineering/
│   ├── models/
│   ├── pipeline/
│   └── evaluation/
│
├── tests/                    # Unit tests
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── package.json
└── README.md
```

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| **Programming Language** | Python, JavaScript |
| **Machine Learning** | XGBoost, LightGBM, Scikit-learn |
| **Data Processing** | Pandas, NumPy |
| **Feature Engineering** | Custom Feature Engineering, Lag Features, Rolling Features, Date-based Features |
| **Backend** | FastAPI, Uvicorn |
| **Frontend** | React, Vite, React Router, Axios |
| **Data Visualization** | Recharts |
| **Database & ORM** | SQLAlchemy, Alembic |
| **Configuration** | YAML |
| **Model Serialization** | Pickle (.pkl) |
| **API Validation** | Pydantic |
| **Containerization** | Docker, Docker Compose |
| **Testing** | Pytest |
| **Notebook** | Jupyter Notebook |
| **Version Control** | Git & GitHub |

---

# 📚 API Documentation

The backend is built with **FastAPI**, which automatically generates interactive API documentation.

After starting the backend server, you can access:

| Documentation | URL |
|--------------|-----|
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |
| OpenAPI Schema | http://localhost:8000/openapi.json |

### Start the Backend

```bash
cd backend

uvicorn app:app --reload
```

or

```bash
uvicorn backend.app:app --reload
```

(depending on your project structure)

Once the server is running, open your browser and visit:

```
http://localhost:8000/docs
```

### Available API Features

- 🔮 Demand Prediction
- 📊 Analytics Dashboard
- 📜 Prediction History
- ❤️ Health Check
- 📈 Model Insights

All endpoints are documented with:

- Request Body Schema
- Response Schema
- Status Codes
- Validation Errors
- Example Requests
- Example Responses

The API documentation is generated automatically from FastAPI using the OpenAPI specification, ensuring it always stays synchronized with the backend implementation.

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Manav20032008/INVENTORY-DEMAND-FORECASTING.git
```

Move into the project directory

```bash
cd INVENTORY-DEMAND-FORECASTING
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

If using Python:

```bash
python main.py
```

If using Jupyter Notebook:

```bash
jupyter notebook
```

Open the notebook and execute all cells.

---

# 📊 Workflow

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Train ML Model
      │
      ▼
Evaluate Performance
      │
      ▼
Demand Prediction
      │
      ▼
Inventory Recommendation
```

---

# 📈 Machine Learning Pipeline

The forecasting pipeline includes:

- Data preprocessing
- Handling missing values
- Feature encoding
- Feature scaling (if required)
- Model training
- Model evaluation
- Future demand prediction

---

# 📉 Evaluation Metrics

The model can be evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

# 📷 Sample Output


```
screenshots/

├── dashboard.png
├── prediction.png
├── feature_importance.png
└── forecast_plot.png
```

Example:

```markdown
![Dashboard](screenshots/dashboard.png)
```

---

# 📊 Business Benefits

This project helps businesses:

- Reduce stock shortages
- Minimize overstock inventory
- Improve warehouse efficiency
- Reduce operational costs
- Improve customer satisfaction
- Make data-driven inventory decisions

---

# 📚 Future Improvements

- Deep Learning (LSTM)
- Facebook Prophet
- XGBoost
- LightGBM
- Real-time Prediction API
- Streamlit Dashboard
- Docker Deployment
- AWS Deployment
- Automated Model Retraining
- MLOps Pipeline

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# ⭐ If you like this project

Give it a ⭐ on GitHub.

---

# 👨‍💻 Author

**Manav**

- GitHub: https://github.com/Manav20032008

---

# 📜 License

This project is licensed under the MIT License.

---

<div align="center">

### ⭐ Thank you for visiting this repository!

**Made with ❤️ using Python & Machine Learning**

</div>