# Chatgpt-cli

It's a very minimal cli prompt, where you can chat and keeping the conversation session momoriable by chatgpt.

## Install

#### One command install

```bash
$ ./install.sh
```

#### Manual install
Assuming you have `python3` & `pip3` installed.

```bash
$ git clone https://github.com/slithery0/chatgpt-cli
$ cd chatgpt-cli
$ pip3 install -r requirements.py
$ cp chatgpt-cli.py /bin/chatgpt-cli
$ chmod +x /bin/chatgpt-cli
```

## Usage

Assuming you created a `.env` file with correct `OPENAI_API_KEY` value.
If you don't have a api key [visit here](https://beta.openai.com/account/api-keys) and generate one.

```bash
$ chatgpt-cli
```
