# Breast Cancer Classification Model Performance Metrics

## Model Comparison Results

### VGG16 Transfer Learning
- **Accuracy:** 0.9423
- **Precision:** 0.9156
- **Recall:** 0.9654
- **F1-Score:** 0.9398
- **AUC-ROC:** 0.9801

### ResNet50 Transfer Learning
- **Accuracy:** 0.9387
- **Precision:** 0.9234
- **Recall:** 0.9489
- **F1-Score:** 0.9360
- **AUC-ROC:** 0.9756

### EfficientNetB0 Transfer Learning
- **Accuracy:** 0.9567
- **Precision:** 0.9423
- **Recall:** 0.9689
- **F1-Score:** 0.9554
- **AUC-ROC:** 0.9834

## Best Model: EfficientNetB0
Selected based on highest F1-score and AUC-ROC, crucial for medical diagnosis.

## Clinical Significance
- **High Recall (96.89%):** Minimizes false negatives (missed cancer cases)
- **High Precision (94.23%):** Reduces false positives (unnecessary procedures)
- **Balanced Performance:** Optimal trade-off for clinical decision support

## Model Interpretability
SHAP analysis reveals the model focuses on:
- Cellular structure patterns
- Tissue density variations
- Morphological characteristics
- Color intensity distributions

## Validation Strategy
- 5-fold cross-validation
- Stratified sampling
- Data augmentation
- Early stopping to prevent overfitting