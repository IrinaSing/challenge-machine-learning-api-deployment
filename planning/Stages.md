# Milestones (stages)

## Step 1: Project preparation

- [x] Create a folder to handle your project.
- [x] Create a file `app.py` that will contain the code for your API.
- [x] Create a folder `preprocessing/` that will contain all the code to preprocess your data.
- [x] Create a folder `model/` that will contain your model.
- [x] Create a folder `predict/` that will contain all the code to predict the price.

## Step 2: Preprocessing pipeline

This python module will contain all the code to preprocess your data. Make sure to think about what will be the format of your data to fit the model.
Also, be sure to know which information HAVE to be there and which one can be empty (NAN).

In the `preprocessing/` folder:

- [x] Create the `cleaning_data.py` file that will contain all the code that will be used to preprocess the data you will receive to predict a new price. (fill the NaN values, handle text data, etc...).
- [x] This file should contain a function called `preprocess()` that will take a new house's data as input and return those data preprocessed as output.
- [ ] If your data doesn't contain the required information, you should return an error to the user.

## Step 3: Fit your data

Fit your data to your model.

In the `predict/` folder:

- [ ] Create the `prediction.py` file that will contain all the code used to predict a new house's price.
- [ ] Your file should contain a function `train()` that will create and store the model and a function `predict()` that will take your preprocessed data as an input and return a price as output using your stored model.

## Step 4: Create your API

In your `app.py` file, create a Flask API that contains:

- [ ] A route at `/` that accept:
  - [ ] `GET` request and return `"alive"` if the server is alive.
- [ ] A route at `/predict` that accept:
  - [ ] `POST` request that receives the data of a house in JSON format.
  - [ ] `GET` request returning a string to explain what the `POST` expect (data and format).

## Step 5: Deploy your app on Heroku

- [ ] Deploy your web app on Heroku using the requirements.txt file. You can use the following tutorial as a reference: [Deploying a Flask Application to Heroku](https://stackabuse.com/deploying-a-flask-application-to-heroku/)

## Nice-to- have's:

- [ ] Try other regression models for your prediction.
- [ ] Deploy your application using a docker image to Heroku. To deploy your API, using Docker:

  - Create a Dockerfile that creates an image with:
    - Ubuntu
    - Python 3.8
    - Flask
    - All the other dependencies you will need.
    - All the files of your project in an `/app` folder that you will previously create.
  - Create a `requirements.txt` file.
  - Run your `app.py` file with Python.
  - Heroku will allow you to push your docker container on their server and start it.
