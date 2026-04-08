*** Settings ***
Library       RequestsLibrary

*** Test Cases ***
Test Requête Get Simple
    ${response}=    GET    https://www.google.com
    Should Be Equal As Integers    ${response.status_code}    200
