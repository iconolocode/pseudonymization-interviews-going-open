# "error_log.txt" should be emptied

import pandas as pd

path = "\."

table_filename = f"{path}testtable.xlsx"
text_filename = f"{path}testtranscript.docx"
newtext_filename = f"{path}testresults.docx"

if __name__ == '__main__':


    with open("error_log.txt", "w") as tempfile:
        tempfile.write("") # make empty

    df = pd.read_csv(table_filename, encoding='utf8')
    df['Sensitive Info, original text'] = df['Sensitive Info, original text'].str.replace(u"\u00A0", " ")
    df['Pseudonymized'] = df['Pseudonymized'].str.replace(u"\u00A0", " ")

    df['Sensitive Info, original text'] = df['Sensitive Info, original text'].str.replace("'", u"\u2019")
    df['Pseudonymized'] = df['Pseudonymized'].str.replace("'", u"\u2019")

    with open(text_filename, 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.replace("'", u"\u2019")

        for index, row in df.iterrows():
            if row['Pseudonymized'] != 'not changed':

                if text.find(row['Sensitive Info, original text'].strip()) > 0:

                    text = text.replace(row['Sensitive Info, original text'].strip(),
                                "//CHANGED://"+str(row['Pseudonymized']))

                else:
                    with open("error_log.txt", "a", encoding='utf-8') as tempfile:
                        tempfile.write(
                            f"""{row['Interview']} {row['Speaker']} {row["Time stamp"]}\n"""
                            f"""{row['Sensitive Info, original text'].strip()}"""
                            f"""\n{row['Pseudonymized'.strip()]}\n\n"""
                            )

        with open(newtext_filename, 'w', encoding='utf-8') as newfile:
            newfile.write(text)


