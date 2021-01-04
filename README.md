<div align="center" id="top"> 
  <img src="https://github.com/haziq9978/PythonChatbot/blob/main/images/logo.jfif" alt="Prof PC" />

&#xa0;

  <!-- <a href="https://profpc.netlify.app">Demo</a> -->
</div>

<h1 align="center">Prof PC</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/ariffrahimin/prof-pc?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/ariffrahimin/prof-pc?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/ariffrahimin/prof-pc?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/ariffrahimin/prof-pc?color=56BEB8">


</p>

<!-- Status -->

 <h4 align="center">
	🚧  Prof PC 🚀 Under construction...  🚧
</h4>

<hr>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/ariffrahimin" target="_blank">Author</a>
</p>

<br>

## :dart: About
Simple chatbot implementation with PyTorch. 

- The implementation should be easy to follow for beginners and provide a basic understanding of chatbots.
- The implementation is straightforward with a Feed Forward Neural net with 2 hidden layers.
- Customization for your own use case is super easy. Just modify `intents.json` with possible patterns and responses and re-run the training (see below for more info).
Our project is to create a chatbot that responds
The approach is inspired by this article and ported to PyTorch: [https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077](https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077).

## :sparkles: Features

:heavy_check_mark: Feature 1;\
:heavy_check_mark: Feature 2;\
:heavy_check_mark: Feature 3;

## :rocket: Technologies

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Pytorch](https://pytorch.org/)

## :white_check_mark: Requirements
## Watch the Tutorial
[![Alt text](https://img.youtube.com/vi/RpWeNzfSUHw/hqdefault.jpg)](https://www.youtube.com/watch?v=RpWeNzfSUHw&list=PLqnslRFeH2UrFW4AUgn-eY37qOAWQpJyg)


Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.

## Installation

### Create an environment
Whatever you prefer (e.g. `conda` or `venv`)
```console
mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

### Activate it
Mac / Linux:
```console
. venv/bin/activate
```
Windows:
```console
venv\Scripts\activate
```
### Install PyTorch and dependencies

For Installation of PyTorch see [official website](https://pytorch.org/).

You also need `nltk`:
 ```console
pip install nltk
 ```

If you get an error during the first run, you also need to install `nltk.tokenize.punkt`:
Run this once in your terminal:
 ```console
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## Usage
Run
```console
python train.py
```
This will dump `data.pth` file. And then run
```console
python chat.py
```
## Customize
Have a look at [intents.json](intents.json). You can customize it according to your own use case. Just define a new `tag`, possible `patterns`, and possible `responses` for the chat bot. You have to re-run the training whenever this file is modified.
```console
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": [
        "Hi",
        "Hey",
        "How are you",
        "Is anyone there?",
        "Hello",
        "Good day"
      ],
      "responses": [
        "Hey :-)",
        "Hello, thanks for visiting",
        "Hi there, what can I do for you?",
        "Hi there, how can I help?"
      ]
    },
    ...
  ]
}
```
## :memo: License

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.

Made with :heart: by <a href="https://github.com/ariffrahimin" target="_blank">Ariff Rahimin</a>

&#xa0;

<a href="#top">Back to top</a>
