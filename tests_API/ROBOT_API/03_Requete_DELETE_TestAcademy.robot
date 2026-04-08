*** Settings ***
Library    RequestsLibrary

*** Variables ***
${Base_URL}         https://mock-api-h0g7.onrender.com/
${API_KEY}          Cle-API-ReqRes-test-academy
${Id_Utilisateur}   5

*** Test Cases ***
Test Requete DELETE
    &{headers}=    Create Dictionary    Authorization=Bearer ${API_KEY}
    DELETE
    ...    ${Base_URL}api/users/${Id_Utilisateur}
    ...    headers=${headers}
    ...    expected_status=any
