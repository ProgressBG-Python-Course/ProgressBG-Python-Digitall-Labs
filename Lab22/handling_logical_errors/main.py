# transform.py
import pandas as pd
import logging

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Transformation function with a logical error
def calculate_transaction_volume(df):
    # Incorrect logic for demonstration purposes
    df['transaction_volume'] = df['quantity'] + df['unit_price']
    logging.info("Transaction volume calculated.")
    return df

if __name__ == "__main__":
    data = {
        'quantity': [1,2,3],
        'unit_price': [2,2,2]
    }

    df = pd.DataFrame(data)
    print(df)

    df = calculate_transaction_volume(df)
    print(df)