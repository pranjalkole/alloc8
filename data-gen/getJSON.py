import json
from strictyaml import load, Map, MapPattern, Str, Int, Seq, YAMLError

batches = "btech22", "btech23", "btech24", "phd19", "phd20" # Define batches here
genders = "male", "female"
blocks = "A", "B", "C", "D" # Define blocks here
hostels = "Aryabhatta", "Kalam", "Asima" # Define hostels here
schema = MapPattern(Str(), MapPattern(Str(), Map({ "capacity": Int(), "hostels": MapPattern(Str(), MapPattern(Str(), Seq(Str()))) })))
with open("hostel_choice.yaml") as fin:
    try:
        data = load(fin.read(), schema).data
    except YAMLError as error:
        print(error)
    for batch in data:
        if batch not in batches:
            print(f"Invalid batch {batch}")
            exit()
        for gender in data[batch]:
            if gender not in genders or data[batch][gender]["capacity"] < 1:
                print(f"Invalid gender {gender} or capacity {capacity}")
                exit()
            for hostel in data[batch][gender]["hostels"]:
                if hostel not in hostels:
                    print(f"Invalid hostel {hostel}")
                    exit()
                for block in data[batch][gender]["hostels"][hostel]:
                    numRooms = 0
                    if block not in blocks:
                        print(f"Invalid block {block}")
                        exit()
                    for roomRange in data[batch][gender]["hostels"][hostel][block]:
                        roomRange = roomRange.split("-")
                        numRooms += int(roomRange[1])-int(roomRange[0])+1
                    print(batch, gender, hostel, block, numRooms)
    with open("available_rooms.json", "w") as fout:
        json.dump(data, fout)
