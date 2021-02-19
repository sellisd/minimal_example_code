from setuptools import setup

setup(
    name="me",
    version='0.0.1',
    py_modules=['me'],
    python_requires='>=3.9',  # use importlib.resources
    install_requires=[
      'click',
    ],
    package_data={'me': ['sql_scripts/*.sql']},
    packages=['me'],
    entry_points={
        'console_scripts':
        [
          'me=me.me:me'
        ]
    },
)
