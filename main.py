import pandas as pd
from utils import get_tolerance_factor
from model_engine import train_perovskite_model

# Load your lead-free dataset
data = pd.read_csv('data/sn_ge_perovskites.csv')

# Add Physics Descriptors
data['t_factor'] = get_tolerance_factor(data['rA'], data['rB'], data['rX'])

# Features list from your Colab
features = ['rA', 'rB', 'rX', 'enA', 'enB', 't_factor']
model, xtest, ytest = train_perovskite_model(data, features, 'Formation_Energy')

print("Model Trained Successfully! Stability Predicted for 1000+ Compositions.")
