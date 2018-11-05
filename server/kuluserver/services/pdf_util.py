import jinja2
import os
from subprocess import call
from sys import stderr

latex_jinja2_env = jinja2.Environment(
    block_start_string='\BLOCK{',
    block_end_string='}',
    variable_start_string='\VAR{',
    variable_end_string='}',
    comment_start_string='\#{',
    comment_end_string='}',
    line_statement_prefix='%%',
    trim_blocks=True,
    line_comment_prefix='%#',
    autoescape=False,
    loader=jinja2.FileSystemLoader('kuluserver/templates'),
)


def __esc(s):
    escaped_chars = {
        '$': "\\$",
        '%': "\\%",
        '&': "\\&",
        '#': "\\#",
        '_': "\\_",
        '{': "\\{",
        '}': "\\}",
        '[': "{[}",
        ']': "{]}",
        '"': "{''}",
        '\\': "\\textbackslash{}",
        '~': "\\textasciitilde{}",
        '<': "\\textless{}",
        '>': "\\textgreater{}",
        '^': "\\textasciicircum{}",
        '`': "{}`",
        '\n': "\\\\",  # xkcd.com/1638/
    }
    res = ""
    for c in s:
        res += escaped_chars.get(c, c)
    return res


def esc(obj, exclude=[], path=''):
    if path in exclude:
        return obj
    if isinstance(obj, list):
        return [ esc(v, exclude, '{}.[]'.format(path)) for v in obj ]
    elif isinstance(obj, dict):
        return {
            k: esc(v, exclude, '{}.{}'.format(path, k)) for k,v in obj.items()
        }
    elif isinstance(obj, str):
        return __esc(obj)
    return obj


def render_tex(template, destinantion, obj):
    template = latex_jinja2_env.get_template(template)
    formatted = template.render(**obj)

    texf = 'tex/' + destinantion + '.tex'
    with open(texf, 'w') as f:
        f.write(formatted)

    dev = open(os.devnull, 'w')
    ret = call(
        [
            'pdflatex',
            '-halt-on-error',
            '-output-directory',
            'rendered',
            texf,
        ],
        stdout=dev,
        stderr=stderr,
    )
    ret |= call(
        [
            'pdflatex',
            '-halt-on-error',
            '-output-directory',
            'rendered',
            texf,
        ],
        stdout=dev,
        stderr=stderr,
    )

    dev.close()
    os.unlink(texf)

    return '{}.pdf'.format(destinantion)
