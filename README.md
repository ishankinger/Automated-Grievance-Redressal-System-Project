# Automated Grievance Redressal Framework

## Overview
This repository contains a modular machine learning pipeline designed to transform unstructured public grievance text into structured, actionable information for administrative decision-making. The system processes complaint data through multiple analytical stages, from initial data cleaning to final resolution-time prediction and citizen feedback analysis.

## Pipeline Modules
The framework is divided into seven sequential stages:
1. **Data Acquisition & Preprocessing:** Cleans and normalizes raw complaint text.
2. **Anomaly Detection:** Filters invalid, spam, and duplicate entries using zero-shot classification and TF-IDF cosine similarity.
3. **Domain Classification:** Routes complaints to the appropriate organizational domain using a Linear SVM classifier.
4. **Keyword Extraction & Summarization:** Extracts representative phrases and generates summaries using YAKE, TextRank, and LexRank.
5. **Severity Risk Scoring:** Estimates complaint urgency utilizing textual and contextual metadata via Linear SVM.
6. **Resolution Time Prediction:** Predicts the expected number of days required to resolve a grievance using an XGBoost Regressor.
7. **Sentiment Analysis:** Evaluates citizen feedback sentiment using weak supervision and text classification.

## Technology Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, scikit-learn, XGBoost, spaCy, YAKE
* **Environment:** Jupyter Notebooks

## Repository Structure
* `00-Data-Acquisition-Analysis/`: Exploratory data analysis and understanding.
* `01-Data-Preprocessing/`: Text cleaning, normalization, and dataset filtering.
* `02-Anomaly-Detection/`: Duplicate and near-duplicate grievance filtering.
* `03-Domain-Classification/`: Complaint domain prediction models.
* `04-Keyword-Extraction/`: Keyword extraction and extractive summarization.
* `05-Severity-Risk-Scoring/`: Urgency prediction and severity classification.
* `06-Resolution-Time-Prediction/`: Resolution-time regression models.
* `07-Sentiment-Analysis/`: Feedback sentiment analysis track.
* `run_pipeline.py`: Main execution script for sequential notebook processing.

## Execution
The system is designed for sequential execution where each module generates an intermediate output file used by the subsequent stage. To execute the end-to-end pipeline, run:

```bash
python run_pipeline.py
```
