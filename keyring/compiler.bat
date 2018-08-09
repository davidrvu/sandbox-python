::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:: RUN FILE
::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@echo off
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo RUN COMPILER
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


CALL timecmd pyinstaller --noupx --icon=key.ico  store_user_pass.py
CALL timecmd xcopy /i /e /y "C:\Anaconda3\Lib\site-packages\keyring" "C:\repos\sandbox-python\keyring\dist\store_user_pass\keyring"
CALL timecmd xcopy /i /e /y "C:\Anaconda3\Lib\site-packages\keyring-13.2.1.dist-info" "C:\repos\sandbox-python\keyring\dist\store_user_pass\keyring-13.2.1.dist-info"


CALL timecmd pyinstaller --noupx --icon=key.ico  retrieve_user_pass.py
CALL timecmd xcopy /i /e /y "C:\Anaconda3\Lib\site-packages\keyring" "C:\repos\sandbox-python\keyring\dist\retrieve_user_pass\keyring"
CALL timecmd xcopy /i /e /y "C:\Anaconda3\Lib\site-packages\keyring-13.2.1.dist-info" "C:\repos\sandbox-python\keyring\dist\retrieve_user_pass\keyring-13.2.1.dist-info"

echo DONE!