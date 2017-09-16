from TableRowClass import *

TargetList = [None] * 17

TargetList[0] = (TableRow('Число', method=get_numbers))

TargetList[1] = (TableRow('Число ступеней', value='1', method=fill_zeros))
TargetList[2] = (TableRow('Подача', method=get_numbers))
TargetList[3] = (TableRow('Давление на входе макс', method=get_numbers))
TargetList[4] = (TableRow('Давление на выходе', method=get_numbers))

TargetList[5] = (TableRow('NPSH насоса', method=get_numbers))
TargetList[6] = (TableRow('Потребляемая мощность', method=get_numbers))
TargetList[7] = (TableRow('Частота вращения насоса', method=get_numbers))
TargetList[8] = (TableRow('Вид уплотнения вала', method=None))
TargetList[9] = (TableRow('Изготовитель двигателя', value='Без двигателя', method=None))
TargetList[10] = (TableRow('Расчетная мощность Р2', method=get_numbers))
TargetList[11] = (TableRow('Частота вращения двигателя', method=get_numbers))

TargetList[12] = (TableRow('Тип муфты', method=None))
TargetList[13] = (TableRow('Номинальный размер', method=get_numbers))
TargetList[14] = (TableRow('Проставок', method=PROSTAVOK))
TargetList[15] = (TableRow('Перекачиваемая среда', method=None))
TargetList[16] = (TableRow('Изготовитель муфт', method=get_text))
# TargetList[16] = (TableRow('', method=get_numbers))
# TargetList[17] = (TableRow('', method=get_numbers))
# TargetList[18] = (TableRow('', method=get_numbers))
# TargetList[19] = (TableRow('', method=get_numbers))


for i in TargetList:
	if i:
		i.process()
		TableRow.printObj(i)
	else:
		print(None)

# print(sample.tag)
# print(sample.varname)
# sample = sample.process()
# print(sample.tag)