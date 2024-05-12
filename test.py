import cv2
import numpy as np
import pytesseract
import re
import time

start = time.time()

def scan(image_path):
    
    img = cv2.imread(image_path)
    result = pytesseract.image_to_string(image_path, lang="eng")
    print(result)
    return result


def findDOB(text):    

    
    pattern1 = r"\d{2}\/\d{2}\/\d{4}"

    if(re.findall(pattern1, text)):
        print("----DOB FOUND----")
        return (re.findall(pattern1, text))[0]

    
    else:
        pattern2 = r'\S.{6,10}\S'   
        #his regular expression pattern will match strings that start and end with non-whitespace characters, have a total length of 8 to 12 characters, and can include whitespace characters in between.

        # Find all matches of the pattern in the text
        matches = re.findall(pattern2, text)
        
        
        # Filter the matches
        filtered_matches = []
        for match in matches:
            if match.count('/') in (1, 2) and 7 <= len(re.findall(r'\d', match)) <= 8:
                filtered_matches.append(match)

            max_digits = 0
            max_digit_string = ""

            for string in filtered_matches:
                digit_count = sum(char.isdigit() for char in string)
                if digit_count > max_digits:
                    max_digits = digit_count
                    max_digit_string = string
        print("----DOB FOUND----")
        return max_digit_string


def uid(text):
    
    
    # pan 10 digits - 5 char 4 digit 1 char
    # pan keywords - INCOME, PAN, PERMANENT
    if ("INCOME" in text or "I N C O M E" in text or "I NCOME" in text or "INCOM E" in text or "INCOME55" in text or "4NCOME" in text or "INCOM" in text or "INC OME" in text or "INCOM$" in text or "INCOM5E" in text or "PAN" in text or "PA N" in text or "P AN" in text or "P A N " in text or "PAN55" in text or "PANSS" in text or "PERMANENT" in text or "PERMANEN" in text or "PERM4NENT" in text or "PERMANE" in text):
        print("hihi")
        pattern1 = r"[A-Za-z]{5}\d{4}[A-Za-z]"
        if (re.findall(pattern1, text)):
            print("----UID FOUND----")
            return re.findall(pattern1, text)[0]
        else:
            pattern2 = r'\S.{7,11}\S'  
            matches = re.findall(pattern2, text)
            text = text.upper()
            
            for string in matches:
                if re.search(r'\d{3,5}', string) and re.search(r'[a-zA-Z]{5,7}', string):
                    print("----UID FOUND----")
                    return string 
    # for voter id card
    # 10 length 3 chars 7 digits         

    elif "ELECTION" in text or "E L E C T I O N" in text or "ELECTIO N" in text or "ELECTION55" in text or "COMMISSION" in text or "C O M M I S S I O N" in text or "COMMISSION55" in text or "COMMI$$ION" in text or "C0MM1SS1ON" in text or "ELEC71ON" in text or "COMM15SI0N" in text or    "3LECTI0N" in text or "C0MM1SSI0N" in text or    "ELEETI0N" in text or "K0MMI55I0N" in text or    "EL3C710N" in text or "K0MMS51ON" in text or    "3L3C710N" in text or "C0MM15SI0N" in text or    "EL3CTI0N" in text or "K0MM15510N" in text or    "3LECT10N" in text or "C0MM1S510N" in text or    "ELEKTION" in text or "KOMMI55ION" in text or    "3LEKT1ON" in text or "K0M1SSI0N" in text or "ELECHUN" in text or "COMMISHUN" in text or    "3LEKT10N" in text or "C0M1SS10N" in text or    "EL3K71ON" in text or "K0MMI5HUN" in text:
        
        pattern1 = r"^[A-Za-z]{3}[A-Za-z]{7}$"
        if (re.findall(pattern1, text)):
            print("----UID FOUND----")
            return re.findall(pattern1, text)[0]
        else:
            pattern2 = r'\S.{7,11}\S'  
            matches = re.findall(pattern2, text)
            text = text.upper()
            for string in matches:
                if  re.search(r'[a-zA-Z]{2,5}', string)and re.search(r'\d{5,9}', string):
                    print("----UID FOUND----")
                    return string 

    # assuming it is aaadhaar card if all other conditions fail
    else:
        pattern1=r'\b\d{4}\s\d{4}\s\d{4}\b'
        if (re.findall(pattern1, text)):
            print("----UID FOUND----")
            return re.findall(pattern1, text)[0]
        else:
            pattern2 = r'\S.{9,14}\S'   
            matches = re.findall(pattern2, text)
            text = text.upper()
            for string in matches:
                if re.search(r'\d{9,13}', string) and re.search(r'[a-zA-Z]{0,3}', string) and re.search(r'\s{0,3}', string):
  
                    print("----UID FOUND----")
                    return string 
    


startTime = time.time()


image_path="./aadhaar.png"

print("reading...")
# scan with OCR
text=scan(image_path)

print("\n***\n")

# scan for dob
dob = findDOB(text)
print(dob)

print("\n***\n")

#scan for UID
id = uid(text)
print(id)

print("\n***\n")

endTime = time.time()

print("Total Time Taken: "+str(endTime - startTime))