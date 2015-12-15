
SPSSINC GETURI DATA
URI="http://media.pearsoncmg.com/aw/aw_deveaux_stats_2/activstats/spss/Ch03_Magnet_schools.sav"
FILETYPE=SAV 
/OPTIONS
SHEETNUMBER=1 READNAMES=YES ASSUMEDSTRWIDTH=32767.

SPSSINC GETURI DATA
URI="http://som.yale.edu/sites/default/files/files/Earnings.xls"
FILETYPE=XLS DATASET=shiller 
/OPTIONS
SHEETNUMBER=1 READNAMES=YES ASSUMEDSTRWIDTH=500.



SPSSINC GETURI DATA
URI="http://www2.census.gov/prod2/statcomp/usac/excel/Source.xls"
FILETYPE=XLS 
/OPTIONS
SHEETNUMBER=1 READNAMES=YES ASSUMEDSTRWIDTH=32767.
