# Emergency-Department-Team19

instructions to run this program:

OPEN CMD

1- clone  the project to an empty repositry

             
         git clone https://github.com/Amrmohamed090/Emergency-Department-Team19.git
              
       

2- go to the project directory, "the directory where you can find run.py"

             cd <project Directory>


3- add a virtual environment

              py -m venv env

note: if virtualenv is not installed in your device use "pip install virtualenv"

4- activate the virtual environment

              env\Scripts\activate
              
              note: IF you are using vscode terminal and had an ERROR with 'cannot be loaded because running scripts is disabled on this system.'
              open powershell as adminstrator ant type:
               "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine"
               and confirm with YES
                    

5-install requirment packages

              pip install -r requirements.text

6-run the app

              py run.py


  after installation every time you want to run the app you need to activate tha virtual environment before running the up
  

              env\Scripts\activate
              py run.py

  
            
