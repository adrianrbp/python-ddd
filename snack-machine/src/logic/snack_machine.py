class SnackMachine:
    def __init__(self):
        self.one_cent_count = 0
        self.ten_cent_count = 0
        self.quarter_count = 0
        self.one_dollar_count = 0
        self.five_dollar_count = 0
        self.twenty_dollar_count = 0
    
    def insert_money(self, one_cent_count, ten_cent_count, quarter_count, one_dollar_count, five_dollar_count, twenty_dollar_count):
        self.one_cent_count += one_cent_count
        self.ten_cent_count += ten_cent_count
        self.quarter_count += quarter_count
        self.one_dollar_count += one_dollar_count
        self.five_dollar_count += five_dollar_count
        self.twenty_dollar_count += twenty_dollar_count
