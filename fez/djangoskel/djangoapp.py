from paste.script.templates import Template, var

class DjangoAppTemplate(Template):
    
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
        var('settings', 'Generate a settings file?', default=False)
    ]
    
    _template_dir = 'templates/django_app'
    summary = 'Template for a basic Django reusable application'
    use_cheetah = True
    required_templates = []
    
    def check_vars(self, vars, command):
        if not command.options.no_interactive and \
           not hasattr(command, '_deleted_once'):
            del vars['package']
            command._deleted_once = True
        return super(DjangoAppTemplate, self).check_vars(vars, command)
