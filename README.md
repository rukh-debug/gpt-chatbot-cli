# gpt-chatbot-cli

It's a very minimal cli prompt, where you can chat and keeping the conversation session memorable by chatgpt and keep chat history for future use.

## Installation

Assuming you created a env variable with key named `OPENAI_API_KEY`.
If you don't have a api key [visit here](https://platform.openai.com/account/api-keys) and generate one.

To install ChatGPT-CLI, you'll first need to set up an OpenAI API key. If you don't have one yet, visit the [OpenAI Website](https://platform.openai.com/account/api-keys) to sign up and generate an API key.


Next, add the following line to your `~/.bashrc` or `~/.zshrc` file:

```bash
export OPENAI_API_KEY=<YOUR OPENAI API KEY>

```
Be sure to replace <YOUR OPENAI API KEY> with your actual API key. Then, source the file using:

Finally source the file using `source ~/.bashrc` or `source ~/.zshrc`


-

Finally, install the package using pip:

```bash
$ pip3 install gpt-chatbot-cli
```

## Usage

Once you have installed ChatGPT-CLI, you can run it by typing:
```bash
$ gpt-chatbot-cli
```

This will start the CLI prompt, and you can begin chatting with the AI bot.

You can also pass various options to the gpt-chatbot-cli command to customize its behavior. Here are the available options:

```bash
  -k, --api_key TEXT       Openai API key. If not provided, will prompt for it
                           or use the environment variable OPENAI_API_KEY.
  -m, --model TEXT         Model to use for text generation | (default:
                           gpt-3.5-turbo)
  -t, --temperature FLOAT  Temperature for text generation | (default: 0.9)
  -p, --preset TEXT        Preset mode to use for text generation | (default:
                           Chat)  Available presets: Chat, Q&A, Grammar
                           Correction, Eli5, Custom
  -hs, --history           Show chat history picker | (default: False)
  -h, --help               Show this message and exit.
```

## Demo

[![asciicast](https://asciinema.org/a/9L0MjDExrMFb0XhBbqYaXBBWL.svg)](https://asciinema.org/a/9L0MjDExrMFb0XhBbqYaXBBWL)



## Dependencies

ChatGPT-CLI depends on the following Python packages:

- Openai
- prompt-toolkit
- termcolor
- tinyDB
- click

## License

MIT

## Author

[![Twitter Follow](https://img.shields.io/twitter/follow/getrubenk?style=social)](https://twitter.com/getrubenk)

[![GitHub followers](https://img.shields.io/github/followers/slithery0?style=social)](https://github.com/slithery0)

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.
