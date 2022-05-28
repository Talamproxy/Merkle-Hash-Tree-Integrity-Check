@echo off
set STARTTIME=%TIME%
FOR /L %%A IN (10000,1,20000) DO (
  ECHO %%A
echo auto-commit %%A > commit-bat.txt
git add --all
git commit -am "auto-commit %%A"
)

set ENDTIME=%TIME%

    rem ******************  END MAIN CODE SECTION


    rem Change formatting for the start and end times
    for /F "tokens=1-4 delims=:.," %%a in ("%STARTTIME%") do (
       set /A "start=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
    )

    for /F "tokens=1-4 delims=:.," %%a in ("%ENDTIME%") do ( 
       IF %ENDTIME% GTR %STARTTIME% set /A "end=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100" 
       IF %ENDTIME% LSS %STARTTIME% set /A "end=((((%%a+24)*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100" 
    )

    rem Calculate the elapsed time by subtracting values
    set /A elapsed=end-start

    rem Format the results for output
    set /A hh=elapsed/(60*60*100), rest=elapsed%%(60*60*100), mm=rest/(60*100), rest%%=60*100, ss=rest/100, cc=rest%%100
    if %hh% lss 10 set hh=0%hh%
    if %mm% lss 10 set mm=0%mm%
    if %ss% lss 10 set ss=0%ss%
    if %cc% lss 10 set cc=0%cc%

set DURATION=%hh%:%mm%:%ss%.%cc%0000

echo %DURATION% 

set NLM=^


set NL=^^^%NLM%%NLM%^%NLM%%NLM%

echo auto-commit.bat%NL%10000 commits in %DURATION% > commit-bat.txt
git add --all
git commit -am "auto-commit.bat time"
