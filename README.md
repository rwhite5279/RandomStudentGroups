README.md
=========

PROJECT TITLE
-------------
RandomStudentGroups

AUTHOR
------
Richard White  
*rwhite@crashwhite.com*

PURPOSE OF PROJECT
------------------
This web-based project uses an HTML page to collect from a teacher a list
of student names and a group size. The page returns those values to a
Python-based CGI script which randomly groups the names from the list into
a series of groups of the given size.

VERSION
-------
2017-05-23

FILES INCLUDED
--------------
* random-student-groups.py
* random-student-groups.html

HOW TO USE THIS PROJECT
-----------------------
1. Place the `random-student-groups.html` file in a convenient directory on your LAMP server (public_html, etc.).
2. Place the `random-student-groups.py` file in the `cgi-bin` directory of your LAMP server. Confirm that the permissions on this file are 755 so the script will be able to execute.
3. Confirm that your server has Python installed, and has an `.htaccess` file with the line  
        `AddHandler cgi-script .py`  
in it.
4. The user may enter names on separate lines or on a single line with commas separating names.
5. The Python script does some degree of error-checking to catch silly errors.



