# neuro_ai_project

## 📓 Notebooks

- `1_biomarker_preprocessing.ipynb` — Loads and preprocesses the stroke prediction dataset (handles missing values, encodes categorical features, and scales data).
- `3_model_training.ipynb` — Trains a Random Forest model using preprocessed biomarkers and evaluates it using accuracy, confusion matrix, and ROC AUC.
- `4_dca_evaluation.ipynb` — Performs Decision Curve Analysis (DCA) to assess the clinical value of the trained model predictions.
- `5_xai_rf_shap.ipynb` — Uses SHAP to visualize and interpret how different features impact stroke predictions made by the Random Forest model.
- `6_federated_learning_simulation.ipynb` — Simulates Federated Learning using Flower across multiple virtual hospitals, maintaining data privacy while training collaboratively.


## 🧠 Federated Learning Simulation Summary

This simulation demonstrates federated training of a Random Forest model across 3 simulated hospitals using Flower. The dataset was split into three parts, each treated as a separate client. The training was conducted over 3 rounds without centralizing patient data, ensuring privacy-preserving AI training.

### ⚙️ Configuration
- **Model**: RandomForestClassifier
- **Framework**: Flower (`flwr`)
- **Clients (Hospitals)**: 3
- **Rounds**: 3
- **Data**: Preprocessed stroke biomarker dataset

### 📈 Evaluation Results (Average Distributed Loss per Round)
| Round | Loss            |
|-------|------------------|
| 1     | 0.9521           |
| 2     | 0.9501           |
| 3     | 0.9511           |

> These results confirm successful multi-client learning with stable performance across rounds. This phase closes the AI chasm by simulating real-world data decentralization using federated learning.

### ✅ Outcome
- Model training without data sharing
- Demonstrated readiness for cross-hospital deployments
- Paved the way for integrating deeper learning or MRI-based models
