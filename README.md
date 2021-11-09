# Vision AI
## _JKL404_


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Derive insights from your images in the cloud or at the edge with AutoML Vision or use pre-trained Vision API models to detect emotion, understand text, and more.
![Cloud Vision](https://nanonets.com/blog/content/images/2021/04/cloud--1--1.gif)

## Features

- Use machine learning to understand your images with industry-leading prediction accuracy
- Train machine learning models that classify images by your custom labels using AutoML Vision
- Detect objects and faces, read handwriting, and build valuable image metadata with Vision API


## Installation
### Setting up the Google Vision API

To use the Google Vision API, you have to sign up for a Google Compute Engine Account. GCE is free to try but you will need a credit card to sign up. From there you select a project (but My First Project is selected if you have just signed up). Then get yourself an API key from the lefthand menu.
![google cloud](https://images.idgesg.net/images/article/2018/04/google-vision-api-screen-1-100755937-medium.jpg?auto=webp&quality=85,70)
Here, I’m using a simple API key that I can use with the command line tool Curl (if you prefer, you can use a different tool able to call REST APIs):

Save the key it generates to a json file 


Install the dependencies and devDependencies and start the server.

```sh
pip install flask, google-cloud, python
export GOOGLE_APPLICATION_CREDENTIALS="yourapikey.json"
python main.py
```

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```
## Demo
![img1](https://github.com/JKL404/Cloud_Vision/blob/main/Demo/Screenshot%20from%202021-11-09%2022-50-43.png?raw=true)
![img2](https://github.com/JKL404/Cloud_Vision/blob/main/Demo/Screenshot%20from%202021-11-09%2022-51-10.png?raw=true)
![img3](https://github.com/JKL404/Cloud_Vision/blob/main/Demo/Screenshot%20from%202021-11-09%2022-51-21.png?raw=true)
![img4](https://github.com/JKL404/Cloud_Vision/blob/main/Demo/Screenshot%20from%202021-11-09%2022-51-37.png?raw=true)
![img5](https://github.com/JKL404/Cloud_Vision/blob/main/Demo/Screenshot%20from%202021-11-09%2022-51-48.png?raw=true)
![img6](https://github.com/JKL404/Cloud_Vision/blob/main/Demo/Screenshot%20from%202021-11-09%2022-52-07.png?raw=true)
![img7](https://github.com/JKL404/Cloud_Vision/blob/main/Demo/Screenshot%20from%202021-11-09%2022-52-26.png?raw=true)
![img8](https://github.com/JKL404/Cloud_Vision/blob/main/Demo/Screenshot%20from%202021-11-09%2022-53-01.png?raw=true)
![img9](https://github.com/JKL404/Cloud_Vision/blob/main/Demo/Screenshot%20from%202021-11-09%2022-53-38.png?raw=true)
![img10](https://github.com/JKL404/Cloud_Vision/blob/main/Demo/Screenshot%20from%202021-11-09%2022-53-50.png?raw=true)

## License

MIT

**Free Software, Hell Yeah!**
