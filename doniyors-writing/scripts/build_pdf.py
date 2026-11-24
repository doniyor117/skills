"""Build the complete public guide from its Markdown sources, entirely locally."""
from pathlib import Path
from html import escape
import os
import re
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

ROOT = Path(__file__).resolve().parents[1]
VERSION = re.search(r'^Version ([^ ·]+)', (ROOT / 'SKILL.md').read_text(), re.M).group(1)
FONT_DIR = Path(os.environ.get('WRITING_FONT_DIR', '/usr/share/fonts/truetype/dejavu'))
for name, filename in [('Guide', 'DejaVuSans.ttf'), ('GuideBold', 'DejaVuSans-Bold.ttf')]:
    font = FONT_DIR / filename
    if not font.exists():
        raise SystemExit(f'Missing font: {font}. See README.md for font installation.')
    pdfmetrics.registerFont(TTFont(name, str(font)))
pdfmetrics.registerFontFamily('Guide', normal='Guide', bold='GuideBold', italic='Guide', boldItalic='GuideBold')

styles = {
    'title': ParagraphStyle('title', fontName='GuideBold', fontSize=25, leading=31, textColor=colors.HexColor('#18324b'), spaceAfter=16, keepWithNext=True),
    'h2': ParagraphStyle('h2', fontName='GuideBold', fontSize=13, leading=18, spaceBefore=12, spaceAfter=6, keepWithNext=True, textColor=colors.HexColor('#18324b')),
    'body': ParagraphStyle('body', fontName='Guide', fontSize=10, leading=13.5, spaceAfter=6, allowWidows=0, allowOrphans=0),
    'source': ParagraphStyle('source', fontName='Guide', fontSize=10, leading=13.5, spaceAfter=6, keepWithNext=True),
    'quote': ParagraphStyle('quote', fontName='Guide', fontSize=10, leading=13.5, leftIndent=14, rightIndent=9, borderColor=colors.HexColor('#dbe4ee'), borderWidth=.5, borderPadding=7, backColor=colors.HexColor('#f4f7fb'), spaceBefore=3, spaceAfter=7),
    'bullet': ParagraphStyle('bullet', fontName='Guide', fontSize=10, leading=13.5, leftIndent=12, firstLineIndent=-10, spaceAfter=6),
}

def inline(text):
    text = escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'`([^`]+)`', r'<b>\1</b>', text)
    text = re.sub(r'https://[^\s<]+', lambda m: f'<link href="{m[0]}" color="#315e8c">{m[0]}</link>', text)
    return text

def render_file(path):
    text = path.read_text(encoding='utf-8')
    if text.startswith('---\n'):
        text = text.split('---\n', 2)[2]
    items=[]
    for block in re.split(r'\n\s*\n', text.strip()):
        lines=block.splitlines()
        if block.startswith('# '):
            items.append(Paragraph(inline(block[2:]), styles['title']))
        elif block.startswith('## '):
            items.append(Paragraph(inline(block[3:]), styles['h2']))
        elif block.startswith('>'):
            # Preserve separate numbered answers and paragraph breaks in the reference.
            parts=[]
            for line in lines:
                value=line.removeprefix('>').strip()
                if value:
                    parts.append(inline(value))
                else:
                    parts.append('')
            items.append(Paragraph('<br/>'.join(parts), styles['quote']))
        elif block.startswith('- '):
            for line in lines:
                items.append(Paragraph('• '+inline(line.removeprefix('- ')), styles['bullet']))
        else:
            items.append(Paragraph(inline(' '.join(lines)), styles['source'] if block.startswith('Source:') else styles['body']))
    return items

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#dbe4ee'))
    canvas.line(46, 37, A4[0]-46, 37)
    canvas.setFont('Guide', 8)
    canvas.setFillColor(colors.HexColor('#5f7082'))
    canvas.drawString(46, 24, f'Doniyor’s writing · Public edition · v{VERSION}')
    canvas.drawRightString(A4[0]-46, 24, str(doc.page))
    canvas.restoreState()

def build():
    story=[]
    for i, filename in enumerate(['SKILL.md', 'references/examples.md', 'references/public-context.md']):
        if i:
            story.append(Spacer(1, 20))
        story.extend(render_file(ROOT / filename))
    doc=SimpleDocTemplate(str(ROOT/'doniyors-writing-skill.pdf'), pagesize=A4, leftMargin=46, rightMargin=46, topMargin=43, bottomMargin=52, title='Doniyor’s writing: a flexible voice reference', author='Doniyor Khudoykulov', subject='Public writing guide with examples in English, Uzbek, and Russian')
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print('Built', ROOT/'doniyors-writing-skill.pdf')

if __name__ == '__main__':
    build()
