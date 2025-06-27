import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import r2_score

from src.utils import save_object
from src.exception import CustomException
from src.logger import logging


def load_data():
    try:
        df = pd.read_csv("notebook\data\stud.csv")  # Update path if needed
        df["total_score"] = df["math_score"] + df["reading_score"] + df["writing_score"]
        df["average"] = df["total_score"] / 3
        return df
    except Exception as e:
        raise CustomException(e, sys)


def build_preprocessor():
    try:
        categorical_cols = ["gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preparation_course"]
        numerical_cols = ["reading_score", "writing_score"]

        # Pipelines
        num_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", StandardScaler())
        ])

        cat_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ("scaler", StandardScaler(with_mean=False))
        ])

        preprocessor = ColumnTransformer([
            ("num_pipeline", num_pipeline, numerical_cols),
            ("cat_pipeline", cat_pipeline, categorical_cols)
        ])

        return preprocessor
    except Exception as e:
        raise CustomException(e, sys)


def train_and_save():
    try:
        df = load_data()

        X = df.drop(columns=["math_score", "total_score", "average"])
        y = df["math_score"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        preprocessor = build_preprocessor()

        model = Pipeline([
            ("preprocessor", preprocessor),
            ("regressor", LinearRegression())
        ])

        model.fit(X_train, y_train)

        # Evaluate
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)

        train_r2 = r2_score(y_train, y_train_pred)
        test_r2 = r2_score(y_test, y_test_pred)

        logging.info(f"Train R2 Score: {train_r2}")
        logging.info(f"Test R2 Score: {test_r2}")

        # Extract fitted preprocessor and model for saving
        fitted_preprocessor = model.named_steps["preprocessor"]
        fitted_model = model.named_steps["regressor"]

        os.makedirs("artifacts", exist_ok=True)

        save_object("artifacts/preprocessor.pkl", fitted_preprocessor)
        save_object("artifacts/model.pkl", fitted_model)

        print("✅ Model and preprocessor saved successfully in 'artifacts/' folder.")

    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    train_and_save()
