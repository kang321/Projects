# CPSC 304 | Vaccination Center

1. Clone the repository to 'C:/CPSC304/' (I will use this directory as a reference) 
    1. ```git clone git@github.students.cs.ubc.ca:CPSC304-2021W-T1/project_a0f2b_j4x5p_s4f3b.git``` 
2. Download PHP from https://windows.php.net/download#php-8.0 (Choose a 'Thread Safe' option and download the zip)
3. Create a new folder under your main drive named PHP (like C:/PHP)
4. Extract everything from the zip to the folder from (3)
5. Add the folder to the PATH
    1. Search for 'environment variables' in Windows
    2. Select "Edit the system environment variables"
    3. Click on the 'Environment Variables...' button on the prompted window
    4. Locate 'System variables' in the most recently prompted window
    5. Locate the variable 'Path' or 'PATH'
    6. Select it and press the 'Edit...' button
    7. Click 'New' button in the most recently prompted window
    8. Type in the path of the PHP folder (e.g. C:\PHP)
    9. Press on the 'Ok' buttons in all prompted windows
    10. If you have any command line instances open, please restart them
    11. Open a command line
    12. Type in the command: ```php -version```
        1. If you see an output "PHP 8..." then you are good to go with PHP! 
6. Download Composer
    1. Go to https://getcomposer.org/download/
    2. Download the Windows installer option
    3. Run the installer (Install for all users)
    4. DO NOT enable developer mode and click next
    5. Be sure that correct php.exe is selected (e.g. C:\PHP\php.exe) and click next
    6. Check 'Create a php.ini file' option and click next
    7. Click next and install and click your way out of the installer
    10. If you have any command line instances open, please restart them
    11. Open a command line
    12. Type in the command: ```composer --version```
        1. If you see an output "Composer version 2..." then you are good to go with Composer!
7. Configure php.ini
    1. Open php.ini which is inside the PHP folder (e.g. C:/PHP/php.ini) with a text editor.
    2. Search for ';extension=intl'
    3. Remove the ';'
8. cd into the project directory
9. Run the command: ```composer install```
    1. This will automatically install all dependencies of the project.
10. To start the development server; Run the command: ```php spark serve```
:)
### You are done with installation! Congrats :fireworks:


# Database setup
1. Download Docker
2. Run ```docker pull mysql```
3. Run ```docker run -p 3306:3306 --name vaccination -e MYSQL_ROOT_PASSWORD=password -d mysql:latest```
4. Download MySQL Workbench
5. Connect to the MySQL server (that we are running inside a docker container, if you can not connect, check if mysql container is running)
    1. Click 'Database' from the top header
    2. Click 'Connect to Database'
    3. Click 'Ok' since we are using default settings
    4. Enter 'password' in the password prompt
6. Create a new schema called 'vacc'
7. Open ```\app\Database\Migrations\create_tables.sql``` in the workbench
8. Run the whole file
9. Open ```\app\Database\Migrations\seed_all.sql``` in the workbench
10. Run the whole file

### You are done with Database setup! CZ :fireworks:
