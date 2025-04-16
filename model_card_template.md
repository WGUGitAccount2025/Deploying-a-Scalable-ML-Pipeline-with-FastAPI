# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This RandomForestClassifier model is trained on the Census Income Dataset to predict whether an individual earns more than $50K per year based on 14 demographic features such as age, education, and occupation. The dataset, donated in 1996, contains 48,842 instances and supports binary classification.
## Intended Use
This model is designed for classification tasks that predict income levels from structured demographic data. Intended for learning and skill building, it demonstrates how machine learning techniques can be applied to social and economic analysis, including pipeline automation for real-world use cases.
## Training Data
This model is trained on a subset of the publicly available Census Income dataset, which includes demographic and work-related features such as age, sex, race, education, occupation, hours worked per week, and more. Some fields, like 'occupation', may contain null values. The target variable is binary, indicating whether an individual's income is ≤50K or >50K.
## Evaluation Data
The Census Income dataset is split into 80% training and 20% testing, with the same preprocessing pipeline applied to both. The test set is used for evaluation to assess the model’s generalization performance.
## Metrics
The model's performance was evaluated with three main metrics:

Precision: Measures the accuracy of positive predictions.
Recall: Measures the ability to identify all positive instances.
F1-score: The harmonic mean of precision and recall, balancing both metrics.

Overall performance:
Precision: 0.7242 | Recall: 0.6134 | F1: 0.6642
## Ethical Considerations
This model is trained on historical census data, which may contain inherent social and economic biases. Monitoring performance across demographic groups is essential to ensure fairness. While the Random Forest offers moderate interpretability, it lacks the transparency of simpler models. Additionally, limited testing and outdated data mean the model may produce inaccurate results if used beyond its intended educational purpose.
## Caveats and Recommendations
Since the dataset was donated in 1996, it may not reflect current socio-economic trends, limiting the model's predictive accuracy on modern data. To enhance reliability, cross-validation on updated datasets is recommended. Users should review feature importance to understand prediction drivers, and if deployed, the model should be monitored continuously for data drift, fairness, and generalization to new data distributions.