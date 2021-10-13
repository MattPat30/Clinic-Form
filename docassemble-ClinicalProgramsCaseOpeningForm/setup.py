import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path
standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out
setup(name='docassemble.ClinicalProgramsCaseOpeningForm',
      version='1.0',
      description=('Clinical Programs Case Opening Form'),
      long_description='# docassemble.ClinicalProgramsCaseOpeningForm\n\nClinical Programs Case Opening Form\n\n## Author\n\nLIT Lab\n\n',
      long_description_content_type='text/markdown',
      author='LIT Lab',
      author_email='',
      license='The MIT License',
      url='https://courtformsonline.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['docassemble.ALMassachusetts>=0.0.7','docassemble.MassAccess','docassemble.AssemblyLine'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/ClinicalProgramsCaseOpeningForm/', package='docassemble.ClinicalProgramsCaseOpeningForm'),
     )
