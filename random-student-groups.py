#!/usr/bin/env python

"""
random-student-groups.py
This Python 2.7 script should be placed in cgi-bin and chmodded to 755 so that it can be run
with form data from random-student-groups.html.
@author Richard White
@version 2017-05-23
"""

import cgi
import string
import sys
import datetime
import random

sys.stderr = sys.stdout

def open_html_headers():
    print "Content-type: text/html\n"
    print """<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<title>Random Groups</title>
	<meta http-equiv="Content-Language" content="en-us" />
	<meta name="resource-type" content="document" />
	<meta name="author" content="richard white" />
	<meta name="Description" content="Random Student Groups" />
	<meta name="Keywords" content="richard white, random, student, groups" />
	<meta name="distribution" content="global" />
	<meta name="Content-Type" content="text/html; charset=utf-8" />	
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<style type="text/css" media="all">
		html {margin: 0; padding: 0; }
		body {margin: 0; padding: 0; font-family: Verdana, Arial, Helvetica, sans-serif; font-size: 1.5em; font-weight: normal; color: #fff; background: #333; }
		a:link, a:visited 	{text-decoration: underline; color: #0f0; font-weight: bold; }
		a:hover, a:active	{text-decoration: none; color: #2f2;}
		#mainwrapper {margin:0; padding: 0; border: 0; width:100%;}
		.columnwrapper {width: 100%; margin: 0 auto; padding: 0; border: 0; overflow: auto; } 		  
		#content {margin: 1em 0.5em; border: 0; padding: 0; }
		input	{background-color: #333; color: #fff; font-size: 110%; border: 0; padding: 5px; width: 90%; }
		.rounded_corner_container {-moz-border-radius:10px; -webkit-border-radius:10px; background-color: #000; margin: 0 0.5em; padding: 10px; border: solid 1px #fff; }
		td    {color: #0f0}
		
		/*
            These specification below are the ones with trigger alterations in display based on browser width.
            The defaults CSS-descriptions above are based on an assumed mobile, "vertically-prominent" display.
            
            This specification, then, describes how to alter those default display values for a wider (>= 600px)
            display port.
        */
                    
        /* desktop display, for large-width desktop-sized display, all the way down to 600px wide*/
        @media (min-width: 600px) { 
            body {font-size: 90%;}
            .columnwrapper {width: 500px; margin: 0 auto; padding: 0;}
            .rounded_corner_container { }
        }
		
	</style>
</head>
<body>
 	<div id="mainwrapper">	    	
    	<div class="columnwrapper">
    		<div id="content">"""
    

def close_html_headers():
    print """       		</div><!--content-->
   		</div><!--columnwrapper-->
  </div><!--mainwrapper-->
</body>
</html>
"""


def main():
    # Create webpage
    open_html_headers()
    # This call places cgi field contents in a dictionary. 
    # The parameter allows us to have blank form fields.
    form = cgi.FieldStorage(keep_blank_values = 1)
    names, groupSize = (form['names'].value, form['groupSize'].value)
    errors = False
    try:
        groupSize = int(eval(groupSize))
    except:
        print("<p>Invalid group size.</p>")
        errors = True
    if len(names) < 1:
        print("<p>Invalid student list.</p>")
        errors = True
    if groupSize < 1:
        print("<p>Invalid group size.</p>")
        errors = True
    if errors:
        print("<p>Go back and try again!</p>")
        close_html_headers()
        exit()
    else:
        # Try splitting up names by blank lines
        students = names.split("\n")
        # If there's only one line, split names up by commas
        if len(students) == 1:
            students = students[0].split(",")
        # Cleaning data a little:
        # 1. Remove whitespace on either side of students' names, and blank students
        students = [student.rstrip().lstrip() for student in students if student.rstrip().lstrip() != '']
        while len(students) > 0:
            i = 0
            print("<p>")
            while i < groupSize and len(students) > 0:
                # Pick a random student from the list of students
                if i > 0:
                    print(", ")
                random_student_num = random.randrange(len(students))  
                # Display result
                print(students[random_student_num])
                # Remove their name from the list
                students.remove(students[random_student_num])     
                i += 1   
                # Check to see if this group is filled
                if i % groupSize == 0:
                    print("</p><p>") 
            print("</p>")
    close_html_headers()   

if __name__ == "__main__":
    main()
