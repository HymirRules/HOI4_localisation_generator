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
        metavar='filepath',
        type=Path,
        help="path to the starting file")

    local_parser.add_argument(
        'LocPath',
        metavar='locpath',
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
        idsToRemoveRegex = [re.compile("id=")]
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
        re.compile("^[a-zA-Z]{3}={$")
    ]

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
