import os
import re
import json

folderPath = r""
newSubId = r""
newLogicappId = r""

oldSubId = r'([^/])+([0-9])+(-)+([a-zA-Z0-9])+(-)+([a-zA-Z0-9])+(-)+([a-zA-Z0-9])+(-)+([a-zA-Z0-9])+([$/])'
oldLogicappId = r'(LogicApp_+[a-zA-Z]+_*[a-zA-z]+_)+([a-zA-Z0-9])+\b'

## TODO: import json frm az cli query

# Function to look through a file and replace a regex pattern with a preset string
def replaceSubId(apiFile, folderPath, regexPattern, newString):

    # Set open method to readContent with read permissions
    with open(os.path.join(folderPath, apiFile), 'r+') as readContent:

        # Set content of file to a string var
        streamString = readContent.read()

        # Search for occurrences of regex pattern
        changes = re.compile(regexPattern).finditer(streamString)

        # For each occurrance print result
        for change in changes:
            print(change)

        # Replace each occurrence and set to a new string
        newContent = re.sub(regexPattern, newString, streamString)

    # Set open method to writeContent with write permissions
    with open(os.path.join(folderPath, apiFile), 'w') as WriteContent:
        
        # Replace file with new string
        WriteContent.write(newContent)
    
    # return when done with file
    return f'{apiFile} done'

# Files from ./apiManagement
files = os.listdir(folderPath)

# Replace sub id then logic app id
for apifile in files:
    print(replaceSubId(apifile, folderPath, oldSubId, newSubId))
    print(replaceSubId(apifile, folderPath, oldLogicappId, newLogicappId))