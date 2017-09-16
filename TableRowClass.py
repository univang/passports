import re


class TableRow():
    def __init__(self, tag=None, method=None, value=None, varname=None, entry=0):
        self.tag = tag
        self.value = value
        self.method = method
        self.varname = tag.replace(" ", "_")
        self.entry = entry

    @classmethod
    def printObj(cls, obj):
        # print('tag=', obj.tag, '; value=', obj.value, ';varname=', obj.varname)
        print("tag='{:28}'; value='{}'; varname='{}'".format(
            obj.tag, obj.value, obj.varname))

    def process(self):
        if self.method:
            if self.value:
                self.method(self)


def fill_zeros(obj=None):
    obj.value = obj.value.zfill(2)


def get_numbers(obj=None):
    # extracts all nubmers from string
    valueList = re.findall(r'\d+[.,]?\d*', obj.value)
    # from '['110,1']' to '110,1'
    obj.value = valueList[0]


def get_text(obj=None):
    obj.value = re.sub('[^a-z\sA-Z]+', '', obj.value)


# вытаскивает количество Проставков из "Тип муфты"
def PROSTAVOK(obj=None):
    found = re.findall(r'\s+[N]{1}\s{1}|\s+[N]{1}$', obj.value)
    if found:
        obj.value = '-'
    else:
        obj.value = '1'


# вытаскивает имя до пробела из "Название"
def NAME(obj=None):
    obj.value = re.findall('^([^\s]+)', obj.value)[0]
