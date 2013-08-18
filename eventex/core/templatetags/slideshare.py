from django import template
from django.template import Context, Template, Node
 
 
TEMPLATE = TEMPLATE = u'<iframe src="http://www.slideshare.net/slideshow/embed_code/{{id}}" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="max-width:427px;border:1px solid #CCC;border-width:1px 1px 0;margin-bottom:5px" allowfullscreen webkitallowfullscreen mozallowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="https://www.slideshare.net/raphaelfranca/flisol-bootstrap" title="Twitter Bootstrap " target="_blank">Twitter Bootstrap </a> </strong> from <strong><a href="http://www.slideshare.net/raphaelfranca" target="_blank">Raphael França</a></strong> </div>'
 
 
def do_slideshare(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, id_, doc = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires 2 arguments" % token.contents.split()[0]
    return SlideShareNode(id_, doc)
 
 
class SlideShareNode(Node):
    def __init__(self, id_, doc):
        self.id = template.Variable(id_)
        self.doc = template.Variable(doc)
 
    def render(self, context):
        try:
            actual_id = self.id.resolve(context)
        except template.VariableDoesNotExist:
            actual_id = self.id
 
        try:
            actual_doc = self.doc.resolve(context)
        except template.VariableDoesNotExist:
            actual_doc = self.doc
 
        t = Template(TEMPLATE)
        c = Context({'id': actual_id, 'doc': actual_doc}, autoescape=context.autoescape)
        return t.render(c)
 
 
register = template.Library()
register.tag('slideshare', do_slideshare)
