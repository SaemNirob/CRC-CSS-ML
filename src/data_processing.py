"""Dataset loading and cohort preparation."""

def load_dataset(path):
    import pandas as pd
    return pd.read_csv(path)

def prepare_cohort(data):
    """Apply the original cohort definition without modifying analytical rules."""
    return data.copy()
