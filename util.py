import json
import pickle
import os
import platform

from cryptography.fernet import Fernet

if platform.system() == 'Windows':
    abs_file_location = 'AudibleData\\'
else:
    abs_file_location = 'AudibleData/'


def get_abs_file_path(relative_path: str = ''):
    relative_path = abs_file_location + relative_path
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, relative_path)
    return abs_file_path

key_path = get_abs_file_path('filekey.key')


def pretty_print_dict(dictionary: dict):
    formatted = json.dumps(dictionary, default=str, indent=2)
    return formatted


def write_local_file(data_to_write, file: str):
    file_path = get_abs_file_path(file)
    with open(file_path, 'wb') as file_to_write:
        key = get_key()
        fernet = Fernet(key)
        data_string = pickle.dumps(data_to_write)
        encrypted_data_string = fernet.encrypt(data_string)
        file_to_write.write(encrypted_data_string)
        file_to_write.close()


def read_local_file(file: str):
    file_path = get_abs_file_path(file)
    try:
        key = get_key()
        fernet = Fernet(key)
        local_file_stream = open(file_path, 'rb')
        encrypted_local_file_string = local_file_stream.read()
        decrypted_local_file_string = fernet.decrypt(encrypted_local_file_string)
        local_file_stream.close()
        local_file_obj = pickle.loads(decrypted_local_file_string)
        return local_file_obj
    except FileNotFoundError:
        print('FileNotFound: No local file found')


def remove_local_file(file:str):
    file_path = get_abs_file_path(file)
    os.remove(file_path)

def generate_key():
    key = Fernet.generate_key()

    key_file = None
    try:
        with open(key_path, 'rb') as key_file_stream:
            key_file = key_file_stream.read()
            key_file_stream.close()
            return key_file
    except FileNotFoundError:
        print('FileNotFound: No encryption key found')

    if key_file is None:
        with open(key_path, 'wb') as filekey:
            filekey.write(key)

    return key

def get_key():
    key = None
    try:
        with open(key_path, 'rb') as filekey:
            key = filekey.read()
            return key
    except FileNotFoundError:
        print('FileNotFound: No encryption key found')

    if key is None:
        new_key = generate_key()
        return new_key
