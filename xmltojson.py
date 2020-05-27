import xmltodict, json, os

pathtofile = input("Filename to convert: (must be in same directory)")

if not os.path.exists(pathtofile):
    print("Error: no file...")
    exit()

with open(pathtofile, "r") as xml_file:

    json_data = xmltodict.parse(xml_file.read())
    output_file = os.path.splitext(xml_file.name)[0]
    with open(output_file + ".json", "w+") as json_file:
        json.dump(json_data, json_file, indent=4)
        print("output file: " + output_file+".json")
