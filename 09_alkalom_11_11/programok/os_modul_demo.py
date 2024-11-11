import os, shutil, time

def teszt():
    try:
        if not os.path.exists("example.txt"):
            with open("example.txt", "w") as f:
                f.write("Hello world")
    except FileNotFoundError as e:
        print(e)


    for file in os.listdir("."):
        print(file)

    print(os.getcwd())

# os.mkdir("new folder")

# os.chdir("..") # egy szinttel visszalépünk
#print(f'hol vagyunk: {os.getcwd()}')

# txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
# print(f'txt files {txt_files}')


# file_size = os.path.getsize("example.txt")
# print(file_size)


"""if os.name == "nt": # win
    os.system("dir")
else:
    os.system("ls") # linux"""


"""base_path = os.getcwd()
file_path = os.path.join(base_path, "folder", "file.txt")
print(f"Full path: {file_path}")"""


#with open("tempfile.tmp", "w") as temp_file:
#    temp_file.write("tmp data")
#print("tmp file created")

#os.remove("tempfile.tmp")


"""# új környezeti változó
os.environ["NEW_VAR"] = "pyautomation"
print("new var: ", os.getenv("NEW_VAR"))"""


"""for root, dirs, files in os.walk("."):
    print("Dir: ", root)
    for file in files:
        print("File: ", file)"""



"""path = "new folder"
if os.path.isfile(path):
    print(f"ez egy file {path}")
elif os.path.isdir(path):
    print(f'ez egy mappa {path}')
else:
    print(f'{path} nem létezik')"""


# last modify time
"""mod_time = os.path.getmtime("example.txt")
print(time.ctime(mod_time))"""


# kivételkezelés
"""try:
    os.remove("nonexistenfile.txt")
except FileNotFoundError as e:
    print(f'Error: {e}')"""


os.makedirs("parent/child/grandchild", exist_ok=True) # többszintű mappa létrehozása
os.removedirs("parent/child/grandchild") # többszintű mappa törlése

# print("current user:", os.getlogin())


"""temp_dir = os.getenv("TEMP", "/tmp") # ideiglenes könyvtárat
print(temp_dir)"""


"""# os név elérése
if os.name == "nt":
    print("windows")
elif os.name == "posix":
    print("linux / mac")
"""


#with open("permission.txt", "w") as f:
#    f.write("permission example")

#os.chmod("permission.txt", 0o444) # csak olvasható read only


# file méret stat-al
"""file_size = os.stat("example.txt").st_size
print(file_size)"""

# összes környezeti változó
"""for key, value in os.environ.items():
    print(f'K: {key} - V: {value}')"""


"""# linux-os változat uptime system
if os.name == "posix":
    print("system uptime: ", os.system("uptime"))"""


# runtime program / függv method
"""start_time = time.time()
time.sleep(2)
end_time = time.time()
print(f'program runtime: {end_time - start_time} sec')"""


"""file_stat = os.stat("example.txt")
print(f'size: {file_stat.st_size} bytes')
print(f'last modify: {file_stat.st_mtime}')
"""














