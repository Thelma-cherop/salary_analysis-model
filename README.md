# salary_analysis-model
End-to-end salary prediction web app built with Linear Regression and Streamlit
💼 Salary Intelligence Tool
An end-to-end Machine Learning web app that predicts salary based on years of experience — and works in reverse to calculate how much experience you need to reach a target salary.
Built as part of a 6-day ML streak over Easter holiday by a second-year Mechatronics Engineering student.

🌐 Live Demo
[https://salaryanalysis-model-lpqucprn5vqxangrhsrkur.streamlit.app/]

🎯 What It Does

Experience → Salary: Input your years of experience and get an instant salary prediction
Salary → Experience: Input your target salary and find out exactly how many years of experience you need
Shows the math behind every prediction transparently


🛠️ Tech Stack
ToolPurposePythonCore languagepandas & NumPyData manipulationscikit-learnLinear Regression, cross-validation, polynomial featuresMatplotlib & SeabornExploratory data analysisjoblibModel serializationStreamlitWeb app deployment

📊 Model Performance
MetricValueAlgorithmLinear RegressionR² Score (test)0.9024RMSE$7,059Cross-validation Mean R²0.9224Cross-validation Std0.0496

🧠 ML Pipeline — What Was Done
Day 1 — Exploratory Data Analysis

Analyzed distributions, spread, and skewness using describe()
Computed correlation between YearsExperience and Salary — 0.978 (very strong)
Ran IQR-based outlier detection — confirmed no outliers (bounds: -$9,014 to $166,281)
Concluded Linear Regression was appropriate before writing a single model line

Day 2 — Linear Regression

Split data 80/20 (24 train, 6 test rows)
Trained Linear Regression model
Intercept: $24,380 | Coefficient: $9,423 per year of experience
Model equation: Salary = 24,380 + (9,423 × YearsExperience)

Day 3 — Residual Analysis

Plotted residuals vs fitted values — confirmed random scatter (no pattern missed)
Residual mean: 609.54 — slight underprediction bias noted
Histogram showed bimodal distribution — traced to noise at low experience levels (1.2–2.3 years)

Day 4 — Cross Validation

Applied K-Fold cross validation (K=5) with shuffle=True
Shuffle was critical — dataset is sorted by experience, without shuffle each fold would test on alien salary ranges
Mean R²: 0.9224 | Std: 0.0496 — model is stable, not a lucky split

Day 5 — Polynomial Regression

Tested degree 2 polynomial regression
Result: R² dropped to 0.897 — worse than linear
Conclusion: 30 rows insufficient to support added complexity — overfitting on training data
Linear Regression selected as final model based on evidence

Day 6 — Deployment

Serialized final model using joblib → salary_model.pkl
Built two-way prediction Streamlit app
Deployed on Streamlit Cloud
├── app.py                 # Streamlit web app
├── training.ipynb         # Full ML pipeline and analysis notebook
├── salary_model.pkl       # Trained and serialized Linear Regression model
├── salary_dataset.csv     # Dataset (30 records)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
💡 Key Learnings

A senior data scientist spends 70% of time on data understanding before modelling
Correlation analysis can validate your model choice before training
Cross validation is essential on small datasets — one split can be misleading
More complexity is not always better — overfitting is real even on simple datasets
A model is only useful when deployed — shipping matters
