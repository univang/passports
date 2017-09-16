import zipfile
import xml.etree.ElementTree
from instances import *
from word_gen import *
from myfuncs import *


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

# print(isEnglish('хаtest'))


WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'
TABLE = WORD_NAMESPACE + 'tbl'
ROW = WORD_NAMESPACE + 'tr'
CELL = WORD_NAMESPACE + 'tc'

# TABLE = 'tbl'
# ROW = 'tr'
# CELL = 'tc'

with zipfile.ZipFile('C:/Users/mrpet/Desktop/passports/sample.docx') as docx:
    tree = xml.etree.ElementTree.XML(docx.read('word/document.xml'))

with zipfile.ZipFile('C:/Users/mrpet/Desktop/passports/sample.docx') as docx:
    HeaderTree = xml.etree.ElementTree.XML(docx.read('word/header3.xml'))
# for table in tree.iter(TABLE):
#     for row in table.iter(ROW):
#         for cell in row.iter(CELL):
#             # print(''.join(node.text for node in cell.iter(TEXT)))
#             for node in cell.iter(TEXT):
#             	print(node.text)


PARAGRAPH = WORD_NAMESPACE + 'p' 
TEXT = WORD_NAMESPACE + 't' 
STYLE = WORD_NAMESPACE + 'pStyle'
TABLE = WORD_NAMESPACE + 'tbl'
ROW   = WORD_NAMESPACE + 'tr'
CELL  = WORD_NAMESPACE + 'tc'
CONTENT = WORD_NAMESPACE + 'r'

strObj = ''
lst = []
masterList = []

for i, table in enumerate(tree.iter(TABLE)):
	# if i < 18:
	if True:

		for num_row, row in enumerate(table.iter(ROW)):
			rowEl = []

			for cell in row.iter(CELL):
				cellEl = []

				for node in cell.iter(PARAGRAPH):
					for rel in node.iter(CONTENT):
						for T in rel.iter(TEXT):
							length = len(T.text)
							if (T.text[length-1] == ',' or T.text[length-1] == '.'):
								strObj+= T.text + '\n'
							else:
								strObj += T.text + ' '
					cellEl.append(strObj)
				# print(cellEl)
				
				lst.append(strObj)
				strObj = ''
				rowEl.append(cellEl)
			if len(rowEl) <= 2:
				rowEl = [item for sublist in rowEl for item in sublist]
				
				# print(rowEl)
				
				for i in TargetList:
					# and (i.value is None) "Tochka 1" over "Tochka 2"
					if compare(i.tag, rowEl[0]) and (i.entry == 0):
						i.entry = i.entry + 1
						i.value = rowEl[-1]
						# print(i.tag)
						# print(rowEl)
						# print('-------------------------')



for i, table in enumerate(HeaderTree.iter(TABLE)):
	# if i < 18:
	if True:
		print(i)

		for num_row, row in enumerate(table.iter(ROW)):
			rowEl = []

			for cell in row.iter(CELL):
				cellEl = []

				for node in cell.iter(PARAGRAPH):
					for rel in node.iter(CONTENT):
						for T in rel.iter(TEXT):
							length = len(T.text)
							if (T.text[length-1] == ',' or T.text[length-1] == '.'):
								strObj+= T.text + '\n'
							else:
								strObj += T.text + ' '
					cellEl.append(strObj)
				# print(cellEl)
				
				lst.append(strObj)
				strObj = ''
				rowEl.append(cellEl)
			if len(rowEl) <= 2:

				rowEl = [item for sublist in rowEl for item in sublist]
				# print(rowEl[-1])
				if (TargetList[0].tag in rowEl[-1]) and (TargetList[0].entry == 0):
					TargetList[0].entry = TargetList[0].entry + 1
					TargetList[0].value = rowEl[-1]
					# print(i.tag)
					# print(rowEl)
					# print('-------------------------')
					
				if isEnglish(rowEl[0]) and rowEl[0]:
					TargetList.append(TableRow('Название', value=rowEl[0], method=None))
					TargetList.append(TableRow('Имя', value=rowEl[0], method=NAME))
# 					



# Проставок
TargetList[14].value = TargetList[12].value

for i in TargetList:
	i.process()
	TableRow.printObj(i)


generate_Word(TargetList, 'my_template.docx')

