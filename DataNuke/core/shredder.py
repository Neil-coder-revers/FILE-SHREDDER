import os
import random
import string
import time

def secure_delete(path, passes=3, callback=None):
    if not os.path.exists(path):
        if callback: callback("Error: Target not found")
        return

    if os.path.isdir(path):
        if callback: callback(f"Processing Directory: {path}")
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                _shred_file(file_path, passes, callback)
            for name in dirs:
                dir_path = os.path.join(root, name)
                _remove_dir(dir_path, callback)
        _remove_dir(path, callback)
        if callback: callback("Success: Directory securely erased.")
    else:
        _shred_file(path, passes, callback)

def _remove_dir(path, callback):
    try:
        dir_name = os.path.dirname(path)
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        new_path = os.path.join(dir_name, random_name + ".tmp")
        os.rename(path, new_path)
        os.rmdir(new_path)
    except Exception:
        pass

def _shred_file(file_path, passes, callback):
    try:
        file_size = os.path.getsize(file_path)
        if callback: callback(f"Wiping: {os.path.basename(file_path)}")

        with open(file_path, "wb") as f:
            for pass_num in range(1, passes + 1):
                data = os.urandom(min(file_size, 1024 * 1024))
                f.seek(0)
                written = 0
                while written < file_size:
                    chunk = min(len(data), file_size - written)
                    f.write(data[:chunk])
                    written += chunk
                f.flush()
                os.fsync(f.fileno())

        dir_name = os.path.dirname(file_path)
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        new_path = os.path.join(dir_name, random_name + ".tmp")
        
        os.rename(file_path, new_path)
        os.remove(new_path)
        
    except Exception as e:
        if callback: callback(f"Error: {str(e)}")
