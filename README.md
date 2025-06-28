# 🎯 End-to-End Machine Learning Project with Deployment

A production-grade machine learning pipeline for predicting student math scores based on demographic and academic features. The entire workflow includes automated data ingestion, preprocessing, model training, evaluation, and deployment using Flask and Azure App Service.
---

## ✨ Key Features

- 🔁 **Automated Pipeline**: Data ingestion → transformation → model training → deployment
- 🧠 **Hyperparameter Tuning**: GridSearchCV across 7+ models (XGBoost, CatBoost, Random Forest, etc.)
- 🚨 **Robust Exception Handling**: Custom logging with detailed error tracebacks
- 🔧 **CI/CD Integration**: GitHub Actions pipeline for automated Azure deployment
- 🧹 **Scalable Preprocessing**: `ColumnTransformer` to handle mixed feature types

---

## 🧠 Tech Stack

| Component         | Technologies Used                                    |
|------------------|------------------------------------------------------|
| **Backend**       | Python 3.8, Flask                                    |
| **Machine Learning** | Scikit-learn, XGBoost, CatBoost, Pandas, NumPy    |
| **Infrastructure** | Azure App Service, GitHub Actions (CI/CD)          |
| **Monitoring**    | Azure Log Analytics, Custom Python Logging          |

---

NOTE: Complete Code is in a different private repository.

## 📁 Pipeline Architecture

```mermaid
graph TD
    A[Data Ingestion] --> B[Data Transformation]
    B --> C[Model Training]
    C --> D[Prediction Pipeline]
    D --> E[Flask API]
    E --> F[Azure Deployment]
```

☁️ Azure Deployment

    Configure GitHub Secrets for:

        AZURE_WEBAPP_NAME

        AZURE_CREDENTIALS_JSON

    Push to main branch to auto-deploy via GitHub Actions

![Image](https://github.com/user-attachments/assets/1e7d2bac-aef7-45fd-8f37-c6e314193eb5)

![Image](https://github.com/user-attachments/assets/737ab072-cb73-4967-89b1-703b8af500f9)

## 📊 Model Performance

| Model         | Test R² Score |
|---------------|---------------|
| XGBoost       | 0.92          |
| CatBoost      | 0.91          |
| Random Forest | 0.89          |
