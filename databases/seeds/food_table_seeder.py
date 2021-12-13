"""FoodTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Food import Food

from pandas import read_csv
import json

# Import CSV to DataFrame
fndds = read_csv('FNDDS.csv', index_col=None, encoding='utf-8')
temp_foods = fndds.loc[:,'I_Code':'N_Value']

# DataFrame to List of Dictionaries
foods = []
for i in range(len(temp_foods)):
    row = json.loads(temp_foods.loc[i].to_json())
    temp = {"I_Code": None, "Ingredient": None, "Nutrients": {}}
    new_food = True
    if len(foods) > 0:        
        for food in foods:
            if food["I_Code"] == str(row["I_Code"]):
                food["Nutrients"][str(row["N_Code"])] = [row["Nutrient"], float(row["N_Value"])]
                new_food = False
                break
    if new_food == True:
        temp["I_Code"] = str(row["I_Code"])
        temp["Ingredient"] = row["Ingredient"]
        temp["Nutrients"] = {str(row["N_Code"]): [row["Nutrient"], float(row["N_Value"])]}
        foods.append(temp)

# List of Dictionaries to SQL
class FoodTableSeeder(Seeder):
    def run(self):
        """Template seeds."""
        for food in foods:
            print(food)
            Food.create({
                "I_Code": food["I_Code"],
                "Ingredient": food["Ingredient"],
                "Nutrients": str(food["Nutrients"])
            })


