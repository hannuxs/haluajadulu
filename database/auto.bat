set MYSQL_USER=root
set MYSQL_DATABASE=loop_db
set MYSQL_HOST=localhost
set MYSQL_PORT=3306
set SQL_FILE=loop_db.sql
::cd aja ke folder xampp
set MYSQL_BIN_PATH=C:\xampp\mysql\bin\mysql.exe

echo Membuat database %MYSQL_DATABASE%...
"%MYSQL_BIN_PATH%" -u %MYSQL_USER% -h %MYSQL_HOST% -P %MYSQL_PORT% -e "DROP DATABASE IF EXISTS %MYSQL_DATABASE%;"
"%MYSQL_BIN_PATH%" -u %MYSQL_USER% -h %MYSQL_HOST% -P %MYSQL_PORT% -e "CREATE DATABASE IF NOT EXISTS %MYSQL_DATABASE%;"

if %ERRORLEVEL% NEQ 0 (
    echo Gagal membuat database %MYSQL_DATABASE%.
    exit /b %ERRORLEVEL%
) else (
    echo Berhasil membuat database %MYSQL_DATABASE%.
)

echo Mengimpor data ke database %MYSQL_DATABASE%...
"%MYSQL_BIN_PATH%" -u %MYSQL_USER% -h %MYSQL_HOST% -P %MYSQL_PORT% %MYSQL_DATABASE% < %SQL_FILE%

if %ERRORLEVEL% NEQ 0 (
    echo Gagal mengimpor data ke MySQL.
    exit /b %ERRORLEVEL%
) else (
    echo Berhasil mengimpor data ke MySQL.
)

pause
