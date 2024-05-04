from datetime import datetime
import os
import json
import pandas as pd

# Define paths and symbol
symbol = 'EURUSD'
base_path = f'dataset/{symbol}/'
indicator = 'macd'  # Define your indicator

# Paths for the main data and the indicator data
main_data_path = base_path
indicator_data_path = os.path.join(base_path, f'indicators/{indicator}/')
# Create a DataFrame to hold all the data
data_m = pd.DataFrame()
try:
    # List all JSON files in the main directory
    main_files = [f for f in os.listdir(main_data_path) if f.endswith('.json')]
    # Process each file in the main directory
    for f in main_files:
        file_path = os.path.join(main_data_path, f)
        with open(file_path, 'r') as file:
            data = json.load(file)
            main_data_df = pd.DataFrame(data).transpose()
            data_m = pd.concat([data_m, main_data_df], axis=0)

        # Corresponding file in the indicators directory
        indicator_file_path = os.path.join(indicator_data_path, f)
        if os.path.exists(indicator_file_path):
            with open(indicator_file_path, 'r') as file:
                data = json.load(file)
                indicator_data_df = pd.DataFrame(data).transpose()
                data_m = pd.concat([data_m, indicator_data_df], axis=0)
    # Group by index and take the last occurrence of each index
    
    if not data_m.empty:
        data_m = data_m.groupby(data_m.index).last()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    try:
        os.mkdir(f'dataset/{symbol}/deploy')
        print(f"Directory created at {base_path}")
    except OSError as error:
        if "File exists" in str(error):
            print(f"Directory already exists at {base_path}")
        else:
            print(f"Error creating directory at {base_path}: {error}") #%H%M%S
    with open(f'dataset/{symbol}/deploy/{symbol}_daploy{datetime.now().strftime("%Y%m%d")}.json', 'w') as f:
        f.write(data_m.to_json(orient="index"))
