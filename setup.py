from setuptools import setup

import spekki

def readme():
    with open('README.md') as f:
        return f.read()


setup(name='spekki',
      version=spekki.__version__,
      description=spekki.__description__,
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GPLv3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Intended Audience :: Science/Research',
      ],
      keywords='microbial genomics kraken',
      url=spekki.__url__,
      author=spekki.__author__,
      author_email=spekki.__email__,
      license=spekki.__license__,
      packages=['spekki'],
      install_requires=[
          'argparse',
      ],
      test_suite='nose.collector',
      tests_require=[],
      entry_points={
          'console_scripts': ['spekki=spekki.spekki:main'],
      },
      include_package_data=True,
      zip_safe=False)
