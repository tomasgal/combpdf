@echo off
setlocal enableextensions enabledelayedexpansion

REM Check if the correct number of arguments are provided
if "%~1"=="" (
    echo Usage: combpdf "first.pdf" "second.pdf"
    exit /b 1
)
if "%~2"=="" (
    echo Usage: combpdf "first.pdf" "second.pdf"
    exit /b 1
)

REM Set input files
set "first_pdf=%~1"
set "second_pdf=%~2"
set "output_pdf=combined.pdf"

REM Combine PDFs with second PDF appended at the end
pdftk "!first_pdf!" "!second_pdf!" cat output "!output_pdf!"

echo Combined PDF saved as "!output_pdf!"
endlocal
