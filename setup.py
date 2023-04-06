import setuptools

setuptools.setup(
    name='gpt-chatbot-cli',
    version="0.3.0",
    description="chatgpt cli without any bloats.",
    author="Ruben Kharel",
    author_email="kharelruben@gmail.com",
    license="MIT",
    url="https://github.com/slithery0/gpt-chatbot-cli",
    scripts=['gpt-chatbot-cli'],
    packages=setuptools.find_packages(),
    install_requires=[
        'openai==0.27.4',
        'prompt-toolkit==3.0.38',
        'termcolor==2.2.0',
        'tinydb==4.7.1',
        'click==8.1.3'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
    ]
)
