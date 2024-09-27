import glob
import pprint
from getrecord import GetRecord
from input import data_input

def main(selected_school):
    TrackField_list = [
    glob.glob("./data/record/５年女子/*"),
    glob.glob("./data/record/５年男子/*"),
    glob.glob("./data/record/６年女子/*"),
    glob.glob("./data/record/６年男子/*"),
    ]
    relay_list = glob.glob("./data/record/リレー/*")

    TrackField_record = GetRecord()
    Relay_record = GetRecord()


    for event in TrackField_list:
        TrackField_record.get_row_number(event, selected_school)

    Relay_record.get_row_number(relay_list, selected_school)

    pprint.pprint(TrackField_record.school_record)
    pprint.pprint(Relay_record.school_record)

    data_input(TrackField_record.school_record, "data/input/TrackField_result.xlsx")
    data_input(Relay_record.school_record, "data/input/Relay_result.xlsx")



