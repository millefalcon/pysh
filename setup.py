from setuptools import setup

setup(name='pysh',
      version='0.1.0',
      packages=['pysh', 'pysh.bin'],
      entry_points={
          'console_scripts': [
              'pysh = pysh.__main__:main'
          ]
      },
)

