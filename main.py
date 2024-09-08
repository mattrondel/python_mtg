import card
import csv

csv_file = "MishrazzPremodern360cube.csv" # input()
cards = []

with open(csv_file, "r") as cube_file:
    newcsv = csv.reader(cube_file)
    next(newcsv) # Removes header
    for each_card in newcsv:
        # print(each_card)
        # print(1, # Prints moxfield
        #       each_card[0],
        #       "("+ each_card[4]+')',
        #       each_card[5]
        #       )
        cards.append(
            card.Card(each_card[0],
                      each_card[1],
                      each_card[2],
                      each_card[3],
                      each_card[4],
                      each_card[5],
                      each_card[6],
                      each_card[7],
                      each_card[8],
                      each_card[9],
                      each_card[10],
                      each_card[11],
                      each_card[12],
                      each_card[13],
                      each_card[14],
                      each_card[15]
                      )
        )

    moxfield = "" # single string to put into a file
    for card in cards:
        moxfield += card.moxfield() + "\n" # moxfield = moxfield + card.moxfield()
print(moxfield)

#card = card.Card()

# Moxfield syntax: QTY Name (set) collector
