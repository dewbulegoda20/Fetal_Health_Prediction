# Fetal Health Prediction

![Baby Fetus in Womb](images/baby-fetus-womb.jpg)

# Table of Contents
- [Introduction](#introduction)
- [Literature Review](#literature-review)
- [Description of the Dataset](#description-of-the-dataset)
- [Conclusion](#conclusion)


---

## Introduction
This is a multi class classification problem.The ultimate goal of fetal health prediction is to develop a machine learning model that 
can accurately classify the health status of a fetus based on various clinical features. 
The dataset consists of 21 features and a target variable with three classes: 1-Normal, 
2-Suspect, and 3-Pathological. By analyzing clinical features derived from the dataset, the project aims to leverage preprocessing, feature engineering, and hyperparameter tuning to improve model performance. Advanced techniques, such as cross-validation and imbalance handling, will ensure robust and reliable predictions. The resulting model will serve as a tool for healthcare professionals to make timely and informed decisions, reducing child and maternal mortality rates.

## Literature Review
Machine learning is transforming fetal health monitoring by analyzing cardiotocography data. The Fetal Health Classification Dataset contains 2,126 instances categorized as normal, suspicious, or pathological, with significant challenges due to class imbalance. Researchers have employed various machine learning techniques, including Support Vector Machines, Random Forests, and deep learning neural networks, to improve health classification accuracy. Despite advanced feature selection strategies, most models struggle to achieve high precision. Current research focuses on addressing data imbalance, improving feature selection, and developing specialized algorithms. The ultimate goal is to enhance prenatal care by providing more accurate and reliable health assessments for both mothers and fetuses.

## Description of the Dataset 
The dataset used in this project contains 21 features and a target variable, which classifies fetal health into three categories: Normal (1), Suspect (2), and Pathological (3). These features represent various clinical parameters critical for fetal health assessment. Below are the features included in the dataset:

## Conclusion
## Model Comparison: Random Forest vs. KNN

When comparing the Random Forest and KNN models, we observe distinct differences in their performance across training, validation, and test datasets.

**Random Forest**:
- The **Random Forest model** achieves a high **training accuracy of 0.98**, indicating strong learning from the training data.
- It maintains a robust **validation accuracy of 0.95** and a **test set accuracy of 0.95**, showing that it generalizes well to unseen data without significant overfitting.
- These results suggest that the Random Forest classifier strikes a good balance between fitting the data and maintaining generalization, making it a more reliable choice for large and complex datasets.

**KNN**:
- The **KNN model** achieves a perfect **training accuracy of 1.00**, but its **validation and test set accuracies drop to 0.93**, indicating potential **overfitting**.
- The discrepancy between training and validation/test performance suggests that KNN may memorize the training data rather than generalize well to new unseen examples.
- KNN is also computationally more expensive with large datasets, and its performance can degrade with noisy or high-dimensional data.

## **Summary**
- The **Random Forest classifier** is a better choice in this scenario due to its superior ability to generalize across different datasets (training, validation, and test) without overfitting.
- The **KNN model**, while simple and interpretable, tends to overfit the training data, which affects its ability to make accurate predictions on unseen data.

For large and complex datasets where generalization and model robustness are critical, **Random Forest is the preferred choice**. In contrast, KNN is more suited for smaller datasets but requires careful parameter tuning to reduce overfitting risks.



