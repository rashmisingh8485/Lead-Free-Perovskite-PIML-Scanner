import pandas as pd
import os
from utils import get_tolerance_factor  # <--- CALLING UTILS
from model_engine import train_perovskite_model # <--- CALLING MODEL_ENGINE

# 1. FILE CONFIGURATION
file_name = 'novel_perovskite_space.csv'

if not os.path.exists(file_name):
    print(f" [ERROR]: Data file '{file_name}' not found.")
else:
    # 2. DATA LOADING
    data = pd.read_csv(file_name)
    
    # Using your CSV columns
    features = ['Cs_Fraction', 'Sn_Fraction', 'Tolerance_Factor']
    target = 'Bandgap_eV'

    # 3. MODEL TRAINING PHASE
    print("Initializing PIML Model Training...")
    model, xtest, ytest = train_perovskite_model(data, features, target)
    print(" SUCCESS: Model trained.")

    # 4. INTERACTIVE USER SCREENING
    print("\n" + "="*45)
    print("   LEAD-FREE PEROVSKITE SCREENING TOOL   ")
    print("="*45)

    try:
        # User input
        cs_val = float(input("Enter Cs_Fraction (e.g., 0.5): "))
        sn_val = float(input("Enter Sn_Fraction (e.g., 0.8): "))
        
        # WE CALL UTILS HERE TO CALCULATE FOR THE USER
        # Note: I'm passing 2.20 as a default for rX (Iodide) to make the function work
        tf_calculated = get_tolerance_factor(cs_val, sn_val, 2.20) 
        
        # Creating input dataframe
        user_input_df = pd.DataFrame([[cs_val, sn_val, tf_calculated]], columns=features)

        # Prediction
        prediction = model.predict(user_input_df)

        print("\n" + "-"*30)
        print(f" Predicted Bandgap: {prediction[0]:.4f} eV")
        print(f" Calculated Tolerance Factor: {tf_calculated:.4f}")
        
        if 0.8 <= tf_calculated <= 1.0:
            print(" Structural Status: STABLE")
        else:
            print(" Structural Status: UNSTABLE")
        print("-"*30)

    except ValueError:
        print(" [INPUT ERROR]: Please enter numeric values only.")
