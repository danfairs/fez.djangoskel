from paste.script.templates import Template
from paste.script.templates import var
from random import choice

class DjangoTemplate(Template):

    vars = [
        var('version', 'Version (like 0.1)', default='0.1'),
        var('description', 'One-line description of the package'),
        var('long_description', 'Multi-line description (in reST)'),
        var('keywords', 'Space-separated keywords/tags'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
        var('url', 'URL of homepage'),
        var('license_name', 'License name'),
        var('zip_safe', 'True/False: if the package can be distributed as a .zip file',
            default=False),
    ]

    use_cheetah = True
    required_templates = []

    def check_vars(self, vars, command):
        if not command.options.no_interactive and \
           not hasattr(command, '_deleted_once'):
            del vars['package']
            command._deleted_once = True
        return super(DjangoTemplate, self).check_vars(vars, command)


class DjangoAppTemplate(DjangoTemplate):    
    _template_dir = 'templates/django_app'
    summary = 'Template for a basic Django reusable application'
    vars = [
        var('django_version',
            'Django version to fetch, the default is 1.0.2',
            default='1.0.2'),
    ] + DjangoTemplate.vars

def append_secret_key(vars):
    default_key = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    vars.append(
        var('secret_key', 'Secret key', default=default_key)
    )


class DjangoProjectTemplate(DjangoTemplate):
    _template_dir = 'templates/django_project'
    summary = 'Template for a Django project'
    
    def __init__(self, name):
        append_secret_key(self.vars)
        super(DjangoProjectTemplate, self).__init__(name)

class DjangoNamespaceTemplate(DjangoTemplate):

    vars = [
        var('namespace_package', 'Top-level namespace package'),
        var('package', 'The name of the package contained within the namespace')
    ] + DjangoTemplate.vars
    
    
class DjangoNamespaceAppTemplate(DjangoNamespaceTemplate):
    _template_dir = 'templates/django_namespace_app'
    summary = 'Template for a namespaced Django reusable application'
    
    
class DjangoNamespaceProjectTemplate(DjangoNamespaceTemplate):
    _template_dir = 'templates/django_namespace_project'
    summary = 'Template for a namespaced Django project'

    def __init__(self, name):
        append_secret_key(self.vars)
        super(DjangoNamespaceProjectTemplate, self).__init__(name)

class DjangoBuildoutTemplate(Template):
    _template_dir = 'templates/django_buildout'
    summary = 'A plain Django buildout'
    required_templates = []
    use_cheetah = True
    
    vars = [
        var('django_version',
            'Django version to fetch, the default is 1.0.2',
            default='1.0.2'),
        var('django_project_name',
            'Name of the main Django project folder',
            default='project')
    ]
    
    def post(self, command, output_dir, vars):
        print "-----------------------------------------------------------"
        print "Generation finished"
        print "You probably want to run python bootstrap.py and then edit"
        print "buildout.cfg before running bin/buildout -v"
        print
        print "See README.txt for details"
        print "-----------------------------------------------------------"
