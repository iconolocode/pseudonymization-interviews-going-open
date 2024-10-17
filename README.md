These code were made during the process of “Interviews Going Open! Developing Interdisciplinary Guidelines on How to Publish Qualitative Interview Data as Open Data”. 

None of these small scripts are intended to be used as is, but to serve as inspiration. For another project, the methods might differ greatly, a new script must be made to match the particularities of the initial documents.

What these scripts do:
- prerequisites: an original transcipt (docx) and a table with the changes to apply (a column with original text and another with pseudonymized text)
- standardize differences in Unicode
- it looks in the transcript for the table's original text and replaces it with the pseudonymized text.

Different approaches were taken, as some resulted in problems due to the nature of our file formats.
In the end we converted our docx file to markdown, and used that to edit it with the pseudonymizations (replace_markdown.py), then converted it back to docx using another tool (eg. Pandoc). Some minor formatting changes were done in Word.

At the end each edited instance is preceded by //CHANGED://, double check if everything went well and use the search and replace function of your text editor.
Look at the error log and correct these instances manually.

Handy things to implement:
- better filepaths
- better logging
- fuzzy matching
- deal with inconsistencies in linebreaks (missing or new)
- deal with differences in markup (italics, bold, underline)


CC BY 4.0