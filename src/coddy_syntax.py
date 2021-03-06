### coddy by loadycode
### graphite00070
### gnu general public license v3.0

pygmentImportError = False

import tkinter as tk
try:
	from pygments.lexers import JsonLexer
	from pygments.lexers import CLexer
	from pygments.lexers import HtmlLexer
	from pygments.lexers import CssLexer
	from pygments.lexers import CppLexer
	from pygments.lexers import PythonLexer
	from pygments.lexers import JavascriptLexer
	from pygments.token import Token
except ImportError:
	pygmentImportError = True
	print ('coddy!error: cant import pygment lib')

print ('coddy!alert: syntax highlighting lib import successful')

color_keyword = '#ff00cc'
color_string_literal = '#00cc66'
color_comment = '#999999'
color_name_builtin = '#3399cc'
color_keyword_ext = '#ff0000'

token_type_to_tag = {
		Token.Keyword: 'keyword',
		Token.Keyword.Type: 'keyword_ext',
		Token.Keyword.Reserved: 'keyword_ext',
		Token.Keyword.Constant: 'keyword_ext',
		Token.Operator.Word: 'keyword',
		Token.Name.Builtin: 'name_builtin',
		Token.Literal.String.Single: 'string_literal',
		Token.Literal.String.Double: 'string_literal',
		Token.Comment.Single: 'comment',
		Token.Comment.Hashbang: 'comment',
		Token.Comment.Multiline: 'comment',
}

def tokens_init (textbox):
	textbox.tag_config ('keyword', foreground = color_keyword)
	textbox.tag_config ('keyword_ext', foreground = color_keyword_ext)
	textbox.tag_config ('name_builtin', foreground = color_name_builtin)
	textbox.tag_config ('string_literal', foreground = color_string_literal)
	textbox.tag_config ('comment', foreground = color_comment)
def tokens_get (textbox, lexer):
	def get_text_coord (s: str, i: int):
		for row_number, line in enumerate (s.splitlines(keepends = True), 1):
			if i < len(line): return f'{row_number}.{i}'
			i -= len(line)
	for tag in textbox.tag_names (): textbox.tag_remove (tag, 1.0, 'end')
	s = textbox.get (1.0, 'end')
	tokens = lexer.get_tokens_unprocessed(s)
	for i , token_type, token in tokens:
		j = i + len (token)
		if token_type in token_type_to_tag: textbox.tag_add (token_type_to_tag [token_type], get_text_coord (s, i), get_text_coord (s, j))
	textbox.edit_modified (0)

def python_check (textbox):
	lexer = PythonLexer ()
	tokens_get (textbox, lexer)

def c_check (textbox):
	lexer = CLexer ()
	tokens_get (textbox, lexer)

def cpp_check (textbox):
	lexer = CppLexer ()
	tokens_get (textbox, lexer)

def js_check (textbox):
	lexer = JavascriptLexer ()
	tokens_get (textbox, lexer)

def html_check (textbox):
	lexer = HtmlLexer ()
	tokens_get (textbox, lexer)

def css_check (textbox):
	lexer = CssLexer ()
	tokens_get (textbox,lexer)

def json_check (textbox):
	lexer = JsonLexer ()
	tokens_get (textbox,lexer)

def delete_tokens (textbox):
	for tag in textbox.tag_names ():
		textbox.tag_remove (tag, 1.0, 'end')

def switch (file_syntax, syntaxbtn, file_extension, textbox):
	switched = False
	if file_syntax == 'python':
		file_syntax = 'text'
		syntaxbtn ['text'] = 'plain text'
		delete_tokens (textbox)
		switched = True
	elif file_syntax == 'json':
		file_syntax = 'text'
		syntaxbtn ['text'] = 'plain text'
		delete_tokens (textbox)
		switched = True
	elif file_syntax == 'c':
		file_syntax = 'text'
		syntaxbtn ['text'] = 'plain text'
		delete_tokens (textbox)
		switched = True
	elif file_syntax == 'cpp':
		file_syntax = 'text'
		syntaxbtn ['text'] = 'plain text'
		delete_tokens (textbox)
		switched = True
	elif file_syntax == 'html':
		file_syntax = 'text'
		syntaxbtn ['text'] = 'plain text'
		delete_tokens (textbox)
		switched = True
	elif file_syntax == 'css':
		file_syntax = 'text'
		syntaxbtn ['text'] = 'plain text'
		delete_tokens (textbox)
		switched = True
	elif file_syntax == 'javascript':
		file_syntax = 'text'
		syntaxbtn ['text'] = 'plain text'
		delete_tokens (textbox)
		switched = True
	elif switched == True:
		if file_extension == '.py':
			file_syntax = 'python'
			syntaxbtn ['text'] = 'python'
			python_check (textbox)
			switched = False
		elif file_extension == '.c':
			file_syntax = 'c'
			syntaxbtn ['text'] = 'c lang'
			c_check (textbox)
			switched = False
		elif file_extension == '.cpp':
			file_syntax = 'cpp'
			syntaxbtn ['text'] = 'cpp lang'
			cpp_check (textbox)
			switched = False
		elif file_extension == '.json':
			file_syntax = 'json'
			syntaxbtn ['text'] = 'json'
			json_check (textbox)
			switched = False
		elif file_extension == '.html':
			file_syntax = 'html'
			syntaxbtn ['text'] = 'html'
			html_check (textbox)
			switched = False
		elif file_extension == '.css':
			file_syntax = 'css'
			syntaxbtn ['text'] = 'css'
			css_check (textbox)
			switched = False
		elif file_extension == '.js':
			file_syntax = 'javascript'
			syntaxbtn ['text'] = 'javascript'
			js_check (textbox)
			switched = False