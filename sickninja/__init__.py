from jinja2 import Environment
from jinja2 import FileSystemLoader
import os
import argparse

parser = argparse.ArgumentParser(description='Generate css from ninja files.')
parser.add_argument('dir', help='Directory in which file exists.')
parser.add_argument('file', help='File to parse.')
args = parser.parse_args()

sickninja = Environment(
	loader=FileSystemLoader(args.dir),
	**{
		'block_start_string': '<%',
		'block_end_string': '%>',
		'variable_start_string': '<%=',
		'variable_end_string': '%>',
		'comment_start_string': '<#',
		'comment_end_string': '#>',
		'line_statement_prefix': '#',
		'line_comment_prefix': '##',
		'trim_blocks': True,
		'lstrip_blocks': True,
		'newline_sequence': '\n',
		'keep_trailing_newline': False
	}
)

template = sickninja.get_template(f'{args.file}.ninja')
print(template.render())
