#Returns the customized template object
import os
import sys

from string import Template

def read_template(filename):
    with open(os.path.join(sys.path[0],filename), mode='r', encoding='utf-8') as template_file:

        template_file_content = template_file.read()

    return Template(template_file_content)