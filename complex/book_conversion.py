# This is a script that will enable conversion of the book from html to markdown

import pypandoc
s_file="header.html"
pypandoc.convert_file(s_file,to="rst",outputfile="header.rst")