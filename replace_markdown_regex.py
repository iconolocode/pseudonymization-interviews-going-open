# "error_log.txt" should be emptied

import pandas as pd
import re

path = "\."

table_filename = f"{path}testtable.xlsx"
text_filename = f"{path}testtranscript.docx"
newtext_filename = f"{path}testresults.docx"

if __name__ == '__main__':
    df = pd.read_excel(table_filename)

    with open(text_filename, 'r', encoding='utf-8') as file:
        text = file.read()

        for index, row in df[:55].iterrows():
            if row['Pseudonymized'] != 'not changed':

                if re.search(
                            row['Sensitive Info, original text'].strip(),
                            text,
                            flags=re.ASCII):

                    print(re.search(
                            row['Sensitive Info, original text'].strip(),
                            text,
                            flags=re.ASCII))

                    text = re.sub(
                                    row['Sensitive Info, original text'].strip(),
                                    "//CHANGED://"+str(row['Pseudonymized']),
                                    text,
                                    flags=re.ASCII)

                else:
                    with open("error_log.txt", "a") as file:
                        file.write(
                            f"""{row['Interview']} {row['Speaker']} {row["Time stamp"]}\n"""
                            f"""{row['Sensitive Info, original text'].strip()}"""
                            f"""\n{row['Pseudonymized'.strip()]}\n\n"""
                            )

        with open(newtext_filename, 'w', encoding='utf-8') as newfile:
            newfile.write(text)


