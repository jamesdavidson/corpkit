from setuptools import setup, find_packages

setup(name='corpkit',
      version='1.21',
      description='A toolkit for working with linguistic corpora',
      url='http://github.com/interrogator/corpkit',
      author='Daniel McDonald',
      package_data={'corpkit': ['*.jar', 'corpkit/*.jar', '*.sh', 'corpkit/*.sh', 
                                '*.ipynb', 'corpkit/*.ipynb'],
                    'dictionaries': ['*.p', 'dictionaries/*.p']},
      author_email='mcdonaldd@unimelb.edu.au',
      license='MIT',
      packages=['corpkit', 'dictionaries'],
      install_requires=["matplotlib >= 1.4.3",
                        "nltk >= 3.0.0",
                        "pandas >= 0.16.1",
                        "mpld3 >= 0.2", 
                        "beautifulsoup4>=4.3.2",
                        "pattern>=2.6",
                        "tkintertable>=1.2"],
      zip_safe = False)
