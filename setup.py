from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy==1.20.3',
        'pandas==1.3.3',
        'matplotlib==3.4.3',
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:main',
        ],
    },
)