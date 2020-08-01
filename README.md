# Avybe Code Challenge

## Set up

Clone this Repo and cd into it

```bash
$ git clone https://github.com/f3ve/Avybe-Code-Challenge.git

$ cd Avybe-Code-Challenge
```

Migrate:

```bash
$ python manage.py migrate
```
Launch the app

```bash
$ python manage.py runserver
```
## Creating an Account

After running the server go to [http://127.0.0.1:8000/accounts/](http://127.0.0.1:8000/accounts/) to view the landing page

From here you can register a new account or login to an existing one.

## Setting Up Your Profile

After you create an account you'll be redirected to a page where you can set up your profile. You will be able to upload a profile picture and add a nickname

After setting up your profile you will be redirected to your profile page to view your new changes. from here you can either update your profile picture and nickname or you can logout and be redirected back to login screen.

You can create as many accounts as you like!

## Creating an Admin Acount

In your shell run this command:

```bash
$ python manage.py createsuperuser
```
After you finish setting yor the admin you can go to [http://127.0.0.1:8000/admin/login/?next=/admin/](http://127.0.0.1:8000/admin/login/?next=/admin/) and login with the admin credentials you just created.

While you are on the admin site you will be able to view and edit all users and profiles. 

Admins can also log in as a normal user on the user side. You wont be able to edit other users info but you can create your own profile like a normal user.
