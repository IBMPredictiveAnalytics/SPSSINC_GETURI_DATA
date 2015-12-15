spssinc geturi data uri="https://www.ibm.com/developerworks/community/files/app/file/85f6fd50-5409-48e8-982b-0e16084b00e0"
filetype=other save="c:/temp/fred.xyz".


begin program.
import SPSSINC_GETURI_DATA
reload(SPSSINC_GETURI_DATA)
end program.

spssinc geturi data uri="ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NIS/NIS_Child_HHQuex_Q1_2012.pdf"
filetype=other save="c:/temp/fred".

spssinc geturi data uri="ftp://ftp.cdc.gov/pub/badspec"
filetype=other save="c:/temp/fred".
