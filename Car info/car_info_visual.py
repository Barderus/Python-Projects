"""
    Car Maintenance price

I want to know:
    * How many miles driven total from 2021 to 2023
    * How much it was spent on each year, the highest price, the lowest price
    * Know how often a service was done to the car
    * Services by season
"""

import matplotlib as plt
import pandas as pd
from collections import Counter

def data():
    car_data = {
        "date": ["12/31/2021", "02/28/2022", "05/26/2022", "06/30/2022", "07/20/2022", "09/01/2022", "09/03/2022",
                 "09/16/2022",
                 "11/09/2022", "11/28/2022", "01/11/2023", "03/10/2023", "06/27/2023", "08/31/2023", "10/24/2023",
                 "12/22/2023"],

        "price": [1925.00, 238.72, 1884.29, 226.67, 129.59, 120.84, 1338.00, 257.80,
                  37.78, 1063.60, 101.40, 1709.66, 1582.20, 1003.75, 101.40, 1856.20],

        "miles": [103981, 106908, 111447, 112816, 113639, 115386, 115400, 116164,
                  117500, 119299, 120279, 123011, 128619, 131963, 135066, 137356]  # 16 values
    }

    df = pd.DataFrame(car_data)

    # Transform the date object from string to datetime
    df["date"] = pd.to_datetime(df["date"])

    return df

def get_total_miles(df):
    """
        This function returns the total amount of miles driven from 2021 to 2023
    """
    total_driven = df["miles"][15] - df["miles"][0]
    return total_driven


def get_total(df):
    """
        This function returns the total amount of money spent with repairs from 2021 to 2023
    """
    total_spent = df["price"].sum()
    return total_spent


def get_highest(df):
    """
        This function returns the highest repair price from 2021 to 2023
    """
    highest_val = df["price"].idxmax()
    return highest_val


def get_lowest(df):
    """
        This function returns the highest repair price from 2021 to 2023
    """
    lowest_val = df["price"].idxmin()
    return lowest_val


def how_often(df, elapsed_time):
    repairs = len(df.index)
    print(repairs)
    avg = elapsed_time / repairs

    return avg


def get_per_season(df):
    seasons = []  # Initialize an empty list to store seasons

    for date in df["date"]:  # Iterate over each date in the DataFrame
        if date.month in [12, 1, 2]:
            seasons.append("Winter")
        elif date.month in [3, 4, 5]:
            seasons.append("Spring")
        elif date.month in [6, 7, 8]:
            seasons.append("Summer")
        elif date.month in [9, 10, 11]:
            seasons.append("Fall")

    return seasons # Return the list of seasons



def main():
    df = data()
    elapsed_time = df["date"][15] - df["date"][0]

    while True:
         """ Menu """
         print("""\nWould you like to see...
               1. Miles total driven from 2021 to 2023
               2. Money spent
               3. Service rate
               4. Services per season
               5. Some visualizations
               0. to quit
               """)
         user_choice = int(input("Choose your option: "))

         match user_choice:
             case 0:
                 exit()
             case 1:
                 total_miles = get_total_miles(df)
                 print(f"\nTotal miles:\n\tGabriel drove for {total_miles:,} miles in the span of {elapsed_time.days} days." )
             case 2:
                 total = get_total(df)
                 max_index = get_highest(df)
                 max_date = df.iloc[max_index]["date"]
                 max_price = df.iloc[max_index]["price"]

                 min_index = get_lowest(df)
                 min_price = df.iloc[min_index]["price"]
                 min_date = df.iloc[min_index]["date"]
                 print(f"\nIn the total of {len(df.index)} trips to the shop, it was spent ${total:,.2f} in repairs")
                 print(f"\nThe highest repair cost was on {max_date.strftime('%b %d %Y')}.\n\tThe repair cost was ${max_price:,.2f}.")
                 print(f"\nThe lowest repair cost was on {min_date.strftime('%b %d %Y')}.\n\tThe repair cost was ${min_price:,.2f}.")
             case 3:
                 often = how_often(df, elapsed_time)
                 print(f"The car was serviced in average every {often.days} days.")
             case 4:
                 seasons = get_per_season(df)
                 season_count = Counter(seasons)
                 # Nicely formatted output
                 print("\nSeason Counts:")
                 for season, count in season_count.items():
                     print(f"\t{season}: {count} times")
             case 5:
                 print("\nComing soon!")

main()
