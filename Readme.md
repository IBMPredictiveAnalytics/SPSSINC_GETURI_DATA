# SPSSINC GETURI DATA
## Open an SPSS, Excel, SAS, or Stata dataset from a web url.
 This command takes a URL as input and downloads and opens a data file.  It can be used to download and save files of other typ  es, but these will not be opened.

---
Requirements
----
- IBM SPSS Statistics 18 or later and the corresponding IBM SPSS Statistics-Integration Plug-in for Python.

Note: For users with IBM SPSS Statistics version 23 or higher, the SPSSINC GETURI DATA extension is installed as part of IBM SPSS Statistics-Essentials for Python.

---
Installation intructions
----
1. Open IBM SPSS Statistics
2. Navigate to Utilities -> Extension Bundles -> Download and Install Extension Bundles
3. Search for the name of the extension and click Ok. Your extension will be available.

---
Tutorial
----
SPSSINC GETURI DATA URI="*uri including filename*"^&#42; "..."  
FILETYPE=SPSS^&#42;&#42; or XLS or SAS or STATA or OTHER
DATASET = *dataset*  
SAVE="directory"  

/OPTIONS
-- options for Excel --  
ASSUMEDSTRWIDTH = *number*  
SHEETNAME ="*sheet name*"  
SHEETNUMBER = *number*  
CELLRANGE = "*Excel range specification*"  
READNAMES=YES^&#42;&#42; or NO  
-- options for SAS --  
DSET = "*dataset*"

/HELP

^&#42; Required  
^&#42;&#42; Default

/HELP displays this help and does nothing else.



Example:
```
SPSSINC GETURI DATA
URI="http://www2.census.gov/prod2/statcomp/usac/excel/Source.xls"
FILETYPE=XLS 
/OPTIONS SHEETNUMBER=1 READNAMES=YES ASSUMEDSTRWIDTH=100.
```

**URI** specifies the full web address including the protocol such as http:// or ftp://
If the name is too long for an SPSS literal, write it as multiple quoted
strings that are NOT joined with "+".  For example,
```URI="http://abc" "defghi/somefile.xls"```

**FILETYPE** specifies the type of file to read.

You can optionally use **DATASET** to assign a dataset name to the opened file.

If the filetype is OTHER, the **SAVE** keyword is required and specifies the directory
for the download.  The file is not opened.  If a file with the same name exists in the download
location, it may or may not be overwritten depending on the operating system.

Options are specific to the file type and are ignored if they do not apply.
For Excel, you can specify
* ASSUMEDSTRWIDTH - the width to use for string variables
* SHEETNAME - the name of the sheet to read
* SHEETNUMBER - the number of the sheet to read.
You cannot specify both the name and the number.  The default is SHEETNUMBER=1
* CELLRANGE - the range to read within the sheet.  The default is to read the entire sheet.
* READNAMES - whether to read variable names from the first row of the range.  The default is YES.

For SAS you can specify the dataset name within the uri with **DSET**.

There are no options for SPSS or Stata files.

---
License
----

- Apache 2.0
                              
Contributors
----

  - JKP, IBM SPSS
