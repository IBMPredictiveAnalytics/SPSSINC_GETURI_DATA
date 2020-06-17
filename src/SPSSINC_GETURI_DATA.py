
#/***********************************************************************
# * Licensed Materials - Property of IBM 
# *
# * IBM SPSS Products: Statistics Common
# *
# * (C) Copyright IBM Corp. 1989, 2020
# *
# * US Government Users Restricted Rights - Use, duplication or disclosure
# * restricted by GSA ADP Schedule Contract with IBM Corp. 
# ************************************************************************/
"""SPSSINC GETURI DATA extension command"""

__author__ =  'spss, JKP'
__version__=  '1.2.0'

# history
# 27-may-2014 support long uris

helptext = """SPSSINC GETURI DATA URI="uri including filename" "..."
FILETYPE={SPSS* | XLS | SAS | STATA | OTHER}
[DATASET = datasetname]
[SAVE="directoryspec"]
[/OPTIONS
-- options for Excel --
[ASSUMEDSTRWIDTH=number]
[SHEETNAME="sheet name"]
[SHEETNUMBER = number]
[CELLRANGE = "Excel range specification"]
[READNAMES={YES* | NO}]
-- options for SAS --
[DSET = "dataset name"]]
[/HELP]

Open an SPSS, Excel, SAS, or Stata dataset from a web url or download and save
a file if type is OTHER.

URI specifies the full web address including the protocol such as http:// or ftp://
If the name is too long for an SPSS literal, write it as multiple quoted
strings that are NOT joined with "+".  For example,
URI="http://abc"
"defghi/somefile.xls"

FILETYPE specifies the type of file to read.
You can optionally assign a dataset name to the opened file.
If the filetype is OTHER, the SAVE keyword is required and specifies the directory
for the download.  If a file with the same name exists in the download
location, it may or may not be overwritten depending on the operating system.

Options are specific to the file type and are ignored if they do not apply.
For Excel, you can specify
ASSUMEDSTRWIDTH - the width to use for string variables
SHEETNAME - the name of the sheet to read
SHEETNUMBER - the number of the sheet to read.
You cannot specify both the name and the number.  The default is SHEETNUMBER=1
CELLRANGE - the range to read within the sheet.  The default is to read the entire sheet.
READNAMES - whether to read variable names from the first row of the range.  The default is YES.

For SAS you can specify the dataset name within the uri.

There are no options for SPSS or Stata files.

/HELP displays this help and does nothing else.
"""
import spss, spssaux
from extension import Template, Syntax, processcmd
import urllib.request, urllib.parse, urllib.error, os, shutil
        
def geturidata(uri, filetype="sav", save=None, dataset=None, assumedstrwidth=32767, sheetname=None,
    sheetnumber=None, cellrange=None, readnames="ON", dset=None):
    """Open a data file from a uri"""
    # debugging
    # makes debug apply only to the current thread
    #try:
        #import wingdbstub
        #if wingdbstub.debugger != None:
            #import time
            #wingdbstub.debugger.StopDebug()
            #time.sleep(1)
            #wingdbstub.debugger.StartDebug()
        #import thread
        #wingdbstub.debugger.SetDebugThreads({thread.get_ident(): 1}, default_policy=0)
        ### for V19 use
        ####    ###SpssClient._heartBeat(False)
    #except:
        #pass
    kwargs = {}
    uri = "".join(uri)
    kwargs["filetype"] = filetype
    if filetype == "other" and save is None:
        raise ValueError(_("""An output file must be specified for type other."""))
    if filetype == "other":
        getfile(uri, save)
    else:
        if dataset:
            kwargs["datasetName"] = dataset
        kwargs["assumedstrwidth"] = assumedstrwidth
        kwargs["readnames"] = readnames and "ON" or "OFF"
        if dset:
            kwargs["dset"] = dset
        if sheetname and sheetnumber:
            print("Warning: both sheet name and sheet number specified.  Using the name")
        if sheetname:    # if both present, use the name
            kwargs["sheet"] = "name"
            kwargs["sheetid"] = sheetname
        elif sheetnumber:
            kwargs["sheet"] ="index"
            kwargs["sheetid"] = sheetnumber  
        if cellrange:
            kwargs["cellrange"] = "range"
            kwargs["rangespec"] = cellrange
        
        spssaux.openDataFileFromUrl(uri, **kwargs)
       
def getfile(uri, saveloc):
    """Retrieve and save file but do not try to open it
    
    uri is the source location
    saveloc is the output location"""
    
    if not os.path.isdir(saveloc):
        raise ValueError(_("""The save location specified does not exist or is not a directory"""))
    try:
        localfilename, headers = urllib.request.urlretrieve(uri)
    except:
        raise ValueError(_("""The specified uri is not valid: %s""") % uri)
    unqname = urllib.parse.unquote_plus(uri)
    truefilename = os.path.split(unqname)[-1]
    localdir = "".join(os.path.split(localfilename)[:-1])
    newname = localdir + "/" + truefilename
    try:
        shutil.move(localfilename, saveloc)
    except:
        raise ValueError(_("""Could not write to the specified destination: %s""") % saveloc)
    try:
        os.rename(saveloc + os.sep + os.path.basename(localfilename), saveloc + os.sep + truefilename)
    except:
        raise ValueError(_("""Cannot assign the original name.
        The downloaded file is in %s and is named %s""") % (saveloc, os.path.basename(localfilename)))
    print(_("""The requested file, %s, has been saved in %s.""") % (truefilename, saveloc))
 
def Run(args):
    """Execute the SPSSINC GETURI DATA extension command"""

    args = args[list(args.keys())[0]]
    ###print args   #debug

    oobj = Syntax([
        Template("URI", subc="",  ktype="literal", var="uri", islist=True),
        Template("FILETYPE", subc="", ktype="str", var="filetype", 
            vallist=["sav","xls","xlsx","xlsm","sas", "stata", "other"]),
        Template("SAVE", subc="", ktype="literal", var="save"),
        Template("DATASET", subc="", ktype="varname", var="dataset"),
        Template("ASSUMEDSTRWIDTH", subc="OPTIONS", ktype="int", var="assumedstrwidth"),
        Template("SHEETNAME", subc="OPTIONS", ktype="literal", var="sheetname"),
        Template("SHEETNUMBER", subc="OPTIONS", ktype="int", var="sheetnumber"),
        Template("CELLRANGE", subc="OPTIONS", ktype="literal", var="cellrange"),
        Template("READNAMES", subc="OPTIONS", ktype="bool", var="readnames"),
        Template("DSET", subc="OPTIONS",  ktype="literal", var="dset"),
        Template("HELP", subc="", ktype="bool")])
    
    # A HELP subcommand overrides all else
    if "HELP" in args:
        #print helptext
        helper()
    else:
        processcmd(oobj, args, geturidata)

def helper():
    """open html help in default browser window
    
    The location is computed from the current module name"""
    
    import webbrowser, os.path
    
    path = os.path.splitext(__file__)[0]
    helpspec = "file://" + path + os.path.sep + \
         "markdown.html"
    
    # webbrowser.open seems not to work well
    browser = webbrowser.get()
    if not browser.open_new(helpspec):
        print(("Help file not found:" + helpspec))
try:    #override
    from extension import helper
except:
    pass