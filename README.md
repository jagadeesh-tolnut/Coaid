# Coaid
###### help and heal

This Project was done on `Python 3.9.5`.
The Project dependencies are mentioned in `requirements.txt`, To install it perform `pip install -r requirements.txt`.

This Bot is Trained to answer FAQ's & Updates on Covid-19 and Vaccination.
Run have a Coaid Bot Working 
* Get into `coaidbot` folder
* execute to run the bot-api `rasa run -m models --enable-api --cors "*" --debug`
* execute to run bot custom actions `rasa run actions`
Now the bot-apt will be running at server `localhost:5005` and bot custom actions at `localhost:5055`

And Finally To run The Django Server:
* Get into Django Porject Folder `coaid`
* Execute `python manage.py makemigrations`
* Execute `python manage.py migrate`
* Execute `python manage.py runserver`

Django will run the server at `localhost:8000`