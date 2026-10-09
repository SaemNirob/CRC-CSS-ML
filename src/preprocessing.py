"""Feature preprocessing utilities."""

def prepare_features(data, feature_columns):
    return data[feature_columns].copy()
