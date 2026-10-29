# Placement Predictor

A Streamlit machine learning application that predicts whether a student is likely to get placed based on academic performance, technical ability, communication skills, projects, and internship experience.

## Run Locally

Install the required Python packages:

```bash
pip install streamlit pandas scikit-learn joblib
```

Start the Streamlit application:

```bash
streamlit run placement_pro.py
```

The application uses the trained model stored in `placement_predictor.joblib`.

> The current application contains a machine-specific model path in `placement_pro.py`. Before running it on another computer, update that path to the local repository file, for example: `joblib.load("placement_predictor.joblib")`.

## Project Files

- `placement_pro.py` — Streamlit web application for placement predictions
- `placement_predictor.joblib` — Saved trained scikit-learn classification model

## Model Information

- **Problem type:** Binary classification
- **Model:** Random Forest Classifier
- **Target:** Whether the student is likely to be placed
- **Output:** Placement prediction and placement probability
- **Model format:** Joblib serialized model

The model provides both a predicted class and class probabilities through `predict()` and `predict_proba()`. The application displays the probability of getting placed and the probability of not getting placed.

## Input Features

The application collects the following student information:

- **IQ** — Intelligence quotient score
- **Previous Semester Result** — Previous semester grade point score
- **CGPA** — Cumulative Grade Point Average
- **Academic Performance** — Academic performance score from 1 to 10
- **Extra-Curricular Score** — Extra-curricular activities score from 0 to 10
- **Communication Skills** — Communication skill score from 1 to 10
- **Projects Completed** — Number of completed academic or professional projects
- **Internship Experience** — Whether the student has completed an internship

The internship value is encoded as `1` for **Yes** and `0` for **No** before the model makes a prediction.

## Application Features

- Predicts whether a student is likely to get placed
- Displays a success or warning message for the prediction
- Shows the probability of getting placed
- Shows the probability of not getting placed
- Provides a button to clear the current results

> This project is intended for educational purposes. Its predictions are estimates and should not be treated as a guarantee of placement or as a substitute for professional career guidance.
