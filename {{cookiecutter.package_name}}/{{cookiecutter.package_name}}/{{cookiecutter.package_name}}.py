import logging
{% if cookiecutter.use_click == 'y' -%}
import click
{% endif -%}


logger = logging.getLogger(__name__)

{% raw -%}
LOG_FORMAT = '[%(asctime)s] %(levelname).4s {%(name)s:%(lineno)s} %(message)s'
{%- endraw %}

logging.basicConfig(format=LOG_FORMAT)


{% if cookiecutter.use_click == 'y' -%}
@click.command()
{% endif -%}
def main():
    print('{{ cookiecutter.package_name }} application. File: {{ cookiecutter.package_name }}.py')
