import pandas as pd
import os
from utils import get_tolerance_factor
from model_engine import train_perovskite_model

# 1. FILE CONFIGURATION
# Ensure this file is in the same root directory as main.py
file_name = 'novel_perovskite_space.csv'

if not os.path.exists(file_name):
    print(f" [ERROR]: Data file '{file_name}' not found in the root directory.")
else:
    # 2. DATA LOADING
    data = pd.read_csv(file_name)
    
    # Columns based on your uploaded CSV: Cs_Fraction, Sn_Fraction, Tolerance_Factor, Bandgap_eV
    features = ['Cs_Fraction', 'Sn_Fraction', 'Tolerance_Factor']
    target = 'Bandgap_eV'

    # 3. MODEL TRAINING PHASE
    print("Initializing PIML Model Training... Please wait.")
    model, xtest, ytest = train_perovskite_model(data, features, target)
    print(" SUCCESS: Model trained and verified.")

    # 4. INTERACTIVE USER SCREENING TOOL (English Interface)
    print("\n" + "="*45)
    print("   LEAD-FREE PEROVSKITE SCREENING TOOL v1.0   ")
    print("="*45)
    print("Instructions: Enter the chemical composition details below.")

    try:
        # User input via keyboard
        cs_val = float(input("Enter Cs_Fraction (e.g., 0.5): "))
        sn_val = float(input("Enter Sn_Fraction (e.g., 0.8): "))
        tf_val = float(input("Enter Tolerance_Factor (e.g., 0.98): "))

        # Creating input dataframe for prediction
        user_input_df = pd.DataFrame([[cs_val, sn_val, tf_val]], columns=features)

        # Generating Prediction
        prediction = model.predict(user_input_df)

        print("\n" + "-"*30)
        print(f" ANALYSIS RESULT ")
        print(f" Predicted Bandgap: {prediction[0]:.4f} eV")
        
        # Stability Logic (Physics-Informed)
        if 0.8 <= tf_val <= 1.0:
            print(" Structural Status: STABLE (Black Phase)")
        else:
            print(" Structural Status: UNSTABLE / NON-PEROVSKITE")
        print("-"*30)

    except ValueError:
        print(" [INPUT ERROR]: Please enter numeric values only.")
    except Exception as e:
        print(f" [SYSTEM ERROR]: {e}")
