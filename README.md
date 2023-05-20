# cits_3403_2023
## Purpose of our project
Our project is going to make a chatbot web application with multiple functions to our users including:
1) login and sign up with username and password
2) chat with chatbot interactively
3) review and search the chat log

## The architecture our web application
Our web application mainly consists of a front-end and a back-end.

### Front-end
The front-end is primarily responsible for rendering the user interface. It is constructed using HTML, CSS, and JavaScript, with Ajax for asynchronous communication with the back-end. Functions such as user login, sign up, interaction with the chatbot, and viewing and searching chat logs are all executed here.

### Back-end
The back-end uses the Flask framework to handle requests sent from the front-end, such as user login, registration, and processing user interactions with the chatbot. For the chatbot implementation, we are using the OpenAI's GPT model.

### Database
We use MongoDB as our database to store user account information and chat logs.

## How to launch the application?

### Environment Setup
1. Install Python and pip (Python Package Installer).
2. Clone the project to your local machine:
`git clone https://github.com/yourusername/cits_3403_2023.git`
3. Navigate to the project root directory and install the required dependencies:
`pip install -r requirements.txt`

### Starting the Application
1. To start the back-end server, run the following command in the project root directory:
`flask run`
3. For the front-end, open the `index.html` file in a web browser.

### Note
Ensure that your MongoDB database is running, and that the connection details in your Flask application are set correctly.

## Tests of the application

Testing is an essential part of our application development process to ensure the functionality and reliability of our chatbot application. Here are some ways we test our application:

 first setting gpt api using below command line
    export OPENAI_API_KEY="xxx"
    xxx= gpt_api

    

### Unit Tests

We have unit tests in place for both our front-end and back-end components. For front-end JavaScript code, we use Jest to test individual functions and user interface components. For back-end Python code, we use the built-in `unittest` module in Python.

To run unit tests, navigate to the project root directory and run the following command:

```shell
python -m unittest discover tests
```
### System Tests

We perform system tests manually to ensure that all parts of our application work together as expected. This includes testing the user registration, login, chatbot interaction, and chat log review and search functionalities.
## Contributions
