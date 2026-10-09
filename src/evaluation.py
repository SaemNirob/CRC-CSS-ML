"""Evaluation metrics and reporting."""

def evaluate_models(models, X_test, y_test):
    results = {}
    for name, model in models.items():
        results[name] = model.predict_proba(X_test)
    return results
