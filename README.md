\# 231FA04A91-MLOps-Feast-SkillGap



\## 1. Project Overview



This project implements a Machine Learning Operations (MLOps) workflow using Feast for a Student Skill Gap Analysis and Placement Prediction system.



The project uses student academic, internship, project, certification, and technical skill information to create features and predict student placement status.



The project demonstrates:



\- Data preparation

\- Feature engineering

\- Feast Feature Store

\- Historical feature retrieval

\- Feature materialization

\- Online feature retrieval

\- Machine Learning model training

\- Student placement prediction



\---



\## 2. Problem Statement



The objective is to identify the skill gap of CSE graduates by analyzing their academic performance, internships, projects, certifications, and technical skills.



The engineered features are stored and managed using Feast and are used to train a machine learning model for predicting student placement status.



\---



\## 3. Dataset



The dataset used in this project is:



`DatasetSKillGap.csv`



The generated Feast feature data is stored in:



`feature\_data.parquet`



The dataset contains student-level information including:



\- Registration Number

\- Department

\- Graduation Year

\- CGPA

\- Internship

\- Internship Months

\- Projects Count

\- Certifications Count

\- Technical Skills

\- Placement Status



\---



\## 4. Feature Engineering



The project creates features representing academic performance, experience, skills, skill gaps, and employability.



Important engineered features include:



\- Python\_Skill

\- SQL\_Skill

\- DSA\_Skill

\- DBMS\_Skill

\- OOP\_Skill

\- Cloud\_Computing\_Skill

\- Machine\_Learning\_Skill

\- Communication\_Skill

\- Problem\_Solving\_Skill

\- Overall\_Skill\_Gap

\- Skill\_Alignment\_Percentage

\- High\_Priority\_Gap\_Count

\- Employability\_Score



\---



\## 5. Feast Architecture



The Feast workflow used in this project is:



Dataset

↓

Feature Engineering

↓

Parquet Feature Data

↓

Feast FileSource

↓

Feast FeatureView

↓

Historical Feature Retrieval

↓

Machine Learning Model

↓

Materialization

↓

SQLite Online Store

↓

Online Feature Retrieval

↓

Final Placement Prediction



\---



\## 6. Feast Entity



The Feast entity is:



`reg\_number`



Join key:



`REG\_Number`



The registration number uniquely identifies each student.



\---



\## 7. Feast Data Source



The project uses a Feast `FileSource`.



The source data is:



`feature\_data.parquet`



The timestamp field is:



`event\_timestamp`



\---



\## 8. Feature View



The FeatureView is:



`graduate\_skill\_features`



It contains academic, experience, technical skill, skill-gap, and employability features.



The FeatureView uses a TTL of 3650 days.



\---



\## 9. Historical Feature Retrieval



Historical features were successfully retrieved using Feast.



Retrieved dataset shape:



`(1000, 19)`



The historical feature data was used as input for machine learning model training.



\---



\## 10. Machine Learning Model



A Random Forest Classifier was trained using the Feast historical features.



The target variable is:



`Placement\_Status`



Target classes:



\- Not Placed

\- Placed



The dataset was divided into training and testing sets using an 80:20 split.



\---



\## 11. Model Evaluation



The Random Forest model was evaluated using:



\- Accuracy

\- Precision

\- Recall

\- F1-Score

\- Confusion Matrix



The confusion matrix was generated to evaluate the classification performance.



\### Model Accuracy



Update this section with the accuracy obtained from the notebook.



`Accuracy: \_\_\_\_\_\_`



\### Precision



`Precision: \_\_\_\_\_\_`



\### Recall



`Recall: \_\_\_\_\_\_`



\### F1-Score



`F1-Score: \_\_\_\_\_\_`



\---



\## 12. Feature Materialization



The Feast FeatureView was successfully materialized into the SQLite online store.



Materialization range:



`2026-01-01 00:00:00` to `2026-09-07 18:00:00`



The materialized FeatureView was:



`graduate\_skill\_features`



\---



\## 13. Online Feature Retrieval



After materialization, the Feast online store is used to retrieve feature values for an individual student using the student's `REG\_Number`.



Example entity:



`REG\_Number`



The retrieved online features are used as input to the trained Random Forest model.



\---



\## 14. Final Prediction



The final model predicts whether a student is:



\- Placed

\- Not Placed



Final prediction for the selected student:



`\_\_\_\_\_\_\_\_\_\_`



\---



\## 15. Technologies Used



\- Python

\- Pandas

\- NumPy

\- Scikit-learn

\- Feast

\- Matplotlib

\- Jupyter Notebook

\- Parquet

\- SQLite

\- Git

\- GitHub



\---



\## 16. Project Structure



```text

231FA04A91-MLOps-Feast-SkillGap/

│

├── Assignment\_MLOPS\_A91.ipynb

├── DatasetSKillGap.csv

├── feature\_data.parquet

├── README.md

│

└── feature\_repo/

&#x20;   ├── definitions.py

&#x20;   └── feature\_store.yaml

