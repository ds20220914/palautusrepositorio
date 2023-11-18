*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Register With Valid Username And Password
     Go To Register Page
     Set Username  david
     Set Password  david123
     Set Password Confirmation  david123
     Submit Credentials
     Register Should Succeed     

Register With Too Short Username And Valid Password
     Go To Register Page
     Set Username  da
     Set Password  david123
     Set Password Confirmation  david123
     Submit Credentials
     Register Should Not Succeed

Register With Valid Username And Invalid Password
     Go To Register Page
     Set Username  davidd
     Set Password  davidddd
     Set Password Confirmation  davidddd
     Submit Credentials
     Page Should Contain  not only alphabet
Register With Nonmatching Password And Password Confirmation
     Go To Register Page
     Set Username  daviddd
     Set Password  david123
     Set Password Confirmation  david1234
     Submit Credentials
     Page Should Contain  password confirmation wrong

*** Keywords ***
Register Should Succeed
    Register Success

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Register Should Not Succeed
    Register Not Success

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password   password_confirmation  ${password_confirmation}
