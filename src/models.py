"""Model construction utilities."""

def train_models(models, X_train, y_train):
    fitted = {}
    for name, model in models.items():
        fitted[name] = model.fit(X_train, y_train)
    return fitted
