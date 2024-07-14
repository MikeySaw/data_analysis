import numpy as np 
import pandas as pd
import re


def parse_height_to_metric(height: str) -> int:
    match = re.match(r"(\d+)'(\d+)\"", height)
    if match:
        feet = int(match.group(1))
        inches = int(match.group(2))
        total_inches = feet*12 + inches
        return total_inches * 2.54
    else:
        return int(height)
    
    
def parse_weight_to_metric(weight: str) -> int:
    match = re.match(r"(\d+)lbs", weight)
    if match:
        pounds = int(match.group(1))
        return pounds * 0.453592
    else:
        return int(weight)
    
    
def remove_newlines(text) -> str:
    if isinstance(text, str):
        return text.strip()
    else:
        return text
    

def convert_money_to_int(value: str) -> int:
    match_M = re.match(r'€\d+(\.\d+)?M', value)
    if match_M:
        value = value.replace('M', '')
        value = value.replace('€', '')
        value = float(value) * 10**6
    else:
        value = value.replace('K', '')
        value = value.replace('€', '')
        value = float(value) * 10**3
    
    return int(value)


def remove_stars(data: pd.DataFrame) -> pd.DataFrame:    
    star_columns = []
    for column in data.columns:
        match = re.findall(r'★', str(data[column][0]))
        if match:
            star_columns.append(column)

    for column in star_columns:
        data[column] = data[column].str.replace("★", "").str.strip().apply(int)

    return data


def main(data: pd.DataFrame) -> pd.DataFrame:
    data['Height'] = data['Height'].str.replace('cm','').apply(parse_height_to_metric)
    data['Weight'] = data['Weight'].str.replace('kg', '').apply(parse_weight_to_metric)

    data = data.map(remove_newlines)

    data['Value'] = data['Value'].apply(convert_money_to_int)
    data['Wage'] = data['Wage'].apply(convert_money_to_int)
    data['Release Clause'] = data['Release Clause'].apply(convert_money_to_int)
    data = remove_stars(data)

    return data


if __name__ == "__main__":
    print("Processing data...")
    data = pd.read_csv("data/raw/fifa21_raw_data_v2.csv")
    data = main(data)
    data.to_csv("data/processed/fifa21_processed_data_v2.csv", index=False)
    print("Done!")

    
