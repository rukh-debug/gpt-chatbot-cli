import setuptools

setuptools.setup(
    name='gpt-chatbot-cli',
    version="0.1.3",
    description="chatgpt cli without any bloats.",
    author="Ruben Kharel",
    author_email="kharelruben@gmail.com",
    license="MIT",
    url="https://github.com/slithery0/gpt-chatbot-cli",
    scripts=['gpt-chatbot-cli'],
    packages=setuptools.find_packages(),
    install_requires=[
        'openai==0.26.1',
        'prompt_toolkit==3.0.36',
        'termcolor==2.2.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
    ]
)