from setuptools import setup, find_packages

setup(
    name='Bertalign',
    version='0.1.0',
    url='https://github.com/bfsujason/bertalign',
    description='An automatic mulitlingual sentence aligner.',
    packages=find_packages(),    
    install_requires=[
        'numba==0.56.4',
        'faiss-gpu==1.7.2',
        'googletrans==4.0.0rc1',
        'sentence-splitter==1.4',
        'sentence-transformers==2.2.2',
    ],
)
