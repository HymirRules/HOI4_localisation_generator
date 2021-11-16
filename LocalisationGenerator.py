from enum import Enum
from pathlib import Path
import os
import sys
import argparse
import re

class FileTypes(Enum):
    focustree = 1
    ideas = 2
    events = 3
    decisions = 4

def import_techs_units(mod_directory):
    techPath = Path(mod_directory) / "common" / "technologies"
    remove_ids = [
        re.compile("(={)$")
    ]
    ignore_ids = [
        re.compile("technologies="),
        re.compile("add_to_variable="),
        re.compile("enable_subunits="),
        re.compile("modifier="),
        re.compile("ai_will_do="),
        re.compile("dependencies="),
        re.compile("sub_units="),
        re.compile("type="),
        re.compile("categories="),
        re.compile("essential="),
        re.compile("need="),
        re.compile("jungle="),
        re.compile("forest="),
        re.compile("marsh="),
        re.compile("hills="),
        re.compile("mountain="),
        re.compile("amphibious="),
        re.compile("urban="),
        re.compile("fort="),
        re.compile("desert="),
        re.compile("plains="),
        re.compile("river="),
        re.compile("path="),
        re.compile("folder="),
        re.compile("if="),
        re.compile("limit="),
        re.compile("XOR="),
        re.compile("enable_equipments="),
        re.compile("on_research_complete"),
        re.compile("NOT="),
        re.compile("OR="),
        re.compile("hidden_effect="),
        re.compile("allow="),
        re.compile("ai_research_weights=")
    ]

    techs_and_units = []

    if os.path.isdir(techPath):
        for fileName in os.listdir(techPath):
            if fileName.endswith(".txt"):
                techFile = Path(techPath) / fileName
                with open(techFile, "r") as f:
                    tech = f.readlines()
                for s in tech:
                    s = s.strip()
                    s = s.replace(" ", "")
                    if (any(regex.search(s) for regex in remove_ids)
                        and not any(r.search(s) for r in ignore_ids)):
                            for uniqueId in remove_ids:
                                remove_id = re.search(uniqueId, s)
                                if not remove_id == None:
                                    techs_and_units.append(re.compile(s))

    unitsPath = Path(mod_directory) / "common" / "units"

    if os.path.isdir(unitsPath):
        for fileName in os.listdir(unitsPath):
            if fileName.endswith(".txt"):
                unitFile = Path(unitsPath) / fileName
                with open(unitFile, "r") as f:
                    unit = f.readlines()
                for s in unit:
                    s = s.strip()
                    s = s.replace(" ", "")
                    if (any(regex.search(s) for regex in remove_ids)
                        and not any(r.search(s) for r in ignore_ids)):
                        for uniqueId in remove_ids:
                            remove_id = re.search(uniqueId, s)
                            if not remove_id == None:
                                techs_and_units.append(re.compile(s))


    return techs_and_units




if __name__ == '__main__':

    local_parser = argparse.ArgumentParser(prog='Localisation Generator',
                                           description='Generates a localisation file based on hoi4 pdxscript file')

    local_parser.add_argument(
        'ModPath',
        metavar='path',
        type=Path,
        help="the path to the mod")

    local_parser.add_argument(
        'FileType',
        metavar='filetype',
        type=str,
        help="The type of file that will be converted")

    local_parser.add_argument(
        'FilePath',
        metavar='filename',
        type=Path,
        help="path to the starting file")

    local_parser.add_argument(
        'LocPath',
        metavar='locname',
        type=Path,
        help="path to the localisation file")

    args = local_parser.parse_args()

    mod_location = args.ModPath
    type_of_file = args.FileType
    file_location = args.FilePath
    loc_location = args.LocPath

    file = Path(file_location).with_suffix(".txt")

    if FileTypes[type_of_file] == FileTypes.focustree:
        file_path = Path(mod_location) / "common" / "national_focus" / file
        idsToRemoveRegex = [re.compile("^id=")]
    elif FileTypes[type_of_file] == FileTypes.ideas:
        file_path = Path(mod_location) / "common" / "ideas" / file
        idsToRemoveRegex = [re.compile("(={)$")]
    elif FileTypes[type_of_file] == FileTypes.events:
        file_path = Path(mod_location) / "events" / file
        idsToRemoveRegex = [
            re.compile("title="),
            re.compile("desc="),
            re.compile("name=")
        ]
    else:
        file_path = Path(mod_location) / "common" / "decisions" / file
        idsToRemoveRegex = [re.compile("(={)$")]

    idsToRemoveRegex.append(re.compile("([a-zA-Z]+_)+tooltip="))

    if not os.path.isdir(mod_location):
        print('The mod path specified does not exist')
        sys.exit()

    if not os.path.isfile(file_path):
        print("This file does not exist")
        sys.exit()

    import_techs_units(mod_location)

    with open(file_path, 'r') as f:
        file = f.readlines()

    fileIds = []



    idsToIgnoreRegex = [
        re.compile("[0-9]+="),
        re.compile("[a-zA-Z]+?_?modifier="),
        re.compile("available="),
        re.compile("allowed(_[a-zA-Z]+)*?="),
        re.compile("[a-zA-Z]+_bonus="),
        re.compile("[a-zA-Z]+_equipment="),
        re.compile("visible="),
        re.compile("limit="),
        re.compile("ai_will_do="),
        re.compile("hidden_[a-zA-Z]+="),
        re.compile("on_add="),
        re.compile("#"),
        re.compile("set(_[a-zA-Z]+)+="),
        re.compile("any(_[a-zA-Z]+)+="),
        re.compile("check_variable="),
        re.compile("has_country_flag="),
        re.compile("cancel="),
        re.compile("motorized="),
        re.compile("([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?$"),
        re.compile("ideas="),
        re.compile("modifier="),
        re.compile("country="),
        re.compile("ship_hull(_[a-zA-Z]+)+="),
        re.compile("convoy="),
        re.compile("^[a-zA-Z]{3}={$"),
        re.compile("custom_trigger_tooltip="),
        re.compile("effect_tooltip=")
    ]

    for tech_unit in import_techs_units(mod_location):
        idsToIgnoreRegex.append(tech_unit)

    for string in file:
        string = string.strip()
        string = string.replace(" ", "")

        if (any(regex.search(string) for regex in idsToRemoveRegex)
                and not any(r.search(string) for r in idsToIgnoreRegex)):
            for id in idsToRemoveRegex:
                removeId = re.search(id, string)
                if not removeId == None:
                    string = string.replace(removeId.group(0), "")
                    string = string + ":0\"Placeholder Localisation\"\n"
                    fileIds.append(string)

    loc_file_location = Path(loc_location).with_suffix(".yml")
    loc_location = Path(mod_location) / "localisation" / loc_file_location

    if os.path.isfile(loc_location):
        loc_exists = True
    else:
        loc_exists = False

    with open(loc_location, "a") as loc_file:
        for string in fileIds:
            try:
                strippedString = string.strip(":0 \"Placeholder Localisation\"\n")
                if not loc_file.readline().startswith(strippedString):
                    loc_file.writelines(string)
            except:
                loc_file.writelines(string)

    with open(loc_location, "r+") as f:
        lines_seen = set()

        d = f.readlines()
        f.seek(0)
        for i in d:
            a, b, c = i.partition(":")
            if a not in lines_seen:
                f.writelines(i)
                lines_seen.add(a)
        f.truncate()

    if loc_exists:
        print("Successfully saved the localisation IDs to the file")
    else:
        print("Successfully create the localisation file and saved the localisation IDs to the file")
