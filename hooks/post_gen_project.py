#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.packaging }}' != 'pip':
        remove_file('requirements.txt')
    if '{{ cookiecutter.packaging }}' != 'conda':
        remove_file('environment.yml')
    if '{{ cookiecutter.image_recognition }}' != 'y':
        remove_file('resources/train')
        remove_file('resources/test')
    if '{{ cookiecutter.manual_Docker_containers }}' != 'y':
        remove_file('Dockerfile')
        remove_file('entrypoint.sh')
