def focustreeType():
    fileName = input("Enter filename to read in from: ")
    fileName = fileName + ".txt"
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
    f = open(fileName, 'w+')

    f.writelines("#Focus IDs:\n")
    for string in focusIds:
        f.writelines(string)

    f.writelines("#Tooltip IDs:\n")
    for string in tooltipIds:
        f.writelines(string)

    f.close()

def eventType():
    fileName = input("Enter filename to read in from: ")
    fileName = fileName + ".txt"
    f = open(fileName, 'r')
    file = f.readlines()

    eventIds = []
    toolTipIds = []

    for string in file:
        strippedString = string.strip()

        if strippedString.startswith("title = "):
            removedIDString = strippedString.replace("title = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Title\" \n"
            eventIds.append(removedIDString)
        elif strippedString.startswith("desc = "):
            removedIDString = strippedString.replace("desc = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Description\" \n"
            eventIds.append(removedIDString)
        elif strippedString.startswith("name = "):
            removedIDString = strippedString.replace("name = ", "")
            removedIDString = removedIDString + ":0 \"Placeholder Description\" \n"
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
    f = open(fileName, 'w+')

    f.writelines("#Event IDs:\n")
    for string in eventIds:
        f.writelines(string)

    f.writelines("#Tooltip IDs:\n")
    for string in toolTipIds:
        f.writelines(string)

    f.close()


def ideaType():
    fileName = input("Enter filename to read in from: ")
    fileName = fileName + ".txt"
    f = open(fileName, 'r')
    file = f.readlines()

    ideaIds = []
    toolTipIds = []

    bannedStrings = ("ideas = ", "country = ", "modifier = ", "available = ", "allowed = ", "targeted_modifier = ",
                     "allowed_civil_war = ", "research_bonus = ", "equipment_bonus = ", "infantry_equipment = ",
                     "motorized_equipment = ", "demolitions_equipment = ")

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

    f.close()

    fileName = input("Enter a filename to write these ids to: ")
    fileName = fileName + ".yml"
    f = open(fileName, 'w+')

    f.writelines("#Idea IDs:\n")
    for string in ideaIds:
        f.writelines(string)

    f.writelines("#Tooltip IDs:\n")
    for string in toolTipIds:
        f.writelines(string)

    f.close()

def decisionType():
    fileName = input("Enter filename to read in from: ")
    fileName = fileName + ".txt"
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
    f = open(fileName, 'w+')

    f.writelines("#Decision IDs:\n")
    for string in decisionIds:
        f.writelines(string)

    f.writelines("#Tooltip IDs:\n")
    for string in toolTipIds:
        f.writelines(string)

    f.close()


if __name__ == '__main__':

    fileType = input("What kind of file do you want to extract localisation ids from: \n"
                     "F - Focus tree\n"
                     "E - Events\n"
                     "I - Ideas\n"
                     "D - Decisions\n")

    fileType = fileType.upper()

    if fileType == "F":
        focustreeType()
    elif fileType == "E":
        eventType()
    elif fileType == "I":
        ideaType()
    elif fileType == "D":
        decisionType()
    else:
        print("invalid entry >:(")


