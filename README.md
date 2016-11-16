# Subs_Abuse_Train_Test
The training and testing pipelines for the Substance Abuse Detection module in the Argos clinical abstraction project.

##Dependencies:
In order run the training and testing pipelines, there are a number of python libraries, a configuration file, and a specific directory structure that must be set up properly:

1. Python2.7 and the following libraries: <br />
  &nbsp;&nbsp;&nbsp;&nbsp;i. nltk <br />
  &nbsp;&nbsp;&nbsp;&nbsp;ii. pyodbc <br />
  &nbsp;&nbsp;&nbsp;&nbsp;iii.NumPy (>= 1.6.1), <br />
  &nbsp;&nbsp;&nbsp;&nbsp;iv. SciPy (>= 0.9). <br />
  &nbsp;&nbsp;&nbsp;&nbsp;v. sklearn (Find OS-specific instructions on scikit-learn's sometimes tricky install here: http://scikit-learn.org/stable/install.html) <br />
  &nbsp;&nbsp;&nbsp;&nbsp;vi. python-crfsuite (>= 0.8.4) <br />
 
2. ODBC driver and settings config file: <br />
  &nbsp;&nbsp;&nbsp;&nbsp;i. You must have an ODBC driver installed on your machine. <br />
  &nbsp;&nbsp;&nbsp;&nbsp; ii. This application currently relies on Labkey databases storing training and testing data. In order ensure the program pulls data from the correct sources, you must include a config file at the following location: <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. UNIX: '/etc/nlp-abstraction-pipeline/config/odbc_settings' <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. WINDOWS: '%USERPROFILE%\AppData\Local\nlp-abstraction-pipeline\config\odbc_settings' <br />
  &nbsp;&nbsp;&nbsp;&nbsp;iii. The config file at the above location should look something like this: <br />
    <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DRIVER=Name of ODBC Driver installed on your machine <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SERVER=Name of the server where Labkey lives and stores data <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DATABASE=Name of the database where Labkey stores abstrction notes and metadata <br />

3. DataDir data directory structure: <br />
  &nbsp;&nbsp;&nbsp;&nbsp;i. You must create the following folders: DataDir/CRFModels, DataDir/SVMModels, DataDir/Evaluation <br />
  &nbsp;&nbsp;&nbsp;&nbsp;ii. the DataDir folder must live in ../fhcrc_clinical/SocialHistories/DataDir/ <br />
  &nbsp;&nbsp;&nbsp;&nbsp;iii. The structure should look like this: <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;../fhcrc_clinical/ <br />
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- SocialHistories/ <br />
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- DataDir/ <br />
                                   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- SVMModels/ <br />
                                   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- CRFModels/ <br />
                                   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|- Evaluation/ <br />
 <br />
 
##Training the substance abuse information extraction models: <br />
1. cd {Subs_Abuse_Test_Train Project path}/fhcrc_clinical/SocialHistories <br />
2. python train_pipeline <br />
  &nbsp;&nbsp;&nbsp;&nbsp;i. It takes about 20 minutes to train on all the data in labkey training set <br />
  &nbsp;&nbsp;&nbsp;&nbsp;ii. The script, if executed properly and without error, will produce model files in ../DataDir/SVMModels/ and ../DataDir/CRFModels/ <br />
 <br />
 
 
##Testing and evaluating the substance abuse information models: <br />
1. python test_pipeline <br />
  &nbsp;&nbsp;&nbsp;&nbsp;i.  The script will use the models produced in the training step to classify and evaluate the classification of the test data in Labkey <br />
  &nbsp;&nbsp;&nbsp;&nbsp;ii. The output of this script will produce evaluation numbers in ../DataDir/Evaluation/ <br />
