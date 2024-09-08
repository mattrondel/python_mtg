import card
import csv

csv_file = "MishrazzPremodern360cube.csv" # input()
cards = []

with open(csv_file, "r") as cube_file:
    newcsv = csv.reader(cube_file)
    next(newcsv) # Removes header
    for each_card in newcsv:
        # print(each_card)
        print(each_card[0],each_card[2])
        # cards.append(
        #     card.Card(each_card[0])
        # )


#card = card.Card()

# Moxfield syntax: QTY Name (set) collector
