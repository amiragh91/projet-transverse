*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${Base_URL}    https://mock-api-h0g7.onrender.com/
${API_KEY}     Cle-API-ReqRes-test-academy

*** Test Cases ***
Test Requete GET List Resources
    &{headers}=    Create Dictionary    Authorization=Bearer ${API_KEY}
    ${Reponse}=    GET    ${Base_URL}api/unknown    headers=${headers}    expected_status=200
    Log            ${Reponse.json()}
    
    Dictionary Should Contain Key    ${Reponse.json()}    page
    Dictionary Should Contain Key    ${Reponse.json()}    per_page
    Dictionary Should Contain Key    ${Reponse.json()}    total
    Dictionary Should Contain Key    ${Reponse.json()}    data
    
    ${data_list}=    Get From Dictionary    ${Reponse.json()}    data
    Should Not Be Empty    ${data_list}
