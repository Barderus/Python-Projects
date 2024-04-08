'''
    Car Maintenance price 
'''
import matplotlib as plt
import seaborn
import pandas as pd

title = "2015 Volkswagen Tiguan (Red)"

'''
 ->  ->  miles
-> $ -> 
 -> $ -> 
 -> $ -> 
 -> $ -> 
 -> $ -> 
 -> $ -> 
 -> $ -> 
 -> $ -> 
 -> $ -> 
 -> $ -> 
 -> $ -> 
 -> $ -> 
 -> $ -> 
 ->  -> 
 -> $ ->

I want to know:
    * How many miles driven total from 2021 to 2023
    * How much it was spent on each year, the highest price, the lowest price
    * Know how often a service was done to the car (?)
    * Services by season (?)
'''
def data():
    print("You are in data()")
    data = {
        "Date":["12/31/2021", "02/28/2022", "05/23/2022", "06/29/2022", "07/19/2022", "09/01/2022", "09/02/2022", "09/16/2022",
                "11/09/2022", "11/28/2022", "01/11/2023",  "03/09/2023", "06/27/2023", "08/31/2023", "10/24/2023", "12/19/2023"],

        "Price":[1925.00, 238.72, 1884.29, 226.67, 129.59, 120.84, 1338.00, 257.80, 
                 37.78, 1063.60, 101.40, 1709.66, 1582.20, 1003.75, 101.40],

        "Miles":[103981, 106908, 111447, 112816, 113639, 115386, 115400, 116164, 
                 117500, 119299, 120279, 123011, 128619, 131963, 135066, 137356]    # 16 values
    }

    '''
        Season:
            Spring {March, April, May}
                If the datetime obj starts with 03, 04, or 05 -> Spring
            Summer {June, July, August}
                If the datetime obj starts with 06, 07, 08 -> Summer
            Fall {September, October, November}
                If the datetime obj starts with 09, 10, 11 -> Fall
            Winter {December, January, February}
                If the datetime obj starts with 12, 01, 02 -> Winter
    '''

    data["Date"] = pd.to_datetime(data["Date"]) # Converts the data in that column to datetime format and replacing the original data with the converted datetime values.
    print(data)
    df = pd.DataFrame(data)
    print(df)
    

def menu():
    ''' Menu '''
    print("""Would you like to...
          \n1. Miles total driven from 2021 to 2023
          \n2. Money spent
          \n3. Service rate
          \n4. Services per season
          \n0 to quit
          """)
    user_choice = int(input("Choose your option: "))

    match user_choice:
        case 0:
            exit()
        case 1:
            get_total_miles()
        case 2:
            get_total()
        case 3:
            how_often()
        case 4:
            get_per_season()           

def get_total_miles():
    print("You are in the get_total_miles function.")

def get_total():
    print("You are in the get_total function.")

    get_highest()
    get_lowest
    

def get_highest():
    print("You are in the get_highest function.")

def get_lowest():
    print("You are in the get_lowest function.")

def how_often():
    print("You are in the how_often funcion.")

def get_per_season():
    print("You are in the get_per_season function.")

def main():
    data()

if __name__ == "___main__":
    main()