*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${Base_URL}    https://mock-api-h0g7.onrender.com/
${API_KEY}     Cle-API-ReqRes-test-academy
${User_Id}     2

*** Test Cases ***
Test Requete GET Single User
    &{headers}=       Create Dictionary    Authorization=Bearer ${API_KEY}
    ${Reponse}=       GET    ${Base_URL}api/users/${User_Id}    headers=${headers}    expected_status=200
    Log               ${Reponse.json()}
    
    ${data}=          Get From Dictionary    ${Reponse.json()}    data
    ${id}=            Get From Dictionary    ${data}    id
    Should Be Equal As Integers    ${id}    ${User_Id}
    
    Dictionary Should Contain Key    ${data}    email
    Dictionary Should Contain Key    ${data}    first_name
    Dictionary Should Contain Key    ${data}    last_name
    Dictionary Should Contain Key    ${data}    avatar
