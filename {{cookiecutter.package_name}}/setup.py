from pathlib import Path

from setuptools import setup
from setuptools import find_packages


NAME = '{{ cookiecutter.package_name }}'

REQUIRES = [
    {%- if cookiecutter.use_click == 'y' %}'Click>=6'{% endif -%}
]

about = {}
here = Path(__file__).absolute().parent
version_file = here / NAME / '__version__.py'

with open(str(version_file), encoding='utf-8') as f:
    exec(f.read(), about)


setup(
    name=NAME,
    version=about['__version__'],
    python_requires='>={{ cookiecutter.minimum_python_version }}',
    packages=find_packages(exclude=('tests',)),
    zip_safe=False,
    install_requires=REQUIRES,
    include_package_data=True,
    entry_points={
        'console_scripts': ['{{ cookiecutter.entry_point }} = {{ cookiecutter.package_name }}.__main__:main']
    },
    setup_requires=[{%- if cookiecutter.use_pytest == 'y' -%}'pytest-runner',{% endif %}],
    tests_require=[{%- if cookiecutter.use_pytest == 'y' -%}'pytest',{% endif %}],
    {%- if cookiecutter.use_pytest != 'y' %}
    test_suite='tests',
    {%- endif %}
)
