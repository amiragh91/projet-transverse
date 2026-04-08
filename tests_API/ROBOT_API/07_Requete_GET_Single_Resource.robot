*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${Base_URL}       https://mock-api-h0g7.onrender.com/
${API_KEY}        Cle-API-ReqRes-test-academy
${Resource_Id}    2
${Name_Attendu}   fuchsia rose

*** Test Cases ***
Test Requete GET Single Resource
    &{headers}=       Create Dictionary    Authorization=Bearer ${API_KEY}
    ${Reponse}=       GET    ${Base_URL}api/unknown/${Resource_Id}    headers=${headers}    expected_status=200
    Log               ${Reponse.json()}
    
    ${data}=          Get From Dictionary    ${Reponse.json()}    data
    ${id}=            Get From Dictionary    ${data}    id
    Should Be Equal As Integers    ${id}    ${Resource_Id}
    
    ${name}=          Get From Dictionary    ${data}    name
    Should Be Equal As Strings    ${name}    ${Name_Attendu}
    
    Dictionary Should Contain Key    ${data}    year
    Dictionary Should Contain Key    ${data}    color
    Dictionary Should Contain Key    ${data}    pantone_value
