# Howard Discord Token Cracker

> Cloning the repository

- Open command prompt: (Win key + r) and type "cmd"

  - Run:

            git clone https://github.com/ArtemisE1Tara/Howard-Discord-Token-Cracker


> Installation/Setup

- Creating a virtual enviorment

    - Open the project folder in your preffered IDE, Visual Studio Code is a good free option.

    - run:

            pip install virtualenv
    
    - To create the enviorment, run:

            virtualenv venv

- Starting the env

    - To allow proper permissions, run:

            Set-ExecutionPolicy Unrestricted -Scope Process

    - To start run:

            .\venv\Scripts\activate

> Installation of scripts in the env

- The env has only a base installation of python 3.10 without any additional required scripts.

    - Run:

            pip install -r requirements.txt

    - Finally, to install the compiler, run:

            pip install pyinstaller

> Compiling the exe

- Run:

        pyinstaller main.py

  - The exe should now be in an auto generated dist directory in the project folder.

    - Note: If you don't want a directory of files you can run:

                pyinstaller main.py --onefile
