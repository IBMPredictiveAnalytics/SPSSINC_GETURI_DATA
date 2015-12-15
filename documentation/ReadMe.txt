This zip file contains the materials for the extension command

SPSSINC GETURI DATA.


The command provides a way to open data files stored on the Internet
It can open files in SPSS, Excel, SAS, and Stata formats.

This material requires 
SPSS Statistics 17 and 
the Python plug-in.

It includes a dialog box definition with help, the syntax definition, and the

implementation file.




To install this procedure for Version 17 or later, unzip all of the files into the extensions subdirectory
 of your SPSS Statistics installation.  Next, in SPSS Statistics, use
Utilties>Install Custom Dialog

to add this item to the menus.

The dialog box will appear under the File>Open menu.

Executing

SPSSINC GETURI DATA /HELP.

will display the complete syntax help.


This command has not been tested with Version 16, but it should work with two minor changes.
First, rename SPSSINC_GETURI_DATA.py to GETURI.py.  
Rename the xml file similarly.

Second, in the xml file, change the command name to GETURI
Place the Python file in your site-packages directory rather than in the extensions directory.  The dialog box, of course, will not be available in Version 16.


Questions and comments should be directed to the SPSS Developer Central Python
 Programmability forum.