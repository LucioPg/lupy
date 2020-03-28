from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='lupy',
      version='0.1',
      description="Lucio's cookbook",
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
          'Operating System :: Os Independent'
      ],
      url='http://github.com/LucioPg/lupy.git',
      author='Lucio Di Capua',
      author_email='lucio.di.capua@gmail.com',
      keywords='utily tools',
      license='MIT',
      packages=['lupy'],
      include_package_data=True,
      zip_safe=False)