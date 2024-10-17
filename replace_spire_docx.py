# 23/06/2024

# "error_log.txt" should be emptied

# https://github.com/eiceblue/Spire.Doc-for-Python/tree/main/Python%20Examples/02_FindAndReplace

import pandas as pd
from spire.doc import *

path = "C:\Docs\open ling data\\"

table_filename = f"{path}testdata.xlsx"
text_filename = f"{path}testranscript_no_paragraphs.docx"
newtext_filename = f"{path}test-results.docx"

if __name__ == '__main__':
    df = pd.read_excel(table_filename)
    document = Document()
    document.LoadFromFile(text_filename)

    for index, row in df.iterrows():
        if row['Pseudonymized'] != 'not changed':
            try: #Sensitive Info, original text
                document.Replace(row['Sensitive Info, orginal text'].rstrip(),
                                 "//CHANGED://"+str(row['Pseudonymized']),
                                 False, False)

            except:
                with open("error_log.txt", "a") as file:
                    file.write(
                        f"""{row['Interview']} {row['Speaker']} {row["Time Stamp"]}\n"""
                        f"""{row['Sensitive Info, orginal text'].strip()}"""
                        f"""\n{row['Pseudonymized'.strip()]}\n\n"""
                        )

    document.SaveToFile(newtext_filename)
    document.Close()

