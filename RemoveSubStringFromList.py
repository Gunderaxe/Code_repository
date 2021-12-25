#BY: Danial Fraser
#Note: I am an absolute beginner. This is my first practical programme. I am overexplaining everything for other beginners like myself, and for future me.
#DESCRIPTION:
    #This program was made to remove substrings from a list of strings. Particularly, I wanted to remove "MB" and "GB" from a list of my daily internet usage.
    #E.G. 2.03GB becomes 2.03, and 801MB becomes 0.801.
    #This is achieved by creating a text file called Inputlist.txt with all my daily internet usage and appending it into a list in this program called dataUsage
    #The elements in dataUsage is checked for the substring "MB" and then replaces that with "", then divides that value by 1000 to convert it to GigaBytes, and then appends it to a new list called dataUsage2
    #If the elements does not have "MB" then it checks for "GB", removes the "GB" substring and then appends that result to dataUsage2
    #Lastly, the program outputs the list of dataUsage2 into a text file called Outputlist.txt and then opens that file (using webbrowser) for convenience.
#Example for InputList.txt
    #2.62GB
    #4.74GB
    #3.14GB
    #629.23MB
    #816.09MB
#Example of result of Outputlist.txt
    #2.62
    #4.74
    #3.14
    #0.62923
    #0.81609

import webbrowser                                           #This is so the program can automatically open the Output.txt (see line 48)

dataUsage = []                                              #This is for holding the raw data from Inputlist.txt
dataUsage2 = []                                             #This is for holding the edited data for OutputList.txt

Input_File = open("Inputlist.txt", "r")                     #Opens Inputlist.txt and reads data in the file. This list will contain the unedited data such as data usage per day.
for element in Input_File:
        dataUsage.append(element)                           #Adds list from ImportList.txt into dataUsage
unwanted_substring = "MB"                                   #"MB" is one of the unwanted substrings 
for element in dataUsage:
    if unwanted_substring in element:                       #Checks if substring "MB" is in each element (or data/row/list) of dataUsage
        numberConvert = element.replace("MB", "")           #Removes "MB" string by replacing it with ""
        numberConvert = str(float(numberConvert)/1000)      #In my case, I want all my data in Gigabytes, so I have to convert the number from MB to GB
        numberConvert = numberConvert + "\n"                #Each element in the intial list of strings has "\n". Turning the string into a float caused it to lose the "\n", so I had to add it back in.
        dataUsage2.append(numberConvert)                    #Adds the edited element to another list called dataUsage2
    else:
        numberConvert = element.replace("GB", "")           #Removes "GB" string by replacing it with ""
        dataUsage2.append(numberConvert)                    #Adds the edited element to another list called dataUsage2
Input_File.close()

Output_File = open("Outputlist.txt", "w")                   #Opens Output.txt, "w" overwrites any data in the txt file
for element in dataUsage2:                                  
    Output_File.write(element)                              #Writes each element in DataUsage2 into Outputlist.txt
Output_File.close()

webbrowser.open("Outputlist.txt")                           #Automatically opens the Outputlist.txt file in notepad (or your default .txt reading program)