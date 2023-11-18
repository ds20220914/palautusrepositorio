*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  david  david123
    Output Should Contain  New user registered
Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already exist
Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username is too short
Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  dav@  david123
    Output Should Contain  Username is not valid

Register With Valid Username And Too Short Password
    Input Credentials  david  david12
    Output Should Contain  password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  david  davidddd
    Output Should Contain  not only alphabet
*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input New Command
