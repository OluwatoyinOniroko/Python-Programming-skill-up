import re

#Task 1
xfile = open("C:/Users/HP/OneDrive/Desktop/Ty  - Fall 2023/Programming/Datasets/mbox.txt")

# read lines from the text file, and show the length of each line
wholeline = xfile.readlines()
print(wholeline)

#count the total number of lines with content
count = 0
for line in wholeline:
    if line.strip():
        count += 1
print("Total number of lines with content:", count)

#Task 2:
#Write a string function to get lines with "X-DSPAM-Confidence:"
dspam_lines = [line.strip() for line in wholeline if "X-DSPAM-Confidence:" in line]
for line in dspam_lines:
    print(line)

#creating a file for the output
with open("dspam_lines.txt", "w") as output_file:
    for line in dspam_lines:
        output_file.write(line +"\n")

#Task 3
#Use Regex to get all the urls start with "http:\\"
pattern = r'http://[^\s]+'
Curly = open("C:/Users/HP/OneDrive/Desktop/Ty  - Fall 2023/Programming/Datasets/mbox.txt")

for line in Curly:
    line = line.strip()
    search = re.search(pattern, line)
    if search:
        url = search.group()
        print(url)
