

from typing import Any

def render_tag(tag:str,text:Any)->str:
    return f'<{tag}>{text}<{tag}/>' 


def render_tags(tag:str,*text)->str:
    all_tags = list(map(lambda text:render_tag(tag,text),text))
    return ''.join(all_tags)

def br():
    return '<br>'
    
def b(*text:Any)->str:
    return render_tags('b',text)

def p(*text:Any)->str:
    return render_tags('p',text)

