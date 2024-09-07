import card
import csv

csv_file = input()
with open(csv_file, "r") as csv:
    newcsv = csv.reader(csv)

card = card.Card()
