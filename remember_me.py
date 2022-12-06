from pathlib import Path
import json

# Collecting / retrieving user information to store in text files

def get_stored_username(path):
    """Retrieve stored username if exists"""
    path = Path(path)
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Creating new username that will be written to file"""
    path = Path(path)
    username = input("Create new username: ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def get_stored_age(path):
    """Retrieve stored age if exists"""
    path = Path(path)
    if path.exists():
        contents = path.read_text()
        hobbies = json.loads(contents)
        return hobbies
    else:
        return None


def get_new_age(path):
    """Creating new age that will be written to file"""
    path = Path(path)
    age = input("Create age: ")
    contents = json.dumps(age)
    path.write_text(contents)
    return age

def get_stored_job(path):
    """Retrieve job info if stored"""
    path = Path(path)
    if path.exists():
        contents = path.read_text()
        job = json.loads(contents)
        return job
    else:
        None

def get_new_job(path):
    """Create new job to be written to file"""
    path = Path(path)
    job = input("What is your occupation?: ")
    contents = json.dumps(job)
    path.write_text(contents)
    return job

def greet_user(path):
    """Greet user by name"""
    path = Path(path)
    username = get_stored_username(path)
    # check if username True then / input to be stored if not
    if username:
        correct_username = input(f"Is this your username?: {username}: y/n?")
        if correct_username == 'y':
            print(f"Welcome back {username.title()}")
        else:
            username = get_new_username(path)
            print(f"We'll remember {username} when you come back")


# dictionary of full user to be added to file
new_user = {
    'username': get_new_username('files_and_exceptions/new_user.txt'),
    'age': get_new_age('files_and_exceptions/new_user_age.txt'),
    'job': get_new_job('files_and_exceptions/new_user_job.txt'),
}

# adding new user to file
path = Path('files_and_exceptions/full_new_user.txt')
contents = json.dumps(new_user)
path.write_text(contents)


