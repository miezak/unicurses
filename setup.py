#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='UniCurses',
      version='1.2',
      description='Unified Curses Wrapper for Python',
      long_description='A universal Curses wrapper for Python on Windows, Linux, and\nMac OS X, with syntax close to the original NCurses. In order\nto provide Curses functionality on Windows it utilizes the ctype\nforeign function interface to wrap PDCurses, a free and open-source\nCurses implementation for Windows.',
      author='Michael Kamensky',
      author_email='stavdev@mail.ru',
      url='http://pyunicurses.sourceforge.net',
      packages=find_packages(),
      package_data = {
          'unicurses' : ['pdc34dll/*']
      },
      license='General Public License v3',
      platforms=['Windows', 'Linux', 'Mac OS X'],
)
