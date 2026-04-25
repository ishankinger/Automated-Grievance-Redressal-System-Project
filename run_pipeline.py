import subprocess

notebooks = [
    "01-Data-Preprocessing/Data_Preprocessing_pipeline.ipynb",
    "02-Anomaly-Detection/Anomaly_Detection_pipeline.ipynb",
    "03-Domain-Classification/Domain_Classification_pipeline.ipynb",
    "04-Keyword-Extraction/Keyword_Extraction_pipeline.ipynb",
    "05-Severity-Risk-Scoring/Severity_Risk_Scoring_pipeline.ipynb",
    "06-Resolution-Time-Prediction/Resolution_Time_Prediction_pipeline.ipynb"
]

for nb in notebooks:
    print(f"Running {nb}...")
    subprocess.run([
        "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--inplace", 
        nb
    ], check=True)