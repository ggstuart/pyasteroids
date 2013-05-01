from distutils.core import setup

try:
    import pygtk
except ImportError:
    print 'You need to install pyGTK to use this'
    exit()

setup(name='pyasteroids',
    version='0.5',
    description='Python asteroids game demonstrating pyagents library',
    author='Graeme Stuart',
    author_email='ggstuart@gmail.com',
    url='https://github.com/ggstuart/pyasteroids.git',
    license='GPL',
    packages=[
      'pyasteroids'
    ],
    install_requires=[
        'pyagents'
    ],
)
