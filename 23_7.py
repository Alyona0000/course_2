import docx
import os
import glob
import re

if __name__ == '__main__':
    #'Dir4\\'
    path = input('Enter path to directory: ')
    #r'\d{2}.\d{2}.\d{4}'
    regex = re.compile(r'\d{2}.\d{2}.\d{4}')#input('Enter regex: ')
    mask = '*.docx'

    for dirpath, _, __ in os.walk(path):
        for file in glob.glob1(dirpath, mask):
            for i, par in enumerate(docx.Document(rf'{dirpath}\{file}').paragraphs):
                match = regex.search(par.text)

                if match:
                    print(rf"Match: '{match.group()}' in '{dirpath}\{file}'. Line #{i + 1}. Text: {par.text}")

            print()
