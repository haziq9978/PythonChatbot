import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from pathlib import Path

df3 = pd.read_excel('game_data.xlsx')
df3 = df3.dropna()
fullJsonMiddleFormat = ""
for i in range(len(df3)):
    # print(df3['GAMES'].iloc[i])
    tagKey = """{"tag":"""
    tagValue = "'" + str(f"{df3['GAMES'].iloc[i]}") + "',"
    TAG = tagKey + tagValue

    temp = [str(df3['GAMES'].iloc[i]) + ' requirements', str(df3['GAMES'].iloc[i])]
    finalResult = word_tokenize(df3['GAMES'].iloc[i]) + temp
    # print(finalResult)

    patternsKey = """"patterns":"""
    # patternsValue = "'" + f"{df3['GAMES'].iloc[i]} requirements" + "'" + "," + "'" + f"{df3['GAMES'].iloc[i]}" + "'"
    PATTERNS = patternsKey + f"{finalResult},"

    txt = df3['MR'].iloc[i]
    cpu = "\\" + "n" + txt[txt.find("CPU"):txt.find("GPU")] + "\\" + "n"
    gpu =  cpu + txt[txt.find("GPU"):txt.find("RAM")] + "\\" + "n"
    ram = gpu + txt[txt.find("RAM"):txt.find("VRAM")] + "\\" + "n"
    vram = ram + txt[txt.find("VRAM"):] + "\\" + "n" + "\\" + "n"
    
    txt2 = df3['RR'].iloc[i]
    cpu2 = "\\" + "n" + txt2[txt2.find("CPU"):txt2.find("GPU")] + "\\" + "n"
    gpu2 =  cpu2 + txt2[txt2.find("GPU"):txt2.find("RAM")] + "\\" + "n"
    ram2 = gpu2 + txt2[txt2.find("RAM"):txt2.find("VRAM")] + "\\" + "n"
    vram2 = ram2 + txt2[txt2.find("VRAM"):]

    responsesKey = """"responses":"""
    responsesValue = "['"+ "\\" + "n" + "---------------------------------------------------------"+ "\\" + "n"+f"MINIMUM: {df3['GAMES'].iloc[i]}" + f"{vram}" + "\\" + "n" + "\\" + "n" + f"RECOMMENDED {df3['GAMES'].iloc[i]}" + f"{vram2}" + "\\" + "n" + "---------------------------------------------------------"+ "\\" + "n"+"'],"
    REPONSES = responsesKey + f"{responsesValue}"


    jsonMiddleFormat = "\n\t" + TAG + "\n\t" + PATTERNS + "\n\t" + REPONSES + "\n\t" + """"context": [""]},\n\n\t"""
    fullJsonMiddleFormat = fullJsonMiddleFormat + jsonMiddleFormat

fullJsonFormat = """{"intents":[\n\t""" + fullJsonMiddleFormat[:-1] + """\n\t]}"""
# print(fullJsonFormat)

#convert json to text file
text_file = open("intents.json", "wt")
n = text_file.write(fullJsonFormat)
text_file.close()