
import cherrypy
from jinja2 import Environment, FileSystemLoader

from .tools import Tool
from .plugins import TemplatePlugin


class CherrypyJinja(object):
    def __init__(self, template_dirs, loader_class=FileSystemLoader):
        self.template_dirs = template_dirs
        self.env = Environment(loader=loader_class(self.template_dirs))

    def setup(self):
        plugins = TemplatePlugin(cherrypy.engine, env=self.env).subscribe()
        tools = cherrypy.tools.template = Tool()

        return plugins, tools
