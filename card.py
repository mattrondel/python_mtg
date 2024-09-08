class Card:
    def __init__(self, name, CMC,Type,Color,Set,Collector_Number,Rarity,Color_Category,status,Finish,maybeboard,image_URL,image_Back_URL,tags,Notes,MTGO_ID):
        self.name = name
        self.CMC = CMC
        self.Type = Type
        self.Color = Color
        self.Set = Set
        self.Collector_Number = Collector_Number
        self.Rarity = Rarity
        self.Color_Category = Color_Category
        self.status = status
        self.Finish = Finish
        self.maybeboard = maybeboard
        self.image_URL = image_URL
        self.image_Back_URL = image_Back_URL
        self.tags = tags
        self.Notes = Notes
        self.MTGO_ID = MTGO_ID

    def moxfield(self):
        return str("1" + " " + # Prints moxfield
                self.name + " " +
                "("+ self.Set+')' + " " +
                self.Collector_Number
                   )

