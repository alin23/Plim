from typing import Mapping

from docutils.core import publish_parts
import coffeescript
import markdown2
from docutils.core import publish_parts
from scss import Scss
from stylus import Stylus

from .util import u


def rst_to_html(source: str) -> str:
    # This code was taken from http://wiki.python.org/moin/ReStructuredText
    # You may also be interested in http://www.tele3.cz/jbar/rest/about.html
    html: Mapping[str, str] = publish_parts(source=source, writer_name='html')
    return html['html_body']


def coffee_to_js(source: str) -> str:
    return '<script>{js}</script>'.format(js=coffeescript.compile(source))


def scss_to_css(source: str) -> str:
    css = Scss().compile(source).strip()
    return '<style>{css}</style>'.format(css=css)


def stylus_to_css(source: str) -> str:
    compiler = Stylus(compress=True, plugins={"rupture": {}})
    return '<style>{css}</style>'.format(css=compiler.compile(source).strip())


def md_to_html(source):
    return markdown2.markdown(
        source,
        use_file_vars=True,
        extras=[
            "header-ids",
            "fenced-code-blocks",
            "tables",
            "strike",
            "spoiler",
            "footnotes",
        ],
    )
