import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.use_pytest }}' == 'y':
        remove_file('tests/__init__.py')
    else:
        remove_file('setup.cfg')
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, 'tests'))
