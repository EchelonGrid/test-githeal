from jinja2 import Template

def render_custom_template(user_template: str):
    # VULNERABLE: Direct string templating allows SSTI
    return Template(user_template).render()
