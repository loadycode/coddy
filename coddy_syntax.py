### coddy by loadycode
### graphite00010 v0.91
### gnu general public license v3.0

pygmentImportError=False

import tkinter as tk
try:
	from pygments.lexers import CLexer
	from pygments.lexers import CppLexer
	from pygments.lexers import ActionScriptLexer
	from pygments.lexers import PythonLexer
	from pygments.token import Token
except ImportError:
	pygmentImportError=True
	print('coddy!error: cant import pygment lib')

print('coddy!alert: syntax highlighting lib import successful')

def python_check(textbox):
	lexer=PythonLexer()
	textbox.tag_config('keyword',foreground='cyan')
	textbox.tag_config('string_literal',foreground='red')
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

def actionscript_check(textbox):
	lexer=ActionScriptLexer()
	textbox.tag_config('keyword',foreground='cyan')
	textbox.tag_config('string_literal',foreground='red')
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

def c_check(textbox):
	lexer=CLexer()
	textbox.tag_config('keyword',foreground='cyan')
	textbox.tag_config('string_literal',foreground='red')
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
	textbox.tag_config('keyword',foreground='cyan')
	textbox.tag_config('string_literal',foreground='red')
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