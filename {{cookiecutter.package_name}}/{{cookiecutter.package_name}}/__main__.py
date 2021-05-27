import logging
{% if cookiecutter.use_click == 'y' -%}
import click
{% endif -%}


logger = logging.getLogger(__name__)

{% raw -%}
LOG_FORMAT = '[%(asctime)s] %(levelname).4s {%(name)s:%(lineno)s} %(message)s'
{%- endraw %}


{% if cookiecutter.use_click == 'y' -%}
@click.command()
{% endif -%}
def main():
    logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
    logger.info('{{ cookiecutter.package_name }} application stub')


if __name__ == '__main__':
    main()
