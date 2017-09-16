from docxtpl import DocxTemplate
import re


def generate_Word(TargetList=None, templateName=None):
	
	doc = DocxTemplate(templateName)

	varnames = [item.varname for item in TargetList]
	values = [item.value for item in TargetList]
	context = dict(zip(varnames, values))
	doc.render(context)

	doc.save("generated.docx")