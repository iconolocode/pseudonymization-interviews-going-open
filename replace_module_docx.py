# "error_log.txt" should be emptied

# https://python-docx.readthedocs.io/en/latest/

# TOOO replace function doesn't work

import pandas as pd
from docx import Document
from python_docx_replace import docx_replace

path = "\."

table_filename = f"{path}testtable.xlsx"
text_filename = f"{path}testtranscript.docx"
newtext_filename = f"{path}testresults.docx"


if __name__ == '__main__':
    df = pd.read_excel(table_filename)
    document = Document(text_filename)

    for index, row in df.iterrows():
        if row['Pseudonymized'] != 'not changed':
            try:
                docx_replace(document,
                             original=row['Sensitive Info, orginal text'].rstrip(),
                             pseudonymized="//CHANGED://"+str(row['Pseudonymized'])
                             )

            except:
                with open("error_log.txt", "a") as file:
                    file.write(
                        f"""{row['Interview']} {row['Speaker']} {row["Time stamp"]}\n"""
                        f"""{row['Sensitive Info, orginal text'].strip()}"""
                        f"""\n{row['Pseudonymized'.strip()]}\n"""
                        )

    document.save(newtext_filename)


