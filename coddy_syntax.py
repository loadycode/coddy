### coddy by loadycode
### graphite00015
### gnu general public license v3.0

pygmentImportError=False

import tkinter as tk
try:
	from pygments.lexers import CLexer
	from pygments.lexers import CppLexer
	from pygments.lexers import PythonLexer
	from pygments.token import Token
except ImportError:
	pygmentImportError=True
	print('coddy!error: cant import pygment lib')

print('coddy!alert: syntax highlighting lib import successful')

color_keyword='cyan'
color_string_literal='red'
color_comment='gray'
color_name_builtin='blue'
color_keyword_ext='green'

def tokens_init(textbox):
	textbox.tag_config('keyword',foreground=color_keyword)
	textbox.tag_config('keyword_ext',foreground=color_keyword_ext)
	textbox.tag_config('name_builtin',foreground=color_name_builtin)
	textbox.tag_config('string_literal',foreground=color_string_literal)
	textbox.tag_config('comment',foreground=color_comment)

def python_check(textbox):
	lexer=PythonLexer()
	def get_text_coord(s:str,i:int):
		for row_number,line in enumerate(s.splitlines(keepends=True),1):
			if i<len(line):
				return f'{row_number}.{i}'
			i-=len(line)
	token_type_to_tag={
		Token.Keyword:'keyword',
		Token.Keyword.Type:'keyword_ext',
		Token.Keyword.Reserved:'keyword_ext',
		Token.Keyword.Constant:'keyword_ext',
		Token.Operator.Word:'keyword',
		Token.Name.Builtin:'name_builtin',
		Token.Literal.String.Single:'string_literal',
		Token.Literal.String.Double:'string_literal',
		Token.Comment.Single:'comment',
		Token.Comment.Hashbang:'comment',
		Token.Comment.Multiline:'comment',
	}
	for tag in textbox.tag_names():
		textbox.tag_remove(tag,1.0,'end')
	s=textbox.get(1.0,'end')
	tokens=lexer.get_tokens_unprocessed(s)
	for i,token_type,token in tokens:
		j=i+len(token)
		if token_type in token_type_to_tag:
			textbox.tag_add(token_type_to_tag[token_type],get_text_coord(s,i),get_text_coord(s,j))
	textbox.edit_modified(0)

def c_check(textbox):
	lexer=CLexer()
	def get_text_coord(s:str,i:int):
		for row_number,line in enumerate(s.splitlines(keepends=True),1):
			if i<len(line):
				return f'{row_number}.{i}'
			i-=len(line)
	token_type_to_tag={
		Token.Keyword:'keyword',
		Token.Operator.Word:'keyword',
		Token.Name.Builtin:'keyword',
		Token.Literal.String.Single:'string_literal',
		Token.Literal.String.Double:'string_literal',
	}
	for tag in textbox.tag_names():
		textbox.tag_remove(tag,1.0,'end')
	s=textbox.get(1.0,'end')
	tokens=lexer.get_tokens_unprocessed(s)
	for i,token_type,token in tokens:
		j=i+len(token)
		if token_type in token_type_to_tag:
			textbox.tag_add(token_type_to_tag[token_type],get_text_coord(s,i),get_text_coord(s,j))
	textbox.edit_modified(0)

def cpp_check(textbox):
	lexer=CppLexer()
	def get_text_coord(s:str,i:int):
		for row_number,line in enumerate(s.splitlines(keepends=True),1):
			if i<len(line):
				return f'{row_number}.{i}'
			i-=len(line)
	token_type_to_tag={
		Token.Keyword:'keyword',
		Token.Operator.Word:'keyword',
		Token.Name.Builtin:'keyword',
		Token.Literal.String.Single:'string_literal',
		Token.Literal.String.Double:'string_literal',
	}
	for tag in textbox.tag_names():
		textbox.tag_remove(tag,1.0,'end')
	s=textbox.get(1.0,'end')
	tokens=lexer.get_tokens_unprocessed(s)
	for i,token_type,token in tokens:
		j=i+len(token)
		if token_type in token_type_to_tag:
			textbox.tag_add(token_type_to_tag[token_type],get_text_coord(s,i),get_text_coord(s,j))
	textbox.edit_modified(0)

def delete_tokens(textbox):
	for tag in textbox.tag_names():
		textbox.tag_remove(tag,1.0,'end')