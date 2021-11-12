from pathlib import Path


def focustreeType(modDirectory):
    fileName = input("Enter filename to read in from: ")
    fileName = fileName + ".txt"
    fileName = modDirectory + "/common/national_focus/" + fileName
    f = open(fileName, 'r')
    file = f.readlines()

    focusIds = []
    tooltipIds = []

    for string in file:
        strippedString = string.strip()

        if strippedString.startswith("id = ") and (not strippedString.startswith('id = nf')):
            removedIDString = strippedString.replace("id = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Localisation\" \n"
            focusIds.append(removedIDString)
        elif strippedString.startswith("custom_effect_tooltip = "):
            removedIDString = strippedString.replace("custom_effect_tooltip = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Localisation\" \n"
            tooltipIds.append(removedIDString)
        elif strippedString.startswith("tooltip = "):
            removedIDString = strippedString.replace("tooltip = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Localisation\" \n"
            tooltipIds.append(removedIDString)

    f.close()

    fileName = input("Enter a filename to write these ids to: ")
    fileName = fileName + ".yml"
    fileName = modDirectory + "/localisation/" + fileName
    filePath = Path(fileName)
    if filePath.is_file():
        locFile = open(fileName, "a")
    else:
        locFile = open(fileName, 'w+')

    locFile.writelines("#Focus IDs:\n")
    for string in focusIds:
        try:
            snippedString = string.strip(":0 \"Placeholder Localisation\" \n")
            if not locFile.readline().startswith(snippedString):
                locFile.writelines(string)
        except:

            locFile.writelines(string)

    locFile.writelines("#Tooltip IDs:\n")
    for string in tooltipIds:
        try:
            snippedString = string.strip(":0 \"Placeholder Localisation\" \n")
            if not locFile.readline().startswith(snippedString):
                locFile.writelines(string)
        except:
            locFile.writelines(string)

    locFile.close()

    with open(fileName, "r+") as f:
        lines_seen = set()

        d = f.readlines()
        f.seek(0)
        for i in d:
            a, b, c = i.partition(":")
            if a not in lines_seen:
                f.writelines(i)
                lines_seen.add(a)
        f.truncate()

def eventType(modDirectory):
    fileName = input("Enter filename to read in from: ")
    fileName = fileName + ".txt"
    fileName = modDirectory + "/events/" + fileName
    f = open(fileName, 'r')
    file = f.readlines()

    eventIds = []
    toolTipIds = []

    for string in file:
        strippedString = string.strip()

        if strippedString.startswith("title = "):
            removedIDString = strippedString.replace("title = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Localisation\" \n"
            eventIds.append(removedIDString)
        elif strippedString.startswith("desc = "):
            removedIDString = strippedString.replace("desc = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Localisation\" \n"
            eventIds.append(removedIDString)
        elif strippedString.startswith("name = "):
            removedIDString = strippedString.replace("name = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Localisation\" \n"
            eventIds.append(removedIDString)
        elif strippedString.startswith("custom_effect_tooltip = "):
            removedIDString = strippedString.replace("custom_effect_tooltip = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Localisation\" \n"
            toolTipIds.append(removedIDString)
        elif strippedString.startswith("tooltip = "):
            removedIDString = strippedString.replace("tooltip = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Localisation\" \n"
            toolTipIds.append(removedIDString)

    f.close()

    fileName = input("Enter a filename to write these ids to: ")
    fileName = fileName + ".yml"
    fileName = modDirectory + "/localisation/" + fileName
    filePath = Path(fileName)
    if filePath.is_file():
        f = open(fileName, "a")
    else:
        f = open(fileName, 'w+')

    f.writelines("#Event IDs:\n")
    for string in eventIds:
        try:
            snippedString = string.strip(":0 \"Placeholder Localisation\" \n")
            if not f.readline().startswith(snippedString):
                f.writelines(string)
        except:
            f.writelines(string)

    f.writelines("#Tooltip IDs:\n")
    for string in toolTipIds:
        try:
            snippedString = string.strip(":0 \"Placeholder Localisation\" \n")
            if not f.readline().startswith(snippedString):
                f.writelines(string)
        except:
            f.writelines(string)

    f.close()

    with open(fileName, "r+") as f:
        lines_seen = set()

        d = f.readlines()
        f.seek(0)
        for i in d:
            a, b, c = i.partition(":")
            if a not in lines_seen:
                f.writelines(i)
                lines_seen.add(a)
        f.truncate()


def ideaType(modDirectory):
    fileName = input("Enter filename to read in from: ")
    fileName = fileName + ".txt"
    fileName = modDirectory + "/common/ideas/" + fileName
    f = open(fileName, 'r')
    file = f.readlines()

    ideaIds = []
    toolTipIds = []

    bannedStrings = ("ideas = ", "country = ", "modifier = ", "available = ", "allowed = ", "targeted_modifier = ",
                     "allowed_civil_war = ", "research_bonus = ", "equipment_bonus = ", "infantry_equipment = ",
                     "motorized_equipment = ", "demolitions_equipment = ", "visible = ", "limit = ", "ai_will_do = ",
                     "allowed_to_remove = ", "hidden_trigger = ", "on_add = ", "#", "set_temp_variable = ",
                     "add_dynamic_modifier = ", "set_variable = ", "any_enemy_country = ", "check_variable = ",
                     "hidden_ideas = ", "has_country_flag = ", "set_country_flag = ")

    for string in file:
        strippedString = string.strip()

        if strippedString.endswith(" = {") and (not strippedString.startswith(bannedStrings)):
            strippedString = strippedString.replace(" = {", "")
            removedIDString = strippedString + ":0 \"Placeholder Title\" \n"
            if len(strippedString) > 4:
                ideaIds.append(removedIDString)
        elif strippedString.startswith("custom_effect_tooltip = "):
            removedIDString = strippedString.replace("custom_effect_tooltip = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Localisation\" \n"
            toolTipIds.append(removedIDString)
        elif strippedString.startswith("tooltip = "):
            removedIDString = strippedString.replace("tooltip = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Localisation\" \n"
            toolTipIds.append(removedIDString)
        elif strippedString.startswith("custom_trigger_tooltip = "):
            removedIDString = strippedString.replace("custom_trigger_tooltip = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Localisation\" \n"
            toolTipIds.append(removedIDString)

    f.close()

    fileName = input("Enter a filename to write these ids to: ")
    fileName = fileName + ".yml"
    fileName = modDirectory + "/localisation/" + fileName
    f = open(fileName, 'w+')

    f.writelines("#Idea IDs:\n")
    for string in ideaIds:
        try:
            snippedString = string.strip(":0 \"Placeholder Localisation\" \n")
            if not f.readline().startswith(snippedString):
                f.writelines(string)
        except:
            f.writelines(string)

    f.writelines("#Tooltip IDs:\n")
    for string in toolTipIds:
        try:
            snippedString = string.strip(":0 \"Placeholder Localisation\" \n")
            if not f.readline().startswith(snippedString):
                f.writelines(string)
        except:
            f.writelines(string)

    f.close()

    with open(fileName, "r+") as f:
        lines_seen = set()

        d = f.readlines()
        f.seek(0)
        for i in d:
            a, b, c = i.partition(":")
            if a not in lines_seen:
                f.writelines(i)
                lines_seen.add(a)
        f.truncate()

def decisionType(modDirectory):
    fileName = input("Enter filename to read in from: ")
    fileName = fileName + ".txt"
    fileName = modDirectory + "/common/decisions/" + fileName
    f = open(fileName, 'r')
    file = f.readlines()

    decisionIds = []
    toolTipIds = []

    bannedStrings = ("available = ", "visible = ", "visible = ", "complete_effect = ", "remove_effect = ", "if = ",
                     "add_building_construction = ", "every_owned_state = ", "limit = ", "highlight_states = ",
                     "start_border_war = ", "attacker = ", "defender = ")

    for string in file:
        strippedString = string.strip()

        if strippedString.endswith(" = {") and (not strippedString.startswith(bannedStrings)):
            strippedString = strippedString.replace(" = {", "")
            removedIDString = strippedString + ":0 \"Placeholder Localisation\" \n"
            if len(strippedString) > 4:
                decisionIds.append(removedIDString)
        elif strippedString.startswith("custom_effect_tooltip = "):
            removedIDString = strippedString.replace("custom_effect_tooltip = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Localisation\" \n"
            toolTipIds.append(removedIDString)
        elif strippedString.startswith("tooltip = "):
            removedIDString = strippedString.replace("tooltip = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Localisation\" \n"
            toolTipIds.append(removedIDString)

    f.close()

    fileName = input("Enter a filename to write these ids to: ")
    fileName = fileName + ".yml"
    fileName = modDirectory + "/localisation/" + fileName
    filePath = Path(fileName)
    if filePath.is_file():
        f = open(fileName, "a")
    else:
        f = open(fileName, 'w+')

    f.writelines("#Decision IDs:\n")
    for string in decisionIds:
        try:
            snippedString = string.strip(":0 \"Placeholder Localisation\" \n")
            if not f.readline().startswith(snippedString):
                f.writelines(string)
        except:
            f.writelines(string)

    f.writelines("#Tooltip IDs:\n")
    for string in toolTipIds:
        try:
            snippedString = string.strip(":0 \"Placeholder Localisation\" \n")
            if not f.readline().startswith(snippedString):
                f.writelines(string)
        except:
            f.writelines(string)

    f.close()

    with open(fileName, "r+") as f:
        lines_seen = set()

        d = f.readlines()
        f.seek(0)
        for i in d:
            a, b, c = i.partition(":")
            if a not in lines_seen:
                f.writelines(i)
                lines_seen.add(a)
        f.truncate()


if __name__ == '__main__':

    fileType = input("What kind of file do you want to extract localisation ids from: \n"
                     "F - Focus tree\n"
                     "E - Events\n"
                     "I - Ideas\n"
                     "D - Decisions\n")

    fileType = fileType.upper()

    ### ENTER YOUR MOD DIRECTORY BELOW ###
    modDirectory = "C:/userdirectory/moddirectory"

    if fileType == "F":
        focustreeType(modDirectory)
    elif fileType == "E":
        eventType(modDirectory)
    elif fileType == "I":
        ideaType(modDirectory)
    elif fileType == "D":
        decisionType(modDirectory)
    else:
        print("invalid entry >:(")


