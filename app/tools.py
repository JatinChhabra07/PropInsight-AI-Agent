import pandas as pd

def calculate_rent_rolls(path: str):
    """
    Reads an Excel rent roll and calculates total income and occupancy.
    """
    try:

        dataset = pd.read_excel(r"C:\Users\chhab\PropInsight-AI-Agent\data\rent_roll (1).xlsx")
        if 'Monthly_Rent' not in dataset.columns:
            raise ValueError("column Monthly_Rent is not found in the dataset!")
        
        total_income = dataset['Monthly_Rent'].sum()
        
        if ' Status' in dataset.columns:
            total_units = len(dataset)
            occupied_units = len(dataset[dataset[' Status']=='Occupied'])
            occupancy_rate = (occupied_units / total_units) * 100
        else:
            occupancy_rate = 100

        return (
            f"Financial Analysis:\n"
            f"- Total Monthly Income: ${total_income:,.2f}\n"
            f"- Occupancy Rate: {occupancy_rate:.1f}%"
        )
    except Exception as e:
        return f"Error reading file: {str(e)}"




        
    

    