---
title: Vipps eCommerce API v1.0.10
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="vipps-ecommerce-api">Vipps eCommerce API v1.0.10</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

# Vipps eCommerce API
Additional API documentation: https://github.com/vippsas/vipps-ecom-api/

Base URLs:

* <a href="https://apitest.vipps.no">https://apitest.vipps.no</a>

* <a href="https://api.vipps.no">https://api.vipps.no</a>

<h1 id="vipps-ecommerce-api-vipps-ecom-api">Vipps eCom API</h1>

Functionality provided by the Vipps eCommerce API

## initiatePaymentV3UsingPOST

<a id="opIdinitiatePaymentV3UsingPOST"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://apitest.vipps.no/ecomm/v2/payments \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Accept: application/json;charset=UTF-8' \
  -H 'Authorization: [object Object]' \
  -H 'Content-Type: [object Object]' \
  -H 'Ocp-Apim-Subscription-Key: [object Object]'

```

```http
POST https://apitest.vipps.no/ecomm/v2/payments HTTP/1.1
Host: apitest.vipps.no
Content-Type: application/json;charset=UTF-8
Accept: application/json;charset=UTF-8
Authorization: [object Object]
Content-Type: [object Object]
Ocp-Apim-Subscription-Key: [object Object]

```

```javascript
const inputBody = '{
  "type": "object",
  "required": [
    "customerInfo",
    "merchantInfo",
    "transaction"
  ],
  "properties": {
    "customerInfo": {
      "type": "object",
      "properties": {
        "mobileNumber": {
          "type": "string",
          "description": "Mobile number of the user who has to pay for the transation from Vipps. Allowed format: xxxxxxxx",
          "minLength": 8,
          "maxLength": 8,
          "example": 91234567,
          "pattern": "^\\d{8}$"
        }
      }
    },
    "merchantInfo": {
      "type": "object",
      "required": [
        "callbackPrefix",
        "fallBack",
        "merchantSerialNumber"
      ],
      "properties": {
        "authToken": {
          "type": "string",
          "description": "Authorization token that the merchant could share to make callbacks more secure. If provided this token will be returned as an `Authorization` header for our callbacks. This includes shipping details and callback.",
          "maxLength": 255,
          "example": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1Ni"
        },
        "callbackPrefix": {
          "type": "string",
          "description": "This is an URL for receiving the callback after the payment request. Domain name and context path should be provided by merchant as the value for this parameter. Vipps will add `/v2/payments/{orderId}` to the end or this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.",
          "maxLength": 255,
          "example": "https://example.com/vipps/callbacks"
        },
        "consentRemovalPrefix": {
          "type": "string",
          "description": "Required for express checkout payments. This callback URL will be used by Vipps to inform the merchant that the user has revoked his/her consent: This Vipps user does do not want the merchant to store or use his/her personal information anymore. Required by GDPR. Vipps will add `/v2/consents/{userId}` to the end or this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.",
          "maxLength": 255,
          "example": "https://example.com/vipps"
        },
        "fallBack": {
          "type": "string",
          "description": "Vipps will use the fall back URL to redirect Merchant Page once Payment is completed in Vipps System URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html).",
          "maxLength": 255,
          "example": "https://example.com/vipps/fallback/order123abc"
        },
        "isApp": {
          "type": "boolean",
          "example": false,
          "default": false,
          "description": "This parameter indicates whether payment request is triggered from Mobile App or Web browser. Based on this value, response will be redirect URL for Vipps landing page or deeplink URL to connect vipps App. When isApp is set to true, URLs passed to Vipps will not be validated as regular URLs."
        },
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        },
        "paymentType": {
          "type": "string",
          "description": "This parameter will identify difference between a regular ecomm payment and ecomm express payment. For express checkout, use: \"eComm Express Payment\". Express checkouts require `consentRemovalPrefix`.",
          "enum": [
            "eComm Regular Payment",
            "eComm Express Payment"
          ],
          "example": "eComm Regular Payment",
          "default": "eComm Regular Payment"
        },
        "shippingDetailsPrefix": {
          "type": "string",
          "description": "In case of express checkout payment, merchant should pass this prefix to let Vipps fetch shipping cost and method related details. Vipps will add `/v2/payments/{orderId}/shippingDetails` to the end or this URL. We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.",
          "maxLength": 255,
          "example": "https://example.com/vipps/shipping/"
        },
        "staticShippingDetails": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "isDefault",
              "shippingCost",
              "shippingMethod",
              "shippingMethodId"
            ],
            "properties": {
              "isDefault": {
                "type": "string",
                "enum": [
                  "Y",
                  "N"
                ]
              },
              "priority": {
                "type": "integer",
                "format": "int32"
              },
              "shippingCost": {
                "type": "number",
                "format": "double"
              },
              "shippingMethod": {
                "type": "string",
                "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
                "example": "Posten Servicepakke",
                "maxLength": 256
              },
              "shippingMethodId": {
                "type": "string"
              }
            }
          },
          "description": "If shipping method and cost are always a fixed value, for example 50kr,  then the method and price can be provided during the initiate call. The shippingDetailsPrefix callback will not be used if this value is provided."
        }
      }
    },
    "transaction": {
      "type": "object",
      "required": [
        "amount",
        "orderId",
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "integer",
          "format": "int32",
          "description": "Amount in øre. 32 bit Integer (2147483647)",
          "pattern": "^\\d{3,}$",
          "example": 20000
        },
        "orderId": {
          "type": "string",
          "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
          "example": "order123abc",
          "pattern": "^[a-zA-Z0-9-]{1,30}$",
          "maxLength": 30
        },
        "timeStamp": {
          "type": "string",
          "format": "date-time",
          "description": "ISO formatted date time string.",
          "example": "2018-11-14T15:44:26.590Z"
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    }
  }
}';
const headers = {
  'Content-Type':'application/json;charset=UTF-8',
  'Accept':'application/json;charset=UTF-8',
  'Authorization':{
  "type": "string"
},
  'Content-Type':{
  "type": "string"
},
  'Ocp-Apim-Subscription-Key':{
  "type": "string"
}
};

fetch('https://apitest.vipps.no/ecomm/v2/payments',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json;charset=UTF-8',
  'Accept' => 'application/json;charset=UTF-8',
  'Authorization' => {
  "type": "string"
},
  'Content-Type' => {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key' => {
  "type": "string"
}
}

result = RestClient.post 'https://apitest.vipps.no/ecomm/v2/payments',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json;charset=UTF-8',
  'Accept': 'application/json;charset=UTF-8',
  'Authorization': {
  "type": "string"
},
  'Content-Type': {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key': {
  "type": "string"
}
}

r = requests.post('https://apitest.vipps.no/ecomm/v2/payments', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json;charset=UTF-8',
    'Accept' => 'application/json;charset=UTF-8',
    'Authorization' => '[object Object]',
    'Content-Type' => '[object Object]',
    'Ocp-Apim-Subscription-Key' => '[object Object]',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://apitest.vipps.no/ecomm/v2/payments', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://apitest.vipps.no/ecomm/v2/payments");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json;charset=UTF-8"},
        "Accept": []string{"application/json;charset=UTF-8"},
        "Authorization": []string{"[object Object]"},
        "Content-Type": []string{"[object Object]"},
        "Ocp-Apim-Subscription-Key": []string{"[object Object]"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://apitest.vipps.no/ecomm/v2/payments", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /ecomm/v2/payments`

*Initiate Payment*

This API call allows the merchants to initiate a payment flow by using Vipps. In order to identify which sales channel payments are coming from, a merchantSerialNumber is used to distinguish between them. Please note that a single payment is uniquely identified by a composite of merchantSerialNumber and orderId. The Merchant provided orderId must be unique per sales channel. Once the transaction is successfully initiated in Vipps, you will receive a URL in response which will direct the customer to the landing page. The landing page will have functionality to identify and differentiate request coming from mobile browser/desktop browser. The merchant may also pass the 'isApp' parameter that will make Vipps respond with a app-switch deeplink that will take the customer directly to the Vipps app. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html).

> Body parameter

```json
{
  "type": "object",
  "required": [
    "customerInfo",
    "merchantInfo",
    "transaction"
  ],
  "properties": {
    "customerInfo": {
      "type": "object",
      "properties": {
        "mobileNumber": {
          "type": "string",
          "description": "Mobile number of the user who has to pay for the transation from Vipps. Allowed format: xxxxxxxx",
          "minLength": 8,
          "maxLength": 8,
          "example": 91234567,
          "pattern": "^\\d{8}$"
        }
      }
    },
    "merchantInfo": {
      "type": "object",
      "required": [
        "callbackPrefix",
        "fallBack",
        "merchantSerialNumber"
      ],
      "properties": {
        "authToken": {
          "type": "string",
          "description": "Authorization token that the merchant could share to make callbacks more secure. If provided this token will be returned as an `Authorization` header for our callbacks. This includes shipping details and callback.",
          "maxLength": 255,
          "example": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1Ni"
        },
        "callbackPrefix": {
          "type": "string",
          "description": "This is an URL for receiving the callback after the payment request. Domain name and context path should be provided by merchant as the value for this parameter. Vipps will add `/v2/payments/{orderId}` to the end or this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.",
          "maxLength": 255,
          "example": "https://example.com/vipps/callbacks"
        },
        "consentRemovalPrefix": {
          "type": "string",
          "description": "Required for express checkout payments. This callback URL will be used by Vipps to inform the merchant that the user has revoked his/her consent: This Vipps user does do not want the merchant to store or use his/her personal information anymore. Required by GDPR. Vipps will add `/v2/consents/{userId}` to the end or this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.",
          "maxLength": 255,
          "example": "https://example.com/vipps"
        },
        "fallBack": {
          "type": "string",
          "description": "Vipps will use the fall back URL to redirect Merchant Page once Payment is completed in Vipps System URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html).",
          "maxLength": 255,
          "example": "https://example.com/vipps/fallback/order123abc"
        },
        "isApp": {
          "type": "boolean",
          "example": false,
          "default": false,
          "description": "This parameter indicates whether payment request is triggered from Mobile App or Web browser. Based on this value, response will be redirect URL for Vipps landing page or deeplink URL to connect vipps App. When isApp is set to true, URLs passed to Vipps will not be validated as regular URLs."
        },
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        },
        "paymentType": {
          "type": "string",
          "description": "This parameter will identify difference between a regular ecomm payment and ecomm express payment. For express checkout, use: \"eComm Express Payment\". Express checkouts require `consentRemovalPrefix`.",
          "enum": [
            "eComm Regular Payment",
            "eComm Express Payment"
          ],
          "example": "eComm Regular Payment",
          "default": "eComm Regular Payment"
        },
        "shippingDetailsPrefix": {
          "type": "string",
          "description": "In case of express checkout payment, merchant should pass this prefix to let Vipps fetch shipping cost and method related details. Vipps will add `/v2/payments/{orderId}/shippingDetails` to the end or this URL. We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.",
          "maxLength": 255,
          "example": "https://example.com/vipps/shipping/"
        },
        "staticShippingDetails": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "isDefault",
              "shippingCost",
              "shippingMethod",
              "shippingMethodId"
            ],
            "properties": {
              "isDefault": {
                "type": "string",
                "enum": [
                  "Y",
                  "N"
                ]
              },
              "priority": {
                "type": "integer",
                "format": "int32"
              },
              "shippingCost": {
                "type": "number",
                "format": "double"
              },
              "shippingMethod": {
                "type": "string",
                "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
                "example": "Posten Servicepakke",
                "maxLength": 256
              },
              "shippingMethodId": {
                "type": "string"
              }
            }
          },
          "description": "If shipping method and cost are always a fixed value, for example 50kr,  then the method and price can be provided during the initiate call. The shippingDetailsPrefix callback will not be used if this value is provided."
        }
      }
    },
    "transaction": {
      "type": "object",
      "required": [
        "amount",
        "orderId",
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "integer",
          "format": "int32",
          "description": "Amount in øre. 32 bit Integer (2147483647)",
          "pattern": "^\\d{3,}$",
          "example": 20000
        },
        "orderId": {
          "type": "string",
          "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
          "example": "order123abc",
          "pattern": "^[a-zA-Z0-9-]{1,30}$",
          "maxLength": 30
        },
        "timeStamp": {
          "type": "string",
          "format": "date-time",
          "description": "ISO formatted date time string.",
          "example": "2018-11-14T15:44:26.590Z"
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    }
  }
}
```

<h3 id="initiatepaymentv3usingpost-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|Authorization-token is obtained by appending the access_token obtained by using the /accesstoken/get request to 'Bearer '.|
|Content-Type|header|string|true|application/json|
|Ocp-Apim-Subscription-Key|header|string|true|The subscription-key for your product is located in the [developer portal](https://apitest-portal.vipps.no/). Click the username to the right on the page and select ```Profile``` from the dropdown. Find the relevant salesunit and copy the primary key.  See the [getting started guide](https://github.com/vippsas/vipps-developers/blob/master/vipps-developer-portal-getting-started.md) for full guide with images.|
|body|body|[InitiatePaymentCommand](#schemainitiatepaymentcommand)|true|initiatePaymentCommand|
|» customerInfo|body|[CustomerInfoDto](#schemacustomerinfodto)|true|none|
|»» mobileNumber|body|string|false|Mobile number of the user who has to pay for the transation from Vipps. Allowed format: xxxxxxxx|
|» merchantInfo|body|[MerchantInfoDto](#schemamerchantinfodto)|true|none|
|»» authToken|body|string|false|Authorization token that the merchant could share to make callbacks more secure. If provided this token will be returned as an `Authorization` header for our callbacks. This includes shipping details and callback.|
|»» callbackPrefix|body|string|true|This is an URL for receiving the callback after the payment request. Domain name and context path should be provided by merchant as the value for this parameter. Vipps will add `/v2/payments/{orderId}` to the end or this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.|
|»» consentRemovalPrefix|body|string|false|Required for express checkout payments. This callback URL will be used by Vipps to inform the merchant that the user has revoked his/her consent: This Vipps user does do not want the merchant to store or use his/her personal information anymore. Required by GDPR. Vipps will add `/v2/consents/{userId}` to the end or this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.|
|»» fallBack|body|string|true|Vipps will use the fall back URL to redirect Merchant Page once Payment is completed in Vipps System URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html).|
|»» isApp|body|boolean|false|This parameter indicates whether payment request is triggered from Mobile App or Web browser. Based on this value, response will be redirect URL for Vipps landing page or deeplink URL to connect vipps App. When isApp is set to true, URLs passed to Vipps will not be validated as regular URLs.|
|»» merchantSerialNumber|body|string|true|Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.|
|»» paymentType|body|string|false|This parameter will identify difference between a regular ecomm payment and ecomm express payment. For express checkout, use: "eComm Express Payment". Express checkouts require `consentRemovalPrefix`.|
|»» shippingDetailsPrefix|body|string|false|In case of express checkout payment, merchant should pass this prefix to let Vipps fetch shipping cost and method related details. Vipps will add `/v2/payments/{orderId}/shippingDetails` to the end or this URL. We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.|
|»» staticShippingDetails|body|[[ShippingDetails](#schemashippingdetails)]|false|If shipping method and cost are always a fixed value, for example 50kr,  then the method and price can be provided during the initiate call. The shippingDetailsPrefix callback will not be used if this value is provided.|
|»»» isDefault|body|string|true|none|
|»»» priority|body|integer(int32)|false|none|
|»»» shippingCost|body|number(double)|true|none|
|»»» shippingMethod|body|string|true|Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.|
|»»» shippingMethodId|body|string|true|none|
|» transaction|body|[TransactionInfoInitiateDTO](#schematransactioninfoinitiatedto)|true|none|
|»» amount|body|integer(int32)|true|Amount in øre. 32 bit Integer (2147483647)|
|»» orderId|body|string|true|Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.|
|»» timeStamp|body|string(date-time)|false|ISO formatted date time string.|
|»» transactionText|body|string|true|Transaction text to be displayed in Vipps|

#### Enumerated Values

|Parameter|Value|
|---|---|
|»» paymentType|eComm Regular Payment|
|»» paymentType|eComm Express Payment|
|»»» isDefault|Y|
|»»» isDefault|N|

> Example responses

> 200 Response

```json
{
  "type": "object",
  "required": [
    "orderId",
    "url"
  ],
  "properties": {
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "url": {
      "type": "string",
      "description": "URL to redirect the user to Vipps landing page or a deeplink URL to open Vipps app, if isApp was set as true. The landing page will also redirect a user to the app if the user is using a mobile browser. This link will timeout after 5 minutes.",
      "example": "https://example.com"
    }
  }
}
```

<h3 id="initiatepaymentv3usingpost-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Response for Initiate Payment|[InitiatePaymentV2Representation](#schemainitiatepaymentv2representation)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request (Missing a required parameter or bad request format)|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|402|[Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2)|Payment Failed|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Request Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|None|
|405|[Method Not Allowed](https://tools.ietf.org/html/rfc7231#section-6.5.5)|Request method not supported|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Unsupported media type|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Something went wrong from Vipps Server side|None|

### Callbacks

#### callbackExpress

**{$request.body#/merchantInfo/callbackPrefix}/v2/payments/{$request.body#/transaction/orderId}**

## initiatePaymentV3UsingPOST

<a id="opIdInitiatePaymentTransactionUpdateCallbackForRegularPaymentUsingPOSTExpress"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://apitest.vipps.no/ecomm/v2/payments \
  -H 'Content-Type: application/json;charset=UTF-8'

```

```http
POST https://apitest.vipps.no/ecomm/v2/payments HTTP/1.1
Host: apitest.vipps.no
Content-Type: application/json;charset=UTF-8

```

```javascript
const inputBody = '{
  "type": "object",
  "required": [
    "merchantSerialNumber",
    "orderId",
    "shippingDetails",
    "userDetails",
    "transactionInfo"
  ],
  "properties": {
    "merchantSerialNumber": {
      "type": "string",
      "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
      "minLength": 6,
      "maxLength": 6,
      "example": 123456,
      "pattern": "^\\d{6}$"
    },
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "shippingDetails": {
      "type": "object",
      "required": [
        "address",
        "shippingCost",
        "shippingMethod",
        "shippingMethodId"
      ],
      "properties": {
        "address": {
          "type": "object",
          "required": [
            "addressLine1",
            "city",
            "country",
            "postCode"
          ],
          "properties": {
            "addressLine1": {
              "type": "string",
              "description": "Address Line 1",
              "example": "Dronning Eufemias gate 42"
            },
            "addressLine2": {
              "type": "string",
              "description": "Address Line 2",
              "example": "Att: Rune Garborg"
            },
            "city": {
              "type": "string",
              "description": "City",
              "example": "Oslo"
            },
            "country": {
              "type": "string",
              "description": "Country",
              "example": "Norway",
              "enum": [
                "Norway"
              ]
            },
            "postCode": {
              "type": "string",
              "description": "Post Code",
              "example": 191
            }
          }
        },
        "shippingCost": {
          "type": "number",
          "format": "double",
          "description": "Shipping cost"
        },
        "shippingMethod": {
          "type": "string",
          "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
          "example": "Posten Servicepakke",
          "maxLength": 256
        },
        "shippingMethodId": {
          "type": "string"
        }
      }
    },
    "transactionInfo": {
      "type": "object",
      "required": [
        "amount",
        "status",
        "timeStamp",
        "transactionId"
      ],
      "properties": {
        "amount": {
          "type": "number",
          "format": "double",
          "description": "Ordered amount in øre",
          "example": 20000
        },
        "status": {
          "type": "string",
          "enum": [
            "RESERVE",
            "SALE",
            "CANCELLED",
            "REJECTED",
            "AUTO_CANCEL"
          ],
          "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#callbacks) for more information.",
          "example": "RESERVE"
        },
        "timeStamp": {
          "type": "string",
          "description": "Timestamp in ISO-8601 representing when the operation was performed.",
          "example": "2018-12-12T11:18:38.246Z"
        },
        "transactionId": {
          "type": "string",
          "description": "Vipps transaction id",
          "example": "5001420062"
        }
      }
    },
    "userDetails": {
      "type": "object",
      "required": [
        "email",
        "firstName",
        "lastName",
        "mobileNumber",
        "userId"
      ],
      "properties": {
        "bankIdVerified": {
          "type": "string",
          "description": "Optional Y/N string indicating if the user in bankId vertified, must be requested during onboarding.",
          "example": "Y",
          "enum": [
            "Y",
            "N"
          ]
        },
        "dateOfBirth": {
          "type": "string",
          "description": "Optional date of birth infomation, must be requested during onboarding.",
          "example": "12-3-1988"
        },
        "email": {
          "type": "string",
          "description": "Email address",
          "example": "user@example.com"
        },
        "firstName": {
          "type": "string",
          "description": "First name",
          "example": "Ada"
        },
        "lastName": {
          "type": "string",
          "description": "Last name",
          "example": "Lovelace"
        },
        "mobileNumber": {
          "type": "string",
          "description": "Mobile number",
          "example": "12345678",
          "minLength": 8,
          "maxLength": 12,
          "pattern": "^\\d{8,12}$"
        },
        "ssn": {
          "type": "string",
          "description": "Optional social security number for the user, must be requested during onboarding.",
          "example": "12345678901",
          "minLength": 11,
          "maxLength": 11,
          "pattern": "^\\d{11}$"
        },
        "userId": {
          "type": "string",
          "example": "uiJskNQ6qNN1iwN891uuob==",
          "maxLength": 50,
          "description": "Identifies a user in Vipps. Merchant is required to store this field for future references.",
          "pattern": "^[\\d\\w\\/=+]+$"
        }
      }
    },
    "errorInfo": {
      "type": "object",
      "properties": {
        "errorCode": {
          "type": "integer",
          "example": 45,
          "description": "The number code for the error."
        },
        "errorGroup": {
          "type": "string",
          "example": "PAYMENTS"
        },
        "errorMessage": {
          "type": "string",
          "description": "Description of the error",
          "example": "User has cancelled or not acted upon the payment"
        }
      }
    }
  }
}';
const headers = {
  'Content-Type':'application/json;charset=UTF-8'
};

fetch('https://apitest.vipps.no/ecomm/v2/payments',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json;charset=UTF-8'
}

result = RestClient.post 'https://apitest.vipps.no/ecomm/v2/payments',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json;charset=UTF-8'
}

r = requests.post('https://apitest.vipps.no/ecomm/v2/payments', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json;charset=UTF-8',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://apitest.vipps.no/ecomm/v2/payments', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://apitest.vipps.no/ecomm/v2/payments");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json;charset=UTF-8"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://apitest.vipps.no/ecomm/v2/payments", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /ecomm/v2/payments`

*Callback : Transaction Update*

This API call allows Vipps to send the transaction details. During regular ecomm payment order and transaction details will be shared. During express checkout payment it will provide user details and shipping details addition to the order and transaction details. Vipps will add `/v2/payments/{orderId}` to the end of this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.

> Body parameter

```json
{
  "type": "object",
  "required": [
    "merchantSerialNumber",
    "orderId",
    "shippingDetails",
    "userDetails",
    "transactionInfo"
  ],
  "properties": {
    "merchantSerialNumber": {
      "type": "string",
      "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
      "minLength": 6,
      "maxLength": 6,
      "example": 123456,
      "pattern": "^\\d{6}$"
    },
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "shippingDetails": {
      "type": "object",
      "required": [
        "address",
        "shippingCost",
        "shippingMethod",
        "shippingMethodId"
      ],
      "properties": {
        "address": {
          "type": "object",
          "required": [
            "addressLine1",
            "city",
            "country",
            "postCode"
          ],
          "properties": {
            "addressLine1": {
              "type": "string",
              "description": "Address Line 1",
              "example": "Dronning Eufemias gate 42"
            },
            "addressLine2": {
              "type": "string",
              "description": "Address Line 2",
              "example": "Att: Rune Garborg"
            },
            "city": {
              "type": "string",
              "description": "City",
              "example": "Oslo"
            },
            "country": {
              "type": "string",
              "description": "Country",
              "example": "Norway",
              "enum": [
                "Norway"
              ]
            },
            "postCode": {
              "type": "string",
              "description": "Post Code",
              "example": 191
            }
          }
        },
        "shippingCost": {
          "type": "number",
          "format": "double",
          "description": "Shipping cost"
        },
        "shippingMethod": {
          "type": "string",
          "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
          "example": "Posten Servicepakke",
          "maxLength": 256
        },
        "shippingMethodId": {
          "type": "string"
        }
      }
    },
    "transactionInfo": {
      "type": "object",
      "required": [
        "amount",
        "status",
        "timeStamp",
        "transactionId"
      ],
      "properties": {
        "amount": {
          "type": "number",
          "format": "double",
          "description": "Ordered amount in øre",
          "example": 20000
        },
        "status": {
          "type": "string",
          "enum": [
            "RESERVE",
            "SALE",
            "CANCELLED",
            "REJECTED",
            "AUTO_CANCEL"
          ],
          "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#callbacks) for more information.",
          "example": "RESERVE"
        },
        "timeStamp": {
          "type": "string",
          "description": "Timestamp in ISO-8601 representing when the operation was performed.",
          "example": "2018-12-12T11:18:38.246Z"
        },
        "transactionId": {
          "type": "string",
          "description": "Vipps transaction id",
          "example": "5001420062"
        }
      }
    },
    "userDetails": {
      "type": "object",
      "required": [
        "email",
        "firstName",
        "lastName",
        "mobileNumber",
        "userId"
      ],
      "properties": {
        "bankIdVerified": {
          "type": "string",
          "description": "Optional Y/N string indicating if the user in bankId vertified, must be requested during onboarding.",
          "example": "Y",
          "enum": [
            "Y",
            "N"
          ]
        },
        "dateOfBirth": {
          "type": "string",
          "description": "Optional date of birth infomation, must be requested during onboarding.",
          "example": "12-3-1988"
        },
        "email": {
          "type": "string",
          "description": "Email address",
          "example": "user@example.com"
        },
        "firstName": {
          "type": "string",
          "description": "First name",
          "example": "Ada"
        },
        "lastName": {
          "type": "string",
          "description": "Last name",
          "example": "Lovelace"
        },
        "mobileNumber": {
          "type": "string",
          "description": "Mobile number",
          "example": "12345678",
          "minLength": 8,
          "maxLength": 12,
          "pattern": "^\\d{8,12}$"
        },
        "ssn": {
          "type": "string",
          "description": "Optional social security number for the user, must be requested during onboarding.",
          "example": "12345678901",
          "minLength": 11,
          "maxLength": 11,
          "pattern": "^\\d{11}$"
        },
        "userId": {
          "type": "string",
          "example": "uiJskNQ6qNN1iwN891uuob==",
          "maxLength": 50,
          "description": "Identifies a user in Vipps. Merchant is required to store this field for future references.",
          "pattern": "^[\\d\\w\\/=+]+$"
        }
      }
    },
    "errorInfo": {
      "type": "object",
      "properties": {
        "errorCode": {
          "type": "integer",
          "example": 45,
          "description": "The number code for the error."
        },
        "errorGroup": {
          "type": "string",
          "example": "PAYMENTS"
        },
        "errorMessage": {
          "type": "string",
          "description": "Description of the error",
          "example": "User has cancelled or not acted upon the payment"
        }
      }
    }
  }
}
```

<h3 id="initiatepaymentv3usingpost-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|orderId|path|string|true|orderId|
|body|body|[ExpressCheckOutPaymentRequest](#schemaexpresscheckoutpaymentrequest)|false|none|
|» merchantSerialNumber|body|string|true|Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.|
|» orderId|body|string|true|Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.|
|» shippingDetails|body|[ShippingDetailsRequest](#schemashippingdetailsrequest)|true|none|
|»» address|body|[Address](#schemaaddress)|true|none|
|»»» addressLine1|body|string|true|Address Line 1|
|»»» addressLine2|body|string|false|Address Line 2|
|»»» city|body|string|true|City|
|»»» country|body|string|true|Country|
|»»» postCode|body|string|true|Post Code|
|»» shippingCost|body|number(double)|true|Shipping cost|
|»» shippingMethod|body|string|true|Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.|
|»» shippingMethodId|body|string|true|none|
|» transactionInfo|body|[CallbackTransactionInfoStatus](#schemacallbacktransactioninfostatus)|true|none|
|»» amount|body|number(double)|true|Ordered amount in øre|
|»» status|body|string|true|Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#callbacks) for more information.|
|»» timeStamp|body|string|true|Timestamp in ISO-8601 representing when the operation was performed.|
|»» transactionId|body|string|true|Vipps transaction id|
|» userDetails|body|[UserDetails](#schemauserdetails)|true|none|
|»» bankIdVerified|body|string|false|Optional Y/N string indicating if the user in bankId vertified, must be requested during onboarding.|
|»» dateOfBirth|body|string|false|Optional date of birth infomation, must be requested during onboarding.|
|»» email|body|string|true|Email address|
|»» firstName|body|string|true|First name|
|»» lastName|body|string|true|Last name|
|»» mobileNumber|body|string|true|Mobile number|
|»» ssn|body|string|false|Optional social security number for the user, must be requested during onboarding.|
|»» userId|body|string|true|Identifies a user in Vipps. Merchant is required to store this field for future references.|
|» errorInfo|body|[callbackErrorInfo](#schemacallbackerrorinfo)|false|none|
|»» errorCode|body|integer|false|The number code for the error.|
|»» errorGroup|body|string|false|none|
|»» errorMessage|body|string|false|Description of the error|

#### Enumerated Values

|Parameter|Value|
|---|---|
|»»» country|Norway|
|»» status|RESERVE|
|»» status|SALE|
|»» status|CANCELLED|
|»» status|REJECTED|
|»» status|AUTO_CANCEL|
|»» bankIdVerified|Y|
|»» bankIdVerified|N|

<h3 id="initiatepaymentv3usingpost-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Vipps does not require a response for this request.|None|

<aside class="success">
This operation does not require authentication
</aside>

#### callbackRegular

#### consentRemoval

#### shippingDetails

<aside class="success">
This operation does not require authentication
</aside>

## capturePaymentUsingPOST

<a id="opIdcapturePaymentUsingPOST"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://apitest.vipps.no/ecomm/v2/payments/{orderId}/capture \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Accept: application/json;charset=UTF-8' \
  -H 'Authorization: [object Object]' \
  -H 'Content-Type: [object Object]' \
  -H 'Ocp-Apim-Subscription-Key: [object Object]' \
  -H 'X-Request-Id: [object Object]'

```

```http
POST https://apitest.vipps.no/ecomm/v2/payments/{orderId}/capture HTTP/1.1
Host: apitest.vipps.no
Content-Type: application/json;charset=UTF-8
Accept: application/json;charset=UTF-8
Authorization: [object Object]
Content-Type: [object Object]
Ocp-Apim-Subscription-Key: [object Object]
X-Request-Id: [object Object]

```

```javascript
const inputBody = '{
  "type": "object",
  "properties": {
    "merchantInfo": {
      "type": "object",
      "required": [
        "merchantSerialNumber"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        }
      }
    },
    "transaction": {
      "type": "object",
      "required": [
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "integer",
          "format": "int32",
          "description": "Amount in øre, if amount is 0 or not provided then full capture will be performed. 32 Bit Integer (2147483647)",
          "pattern": "^\\d{3,}$",
          "example": 20000
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    }
  }
}';
const headers = {
  'Content-Type':'application/json;charset=UTF-8',
  'Accept':'application/json;charset=UTF-8',
  'Authorization':{
  "type": "string"
},
  'Content-Type':{
  "type": "string"
},
  'Ocp-Apim-Subscription-Key':{
  "type": "string"
},
  'X-Request-Id':{
  "type": "string"
}
};

fetch('https://apitest.vipps.no/ecomm/v2/payments/{orderId}/capture',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json;charset=UTF-8',
  'Accept' => 'application/json;charset=UTF-8',
  'Authorization' => {
  "type": "string"
},
  'Content-Type' => {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key' => {
  "type": "string"
},
  'X-Request-Id' => {
  "type": "string"
}
}

result = RestClient.post 'https://apitest.vipps.no/ecomm/v2/payments/{orderId}/capture',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json;charset=UTF-8',
  'Accept': 'application/json;charset=UTF-8',
  'Authorization': {
  "type": "string"
},
  'Content-Type': {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key': {
  "type": "string"
},
  'X-Request-Id': {
  "type": "string"
}
}

r = requests.post('https://apitest.vipps.no/ecomm/v2/payments/{orderId}/capture', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json;charset=UTF-8',
    'Accept' => 'application/json;charset=UTF-8',
    'Authorization' => '[object Object]',
    'Content-Type' => '[object Object]',
    'Ocp-Apim-Subscription-Key' => '[object Object]',
    'X-Request-Id' => '[object Object]',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://apitest.vipps.no/ecomm/v2/payments/{orderId}/capture', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://apitest.vipps.no/ecomm/v2/payments/{orderId}/capture");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json;charset=UTF-8"},
        "Accept": []string{"application/json;charset=UTF-8"},
        "Authorization": []string{"[object Object]"},
        "Content-Type": []string{"[object Object]"},
        "Ocp-Apim-Subscription-Key": []string{"[object Object]"},
        "X-Request-Id": []string{"[object Object]"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://apitest.vipps.no/ecomm/v2/payments/{orderId}/capture", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /ecomm/v2/payments/{orderId}/capture`

*Capture Payment *

This API call allows merchant to capture the reserved amount. Amount to capture cannot be higher than reserved. The API also allows capturing partial amount of the reserved amount. Partial capture can be called as many times as required so long there is reserved amount to capture. Transaction text is not optional and is used as a proof of delivery (tracking code, consignment number etc.). In a case of direct capture, both fund reservation and capture are executed in a single operation.

> Body parameter

```json
{
  "type": "object",
  "properties": {
    "merchantInfo": {
      "type": "object",
      "required": [
        "merchantSerialNumber"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        }
      }
    },
    "transaction": {
      "type": "object",
      "required": [
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "integer",
          "format": "int32",
          "description": "Amount in øre, if amount is 0 or not provided then full capture will be performed. 32 Bit Integer (2147483647)",
          "pattern": "^\\d{3,}$",
          "example": 20000
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    }
  }
}
```

<h3 id="capturepaymentusingpost-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|orderId|path|string|true|Order id specified in the request body of initiate payment.|
|Authorization|header|string|true|Authorization-token is obtained by running the /accesstoken/get request.|
|Content-Type|header|string|true|`application/json`|
|Ocp-Apim-Subscription-Key|header|string|true|The subscription-key for your product is located in the [developer portal](https://apitest-portal.vipps.no/). Click the username to the right on the page and select ```Profile``` from the dropdown. Find the relevant salesunit and copy the primary key.  See the [getting started guide](https://github.com/vippsas/vipps-developers/blob/master/vipps-developer-portal-getting-started.md) for full guide with images.|
|X-Request-Id|header|string|false|Id used for making requests idempotent. Adding this ID will allow the merchant to retry requests without it making additional changes. Unique for orderId, merchantSerialNumber and endpoint. Max 30 characters.|
|body|body|[PaymentActionsRequest](#schemapaymentactionsrequest)|true|paymentActionsRequest|
|» merchantInfo|body|[MerchantInfoPayment](#schemamerchantinfopayment)|false|none|
|»» merchantSerialNumber|body|string|true|Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.|
|» transaction|body|[Transaction](#schematransaction)|false|none|
|»» amount|body|integer(int32)|false|Amount in øre, if amount is 0 or not provided then full capture will be performed. 32 Bit Integer (2147483647)|
|»» transactionText|body|string|true|Transaction text to be displayed in Vipps|

> Example responses

> 200 Response

```json
{
  "type": "object",
  "required": [
    "orderId"
  ],
  "properties": {
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "transactionInfo": {
      "type": "object",
      "required": [
        "amount",
        "status",
        "timeStamp",
        "transactionId",
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "number",
          "format": "double",
          "description": "Ordered amount in øre",
          "example": 20000
        },
        "status": {
          "type": "string",
          "enum": [
            "Captured"
          ],
          "example": "Captured",
          "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information."
        },
        "timeStamp": {
          "type": "string",
          "description": "Timestamp in ISO-8601 representing when the order was captured.",
          "example": "2018-12-12T11:18:38.246Z"
        },
        "transactionId": {
          "type": "string",
          "description": "Vipps transaction id",
          "example": "5001420062"
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    },
    "transactionSummary": {
      "type": "object",
      "required": [
        "capturedAmount",
        "refundedAmount",
        "remainingAmountToCapture",
        "remainingAmountToRefund"
      ],
      "properties": {
        "capturedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total amount captured",
          "example": 20000
        },
        "refundedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total refunded amount of the order",
          "example": 0
        },
        "remainingAmountToCapture": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to capture",
          "example": 0
        },
        "remainingAmountToRefund": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to refund",
          "example": 20000
        }
      }
    }
  }
}
```

<h3 id="capturepaymentusingpost-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Capture payment response|[TransactionResponseCapture](#schematransactionresponsecapture)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request (Missing a required parameter or bad request format)|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|402|[Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2)|Payment Failed|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Request Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|None|
|405|[Method Not Allowed](https://tools.ietf.org/html/rfc7231#section-6.5.5)|Request method not supported|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Unsupported media type|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Something went wrong from Vipps Server side|None|

<aside class="success">
This operation does not require authentication
</aside>

## cancelPaymentRequestUsingPUT

<a id="opIdcancelPaymentRequestUsingPUT"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT https://apitest.vipps.no/ecomm/v2/payments/{orderId}/cancel \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Accept: application/json;charset=UTF-8' \
  -H 'Authorization: [object Object]' \
  -H 'Content-Type: [object Object]' \
  -H 'Ocp-Apim-Subscription-Key: [object Object]'

```

```http
PUT https://apitest.vipps.no/ecomm/v2/payments/{orderId}/cancel HTTP/1.1
Host: apitest.vipps.no
Content-Type: application/json;charset=UTF-8
Accept: application/json;charset=UTF-8
Authorization: [object Object]
Content-Type: [object Object]
Ocp-Apim-Subscription-Key: [object Object]

```

```javascript
const inputBody = '{
  "type": "object",
  "properties": {
    "merchantInfo": {
      "type": "object",
      "required": [
        "merchantSerialNumber"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        }
      }
    },
    "transaction": {
      "type": "object",
      "properties": {
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    }
  }
}';
const headers = {
  'Content-Type':'application/json;charset=UTF-8',
  'Accept':'application/json;charset=UTF-8',
  'Authorization':{
  "type": "string"
},
  'Content-Type':{
  "type": "string"
},
  'Ocp-Apim-Subscription-Key':{
  "type": "string"
}
};

fetch('https://apitest.vipps.no/ecomm/v2/payments/{orderId}/cancel',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json;charset=UTF-8',
  'Accept' => 'application/json;charset=UTF-8',
  'Authorization' => {
  "type": "string"
},
  'Content-Type' => {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key' => {
  "type": "string"
}
}

result = RestClient.put 'https://apitest.vipps.no/ecomm/v2/payments/{orderId}/cancel',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json;charset=UTF-8',
  'Accept': 'application/json;charset=UTF-8',
  'Authorization': {
  "type": "string"
},
  'Content-Type': {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key': {
  "type": "string"
}
}

r = requests.put('https://apitest.vipps.no/ecomm/v2/payments/{orderId}/cancel', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json;charset=UTF-8',
    'Accept' => 'application/json;charset=UTF-8',
    'Authorization' => '[object Object]',
    'Content-Type' => '[object Object]',
    'Ocp-Apim-Subscription-Key' => '[object Object]',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','https://apitest.vipps.no/ecomm/v2/payments/{orderId}/cancel', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://apitest.vipps.no/ecomm/v2/payments/{orderId}/cancel");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json;charset=UTF-8"},
        "Accept": []string{"application/json;charset=UTF-8"},
        "Authorization": []string{"[object Object]"},
        "Content-Type": []string{"[object Object]"},
        "Ocp-Apim-Subscription-Key": []string{"[object Object]"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "https://apitest.vipps.no/ecomm/v2/payments/{orderId}/cancel", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /ecomm/v2/payments/{orderId}/cancel`

*Cancel Payment*

The API call allows merchant to cancel the reserved transaction, The API will not allow partial cancellation which has the consequence that partially captured transactions cannot be cancelled. Please note that in a case of communication errors during initiate payment service call between Vipps and PSP/Acquirer/Issuer; even in a case that customer has confirmed a payment, the payment will be cancelled by Vipps. Note this means you can not cancel a captured payment.

> Body parameter

```json
{
  "type": "object",
  "properties": {
    "merchantInfo": {
      "type": "object",
      "required": [
        "merchantSerialNumber"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        }
      }
    },
    "transaction": {
      "type": "object",
      "properties": {
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    }
  }
}
```

<h3 id="cancelpaymentrequestusingput-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|orderId|path|string|true|Order id specified in the request body of initiate payment.|
|Authorization|header|string|true|Authorization-token is obtained by running the /accesstoken/get request.|
|Content-Type|header|string|true|`application/json`|
|Ocp-Apim-Subscription-Key|header|string|true|The subscription-key for your product is located in the [developer portal](https://apitest-portal.vipps.no/). Click the username to the right on the page and select ```Profile``` from the dropdown. Find the relevant salesunit and copy the primary key.  See the [getting started guide](https://github.com/vippsas/vipps-developers/blob/master/vipps-developer-portal-getting-started.md) for full guide with images.|
|body|body|[CancelPaymentActionRequest](#schemacancelpaymentactionrequest)|true|paymentActionsRequest|
|» merchantInfo|body|[MerchantInfoPayment](#schemamerchantinfopayment)|false|none|
|»» merchantSerialNumber|body|string|true|Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.|
|» transaction|body|[CancelTransaction](#schemacanceltransaction)|false|none|
|»» transactionText|body|string|false|Transaction text to be displayed in Vipps|

> Example responses

> 200 Response

```json
{
  "type": "object",
  "required": [
    "orderId"
  ],
  "properties": {
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "transactionInfo": {
      "type": "object",
      "required": [
        "amount",
        "status",
        "timeStamp",
        "transactionId",
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "number",
          "format": "double",
          "description": "Ordered amount in øre",
          "example": 20000
        },
        "status": {
          "type": "string",
          "enum": [
            "Cancelled"
          ],
          "example": "Cancelled",
          "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information."
        },
        "timeStamp": {
          "type": "string",
          "description": "Timestamp in ISO-8601 representing when the order was cancelled.",
          "example": "2018-12-12T11:18:38.246Z"
        },
        "transactionId": {
          "type": "string",
          "description": "Vipps transaction id",
          "example": "5001420062"
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    },
    "transactionSummary": {
      "type": "object",
      "required": [
        "capturedAmount",
        "refundedAmount",
        "remainingAmountToCapture",
        "remainingAmountToRefund"
      ],
      "properties": {
        "capturedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total amount captured",
          "example": 20000
        },
        "refundedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total refunded amount of the order",
          "example": 0
        },
        "remainingAmountToCapture": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to capture",
          "example": 0
        },
        "remainingAmountToRefund": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to refund",
          "example": 20000
        }
      }
    }
  }
}
```

<h3 id="cancelpaymentrequestusingput-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Cancel payment response|[TransactionResponseCancel](#schematransactionresponsecancel)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request (Missing a required parameter or bad request format)|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|402|[Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2)|Payment Failed|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Request Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|None|
|405|[Method Not Allowed](https://tools.ietf.org/html/rfc7231#section-6.5.5)|Request method not supported|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Unsupported media type|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Something went wrong from Vipps Server side|None|

<aside class="success">
This operation does not require authentication
</aside>

## refundPaymentUsingPOST

<a id="opIdrefundPaymentUsingPOST"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://apitest.vipps.no/ecomm/v2/payments/{orderId}/refund \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Accept: application/json;charset=UTF-8' \
  -H 'Authorization: [object Object]' \
  -H 'Content-Type: [object Object]' \
  -H 'Ocp-Apim-Subscription-Key: [object Object]' \
  -H 'X-Request-Id: [object Object]'

```

```http
POST https://apitest.vipps.no/ecomm/v2/payments/{orderId}/refund HTTP/1.1
Host: apitest.vipps.no
Content-Type: application/json;charset=UTF-8
Accept: application/json;charset=UTF-8
Authorization: [object Object]
Content-Type: [object Object]
Ocp-Apim-Subscription-Key: [object Object]
X-Request-Id: [object Object]

```

```javascript
const inputBody = '{
  "type": "object",
  "properties": {
    "merchantInfo": {
      "type": "object",
      "required": [
        "merchantSerialNumber"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        }
      }
    },
    "transaction": {
      "type": "object",
      "required": [
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "integer",
          "format": "int32",
          "description": "Amount in øre, if amount is 0 or not provided then full capture will be performed. 32 Bit Integer (2147483647)",
          "pattern": "^\\d{3,}$",
          "example": 20000
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    }
  }
}';
const headers = {
  'Content-Type':'application/json;charset=UTF-8',
  'Accept':'application/json;charset=UTF-8',
  'Authorization':{
  "type": "string"
},
  'Content-Type':{
  "type": "string"
},
  'Ocp-Apim-Subscription-Key':{
  "type": "string"
},
  'X-Request-Id':{
  "type": "string"
}
};

fetch('https://apitest.vipps.no/ecomm/v2/payments/{orderId}/refund',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json;charset=UTF-8',
  'Accept' => 'application/json;charset=UTF-8',
  'Authorization' => {
  "type": "string"
},
  'Content-Type' => {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key' => {
  "type": "string"
},
  'X-Request-Id' => {
  "type": "string"
}
}

result = RestClient.post 'https://apitest.vipps.no/ecomm/v2/payments/{orderId}/refund',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json;charset=UTF-8',
  'Accept': 'application/json;charset=UTF-8',
  'Authorization': {
  "type": "string"
},
  'Content-Type': {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key': {
  "type": "string"
},
  'X-Request-Id': {
  "type": "string"
}
}

r = requests.post('https://apitest.vipps.no/ecomm/v2/payments/{orderId}/refund', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json;charset=UTF-8',
    'Accept' => 'application/json;charset=UTF-8',
    'Authorization' => '[object Object]',
    'Content-Type' => '[object Object]',
    'Ocp-Apim-Subscription-Key' => '[object Object]',
    'X-Request-Id' => '[object Object]',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://apitest.vipps.no/ecomm/v2/payments/{orderId}/refund', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://apitest.vipps.no/ecomm/v2/payments/{orderId}/refund");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json;charset=UTF-8"},
        "Accept": []string{"application/json;charset=UTF-8"},
        "Authorization": []string{"[object Object]"},
        "Content-Type": []string{"[object Object]"},
        "Ocp-Apim-Subscription-Key": []string{"[object Object]"},
        "X-Request-Id": []string{"[object Object]"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://apitest.vipps.no/ecomm/v2/payments/{orderId}/refund", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /ecomm/v2/payments/{orderId}/refund`

*Refund Payment *

The API allows a merchant to do a refund of already captured transaction. There is an option to do a partial refund of the captured amount. Refunded amount cannot be larger than captured. Timeframe for issuing a refund for a payment is 365 days from the date payment has been captured. If the refund payment service call is called after the refund timeframe, service call will respond with an error. Refunded funds will be transferred from the merchant account to the customer credit card that was used in payment flow. Pay attention that in order to perform refund, there must be enough funds at merchant settlements account.

> Body parameter

```json
{
  "type": "object",
  "properties": {
    "merchantInfo": {
      "type": "object",
      "required": [
        "merchantSerialNumber"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        }
      }
    },
    "transaction": {
      "type": "object",
      "required": [
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "integer",
          "format": "int32",
          "description": "Amount in øre, if amount is 0 or not provided then full capture will be performed. 32 Bit Integer (2147483647)",
          "pattern": "^\\d{3,}$",
          "example": 20000
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    }
  }
}
```

<h3 id="refundpaymentusingpost-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|orderId|path|string|true|Order id specified in the request body of initiate payment.|
|Authorization|header|string|true|Authorization-token is obtained by running the /accesstoken/get request.|
|Content-Type|header|string|true|`application/json`|
|Ocp-Apim-Subscription-Key|header|string|true|The subscription-key for your product is located in the [developer portal](https://apitest-portal.vipps.no/). Click the username to the right on the page and select ```Profile``` from the dropdown. Find the relevant salesunit and copy the primary key.  See the [getting started guide](https://github.com/vippsas/vipps-developers/blob/master/vipps-developer-portal-getting-started.md) for full guide with images.|
|X-Request-Id|header|string|false|Id used for making requests idempotent. Adding this ID will allow the merchant to retry requests without it making additional changes. Unique for orderId, merchantSerialNumber and endpoint. Max 30 characters.|
|body|body|[PaymentActionsRequest](#schemapaymentactionsrequest)|true|paymentActionsRequest|
|» merchantInfo|body|[MerchantInfoPayment](#schemamerchantinfopayment)|false|none|
|»» merchantSerialNumber|body|string|true|Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.|
|» transaction|body|[Transaction](#schematransaction)|false|none|
|»» amount|body|integer(int32)|false|Amount in øre, if amount is 0 or not provided then full capture will be performed. 32 Bit Integer (2147483647)|
|»» transactionText|body|string|true|Transaction text to be displayed in Vipps|

> Example responses

> 200 Response

```json
{
  "type": "object",
  "required": [
    "orderId"
  ],
  "properties": {
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "transaction": {
      "type": "object",
      "required": [
        "amount",
        "status",
        "timeStamp",
        "transactionId",
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "number",
          "format": "double",
          "description": "Ordered amount in øre",
          "example": 20000
        },
        "status": {
          "type": "string",
          "enum": [
            "Refund"
          ],
          "example": "Refund",
          "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information."
        },
        "timeStamp": {
          "type": "string",
          "description": "Timestamp in ISO-8601 representing when the order was refunded.",
          "example": "2018-12-12T11:18:38.246Z"
        },
        "transactionId": {
          "type": "string",
          "description": "Vipps transaction id",
          "example": "5001420062"
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    },
    "transactionSummary": {
      "type": "object",
      "required": [
        "capturedAmount",
        "refundedAmount",
        "remainingAmountToCapture",
        "remainingAmountToRefund"
      ],
      "properties": {
        "capturedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total amount captured",
          "example": 20000
        },
        "refundedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total refunded amount of the order",
          "example": 0
        },
        "remainingAmountToCapture": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to capture",
          "example": 0
        },
        "remainingAmountToRefund": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to refund",
          "example": 20000
        }
      }
    }
  }
}
```

<h3 id="refundpaymentusingpost-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Refund payment response|[TransactionResponseRefund](#schematransactionresponserefund)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request (Missing a required parameter or bad request format)|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|402|[Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2)|Payment Failed|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Request Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|None|
|405|[Method Not Allowed](https://tools.ietf.org/html/rfc7231#section-6.5.5)|Request method not supported|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Unsupported media type|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Something went wrong from Vipps Server side|None|

<aside class="success">
This operation does not require authentication
</aside>

## getPaymentDetailsUsingGET

<a id="opIdgetPaymentDetailsUsingGET"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://apitest.vipps.no/ecomm/v2/payments/{orderId}/details \
  -H 'Accept: application/json;charset=UTF-8' \
  -H 'Authorization: [object Object]' \
  -H 'Content-Type: [object Object]' \
  -H 'Ocp-Apim-Subscription-Key: [object Object]'

```

```http
GET https://apitest.vipps.no/ecomm/v2/payments/{orderId}/details HTTP/1.1
Host: apitest.vipps.no
Accept: application/json;charset=UTF-8
Authorization: [object Object]
Content-Type: [object Object]
Ocp-Apim-Subscription-Key: [object Object]

```

```javascript

const headers = {
  'Accept':'application/json;charset=UTF-8',
  'Authorization':{
  "type": "string"
},
  'Content-Type':{
  "type": "string"
},
  'Ocp-Apim-Subscription-Key':{
  "type": "string"
}
};

fetch('https://apitest.vipps.no/ecomm/v2/payments/{orderId}/details',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json;charset=UTF-8',
  'Authorization' => {
  "type": "string"
},
  'Content-Type' => {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key' => {
  "type": "string"
}
}

result = RestClient.get 'https://apitest.vipps.no/ecomm/v2/payments/{orderId}/details',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json;charset=UTF-8',
  'Authorization': {
  "type": "string"
},
  'Content-Type': {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key': {
  "type": "string"
}
}

r = requests.get('https://apitest.vipps.no/ecomm/v2/payments/{orderId}/details', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json;charset=UTF-8',
    'Authorization' => '[object Object]',
    'Content-Type' => '[object Object]',
    'Ocp-Apim-Subscription-Key' => '[object Object]',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://apitest.vipps.no/ecomm/v2/payments/{orderId}/details', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://apitest.vipps.no/ecomm/v2/payments/{orderId}/details");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json;charset=UTF-8"},
        "Authorization": []string{"[object Object]"},
        "Content-Type": []string{"[object Object]"},
        "Ocp-Apim-Subscription-Key": []string{"[object Object]"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://apitest.vipps.no/ecomm/v2/payments/{orderId}/details", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /ecomm/v2/payments/{orderId}/details`

*Get payment Details*

This API call allows merchant to get the details of a payment transaction. Service call returns detailed transaction history of given payment where events are sorted from newest to oldest for when the transaction occurred.

<h3 id="getpaymentdetailsusingget-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|orderId|path|string|true|Order id specified in the request body of initiate payment.|
|Authorization|header|string|true|Authorization-token is obtained by running the `/accesstoken/get` request.|
|Content-Type|header|string|true|`application/json`|
|Ocp-Apim-Subscription-Key|header|string|true|The subscription-key for your product is located in the [developer portal](https://apitest-portal.vipps.no/). Click the username to the right on the page and select ```Profile``` from the dropdown. Find the relevant salesunit and copy the primary key.  See the [getting started guide](https://github.com/vippsas/vipps-developers/blob/master/vipps-developer-portal-getting-started.md) for full guide with images.|

> Example responses

> 200 Response

```json
{
  "type": "object",
  "properties": {
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "shippingDetails": {
      "type": "object",
      "required": [
        "shippingCost",
        "shippingMethod",
        "shippingMethodId"
      ],
      "properties": {
        "address": {
          "type": "object",
          "required": [
            "addressLine1",
            "city",
            "country",
            "postCode"
          ],
          "properties": {
            "addressLine1": {
              "type": "string",
              "description": "Address Line 1",
              "example": "Dronning Eufemias gate 42"
            },
            "addressLine2": {
              "type": "string",
              "description": "Address Line 2",
              "example": "Att: Rune Garborg"
            },
            "city": {
              "type": "string",
              "description": "City",
              "example": "Oslo"
            },
            "country": {
              "type": "string",
              "description": "Country",
              "example": "Norway",
              "enum": [
                "Norway"
              ]
            },
            "postCode": {
              "type": "string",
              "description": "Post Code",
              "example": 191
            }
          }
        },
        "shippingCost": {
          "type": "number",
          "format": "double",
          "description": "Shipping Cost",
          "example": 1500
        },
        "shippingMethod": {
          "type": "string",
          "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
          "example": "Posten Servicepakke",
          "maxLength": 256
        },
        "shippingMethodId": {
          "type": "string"
        }
      }
    },
    "transactionLogHistory": {
      "type": "array",
      "description": "Array of transaction operations. Sorted from newest to oldest.",
      "items": {
        "type": "object",
        "required": [
          "operation",
          "amount",
          "operationSuccess",
          "transactionText"
        ],
        "properties": {
          "amount": {
            "type": "integer",
            "format": "int32"
          },
          "operation": {
            "type": "string",
            "example": "RESERVE",
            "description": "The operation that was performed for this log entry. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information.",
            "enum": [
              "INITIATE",
              "RESERVE",
              "SALE",
              "CAPTURE",
              "REFUND",
              "CANCEL",
              "VOID"
            ]
          },
          "operationf": {
            "type": "boolean",
            "description": "If the corrosponding operation was successfull.",
            "example": true
          },
          "requestId": {
            "description": "The idempotent request id provided by the merchant for the operation.",
            "example": 12983921873981899000,
            "type": "string"
          },
          "timeStamp": {
            "type": "string",
            "description": "Timestamp in ISO-8601 representing when the operation was perfomed.",
            "example": "2019-02-05T12:27:42.311Z"
          },
          "transactionId": {
            "description": "Identifies the transaction",
            "example": 5001446662,
            "type": "string"
          },
          "transactionText": {
            "type": "string",
            "description": "Transaction text to be displayed in Vipps",
            "example": "One pair of Vipps socks",
            "maxLength": 100
          }
        }
      }
    },
    "transactionSummary": {
      "type": "object",
      "required": [
        "capturedAmount",
        "refundedAmount",
        "remainingAmountToCapture",
        "remainingAmountToRefund"
      ],
      "properties": {
        "capturedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total amount captured",
          "example": 20000
        },
        "refundedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total refunded amount of the order",
          "example": 0
        },
        "remainingAmountToCapture": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to capture",
          "example": 0
        },
        "remainingAmountToRefund": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to refund",
          "example": 20000
        }
      }
    },
    "userDetails": {
      "type": "object",
      "required": [
        "email",
        "firstName",
        "lastName",
        "mobileNumber",
        "userId"
      ],
      "properties": {
        "bankIdVerified": {
          "type": "string",
          "description": "Optional Y/N string indicating if the user in bankId vertified, must be requested during onboarding.",
          "example": "Y",
          "enum": [
            "Y",
            "N"
          ]
        },
        "dateOfBirth": {
          "type": "string",
          "description": "Optional date of birth infomation, must be requested during onboarding.",
          "example": "12-3-1988"
        },
        "email": {
          "type": "string",
          "description": "Email address",
          "example": "user@example.com"
        },
        "firstName": {
          "type": "string",
          "description": "First name",
          "example": "Ada"
        },
        "lastName": {
          "type": "string",
          "description": "Last name",
          "example": "Lovelace"
        },
        "mobileNumber": {
          "type": "string",
          "description": "Mobile number",
          "example": "12345678",
          "minLength": 8,
          "maxLength": 12,
          "pattern": "^\\d{8,12}$"
        },
        "ssn": {
          "type": "string",
          "description": "Optional social security number for the user, must be requested during onboarding.",
          "example": "12345678901",
          "minLength": 11,
          "maxLength": 11,
          "pattern": "^\\d{11}$"
        },
        "userId": {
          "type": "string",
          "example": "uiJskNQ6qNN1iwN891uuob==",
          "maxLength": 50,
          "description": "Identifies a user in Vipps. Merchant is required to store this field for future references.",
          "pattern": "^[\\d\\w\\/=+]+$"
        }
      }
    }
  }
}
```

<h3 id="getpaymentdetailsusingget-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Get payment Details|[GetTransactionDetails](#schemagettransactiondetails)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request (Missing a required parameter or bad request format)|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|402|[Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2)|Payment Failed|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Request Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|None|
|405|[Method Not Allowed](https://tools.ietf.org/html/rfc7231#section-6.5.5)|Request method not supported|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Unsupported media type|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Something went wrong from Vipps Server side|None|

<aside class="success">
This operation does not require authentication
</aside>

## getOrderStatusUsingGET

<a id="opIdgetOrderStatusUsingGET"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://apitest.vipps.no/ecomm/v2/payments/{orderId}/status \
  -H 'Accept: application/json;charset=UTF-8' \
  -H 'Authorization: [object Object]' \
  -H 'Ocp-Apim-Subscription-Key: [object Object]'

```

```http
GET https://apitest.vipps.no/ecomm/v2/payments/{orderId}/status HTTP/1.1
Host: apitest.vipps.no
Accept: application/json;charset=UTF-8
Authorization: [object Object]
Ocp-Apim-Subscription-Key: [object Object]

```

```javascript

const headers = {
  'Accept':'application/json;charset=UTF-8',
  'Authorization':{
  "type": "string"
},
  'Ocp-Apim-Subscription-Key':{
  "type": "string"
}
};

fetch('https://apitest.vipps.no/ecomm/v2/payments/{orderId}/status',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json;charset=UTF-8',
  'Authorization' => {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key' => {
  "type": "string"
}
}

result = RestClient.get 'https://apitest.vipps.no/ecomm/v2/payments/{orderId}/status',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json;charset=UTF-8',
  'Authorization': {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key': {
  "type": "string"
}
}

r = requests.get('https://apitest.vipps.no/ecomm/v2/payments/{orderId}/status', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json;charset=UTF-8',
    'Authorization' => '[object Object]',
    'Ocp-Apim-Subscription-Key' => '[object Object]',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://apitest.vipps.no/ecomm/v2/payments/{orderId}/status', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://apitest.vipps.no/ecomm/v2/payments/{orderId}/status");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json;charset=UTF-8"},
        "Authorization": []string{"[object Object]"},
        "Ocp-Apim-Subscription-Key": []string{"[object Object]"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://apitest.vipps.no/ecomm/v2/payments/{orderId}/status", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /ecomm/v2/payments/{orderId}/status`

*Get order status*

This API call allows the merchant to get the status of the last payment transaction. Primarily use of this service is meant for inApp where simple response to check order status is preferred.

<h3 id="getorderstatususingget-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|orderId|path|string|true|Order id specified in the request body of initiate payment.|
|Authorization|header|string|true|Authorization-token is obtained by running the /accesstoken/get request.|
|Ocp-Apim-Subscription-Key|header|string|true|The subscription-key for your product is located in the [developer portal](https://apitest-portal.vipps.no/). Click the username to the right on the page and select ```Profile``` from the dropdown. Find the relevant salesunit and copy the primary key.  See the [getting started guide](https://github.com/vippsas/vipps-developers/blob/master/vipps-developer-portal-getting-started.md) for full guide with images.|

> Example responses

> 200 Response

```json
{
  "type": "object",
  "properties": {
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "transactionInfo": {
      "type": "object",
      "required": [
        "amount",
        "status",
        "timeStamp",
        "transactionId"
      ],
      "properties": {
        "amount": {
          "type": "number",
          "format": "double",
          "description": "Ordered amount in øre",
          "example": 20000
        },
        "status": {
          "type": "string",
          "enum": [
            "INITIATE",
            "REGISTER",
            "RESERVE",
            "SALE",
            "CAPTURE",
            "REFUND",
            "CANCEL",
            "VOID",
            "FAILED",
            "REJECTED"
          ],
          "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information.",
          "example": "RESERVE"
        },
        "timeStamp": {
          "type": "string",
          "description": "Timestamp in ISO-8601 representing when the status operation was performed.",
          "example": "2018-12-12T11:18:38.246Z"
        },
        "transactionId": {
          "type": "string",
          "description": "Vipps transaction id",
          "example": "5001420062"
        }
      }
    }
  }
}
```

<h3 id="getorderstatususingget-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Get order status|[GetPaymentStatusResponse](#schemagetpaymentstatusresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request (Missing a required parameter or bad request format)|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|402|[Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2)|Payment Failed|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Request Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|None|
|405|[Method Not Allowed](https://tools.ietf.org/html/rfc7231#section-6.5.5)|Request method not supported|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Unsupported media type|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Something went wrong from Vipps Server side|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="vipps-ecommerce-api-endpoints-required-by-vipps-from-the-merchant">Endpoints required by Vipps from the merchant</h1>

These endpoints must be implemented by the merchant, and are called by Vipps.

## removeUserConsentUsingDELETE

<a id="opIdremoveUserConsentUsingDELETE"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://apitest.vipps.no[consentRemovalPrefix]/v2/consents/{userId}

```

```http
DELETE https://apitest.vipps.no[consentRemovalPrefix]/v2/consents/{userId} HTTP/1.1
Host: apitest.vipps.no

```

```javascript

fetch('https://apitest.vipps.no[consentRemovalPrefix]/v2/consents/{userId}',
{
  method: 'DELETE'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.delete 'https://apitest.vipps.no[consentRemovalPrefix]/v2/consents/{userId}',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.delete('https://apitest.vipps.no[consentRemovalPrefix]/v2/consents/{userId}')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://apitest.vipps.no[consentRemovalPrefix]/v2/consents/{userId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://apitest.vipps.no[consentRemovalPrefix]/v2/consents/{userId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://apitest.vipps.no[consentRemovalPrefix]/v2/consents/{userId}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE [consentRemovalPrefix]/v2/consents/{userId}`

*Remove User Consent (for express checkout)*

This API endpoint on the merchant side allows Vipps to send consent removal requests to the merchant. When receiving requests the merchant is obliged to remove the user details permanently, as per the GDPR guidelines. Vipps will add `/v2/consents/{userId}` to the end of this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.

<h3 id="removeuserconsentusingdelete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|userId|path|string|true|URL encoded userId provided when requesting user information from Vipps. Received by callback or get detail request.|

<h3 id="removeuserconsentusingdelete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Remove User Consent (for express checkout)|None|

<aside class="success">
This operation does not require authentication
</aside>

## fetchShippingCostUsingPOST

<a id="opIdfetchShippingCostUsingPOST"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://apitest.vipps.no[shippingDetailsPrefix]/v2/payments/{orderId}/shippingDetails \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Accept: application/json;charset=UTF-8' \
  -H 'Authorization: [object Object]'

```

```http
POST https://apitest.vipps.no[shippingDetailsPrefix]/v2/payments/{orderId}/shippingDetails HTTP/1.1
Host: apitest.vipps.no
Content-Type: application/json;charset=UTF-8
Accept: application/json;charset=UTF-8
Authorization: [object Object]

```

```javascript
const inputBody = '{
  "type": "object",
  "required": [
    "addressId",
    "addressLine1",
    "city",
    "country",
    "postCode"
  ],
  "properties": {
    "addressId": {
      "type": "integer",
      "format": "int32",
      "description": "Vipps Provided address Id. To be returned in response in the same field"
    },
    "addressLine1": {
      "type": "string",
      "example": "Dronning Eufemias gate 42"
    },
    "addressLine2": {
      "type": "string"
    },
    "city": {
      "type": "string",
      "description": "City",
      "example": "Oslo"
    },
    "country": {
      "type": "string",
      "description": "The only country supported is Norway",
      "example": "NO"
    },
    "postCode": {
      "type": "string",
      "description": "Four digits",
      "pattern": "^\\d{4}$",
      "example": "0603"
    },
    "addressType": {
      "type": "string",
      "example": "H"
    }
  }
}';
const headers = {
  'Content-Type':'application/json;charset=UTF-8',
  'Accept':'application/json;charset=UTF-8',
  'Authorization':{
  "type": "string"
}
};

fetch('https://apitest.vipps.no[shippingDetailsPrefix]/v2/payments/{orderId}/shippingDetails',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json;charset=UTF-8',
  'Accept' => 'application/json;charset=UTF-8',
  'Authorization' => {
  "type": "string"
}
}

result = RestClient.post 'https://apitest.vipps.no[shippingDetailsPrefix]/v2/payments/{orderId}/shippingDetails',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json;charset=UTF-8',
  'Accept': 'application/json;charset=UTF-8',
  'Authorization': {
  "type": "string"
}
}

r = requests.post('https://apitest.vipps.no[shippingDetailsPrefix]/v2/payments/{orderId}/shippingDetails', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json;charset=UTF-8',
    'Accept' => 'application/json;charset=UTF-8',
    'Authorization' => '[object Object]',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://apitest.vipps.no[shippingDetailsPrefix]/v2/payments/{orderId}/shippingDetails', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://apitest.vipps.no[shippingDetailsPrefix]/v2/payments/{orderId}/shippingDetails");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json;charset=UTF-8"},
        "Accept": []string{"application/json;charset=UTF-8"},
        "Authorization": []string{"[object Object]"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://apitest.vipps.no[shippingDetailsPrefix]/v2/payments/{orderId}/shippingDetails", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST [shippingDetailsPrefix]/v2/payments/{orderId}/shippingDetails`

*Fetch Shipping Cost & Method*

This API endpoint on the merchant side allows Vipps to get the shipping cost and method based on the provided address and product details. The primary use of this service is Vipps Hurtigkasse (express checkout) where Vipps needs to present shipping cost and method to the Vipps user. Vipps will add `/v2/payments/{orderId}/shippingDetails` to the end of this URL. Vipps has a *10 second timeout* for these requests, and thus requires a quick reply from the merchant's server for successful payments. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.

> Body parameter

```json
{
  "type": "object",
  "required": [
    "addressId",
    "addressLine1",
    "city",
    "country",
    "postCode"
  ],
  "properties": {
    "addressId": {
      "type": "integer",
      "format": "int32",
      "description": "Vipps Provided address Id. To be returned in response in the same field"
    },
    "addressLine1": {
      "type": "string",
      "example": "Dronning Eufemias gate 42"
    },
    "addressLine2": {
      "type": "string"
    },
    "city": {
      "type": "string",
      "description": "City",
      "example": "Oslo"
    },
    "country": {
      "type": "string",
      "description": "The only country supported is Norway",
      "example": "NO"
    },
    "postCode": {
      "type": "string",
      "description": "Four digits",
      "pattern": "^\\d{4}$",
      "example": "0603"
    },
    "addressType": {
      "type": "string",
      "example": "H"
    }
  }
}
```

<h3 id="fetchshippingcostusingpost-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|orderId|path|string|true|orderId|
|Authorization|header|string|false|Token provided by the merchant in initiate payment request as `authToken`. Used so that the merchant may authenticate the request.|
|body|body|[FetchShippingCostAndMethod](#schemafetchshippingcostandmethod)|true|fetchShippingCostAndMethod|
|» addressId|body|integer(int32)|true|Vipps Provided address Id. To be returned in response in the same field|
|» addressLine1|body|string|true|none|
|» addressLine2|body|string|false|none|
|» city|body|string|true|City|
|» country|body|string|true|The only country supported is Norway|
|» postCode|body|string|true|Four digits|
|» addressType|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "type": "object",
  "required": [
    "addressId",
    "orderId",
    "shippingDetails"
  ],
  "properties": {
    "addressId": {
      "type": "integer",
      "format": "int32"
    },
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "shippingDetails": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "isDefault",
          "shippingCost",
          "shippingMethod",
          "shippingMethodId"
        ],
        "properties": {
          "isDefault": {
            "type": "string",
            "enum": [
              "Y",
              "N"
            ]
          },
          "priority": {
            "type": "integer",
            "format": "int32"
          },
          "shippingCost": {
            "type": "number",
            "format": "double"
          },
          "shippingMethod": {
            "type": "string",
            "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
            "example": "Posten Servicepakke",
            "maxLength": 256
          },
          "shippingMethodId": {
            "type": "string"
          }
        }
      }
    }
  }
}
```

<h3 id="fetchshippingcostusingpost-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Fetch Shipping Cost & Method.|[FetchShippingCostResponse](#schemafetchshippingcostresponse)|

<aside class="success">
This operation does not require authentication
</aside>

## transactionUpdateCallbackForRegularPaymentUsingPOST

<a id="opIdtransactionUpdateCallbackForRegularPaymentUsingPOST"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://apitest.vipps.no[callbackPrefix]/v2/payments/{orderId} \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Authorization: [object Object]'

```

```http
POST https://apitest.vipps.no[callbackPrefix]/v2/payments/{orderId} HTTP/1.1
Host: apitest.vipps.no
Content-Type: application/json;charset=UTF-8

Authorization: [object Object]

```

```javascript
const inputBody = '{
  "oneOf": [
    {
      "type": "object",
      "required": [
        "merchantSerialNumber",
        "orderId",
        "shippingDetails",
        "userDetails",
        "transactionInfo"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        },
        "orderId": {
          "type": "string",
          "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
          "example": "order123abc",
          "pattern": "^[a-zA-Z0-9-]{1,30}$",
          "maxLength": 30
        },
        "shippingDetails": {
          "type": "object",
          "required": [
            "address",
            "shippingCost",
            "shippingMethod",
            "shippingMethodId"
          ],
          "properties": {
            "address": {
              "type": "object",
              "required": [
                "addressLine1",
                "city",
                "country",
                "postCode"
              ],
              "properties": {
                "addressLine1": {
                  "type": "string",
                  "description": "Address Line 1",
                  "example": "Dronning Eufemias gate 42"
                },
                "addressLine2": {
                  "type": "string",
                  "description": "Address Line 2",
                  "example": "Att: Rune Garborg"
                },
                "city": {
                  "type": "string",
                  "description": "City",
                  "example": "Oslo"
                },
                "country": {
                  "type": "string",
                  "description": "Country",
                  "example": "Norway",
                  "enum": [
                    "Norway"
                  ]
                },
                "postCode": {
                  "type": "string",
                  "description": "Post Code",
                  "example": 191
                }
              }
            },
            "shippingCost": {
              "type": "number",
              "format": "double",
              "description": "Shipping cost"
            },
            "shippingMethod": {
              "type": "string",
              "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
              "example": "Posten Servicepakke",
              "maxLength": 256
            },
            "shippingMethodId": {
              "type": "string"
            }
          }
        },
        "transactionInfo": {
          "type": "object",
          "required": [
            "amount",
            "status",
            "timeStamp",
            "transactionId"
          ],
          "properties": {
            "amount": {
              "type": "number",
              "format": "double",
              "description": "Ordered amount in øre",
              "example": 20000
            },
            "status": {
              "type": "string",
              "enum": [
                "RESERVE",
                "SALE",
                "CANCELLED",
                "REJECTED",
                "AUTO_CANCEL"
              ],
              "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#callbacks) for more information.",
              "example": "RESERVE"
            },
            "timeStamp": {
              "type": "string",
              "description": "Timestamp in ISO-8601 representing when the operation was performed.",
              "example": "2018-12-12T11:18:38.246Z"
            },
            "transactionId": {
              "type": "string",
              "description": "Vipps transaction id",
              "example": "5001420062"
            }
          }
        },
        "userDetails": {
          "type": "object",
          "required": [
            "email",
            "firstName",
            "lastName",
            "mobileNumber",
            "userId"
          ],
          "properties": {
            "bankIdVerified": {
              "type": "string",
              "description": "Optional Y/N string indicating if the user in bankId vertified, must be requested during onboarding.",
              "example": "Y",
              "enum": [
                "Y",
                "N"
              ]
            },
            "dateOfBirth": {
              "type": "string",
              "description": "Optional date of birth infomation, must be requested during onboarding.",
              "example": "12-3-1988"
            },
            "email": {
              "type": "string",
              "description": "Email address",
              "example": "user@example.com"
            },
            "firstName": {
              "type": "string",
              "description": "First name",
              "example": "Ada"
            },
            "lastName": {
              "type": "string",
              "description": "Last name",
              "example": "Lovelace"
            },
            "mobileNumber": {
              "type": "string",
              "description": "Mobile number",
              "example": "12345678",
              "minLength": 8,
              "maxLength": 12,
              "pattern": "^\\d{8,12}$"
            },
            "ssn": {
              "type": "string",
              "description": "Optional social security number for the user, must be requested during onboarding.",
              "example": "12345678901",
              "minLength": 11,
              "maxLength": 11,
              "pattern": "^\\d{11}$"
            },
            "userId": {
              "type": "string",
              "example": "uiJskNQ6qNN1iwN891uuob==",
              "maxLength": 50,
              "description": "Identifies a user in Vipps. Merchant is required to store this field for future references.",
              "pattern": "^[\\d\\w\\/=+]+$"
            }
          }
        },
        "errorInfo": {
          "type": "object",
          "properties": {
            "errorCode": {
              "type": "integer",
              "example": 45,
              "description": "The number code for the error."
            },
            "errorGroup": {
              "type": "string",
              "example": "PAYMENTS"
            },
            "errorMessage": {
              "type": "string",
              "description": "Description of the error",
              "example": "User has cancelled or not acted upon the payment"
            }
          }
        }
      }
    },
    {
      "type": "object",
      "required": [
        "merchantSerialNumber",
        "orderId",
        "transactionInfo"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        },
        "orderId": {
          "type": "string",
          "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
          "example": "order123abc",
          "pattern": "^[a-zA-Z0-9-]{1,30}$",
          "maxLength": 30
        },
        "transactionInfo": {
          "type": "object",
          "required": [
            "amount",
            "status",
            "timeStamp",
            "transactionId"
          ],
          "properties": {
            "amount": {
              "type": "number",
              "format": "double",
              "description": "Ordered amount in øre",
              "example": 20000
            },
            "status": {
              "type": "string",
              "enum": [
                "RESERVE",
                "SALE",
                "CANCELLED",
                "REJECTED",
                "AUTO_CANCEL"
              ],
              "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#callbacks) for more information.",
              "example": "RESERVE"
            },
            "timeStamp": {
              "type": "string",
              "description": "Timestamp in ISO-8601 representing when the operation was performed.",
              "example": "2018-12-12T11:18:38.246Z"
            },
            "transactionId": {
              "type": "string",
              "description": "Vipps transaction id",
              "example": "5001420062"
            }
          }
        },
        "errorInfo": {
          "type": "object",
          "properties": {
            "errorCode": {
              "type": "integer",
              "example": 45,
              "description": "The number code for the error."
            },
            "errorGroup": {
              "type": "string",
              "example": "PAYMENTS"
            },
            "errorMessage": {
              "type": "string",
              "description": "Description of the error",
              "example": "User has cancelled or not acted upon the payment"
            }
          }
        }
      }
    }
  ]
}';
const headers = {
  'Content-Type':'application/json;charset=UTF-8',
  'Authorization':{
  "type": "string"
}
};

fetch('https://apitest.vipps.no[callbackPrefix]/v2/payments/{orderId}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json;charset=UTF-8',
  'Authorization' => {
  "type": "string"
}
}

result = RestClient.post 'https://apitest.vipps.no[callbackPrefix]/v2/payments/{orderId}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json;charset=UTF-8',
  'Authorization': {
  "type": "string"
}
}

r = requests.post('https://apitest.vipps.no[callbackPrefix]/v2/payments/{orderId}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json;charset=UTF-8',
    'Authorization' => '[object Object]',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://apitest.vipps.no[callbackPrefix]/v2/payments/{orderId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://apitest.vipps.no[callbackPrefix]/v2/payments/{orderId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json;charset=UTF-8"},
        "Authorization": []string{"[object Object]"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://apitest.vipps.no[callbackPrefix]/v2/payments/{orderId}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST [callbackPrefix]/v2/payments/{orderId}`

*Callback : Transaction Update*

This API call allows Vipps to send the transaction details. During regular ecomm payment order and transaction details will be shared. During express checkout payment it will provide user details and shipping details addition to the order and transaction details. Vipps will add `/v2/payments/{orderId}` to the end of this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.

> Body parameter

```json
{
  "oneOf": [
    {
      "type": "object",
      "required": [
        "merchantSerialNumber",
        "orderId",
        "shippingDetails",
        "userDetails",
        "transactionInfo"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        },
        "orderId": {
          "type": "string",
          "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
          "example": "order123abc",
          "pattern": "^[a-zA-Z0-9-]{1,30}$",
          "maxLength": 30
        },
        "shippingDetails": {
          "type": "object",
          "required": [
            "address",
            "shippingCost",
            "shippingMethod",
            "shippingMethodId"
          ],
          "properties": {
            "address": {
              "type": "object",
              "required": [
                "addressLine1",
                "city",
                "country",
                "postCode"
              ],
              "properties": {
                "addressLine1": {
                  "type": "string",
                  "description": "Address Line 1",
                  "example": "Dronning Eufemias gate 42"
                },
                "addressLine2": {
                  "type": "string",
                  "description": "Address Line 2",
                  "example": "Att: Rune Garborg"
                },
                "city": {
                  "type": "string",
                  "description": "City",
                  "example": "Oslo"
                },
                "country": {
                  "type": "string",
                  "description": "Country",
                  "example": "Norway",
                  "enum": [
                    "Norway"
                  ]
                },
                "postCode": {
                  "type": "string",
                  "description": "Post Code",
                  "example": 191
                }
              }
            },
            "shippingCost": {
              "type": "number",
              "format": "double",
              "description": "Shipping cost"
            },
            "shippingMethod": {
              "type": "string",
              "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
              "example": "Posten Servicepakke",
              "maxLength": 256
            },
            "shippingMethodId": {
              "type": "string"
            }
          }
        },
        "transactionInfo": {
          "type": "object",
          "required": [
            "amount",
            "status",
            "timeStamp",
            "transactionId"
          ],
          "properties": {
            "amount": {
              "type": "number",
              "format": "double",
              "description": "Ordered amount in øre",
              "example": 20000
            },
            "status": {
              "type": "string",
              "enum": [
                "RESERVE",
                "SALE",
                "CANCELLED",
                "REJECTED",
                "AUTO_CANCEL"
              ],
              "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#callbacks) for more information.",
              "example": "RESERVE"
            },
            "timeStamp": {
              "type": "string",
              "description": "Timestamp in ISO-8601 representing when the operation was performed.",
              "example": "2018-12-12T11:18:38.246Z"
            },
            "transactionId": {
              "type": "string",
              "description": "Vipps transaction id",
              "example": "5001420062"
            }
          }
        },
        "userDetails": {
          "type": "object",
          "required": [
            "email",
            "firstName",
            "lastName",
            "mobileNumber",
            "userId"
          ],
          "properties": {
            "bankIdVerified": {
              "type": "string",
              "description": "Optional Y/N string indicating if the user in bankId vertified, must be requested during onboarding.",
              "example": "Y",
              "enum": [
                "Y",
                "N"
              ]
            },
            "dateOfBirth": {
              "type": "string",
              "description": "Optional date of birth infomation, must be requested during onboarding.",
              "example": "12-3-1988"
            },
            "email": {
              "type": "string",
              "description": "Email address",
              "example": "user@example.com"
            },
            "firstName": {
              "type": "string",
              "description": "First name",
              "example": "Ada"
            },
            "lastName": {
              "type": "string",
              "description": "Last name",
              "example": "Lovelace"
            },
            "mobileNumber": {
              "type": "string",
              "description": "Mobile number",
              "example": "12345678",
              "minLength": 8,
              "maxLength": 12,
              "pattern": "^\\d{8,12}$"
            },
            "ssn": {
              "type": "string",
              "description": "Optional social security number for the user, must be requested during onboarding.",
              "example": "12345678901",
              "minLength": 11,
              "maxLength": 11,
              "pattern": "^\\d{11}$"
            },
            "userId": {
              "type": "string",
              "example": "uiJskNQ6qNN1iwN891uuob==",
              "maxLength": 50,
              "description": "Identifies a user in Vipps. Merchant is required to store this field for future references.",
              "pattern": "^[\\d\\w\\/=+]+$"
            }
          }
        },
        "errorInfo": {
          "type": "object",
          "properties": {
            "errorCode": {
              "type": "integer",
              "example": 45,
              "description": "The number code for the error."
            },
            "errorGroup": {
              "type": "string",
              "example": "PAYMENTS"
            },
            "errorMessage": {
              "type": "string",
              "description": "Description of the error",
              "example": "User has cancelled or not acted upon the payment"
            }
          }
        }
      }
    },
    {
      "type": "object",
      "required": [
        "merchantSerialNumber",
        "orderId",
        "transactionInfo"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        },
        "orderId": {
          "type": "string",
          "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
          "example": "order123abc",
          "pattern": "^[a-zA-Z0-9-]{1,30}$",
          "maxLength": 30
        },
        "transactionInfo": {
          "type": "object",
          "required": [
            "amount",
            "status",
            "timeStamp",
            "transactionId"
          ],
          "properties": {
            "amount": {
              "type": "number",
              "format": "double",
              "description": "Ordered amount in øre",
              "example": 20000
            },
            "status": {
              "type": "string",
              "enum": [
                "RESERVE",
                "SALE",
                "CANCELLED",
                "REJECTED",
                "AUTO_CANCEL"
              ],
              "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#callbacks) for more information.",
              "example": "RESERVE"
            },
            "timeStamp": {
              "type": "string",
              "description": "Timestamp in ISO-8601 representing when the operation was performed.",
              "example": "2018-12-12T11:18:38.246Z"
            },
            "transactionId": {
              "type": "string",
              "description": "Vipps transaction id",
              "example": "5001420062"
            }
          }
        },
        "errorInfo": {
          "type": "object",
          "properties": {
            "errorCode": {
              "type": "integer",
              "example": 45,
              "description": "The number code for the error."
            },
            "errorGroup": {
              "type": "string",
              "example": "PAYMENTS"
            },
            "errorMessage": {
              "type": "string",
              "description": "Description of the error",
              "example": "User has cancelled or not acted upon the payment"
            }
          }
        }
      }
    }
  ]
}
```

<h3 id="transactionupdatecallbackforregularpaymentusingpost-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|orderId|path|string|true|orderId|
|Authorization|header|string|false|Token provided by the merchant in initiate payment request as `authToken`. Used so that the merchant may authenticate the request.|
|body|body|[TransactionUpdateCallbackOneOf](#schematransactionupdatecallbackoneof)|true|The body of the request made by Vipps. It will differ if the request is a regular or express payment.|

<h3 id="transactionupdatecallbackforregularpaymentusingpost-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|All ok|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="vipps-ecommerce-api-authorization-service">Authorization Service</h1>

## fetchAuthorizationTokenUsingPost

<a id="opIdfetchAuthorizationTokenUsingPost"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://apitest.vipps.no/accesstoken/get \
  -H 'Accept: application/json;charset=UTF-8' \
  -H 'client_id: [object Object]' \
  -H 'client_secret: [object Object]' \
  -H 'Ocp-Apim-Subscription-Key: [object Object]'

```

```http
POST https://apitest.vipps.no/accesstoken/get HTTP/1.1
Host: apitest.vipps.no
Accept: application/json;charset=UTF-8
client_id: [object Object]
client_secret: [object Object]
Ocp-Apim-Subscription-Key: [object Object]

```

```javascript

const headers = {
  'Accept':'application/json;charset=UTF-8',
  'client_id':{
  "type": "string",
  "format": "guid"
},
  'client_secret':{
  "type": "string"
},
  'Ocp-Apim-Subscription-Key':{
  "type": "string"
}
};

fetch('https://apitest.vipps.no/accesstoken/get',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json;charset=UTF-8',
  'client_id' => {
  "type": "string",
  "format": "guid"
},
  'client_secret' => {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key' => {
  "type": "string"
}
}

result = RestClient.post 'https://apitest.vipps.no/accesstoken/get',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json;charset=UTF-8',
  'client_id': {
  "type": "string",
  "format": "guid"
},
  'client_secret': {
  "type": "string"
},
  'Ocp-Apim-Subscription-Key': {
  "type": "string"
}
}

r = requests.post('https://apitest.vipps.no/accesstoken/get', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json;charset=UTF-8',
    'client_id' => '[object Object]',
    'client_secret' => '[object Object]',
    'Ocp-Apim-Subscription-Key' => '[object Object]',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://apitest.vipps.no/accesstoken/get', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://apitest.vipps.no/accesstoken/get");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json;charset=UTF-8"},
        "client_id": []string{"[object Object]"},
        "client_secret": []string{"[object Object]"},
        "Ocp-Apim-Subscription-Key": []string{"[object Object]"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://apitest.vipps.no/accesstoken/get", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /accesstoken/get`

*Fetch Authorization token*

Authorization token API endpoint helps to get the JWT Bearer token that needs to be passed in every API request in the Authorization header. The merchant application use the API to get a JWT access token. JWT access token is a base 64 encoded string value that must be aquire first before making any Vipps api calls

<h3 id="fetchauthorizationtokenusingpost-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|client_id|header|string(guid)|true|Client id is located in the [developer portal](https://apitest-portal.vipps.no/). Navigate to the ```Applications``` tab and click the ```View secrets``` button to display the client id. See the [getting started guide](https://github.com/vippsas/vipps-developers/blob/master/vipps-developer-portal-getting-started.md) for full guide with images.|
|client_secret|header|string|true|Client secret is located in the [developer portal](https://apitest-portal.vipps.no/). Navigate to the ```Applications``` tab and click the ```View secrets``` button to display the client id. See the [getting started guide](https://github.com/vippsas/vipps-developers/blob/master/vipps-developer-portal-getting-started.md) for full guide with images.|
|Ocp-Apim-Subscription-Key|header|string|true|The subscription-key for Authorization token is located in the [developer portal](https://apitest-portal.vipps.no/). Click the username to the right on the page and select ```Profile``` from the dropdown. The ```DEFAULT_ACCESSTOKEN``` key is the value for subscription-key. See the [getting started guide](https://github.com/vippsas/vipps-developers/blob/master/vipps-developer-portal-getting-started.md) for full guide with images.|

> Example responses

> 200 Response

```json
{
  "type": "object",
  "required": [
    "token_type",
    "expires_in",
    "ext_expires_in",
    "expires_on",
    "not_before",
    "resource",
    "access_token"
  ],
  "properties": {
    "token_type": {
      "type": "string",
      "description": "String containing the type for the Access Token.",
      "example": "Bearer"
    },
    "expires_in": {
      "type": "integer",
      "description": "Token expiry time in seconds.",
      "example": 3600
    },
    "ext_expires_in": {
      "type": "integer",
      "description": "Extra time added to expiry time. Currently disabled.",
      "example": 3600
    },
    "expires_on": {
      "type": "integer",
      "description": "Token expiry time in epoch time format.",
      "example": 1547823408
    },
    "not_before": {
      "type": "integer",
      "description": "Token creation time in epoch time format.",
      "example": 1547819508
    },
    "resource": {
      "type": "string",
      "description": "A common resource object. Not used in token validation",
      "example": "00000002-0000-0000-c000-000000000000"
    },
    "access_token": {
      "type": "string",
      "format": "byte",
      "example": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1Ni"
    }
  }
}
```

<h3 id="fetchauthorizationtokenusingpost-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[AuthorizationTokenResponse](#schemaauthorizationtokenresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request (Missing a required parameter or bad request format)|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|402|[Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2)|Payment Failed|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Request Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|None|
|405|[Method Not Allowed](https://tools.ietf.org/html/rfc7231#section-6.5.5)|Request method not supported|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Unsupported media type|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Something went wrong from Vipps Server side|None|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_PaymentActionsRequest">PaymentActionsRequest</h2>
<!-- backwards compatibility -->
<a id="schemapaymentactionsrequest"></a>
<a id="schema_PaymentActionsRequest"></a>
<a id="tocSpaymentactionsrequest"></a>
<a id="tocspaymentactionsrequest"></a>

```json
{
  "type": "object",
  "properties": {
    "merchantInfo": {
      "type": "object",
      "required": [
        "merchantSerialNumber"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        }
      }
    },
    "transaction": {
      "type": "object",
      "required": [
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "integer",
          "format": "int32",
          "description": "Amount in øre, if amount is 0 or not provided then full capture will be performed. 32 Bit Integer (2147483647)",
          "pattern": "^\\d{3,}$",
          "example": 20000
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|merchantInfo|[MerchantInfoPayment](#schemamerchantinfopayment)|false|none|none|
|transaction|[Transaction](#schematransaction)|false|none|none|

<h2 id="tocS_Address">Address</h2>
<!-- backwards compatibility -->
<a id="schemaaddress"></a>
<a id="schema_Address"></a>
<a id="tocSaddress"></a>
<a id="tocsaddress"></a>

```json
{
  "type": "object",
  "required": [
    "addressLine1",
    "city",
    "country",
    "postCode"
  ],
  "properties": {
    "addressLine1": {
      "type": "string",
      "description": "Address Line 1",
      "example": "Dronning Eufemias gate 42"
    },
    "addressLine2": {
      "type": "string",
      "description": "Address Line 2",
      "example": "Att: Rune Garborg"
    },
    "city": {
      "type": "string",
      "description": "City",
      "example": "Oslo"
    },
    "country": {
      "type": "string",
      "description": "Country",
      "example": "Norway",
      "enum": [
        "Norway"
      ]
    },
    "postCode": {
      "type": "string",
      "description": "Post Code",
      "example": 191
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|addressLine1|string|true|none|Address Line 1|
|addressLine2|string|false|none|Address Line 2|
|city|string|true|none|City|
|country|string|true|none|Country|
|postCode|string|true|none|Post Code|

#### Enumerated Values

|Property|Value|
|---|---|
|country|Norway|

<h2 id="tocS_PaymentShippingDetails">PaymentShippingDetails</h2>
<!-- backwards compatibility -->
<a id="schemapaymentshippingdetails"></a>
<a id="schema_PaymentShippingDetails"></a>
<a id="tocSpaymentshippingdetails"></a>
<a id="tocspaymentshippingdetails"></a>

```json
{
  "type": "object",
  "required": [
    "shippingCost",
    "shippingMethod",
    "shippingMethodId"
  ],
  "properties": {
    "address": {
      "type": "object",
      "required": [
        "addressLine1",
        "city",
        "country",
        "postCode"
      ],
      "properties": {
        "addressLine1": {
          "type": "string",
          "description": "Address Line 1",
          "example": "Dronning Eufemias gate 42"
        },
        "addressLine2": {
          "type": "string",
          "description": "Address Line 2",
          "example": "Att: Rune Garborg"
        },
        "city": {
          "type": "string",
          "description": "City",
          "example": "Oslo"
        },
        "country": {
          "type": "string",
          "description": "Country",
          "example": "Norway",
          "enum": [
            "Norway"
          ]
        },
        "postCode": {
          "type": "string",
          "description": "Post Code",
          "example": 191
        }
      }
    },
    "shippingCost": {
      "type": "number",
      "format": "double",
      "description": "Shipping Cost",
      "example": 1500
    },
    "shippingMethod": {
      "type": "string",
      "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
      "example": "Posten Servicepakke",
      "maxLength": 256
    },
    "shippingMethodId": {
      "type": "string"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|[Address](#schemaaddress)|false|none|none|
|shippingCost|number(double)|true|none|Shipping Cost|
|shippingMethod|string|true|none|Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.|
|shippingMethodId|string|true|none|none|

<h2 id="tocS_TransactionLogHistory">TransactionLogHistory</h2>
<!-- backwards compatibility -->
<a id="schematransactionloghistory"></a>
<a id="schema_TransactionLogHistory"></a>
<a id="tocStransactionloghistory"></a>
<a id="tocstransactionloghistory"></a>

```json
{
  "type": "object",
  "required": [
    "operation",
    "amount",
    "operationSuccess",
    "transactionText"
  ],
  "properties": {
    "amount": {
      "type": "integer",
      "format": "int32"
    },
    "operation": {
      "type": "string",
      "example": "RESERVE",
      "description": "The operation that was performed for this log entry. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information.",
      "enum": [
        "INITIATE",
        "RESERVE",
        "SALE",
        "CAPTURE",
        "REFUND",
        "CANCEL",
        "VOID"
      ]
    },
    "operationf": {
      "type": "boolean",
      "description": "If the corrosponding operation was successfull.",
      "example": true
    },
    "requestId": {
      "description": "The idempotent request id provided by the merchant for the operation.",
      "example": 12983921873981899000,
      "type": "string"
    },
    "timeStamp": {
      "type": "string",
      "description": "Timestamp in ISO-8601 representing when the operation was perfomed.",
      "example": "2019-02-05T12:27:42.311Z"
    },
    "transactionId": {
      "description": "Identifies the transaction",
      "example": 5001446662,
      "type": "string"
    },
    "transactionText": {
      "type": "string",
      "description": "Transaction text to be displayed in Vipps",
      "example": "One pair of Vipps socks",
      "maxLength": 100
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|amount|integer(int32)|true|none|none|
|operation|string|true|none|The operation that was performed for this log entry. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information.|
|operationf|boolean|false|none|If the corrosponding operation was successfull.|
|requestId|string|false|none|The idempotent request id provided by the merchant for the operation.|
|timeStamp|string|false|none|Timestamp in ISO-8601 representing when the operation was perfomed.|
|transactionId|string|false|none|Identifies the transaction|
|transactionText|string|true|none|Transaction text to be displayed in Vipps|

#### Enumerated Values

|Property|Value|
|---|---|
|operation|INITIATE|
|operation|RESERVE|
|operation|SALE|
|operation|CAPTURE|
|operation|REFUND|
|operation|CANCEL|
|operation|VOID|

<h2 id="tocS_CancelTransaction">CancelTransaction</h2>
<!-- backwards compatibility -->
<a id="schemacanceltransaction"></a>
<a id="schema_CancelTransaction"></a>
<a id="tocScanceltransaction"></a>
<a id="tocscanceltransaction"></a>

```json
{
  "type": "object",
  "properties": {
    "transactionText": {
      "type": "string",
      "description": "Transaction text to be displayed in Vipps",
      "example": "One pair of Vipps socks",
      "maxLength": 100
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|transactionText|string|false|none|Transaction text to be displayed in Vipps|

<h2 id="tocS_UserDetails">UserDetails</h2>
<!-- backwards compatibility -->
<a id="schemauserdetails"></a>
<a id="schema_UserDetails"></a>
<a id="tocSuserdetails"></a>
<a id="tocsuserdetails"></a>

```json
{
  "type": "object",
  "required": [
    "email",
    "firstName",
    "lastName",
    "mobileNumber",
    "userId"
  ],
  "properties": {
    "bankIdVerified": {
      "type": "string",
      "description": "Optional Y/N string indicating if the user in bankId vertified, must be requested during onboarding.",
      "example": "Y",
      "enum": [
        "Y",
        "N"
      ]
    },
    "dateOfBirth": {
      "type": "string",
      "description": "Optional date of birth infomation, must be requested during onboarding.",
      "example": "12-3-1988"
    },
    "email": {
      "type": "string",
      "description": "Email address",
      "example": "user@example.com"
    },
    "firstName": {
      "type": "string",
      "description": "First name",
      "example": "Ada"
    },
    "lastName": {
      "type": "string",
      "description": "Last name",
      "example": "Lovelace"
    },
    "mobileNumber": {
      "type": "string",
      "description": "Mobile number",
      "example": "12345678",
      "minLength": 8,
      "maxLength": 12,
      "pattern": "^\\d{8,12}$"
    },
    "ssn": {
      "type": "string",
      "description": "Optional social security number for the user, must be requested during onboarding.",
      "example": "12345678901",
      "minLength": 11,
      "maxLength": 11,
      "pattern": "^\\d{11}$"
    },
    "userId": {
      "type": "string",
      "example": "uiJskNQ6qNN1iwN891uuob==",
      "maxLength": 50,
      "description": "Identifies a user in Vipps. Merchant is required to store this field for future references.",
      "pattern": "^[\\d\\w\\/=+]+$"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bankIdVerified|string|false|none|Optional Y/N string indicating if the user in bankId vertified, must be requested during onboarding.|
|dateOfBirth|string|false|none|Optional date of birth infomation, must be requested during onboarding.|
|email|string|true|none|Email address|
|firstName|string|true|none|First name|
|lastName|string|true|none|Last name|
|mobileNumber|string|true|none|Mobile number|
|ssn|string|false|none|Optional social security number for the user, must be requested during onboarding.|
|userId|string|true|none|Identifies a user in Vipps. Merchant is required to store this field for future references.|

#### Enumerated Values

|Property|Value|
|---|---|
|bankIdVerified|Y|
|bankIdVerified|N|

<h2 id="tocS_callbackErrorInfo">callbackErrorInfo</h2>
<!-- backwards compatibility -->
<a id="schemacallbackerrorinfo"></a>
<a id="schema_callbackErrorInfo"></a>
<a id="tocScallbackerrorinfo"></a>
<a id="tocscallbackerrorinfo"></a>

```json
{
  "type": "object",
  "properties": {
    "errorCode": {
      "type": "integer",
      "example": 45,
      "description": "The number code for the error."
    },
    "errorGroup": {
      "type": "string",
      "example": "PAYMENTS"
    },
    "errorMessage": {
      "type": "string",
      "description": "Description of the error",
      "example": "User has cancelled or not acted upon the payment"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|errorCode|integer|false|none|The number code for the error.|
|errorGroup|string|false|none|none|
|errorMessage|string|false|none|Description of the error|

<h2 id="tocS_CallbackTransactionInfoStatus">CallbackTransactionInfoStatus</h2>
<!-- backwards compatibility -->
<a id="schemacallbacktransactioninfostatus"></a>
<a id="schema_CallbackTransactionInfoStatus"></a>
<a id="tocScallbacktransactioninfostatus"></a>
<a id="tocscallbacktransactioninfostatus"></a>

```json
{
  "type": "object",
  "required": [
    "amount",
    "status",
    "timeStamp",
    "transactionId"
  ],
  "properties": {
    "amount": {
      "type": "number",
      "format": "double",
      "description": "Ordered amount in øre",
      "example": 20000
    },
    "status": {
      "type": "string",
      "enum": [
        "RESERVE",
        "SALE",
        "CANCELLED",
        "REJECTED",
        "AUTO_CANCEL"
      ],
      "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#callbacks) for more information.",
      "example": "RESERVE"
    },
    "timeStamp": {
      "type": "string",
      "description": "Timestamp in ISO-8601 representing when the operation was performed.",
      "example": "2018-12-12T11:18:38.246Z"
    },
    "transactionId": {
      "type": "string",
      "description": "Vipps transaction id",
      "example": "5001420062"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|amount|number(double)|true|none|Ordered amount in øre|
|status|string|true|none|Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#callbacks) for more information.|
|timeStamp|string|true|none|Timestamp in ISO-8601 representing when the operation was performed.|
|transactionId|string|true|none|Vipps transaction id|

#### Enumerated Values

|Property|Value|
|---|---|
|status|RESERVE|
|status|SALE|
|status|CANCELLED|
|status|REJECTED|
|status|AUTO_CANCEL|

<h2 id="tocS_OrderStatusInfoTransactionInfo">OrderStatusInfoTransactionInfo</h2>
<!-- backwards compatibility -->
<a id="schemaorderstatusinfotransactioninfo"></a>
<a id="schema_OrderStatusInfoTransactionInfo"></a>
<a id="tocSorderstatusinfotransactioninfo"></a>
<a id="tocsorderstatusinfotransactioninfo"></a>

```json
{
  "type": "object",
  "required": [
    "amount",
    "status",
    "timeStamp",
    "transactionId"
  ],
  "properties": {
    "amount": {
      "type": "number",
      "format": "double",
      "description": "Ordered amount in øre",
      "example": 20000
    },
    "status": {
      "type": "string",
      "enum": [
        "INITIATE",
        "REGISTER",
        "RESERVE",
        "SALE",
        "CAPTURE",
        "REFUND",
        "CANCEL",
        "VOID",
        "FAILED",
        "REJECTED"
      ],
      "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information.",
      "example": "RESERVE"
    },
    "timeStamp": {
      "type": "string",
      "description": "Timestamp in ISO-8601 representing when the status operation was performed.",
      "example": "2018-12-12T11:18:38.246Z"
    },
    "transactionId": {
      "type": "string",
      "description": "Vipps transaction id",
      "example": "5001420062"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|amount|number(double)|true|none|Ordered amount in øre|
|status|string|true|none|Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information.|
|timeStamp|string|true|none|Timestamp in ISO-8601 representing when the status operation was performed.|
|transactionId|string|true|none|Vipps transaction id|

#### Enumerated Values

|Property|Value|
|---|---|
|status|INITIATE|
|status|REGISTER|
|status|RESERVE|
|status|SALE|
|status|CAPTURE|
|status|REFUND|
|status|CANCEL|
|status|VOID|
|status|FAILED|
|status|REJECTED|

<h2 id="tocS_TransactionInfoCancel">TransactionInfoCancel</h2>
<!-- backwards compatibility -->
<a id="schematransactioninfocancel"></a>
<a id="schema_TransactionInfoCancel"></a>
<a id="tocStransactioninfocancel"></a>
<a id="tocstransactioninfocancel"></a>

```json
{
  "type": "object",
  "required": [
    "amount",
    "status",
    "timeStamp",
    "transactionId",
    "transactionText"
  ],
  "properties": {
    "amount": {
      "type": "number",
      "format": "double",
      "description": "Ordered amount in øre",
      "example": 20000
    },
    "status": {
      "type": "string",
      "enum": [
        "Cancelled"
      ],
      "example": "Cancelled",
      "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information."
    },
    "timeStamp": {
      "type": "string",
      "description": "Timestamp in ISO-8601 representing when the order was cancelled.",
      "example": "2018-12-12T11:18:38.246Z"
    },
    "transactionId": {
      "type": "string",
      "description": "Vipps transaction id",
      "example": "5001420062"
    },
    "transactionText": {
      "type": "string",
      "description": "Transaction text to be displayed in Vipps",
      "example": "One pair of Vipps socks",
      "maxLength": 100
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|amount|number(double)|true|none|Ordered amount in øre|
|status|string|true|none|Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information.|
|timeStamp|string|true|none|Timestamp in ISO-8601 representing when the order was cancelled.|
|transactionId|string|true|none|Vipps transaction id|
|transactionText|string|true|none|Transaction text to be displayed in Vipps|

#### Enumerated Values

|Property|Value|
|---|---|
|status|Cancelled|

<h2 id="tocS_TransactionInfoRefund">TransactionInfoRefund</h2>
<!-- backwards compatibility -->
<a id="schematransactioninforefund"></a>
<a id="schema_TransactionInfoRefund"></a>
<a id="tocStransactioninforefund"></a>
<a id="tocstransactioninforefund"></a>

```json
{
  "type": "object",
  "required": [
    "amount",
    "status",
    "timeStamp",
    "transactionId",
    "transactionText"
  ],
  "properties": {
    "amount": {
      "type": "number",
      "format": "double",
      "description": "Ordered amount in øre",
      "example": 20000
    },
    "status": {
      "type": "string",
      "enum": [
        "Refund"
      ],
      "example": "Refund",
      "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information."
    },
    "timeStamp": {
      "type": "string",
      "description": "Timestamp in ISO-8601 representing when the order was refunded.",
      "example": "2018-12-12T11:18:38.246Z"
    },
    "transactionId": {
      "type": "string",
      "description": "Vipps transaction id",
      "example": "5001420062"
    },
    "transactionText": {
      "type": "string",
      "description": "Transaction text to be displayed in Vipps",
      "example": "One pair of Vipps socks",
      "maxLength": 100
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|amount|number(double)|true|none|Ordered amount in øre|
|status|string|true|none|Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information.|
|timeStamp|string|true|none|Timestamp in ISO-8601 representing when the order was refunded.|
|transactionId|string|true|none|Vipps transaction id|
|transactionText|string|true|none|Transaction text to be displayed in Vipps|

#### Enumerated Values

|Property|Value|
|---|---|
|status|Refund|

<h2 id="tocS_TransactionInfoCapture">TransactionInfoCapture</h2>
<!-- backwards compatibility -->
<a id="schematransactioninfocapture"></a>
<a id="schema_TransactionInfoCapture"></a>
<a id="tocStransactioninfocapture"></a>
<a id="tocstransactioninfocapture"></a>

```json
{
  "type": "object",
  "required": [
    "amount",
    "status",
    "timeStamp",
    "transactionId",
    "transactionText"
  ],
  "properties": {
    "amount": {
      "type": "number",
      "format": "double",
      "description": "Ordered amount in øre",
      "example": 20000
    },
    "status": {
      "type": "string",
      "enum": [
        "Captured"
      ],
      "example": "Captured",
      "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information."
    },
    "timeStamp": {
      "type": "string",
      "description": "Timestamp in ISO-8601 representing when the order was captured.",
      "example": "2018-12-12T11:18:38.246Z"
    },
    "transactionId": {
      "type": "string",
      "description": "Vipps transaction id",
      "example": "5001420062"
    },
    "transactionText": {
      "type": "string",
      "description": "Transaction text to be displayed in Vipps",
      "example": "One pair of Vipps socks",
      "maxLength": 100
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|amount|number(double)|true|none|Ordered amount in øre|
|status|string|true|none|Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information.|
|timeStamp|string|true|none|Timestamp in ISO-8601 representing when the order was captured.|
|transactionId|string|true|none|Vipps transaction id|
|transactionText|string|true|none|Transaction text to be displayed in Vipps|

#### Enumerated Values

|Property|Value|
|---|---|
|status|Captured|

<h2 id="tocS_GetTransactionDetails">GetTransactionDetails</h2>
<!-- backwards compatibility -->
<a id="schemagettransactiondetails"></a>
<a id="schema_GetTransactionDetails"></a>
<a id="tocSgettransactiondetails"></a>
<a id="tocsgettransactiondetails"></a>

```json
{
  "type": "object",
  "properties": {
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "shippingDetails": {
      "type": "object",
      "required": [
        "shippingCost",
        "shippingMethod",
        "shippingMethodId"
      ],
      "properties": {
        "address": {
          "type": "object",
          "required": [
            "addressLine1",
            "city",
            "country",
            "postCode"
          ],
          "properties": {
            "addressLine1": {
              "type": "string",
              "description": "Address Line 1",
              "example": "Dronning Eufemias gate 42"
            },
            "addressLine2": {
              "type": "string",
              "description": "Address Line 2",
              "example": "Att: Rune Garborg"
            },
            "city": {
              "type": "string",
              "description": "City",
              "example": "Oslo"
            },
            "country": {
              "type": "string",
              "description": "Country",
              "example": "Norway",
              "enum": [
                "Norway"
              ]
            },
            "postCode": {
              "type": "string",
              "description": "Post Code",
              "example": 191
            }
          }
        },
        "shippingCost": {
          "type": "number",
          "format": "double",
          "description": "Shipping Cost",
          "example": 1500
        },
        "shippingMethod": {
          "type": "string",
          "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
          "example": "Posten Servicepakke",
          "maxLength": 256
        },
        "shippingMethodId": {
          "type": "string"
        }
      }
    },
    "transactionLogHistory": {
      "type": "array",
      "description": "Array of transaction operations. Sorted from newest to oldest.",
      "items": {
        "type": "object",
        "required": [
          "operation",
          "amount",
          "operationSuccess",
          "transactionText"
        ],
        "properties": {
          "amount": {
            "type": "integer",
            "format": "int32"
          },
          "operation": {
            "type": "string",
            "example": "RESERVE",
            "description": "The operation that was performed for this log entry. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information.",
            "enum": [
              "INITIATE",
              "RESERVE",
              "SALE",
              "CAPTURE",
              "REFUND",
              "CANCEL",
              "VOID"
            ]
          },
          "operationf": {
            "type": "boolean",
            "description": "If the corrosponding operation was successfull.",
            "example": true
          },
          "requestId": {
            "description": "The idempotent request id provided by the merchant for the operation.",
            "example": 12983921873981899000,
            "type": "string"
          },
          "timeStamp": {
            "type": "string",
            "description": "Timestamp in ISO-8601 representing when the operation was perfomed.",
            "example": "2019-02-05T12:27:42.311Z"
          },
          "transactionId": {
            "description": "Identifies the transaction",
            "example": 5001446662,
            "type": "string"
          },
          "transactionText": {
            "type": "string",
            "description": "Transaction text to be displayed in Vipps",
            "example": "One pair of Vipps socks",
            "maxLength": 100
          }
        }
      }
    },
    "transactionSummary": {
      "type": "object",
      "required": [
        "capturedAmount",
        "refundedAmount",
        "remainingAmountToCapture",
        "remainingAmountToRefund"
      ],
      "properties": {
        "capturedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total amount captured",
          "example": 20000
        },
        "refundedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total refunded amount of the order",
          "example": 0
        },
        "remainingAmountToCapture": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to capture",
          "example": 0
        },
        "remainingAmountToRefund": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to refund",
          "example": 20000
        }
      }
    },
    "userDetails": {
      "type": "object",
      "required": [
        "email",
        "firstName",
        "lastName",
        "mobileNumber",
        "userId"
      ],
      "properties": {
        "bankIdVerified": {
          "type": "string",
          "description": "Optional Y/N string indicating if the user in bankId vertified, must be requested during onboarding.",
          "example": "Y",
          "enum": [
            "Y",
            "N"
          ]
        },
        "dateOfBirth": {
          "type": "string",
          "description": "Optional date of birth infomation, must be requested during onboarding.",
          "example": "12-3-1988"
        },
        "email": {
          "type": "string",
          "description": "Email address",
          "example": "user@example.com"
        },
        "firstName": {
          "type": "string",
          "description": "First name",
          "example": "Ada"
        },
        "lastName": {
          "type": "string",
          "description": "Last name",
          "example": "Lovelace"
        },
        "mobileNumber": {
          "type": "string",
          "description": "Mobile number",
          "example": "12345678",
          "minLength": 8,
          "maxLength": 12,
          "pattern": "^\\d{8,12}$"
        },
        "ssn": {
          "type": "string",
          "description": "Optional social security number for the user, must be requested during onboarding.",
          "example": "12345678901",
          "minLength": 11,
          "maxLength": 11,
          "pattern": "^\\d{11}$"
        },
        "userId": {
          "type": "string",
          "example": "uiJskNQ6qNN1iwN891uuob==",
          "maxLength": 50,
          "description": "Identifies a user in Vipps. Merchant is required to store this field for future references.",
          "pattern": "^[\\d\\w\\/=+]+$"
        }
      }
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|orderId|string|false|none|Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.|
|shippingDetails|[PaymentShippingDetails](#schemapaymentshippingdetails)|false|none|none|
|transactionLogHistory|[[TransactionLogHistory](#schematransactionloghistory)]|false|none|Array of transaction operations. Sorted from newest to oldest.|
|transactionSummary|[TransactionSummary](#schematransactionsummary)|false|none|none|
|userDetails|[UserDetails](#schemauserdetails)|false|none|none|

<h2 id="tocS_InitiatePaymentV2Representation">InitiatePaymentV2Representation</h2>
<!-- backwards compatibility -->
<a id="schemainitiatepaymentv2representation"></a>
<a id="schema_InitiatePaymentV2Representation"></a>
<a id="tocSinitiatepaymentv2representation"></a>
<a id="tocsinitiatepaymentv2representation"></a>

```json
{
  "type": "object",
  "required": [
    "orderId",
    "url"
  ],
  "properties": {
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "url": {
      "type": "string",
      "description": "URL to redirect the user to Vipps landing page or a deeplink URL to open Vipps app, if isApp was set as true. The landing page will also redirect a user to the app if the user is using a mobile browser. This link will timeout after 5 minutes.",
      "example": "https://example.com"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|orderId|string|true|none|Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.|
|url|string|true|none|URL to redirect the user to Vipps landing page or a deeplink URL to open Vipps app, if isApp was set as true. The landing page will also redirect a user to the app if the user is using a mobile browser. This link will timeout after 5 minutes.|

<h2 id="tocS_ShippingDetailsRequest">ShippingDetailsRequest</h2>
<!-- backwards compatibility -->
<a id="schemashippingdetailsrequest"></a>
<a id="schema_ShippingDetailsRequest"></a>
<a id="tocSshippingdetailsrequest"></a>
<a id="tocsshippingdetailsrequest"></a>

```json
{
  "type": "object",
  "required": [
    "address",
    "shippingCost",
    "shippingMethod",
    "shippingMethodId"
  ],
  "properties": {
    "address": {
      "type": "object",
      "required": [
        "addressLine1",
        "city",
        "country",
        "postCode"
      ],
      "properties": {
        "addressLine1": {
          "type": "string",
          "description": "Address Line 1",
          "example": "Dronning Eufemias gate 42"
        },
        "addressLine2": {
          "type": "string",
          "description": "Address Line 2",
          "example": "Att: Rune Garborg"
        },
        "city": {
          "type": "string",
          "description": "City",
          "example": "Oslo"
        },
        "country": {
          "type": "string",
          "description": "Country",
          "example": "Norway",
          "enum": [
            "Norway"
          ]
        },
        "postCode": {
          "type": "string",
          "description": "Post Code",
          "example": 191
        }
      }
    },
    "shippingCost": {
      "type": "number",
      "format": "double",
      "description": "Shipping cost"
    },
    "shippingMethod": {
      "type": "string",
      "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
      "example": "Posten Servicepakke",
      "maxLength": 256
    },
    "shippingMethodId": {
      "type": "string"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|[Address](#schemaaddress)|true|none|none|
|shippingCost|number(double)|true|none|Shipping cost|
|shippingMethod|string|true|none|Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.|
|shippingMethodId|string|true|none|none|

<h2 id="tocS_TransactionResponseCancel">TransactionResponseCancel</h2>
<!-- backwards compatibility -->
<a id="schematransactionresponsecancel"></a>
<a id="schema_TransactionResponseCancel"></a>
<a id="tocStransactionresponsecancel"></a>
<a id="tocstransactionresponsecancel"></a>

```json
{
  "type": "object",
  "required": [
    "orderId"
  ],
  "properties": {
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "transactionInfo": {
      "type": "object",
      "required": [
        "amount",
        "status",
        "timeStamp",
        "transactionId",
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "number",
          "format": "double",
          "description": "Ordered amount in øre",
          "example": 20000
        },
        "status": {
          "type": "string",
          "enum": [
            "Cancelled"
          ],
          "example": "Cancelled",
          "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information."
        },
        "timeStamp": {
          "type": "string",
          "description": "Timestamp in ISO-8601 representing when the order was cancelled.",
          "example": "2018-12-12T11:18:38.246Z"
        },
        "transactionId": {
          "type": "string",
          "description": "Vipps transaction id",
          "example": "5001420062"
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    },
    "transactionSummary": {
      "type": "object",
      "required": [
        "capturedAmount",
        "refundedAmount",
        "remainingAmountToCapture",
        "remainingAmountToRefund"
      ],
      "properties": {
        "capturedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total amount captured",
          "example": 20000
        },
        "refundedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total refunded amount of the order",
          "example": 0
        },
        "remainingAmountToCapture": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to capture",
          "example": 0
        },
        "remainingAmountToRefund": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to refund",
          "example": 20000
        }
      }
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|orderId|string|true|none|Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.|
|transactionInfo|[TransactionInfoCancel](#schematransactioninfocancel)|false|none|none|
|transactionSummary|[TransactionSummary](#schematransactionsummary)|false|none|none|

<h2 id="tocS_TransactionResponseCapture">TransactionResponseCapture</h2>
<!-- backwards compatibility -->
<a id="schematransactionresponsecapture"></a>
<a id="schema_TransactionResponseCapture"></a>
<a id="tocStransactionresponsecapture"></a>
<a id="tocstransactionresponsecapture"></a>

```json
{
  "type": "object",
  "required": [
    "orderId"
  ],
  "properties": {
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "transactionInfo": {
      "type": "object",
      "required": [
        "amount",
        "status",
        "timeStamp",
        "transactionId",
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "number",
          "format": "double",
          "description": "Ordered amount in øre",
          "example": 20000
        },
        "status": {
          "type": "string",
          "enum": [
            "Captured"
          ],
          "example": "Captured",
          "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information."
        },
        "timeStamp": {
          "type": "string",
          "description": "Timestamp in ISO-8601 representing when the order was captured.",
          "example": "2018-12-12T11:18:38.246Z"
        },
        "transactionId": {
          "type": "string",
          "description": "Vipps transaction id",
          "example": "5001420062"
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    },
    "transactionSummary": {
      "type": "object",
      "required": [
        "capturedAmount",
        "refundedAmount",
        "remainingAmountToCapture",
        "remainingAmountToRefund"
      ],
      "properties": {
        "capturedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total amount captured",
          "example": 20000
        },
        "refundedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total refunded amount of the order",
          "example": 0
        },
        "remainingAmountToCapture": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to capture",
          "example": 0
        },
        "remainingAmountToRefund": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to refund",
          "example": 20000
        }
      }
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|orderId|string|true|none|Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.|
|transactionInfo|[TransactionInfoCapture](#schematransactioninfocapture)|false|none|none|
|transactionSummary|[TransactionSummary](#schematransactionsummary)|false|none|none|

<h2 id="tocS_TransactionResponseRefund">TransactionResponseRefund</h2>
<!-- backwards compatibility -->
<a id="schematransactionresponserefund"></a>
<a id="schema_TransactionResponseRefund"></a>
<a id="tocStransactionresponserefund"></a>
<a id="tocstransactionresponserefund"></a>

```json
{
  "type": "object",
  "required": [
    "orderId"
  ],
  "properties": {
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "transaction": {
      "type": "object",
      "required": [
        "amount",
        "status",
        "timeStamp",
        "transactionId",
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "number",
          "format": "double",
          "description": "Ordered amount in øre",
          "example": 20000
        },
        "status": {
          "type": "string",
          "enum": [
            "Refund"
          ],
          "example": "Refund",
          "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information."
        },
        "timeStamp": {
          "type": "string",
          "description": "Timestamp in ISO-8601 representing when the order was refunded.",
          "example": "2018-12-12T11:18:38.246Z"
        },
        "transactionId": {
          "type": "string",
          "description": "Vipps transaction id",
          "example": "5001420062"
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    },
    "transactionSummary": {
      "type": "object",
      "required": [
        "capturedAmount",
        "refundedAmount",
        "remainingAmountToCapture",
        "remainingAmountToRefund"
      ],
      "properties": {
        "capturedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total amount captured",
          "example": 20000
        },
        "refundedAmount": {
          "type": "integer",
          "format": "int32",
          "description": "Total refunded amount of the order",
          "example": 0
        },
        "remainingAmountToCapture": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to capture",
          "example": 0
        },
        "remainingAmountToRefund": {
          "type": "integer",
          "format": "int32",
          "description": "Total remaining amount to refund",
          "example": 20000
        }
      }
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|orderId|string|true|none|Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.|
|transaction|[TransactionInfoRefund](#schematransactioninforefund)|false|none|none|
|transactionSummary|[TransactionSummary](#schematransactionsummary)|false|none|none|

<h2 id="tocS_MerchantInfoPayment">MerchantInfoPayment</h2>
<!-- backwards compatibility -->
<a id="schemamerchantinfopayment"></a>
<a id="schema_MerchantInfoPayment"></a>
<a id="tocSmerchantinfopayment"></a>
<a id="tocsmerchantinfopayment"></a>

```json
{
  "type": "object",
  "required": [
    "merchantSerialNumber"
  ],
  "properties": {
    "merchantSerialNumber": {
      "type": "string",
      "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
      "minLength": 6,
      "maxLength": 6,
      "example": 123456,
      "pattern": "^\\d{6}$"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|merchantSerialNumber|string|true|none|Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.|

<h2 id="tocS_ShippingDetails">ShippingDetails</h2>
<!-- backwards compatibility -->
<a id="schemashippingdetails"></a>
<a id="schema_ShippingDetails"></a>
<a id="tocSshippingdetails"></a>
<a id="tocsshippingdetails"></a>

```json
{
  "type": "object",
  "required": [
    "isDefault",
    "shippingCost",
    "shippingMethod",
    "shippingMethodId"
  ],
  "properties": {
    "isDefault": {
      "type": "string",
      "enum": [
        "Y",
        "N"
      ]
    },
    "priority": {
      "type": "integer",
      "format": "int32"
    },
    "shippingCost": {
      "type": "number",
      "format": "double"
    },
    "shippingMethod": {
      "type": "string",
      "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
      "example": "Posten Servicepakke",
      "maxLength": 256
    },
    "shippingMethodId": {
      "type": "string"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|isDefault|string|true|none|none|
|priority|integer(int32)|false|none|none|
|shippingCost|number(double)|true|none|none|
|shippingMethod|string|true|none|Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.|
|shippingMethodId|string|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|isDefault|Y|
|isDefault|N|

<h2 id="tocS_InitiatePaymentCommand">InitiatePaymentCommand</h2>
<!-- backwards compatibility -->
<a id="schemainitiatepaymentcommand"></a>
<a id="schema_InitiatePaymentCommand"></a>
<a id="tocSinitiatepaymentcommand"></a>
<a id="tocsinitiatepaymentcommand"></a>

```json
{
  "type": "object",
  "required": [
    "customerInfo",
    "merchantInfo",
    "transaction"
  ],
  "properties": {
    "customerInfo": {
      "type": "object",
      "properties": {
        "mobileNumber": {
          "type": "string",
          "description": "Mobile number of the user who has to pay for the transation from Vipps. Allowed format: xxxxxxxx",
          "minLength": 8,
          "maxLength": 8,
          "example": 91234567,
          "pattern": "^\\d{8}$"
        }
      }
    },
    "merchantInfo": {
      "type": "object",
      "required": [
        "callbackPrefix",
        "fallBack",
        "merchantSerialNumber"
      ],
      "properties": {
        "authToken": {
          "type": "string",
          "description": "Authorization token that the merchant could share to make callbacks more secure. If provided this token will be returned as an `Authorization` header for our callbacks. This includes shipping details and callback.",
          "maxLength": 255,
          "example": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1Ni"
        },
        "callbackPrefix": {
          "type": "string",
          "description": "This is an URL for receiving the callback after the payment request. Domain name and context path should be provided by merchant as the value for this parameter. Vipps will add `/v2/payments/{orderId}` to the end or this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.",
          "maxLength": 255,
          "example": "https://example.com/vipps/callbacks"
        },
        "consentRemovalPrefix": {
          "type": "string",
          "description": "Required for express checkout payments. This callback URL will be used by Vipps to inform the merchant that the user has revoked his/her consent: This Vipps user does do not want the merchant to store or use his/her personal information anymore. Required by GDPR. Vipps will add `/v2/consents/{userId}` to the end or this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.",
          "maxLength": 255,
          "example": "https://example.com/vipps"
        },
        "fallBack": {
          "type": "string",
          "description": "Vipps will use the fall back URL to redirect Merchant Page once Payment is completed in Vipps System URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html).",
          "maxLength": 255,
          "example": "https://example.com/vipps/fallback/order123abc"
        },
        "isApp": {
          "type": "boolean",
          "example": false,
          "default": false,
          "description": "This parameter indicates whether payment request is triggered from Mobile App or Web browser. Based on this value, response will be redirect URL for Vipps landing page or deeplink URL to connect vipps App. When isApp is set to true, URLs passed to Vipps will not be validated as regular URLs."
        },
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        },
        "paymentType": {
          "type": "string",
          "description": "This parameter will identify difference between a regular ecomm payment and ecomm express payment. For express checkout, use: \"eComm Express Payment\". Express checkouts require `consentRemovalPrefix`.",
          "enum": [
            "eComm Regular Payment",
            "eComm Express Payment"
          ],
          "example": "eComm Regular Payment",
          "default": "eComm Regular Payment"
        },
        "shippingDetailsPrefix": {
          "type": "string",
          "description": "In case of express checkout payment, merchant should pass this prefix to let Vipps fetch shipping cost and method related details. Vipps will add `/v2/payments/{orderId}/shippingDetails` to the end or this URL. We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.",
          "maxLength": 255,
          "example": "https://example.com/vipps/shipping/"
        },
        "staticShippingDetails": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "isDefault",
              "shippingCost",
              "shippingMethod",
              "shippingMethodId"
            ],
            "properties": {
              "isDefault": {
                "type": "string",
                "enum": [
                  "Y",
                  "N"
                ]
              },
              "priority": {
                "type": "integer",
                "format": "int32"
              },
              "shippingCost": {
                "type": "number",
                "format": "double"
              },
              "shippingMethod": {
                "type": "string",
                "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
                "example": "Posten Servicepakke",
                "maxLength": 256
              },
              "shippingMethodId": {
                "type": "string"
              }
            }
          },
          "description": "If shipping method and cost are always a fixed value, for example 50kr,  then the method and price can be provided during the initiate call. The shippingDetailsPrefix callback will not be used if this value is provided."
        }
      }
    },
    "transaction": {
      "type": "object",
      "required": [
        "amount",
        "orderId",
        "transactionText"
      ],
      "properties": {
        "amount": {
          "type": "integer",
          "format": "int32",
          "description": "Amount in øre. 32 bit Integer (2147483647)",
          "pattern": "^\\d{3,}$",
          "example": 20000
        },
        "orderId": {
          "type": "string",
          "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
          "example": "order123abc",
          "pattern": "^[a-zA-Z0-9-]{1,30}$",
          "maxLength": 30
        },
        "timeStamp": {
          "type": "string",
          "format": "date-time",
          "description": "ISO formatted date time string.",
          "example": "2018-11-14T15:44:26.590Z"
        },
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|customerInfo|[CustomerInfoDto](#schemacustomerinfodto)|true|none|none|
|merchantInfo|[MerchantInfoDto](#schemamerchantinfodto)|true|none|none|
|transaction|[TransactionInfoInitiateDTO](#schematransactioninfoinitiatedto)|true|none|none|

<h2 id="tocS_TransactionInfoInitiateDTO">TransactionInfoInitiateDTO</h2>
<!-- backwards compatibility -->
<a id="schematransactioninfoinitiatedto"></a>
<a id="schema_TransactionInfoInitiateDTO"></a>
<a id="tocStransactioninfoinitiatedto"></a>
<a id="tocstransactioninfoinitiatedto"></a>

```json
{
  "type": "object",
  "required": [
    "amount",
    "orderId",
    "transactionText"
  ],
  "properties": {
    "amount": {
      "type": "integer",
      "format": "int32",
      "description": "Amount in øre. 32 bit Integer (2147483647)",
      "pattern": "^\\d{3,}$",
      "example": 20000
    },
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "timeStamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO formatted date time string.",
      "example": "2018-11-14T15:44:26.590Z"
    },
    "transactionText": {
      "type": "string",
      "description": "Transaction text to be displayed in Vipps",
      "example": "One pair of Vipps socks",
      "maxLength": 100
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|amount|integer(int32)|true|none|Amount in øre. 32 bit Integer (2147483647)|
|orderId|string|true|none|Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.|
|timeStamp|string(date-time)|false|none|ISO formatted date time string.|
|transactionText|string|true|none|Transaction text to be displayed in Vipps|

<h2 id="tocS_MerchantInfoDto">MerchantInfoDto</h2>
<!-- backwards compatibility -->
<a id="schemamerchantinfodto"></a>
<a id="schema_MerchantInfoDto"></a>
<a id="tocSmerchantinfodto"></a>
<a id="tocsmerchantinfodto"></a>

```json
{
  "type": "object",
  "required": [
    "callbackPrefix",
    "fallBack",
    "merchantSerialNumber"
  ],
  "properties": {
    "authToken": {
      "type": "string",
      "description": "Authorization token that the merchant could share to make callbacks more secure. If provided this token will be returned as an `Authorization` header for our callbacks. This includes shipping details and callback.",
      "maxLength": 255,
      "example": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1Ni"
    },
    "callbackPrefix": {
      "type": "string",
      "description": "This is an URL for receiving the callback after the payment request. Domain name and context path should be provided by merchant as the value for this parameter. Vipps will add `/v2/payments/{orderId}` to the end or this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.",
      "maxLength": 255,
      "example": "https://example.com/vipps/callbacks"
    },
    "consentRemovalPrefix": {
      "type": "string",
      "description": "Required for express checkout payments. This callback URL will be used by Vipps to inform the merchant that the user has revoked his/her consent: This Vipps user does do not want the merchant to store or use his/her personal information anymore. Required by GDPR. Vipps will add `/v2/consents/{userId}` to the end or this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.",
      "maxLength": 255,
      "example": "https://example.com/vipps"
    },
    "fallBack": {
      "type": "string",
      "description": "Vipps will use the fall back URL to redirect Merchant Page once Payment is completed in Vipps System URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html).",
      "maxLength": 255,
      "example": "https://example.com/vipps/fallback/order123abc"
    },
    "isApp": {
      "type": "boolean",
      "example": false,
      "default": false,
      "description": "This parameter indicates whether payment request is triggered from Mobile App or Web browser. Based on this value, response will be redirect URL for Vipps landing page or deeplink URL to connect vipps App. When isApp is set to true, URLs passed to Vipps will not be validated as regular URLs."
    },
    "merchantSerialNumber": {
      "type": "string",
      "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
      "minLength": 6,
      "maxLength": 6,
      "example": 123456,
      "pattern": "^\\d{6}$"
    },
    "paymentType": {
      "type": "string",
      "description": "This parameter will identify difference between a regular ecomm payment and ecomm express payment. For express checkout, use: \"eComm Express Payment\". Express checkouts require `consentRemovalPrefix`.",
      "enum": [
        "eComm Regular Payment",
        "eComm Express Payment"
      ],
      "example": "eComm Regular Payment",
      "default": "eComm Regular Payment"
    },
    "shippingDetailsPrefix": {
      "type": "string",
      "description": "In case of express checkout payment, merchant should pass this prefix to let Vipps fetch shipping cost and method related details. Vipps will add `/v2/payments/{orderId}/shippingDetails` to the end or this URL. We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.",
      "maxLength": 255,
      "example": "https://example.com/vipps/shipping/"
    },
    "staticShippingDetails": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "isDefault",
          "shippingCost",
          "shippingMethod",
          "shippingMethodId"
        ],
        "properties": {
          "isDefault": {
            "type": "string",
            "enum": [
              "Y",
              "N"
            ]
          },
          "priority": {
            "type": "integer",
            "format": "int32"
          },
          "shippingCost": {
            "type": "number",
            "format": "double"
          },
          "shippingMethod": {
            "type": "string",
            "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
            "example": "Posten Servicepakke",
            "maxLength": 256
          },
          "shippingMethodId": {
            "type": "string"
          }
        }
      },
      "description": "If shipping method and cost are always a fixed value, for example 50kr,  then the method and price can be provided during the initiate call. The shippingDetailsPrefix callback will not be used if this value is provided."
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|authToken|string|false|none|Authorization token that the merchant could share to make callbacks more secure. If provided this token will be returned as an `Authorization` header for our callbacks. This includes shipping details and callback.|
|callbackPrefix|string|true|none|This is an URL for receiving the callback after the payment request. Domain name and context path should be provided by merchant as the value for this parameter. Vipps will add `/v2/payments/{orderId}` to the end or this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.|
|consentRemovalPrefix|string|false|none|Required for express checkout payments. This callback URL will be used by Vipps to inform the merchant that the user has revoked his/her consent: This Vipps user does do not want the merchant to store or use his/her personal information anymore. Required by GDPR. Vipps will add `/v2/consents/{userId}` to the end or this URL. URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html). We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.|
|fallBack|string|true|none|Vipps will use the fall back URL to redirect Merchant Page once Payment is completed in Vipps System URLs passed to Vipps should be URL-encoded, and must validate with the Apache Commons [UrlValidator](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/UrlValidator.html).|
|isApp|boolean|false|none|This parameter indicates whether payment request is triggered from Mobile App or Web browser. Based on this value, response will be redirect URL for Vipps landing page or deeplink URL to connect vipps App. When isApp is set to true, URLs passed to Vipps will not be validated as regular URLs.|
|merchantSerialNumber|string|true|none|Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.|
|paymentType|string|false|none|This parameter will identify difference between a regular ecomm payment and ecomm express payment. For express checkout, use: "eComm Express Payment". Express checkouts require `consentRemovalPrefix`.|
|shippingDetailsPrefix|string|false|none|In case of express checkout payment, merchant should pass this prefix to let Vipps fetch shipping cost and method related details. Vipps will add `/v2/payments/{orderId}/shippingDetails` to the end or this URL. We don't send requests to all ports, so to be safe use common ports such as: 80, 443, 8080.|
|staticShippingDetails|[[ShippingDetails](#schemashippingdetails)]|false|none|If shipping method and cost are always a fixed value, for example 50kr,  then the method and price can be provided during the initiate call. The shippingDetailsPrefix callback will not be used if this value is provided.|

#### Enumerated Values

|Property|Value|
|---|---|
|paymentType|eComm Regular Payment|
|paymentType|eComm Express Payment|

<h2 id="tocS_GetPaymentStatusResponse">GetPaymentStatusResponse</h2>
<!-- backwards compatibility -->
<a id="schemagetpaymentstatusresponse"></a>
<a id="schema_GetPaymentStatusResponse"></a>
<a id="tocSgetpaymentstatusresponse"></a>
<a id="tocsgetpaymentstatusresponse"></a>

```json
{
  "type": "object",
  "properties": {
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "transactionInfo": {
      "type": "object",
      "required": [
        "amount",
        "status",
        "timeStamp",
        "transactionId"
      ],
      "properties": {
        "amount": {
          "type": "number",
          "format": "double",
          "description": "Ordered amount in øre",
          "example": 20000
        },
        "status": {
          "type": "string",
          "enum": [
            "INITIATE",
            "REGISTER",
            "RESERVE",
            "SALE",
            "CAPTURE",
            "REFUND",
            "CANCEL",
            "VOID",
            "FAILED",
            "REJECTED"
          ],
          "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#responses-from-requests) for more information.",
          "example": "RESERVE"
        },
        "timeStamp": {
          "type": "string",
          "description": "Timestamp in ISO-8601 representing when the status operation was performed.",
          "example": "2018-12-12T11:18:38.246Z"
        },
        "transactionId": {
          "type": "string",
          "description": "Vipps transaction id",
          "example": "5001420062"
        }
      }
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|orderId|string|false|none|Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.|
|transactionInfo|[OrderStatusInfoTransactionInfo](#schemaorderstatusinfotransactioninfo)|false|none|none|

<h2 id="tocS_Transaction">Transaction</h2>
<!-- backwards compatibility -->
<a id="schematransaction"></a>
<a id="schema_Transaction"></a>
<a id="tocStransaction"></a>
<a id="tocstransaction"></a>

```json
{
  "type": "object",
  "required": [
    "transactionText"
  ],
  "properties": {
    "amount": {
      "type": "integer",
      "format": "int32",
      "description": "Amount in øre, if amount is 0 or not provided then full capture will be performed. 32 Bit Integer (2147483647)",
      "pattern": "^\\d{3,}$",
      "example": 20000
    },
    "transactionText": {
      "type": "string",
      "description": "Transaction text to be displayed in Vipps",
      "example": "One pair of Vipps socks",
      "maxLength": 100
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|amount|integer(int32)|false|none|Amount in øre, if amount is 0 or not provided then full capture will be performed. 32 Bit Integer (2147483647)|
|transactionText|string|true|none|Transaction text to be displayed in Vipps|

<h2 id="tocS_FetchShippingCostAndMethod">FetchShippingCostAndMethod</h2>
<!-- backwards compatibility -->
<a id="schemafetchshippingcostandmethod"></a>
<a id="schema_FetchShippingCostAndMethod"></a>
<a id="tocSfetchshippingcostandmethod"></a>
<a id="tocsfetchshippingcostandmethod"></a>

```json
{
  "type": "object",
  "required": [
    "addressId",
    "addressLine1",
    "city",
    "country",
    "postCode"
  ],
  "properties": {
    "addressId": {
      "type": "integer",
      "format": "int32",
      "description": "Vipps Provided address Id. To be returned in response in the same field"
    },
    "addressLine1": {
      "type": "string",
      "example": "Dronning Eufemias gate 42"
    },
    "addressLine2": {
      "type": "string"
    },
    "city": {
      "type": "string",
      "description": "City",
      "example": "Oslo"
    },
    "country": {
      "type": "string",
      "description": "The only country supported is Norway",
      "example": "NO"
    },
    "postCode": {
      "type": "string",
      "description": "Four digits",
      "pattern": "^\\d{4}$",
      "example": "0603"
    },
    "addressType": {
      "type": "string",
      "example": "H"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|addressId|integer(int32)|true|none|Vipps Provided address Id. To be returned in response in the same field|
|addressLine1|string|true|none|none|
|addressLine2|string|false|none|none|
|city|string|true|none|City|
|country|string|true|none|The only country supported is Norway|
|postCode|string|true|none|Four digits|
|addressType|string|false|none|none|

<h2 id="tocS_CustomerInfoDto">CustomerInfoDto</h2>
<!-- backwards compatibility -->
<a id="schemacustomerinfodto"></a>
<a id="schema_CustomerInfoDto"></a>
<a id="tocScustomerinfodto"></a>
<a id="tocscustomerinfodto"></a>

```json
{
  "type": "object",
  "properties": {
    "mobileNumber": {
      "type": "string",
      "description": "Mobile number of the user who has to pay for the transation from Vipps. Allowed format: xxxxxxxx",
      "minLength": 8,
      "maxLength": 8,
      "example": 91234567,
      "pattern": "^\\d{8}$"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mobileNumber|string|false|none|Mobile number of the user who has to pay for the transation from Vipps. Allowed format: xxxxxxxx|

<h2 id="tocS_CancelPaymentActionRequest">CancelPaymentActionRequest</h2>
<!-- backwards compatibility -->
<a id="schemacancelpaymentactionrequest"></a>
<a id="schema_CancelPaymentActionRequest"></a>
<a id="tocScancelpaymentactionrequest"></a>
<a id="tocscancelpaymentactionrequest"></a>

```json
{
  "type": "object",
  "properties": {
    "merchantInfo": {
      "type": "object",
      "required": [
        "merchantSerialNumber"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        }
      }
    },
    "transaction": {
      "type": "object",
      "properties": {
        "transactionText": {
          "type": "string",
          "description": "Transaction text to be displayed in Vipps",
          "example": "One pair of Vipps socks",
          "maxLength": 100
        }
      }
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|merchantInfo|[MerchantInfoPayment](#schemamerchantinfopayment)|false|none|none|
|transaction|[CancelTransaction](#schemacanceltransaction)|false|none|none|

<h2 id="tocS_ExpressCheckOutPaymentRequest">ExpressCheckOutPaymentRequest</h2>
<!-- backwards compatibility -->
<a id="schemaexpresscheckoutpaymentrequest"></a>
<a id="schema_ExpressCheckOutPaymentRequest"></a>
<a id="tocSexpresscheckoutpaymentrequest"></a>
<a id="tocsexpresscheckoutpaymentrequest"></a>

```json
{
  "type": "object",
  "required": [
    "merchantSerialNumber",
    "orderId",
    "shippingDetails",
    "userDetails",
    "transactionInfo"
  ],
  "properties": {
    "merchantSerialNumber": {
      "type": "string",
      "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
      "minLength": 6,
      "maxLength": 6,
      "example": 123456,
      "pattern": "^\\d{6}$"
    },
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "shippingDetails": {
      "type": "object",
      "required": [
        "address",
        "shippingCost",
        "shippingMethod",
        "shippingMethodId"
      ],
      "properties": {
        "address": {
          "type": "object",
          "required": [
            "addressLine1",
            "city",
            "country",
            "postCode"
          ],
          "properties": {
            "addressLine1": {
              "type": "string",
              "description": "Address Line 1",
              "example": "Dronning Eufemias gate 42"
            },
            "addressLine2": {
              "type": "string",
              "description": "Address Line 2",
              "example": "Att: Rune Garborg"
            },
            "city": {
              "type": "string",
              "description": "City",
              "example": "Oslo"
            },
            "country": {
              "type": "string",
              "description": "Country",
              "example": "Norway",
              "enum": [
                "Norway"
              ]
            },
            "postCode": {
              "type": "string",
              "description": "Post Code",
              "example": 191
            }
          }
        },
        "shippingCost": {
          "type": "number",
          "format": "double",
          "description": "Shipping cost"
        },
        "shippingMethod": {
          "type": "string",
          "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
          "example": "Posten Servicepakke",
          "maxLength": 256
        },
        "shippingMethodId": {
          "type": "string"
        }
      }
    },
    "transactionInfo": {
      "type": "object",
      "required": [
        "amount",
        "status",
        "timeStamp",
        "transactionId"
      ],
      "properties": {
        "amount": {
          "type": "number",
          "format": "double",
          "description": "Ordered amount in øre",
          "example": 20000
        },
        "status": {
          "type": "string",
          "enum": [
            "RESERVE",
            "SALE",
            "CANCELLED",
            "REJECTED",
            "AUTO_CANCEL"
          ],
          "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#callbacks) for more information.",
          "example": "RESERVE"
        },
        "timeStamp": {
          "type": "string",
          "description": "Timestamp in ISO-8601 representing when the operation was performed.",
          "example": "2018-12-12T11:18:38.246Z"
        },
        "transactionId": {
          "type": "string",
          "description": "Vipps transaction id",
          "example": "5001420062"
        }
      }
    },
    "userDetails": {
      "type": "object",
      "required": [
        "email",
        "firstName",
        "lastName",
        "mobileNumber",
        "userId"
      ],
      "properties": {
        "bankIdVerified": {
          "type": "string",
          "description": "Optional Y/N string indicating if the user in bankId vertified, must be requested during onboarding.",
          "example": "Y",
          "enum": [
            "Y",
            "N"
          ]
        },
        "dateOfBirth": {
          "type": "string",
          "description": "Optional date of birth infomation, must be requested during onboarding.",
          "example": "12-3-1988"
        },
        "email": {
          "type": "string",
          "description": "Email address",
          "example": "user@example.com"
        },
        "firstName": {
          "type": "string",
          "description": "First name",
          "example": "Ada"
        },
        "lastName": {
          "type": "string",
          "description": "Last name",
          "example": "Lovelace"
        },
        "mobileNumber": {
          "type": "string",
          "description": "Mobile number",
          "example": "12345678",
          "minLength": 8,
          "maxLength": 12,
          "pattern": "^\\d{8,12}$"
        },
        "ssn": {
          "type": "string",
          "description": "Optional social security number for the user, must be requested during onboarding.",
          "example": "12345678901",
          "minLength": 11,
          "maxLength": 11,
          "pattern": "^\\d{11}$"
        },
        "userId": {
          "type": "string",
          "example": "uiJskNQ6qNN1iwN891uuob==",
          "maxLength": 50,
          "description": "Identifies a user in Vipps. Merchant is required to store this field for future references.",
          "pattern": "^[\\d\\w\\/=+]+$"
        }
      }
    },
    "errorInfo": {
      "type": "object",
      "properties": {
        "errorCode": {
          "type": "integer",
          "example": 45,
          "description": "The number code for the error."
        },
        "errorGroup": {
          "type": "string",
          "example": "PAYMENTS"
        },
        "errorMessage": {
          "type": "string",
          "description": "Description of the error",
          "example": "User has cancelled or not acted upon the payment"
        }
      }
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|merchantSerialNumber|string|true|none|Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.|
|orderId|string|true|none|Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.|
|shippingDetails|[ShippingDetailsRequest](#schemashippingdetailsrequest)|true|none|none|
|transactionInfo|[CallbackTransactionInfoStatus](#schemacallbacktransactioninfostatus)|true|none|none|
|userDetails|[UserDetails](#schemauserdetails)|true|none|none|
|errorInfo|[callbackErrorInfo](#schemacallbackerrorinfo)|false|none|none|

<h2 id="tocS_RegularCheckOutPaymentRequest">RegularCheckOutPaymentRequest</h2>
<!-- backwards compatibility -->
<a id="schemaregularcheckoutpaymentrequest"></a>
<a id="schema_RegularCheckOutPaymentRequest"></a>
<a id="tocSregularcheckoutpaymentrequest"></a>
<a id="tocsregularcheckoutpaymentrequest"></a>

```json
{
  "type": "object",
  "required": [
    "merchantSerialNumber",
    "orderId",
    "transactionInfo"
  ],
  "properties": {
    "merchantSerialNumber": {
      "type": "string",
      "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
      "minLength": 6,
      "maxLength": 6,
      "example": 123456,
      "pattern": "^\\d{6}$"
    },
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "transactionInfo": {
      "type": "object",
      "required": [
        "amount",
        "status",
        "timeStamp",
        "transactionId"
      ],
      "properties": {
        "amount": {
          "type": "number",
          "format": "double",
          "description": "Ordered amount in øre",
          "example": 20000
        },
        "status": {
          "type": "string",
          "enum": [
            "RESERVE",
            "SALE",
            "CANCELLED",
            "REJECTED",
            "AUTO_CANCEL"
          ],
          "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#callbacks) for more information.",
          "example": "RESERVE"
        },
        "timeStamp": {
          "type": "string",
          "description": "Timestamp in ISO-8601 representing when the operation was performed.",
          "example": "2018-12-12T11:18:38.246Z"
        },
        "transactionId": {
          "type": "string",
          "description": "Vipps transaction id",
          "example": "5001420062"
        }
      }
    },
    "errorInfo": {
      "type": "object",
      "properties": {
        "errorCode": {
          "type": "integer",
          "example": 45,
          "description": "The number code for the error."
        },
        "errorGroup": {
          "type": "string",
          "example": "PAYMENTS"
        },
        "errorMessage": {
          "type": "string",
          "description": "Description of the error",
          "example": "User has cancelled or not acted upon the payment"
        }
      }
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|merchantSerialNumber|string|true|none|Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.|
|orderId|string|true|none|Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.|
|transactionInfo|[CallbackTransactionInfoStatus](#schemacallbacktransactioninfostatus)|true|none|none|
|errorInfo|[callbackErrorInfo](#schemacallbackerrorinfo)|false|none|none|

<h2 id="tocS_AuthorizationTokenResponse">AuthorizationTokenResponse</h2>
<!-- backwards compatibility -->
<a id="schemaauthorizationtokenresponse"></a>
<a id="schema_AuthorizationTokenResponse"></a>
<a id="tocSauthorizationtokenresponse"></a>
<a id="tocsauthorizationtokenresponse"></a>

```json
{
  "type": "object",
  "required": [
    "token_type",
    "expires_in",
    "ext_expires_in",
    "expires_on",
    "not_before",
    "resource",
    "access_token"
  ],
  "properties": {
    "token_type": {
      "type": "string",
      "description": "String containing the type for the Access Token.",
      "example": "Bearer"
    },
    "expires_in": {
      "type": "integer",
      "description": "Token expiry time in seconds.",
      "example": 3600
    },
    "ext_expires_in": {
      "type": "integer",
      "description": "Extra time added to expiry time. Currently disabled.",
      "example": 3600
    },
    "expires_on": {
      "type": "integer",
      "description": "Token expiry time in epoch time format.",
      "example": 1547823408
    },
    "not_before": {
      "type": "integer",
      "description": "Token creation time in epoch time format.",
      "example": 1547819508
    },
    "resource": {
      "type": "string",
      "description": "A common resource object. Not used in token validation",
      "example": "00000002-0000-0000-c000-000000000000"
    },
    "access_token": {
      "type": "string",
      "format": "byte",
      "example": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1Ni"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|token_type|string|true|none|String containing the type for the Access Token.|
|expires_in|integer|true|none|Token expiry time in seconds.|
|ext_expires_in|integer|true|none|Extra time added to expiry time. Currently disabled.|
|expires_on|integer|true|none|Token expiry time in epoch time format.|
|not_before|integer|true|none|Token creation time in epoch time format.|
|resource|string|true|none|A common resource object. Not used in token validation|
|access_token|string(byte)|true|none|none|

<h2 id="tocS_FetchShippingCostResponse">FetchShippingCostResponse</h2>
<!-- backwards compatibility -->
<a id="schemafetchshippingcostresponse"></a>
<a id="schema_FetchShippingCostResponse"></a>
<a id="tocSfetchshippingcostresponse"></a>
<a id="tocsfetchshippingcostresponse"></a>

```json
{
  "type": "object",
  "required": [
    "addressId",
    "orderId",
    "shippingDetails"
  ],
  "properties": {
    "addressId": {
      "type": "integer",
      "format": "int32"
    },
    "orderId": {
      "type": "string",
      "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
      "example": "order123abc",
      "pattern": "^[a-zA-Z0-9-]{1,30}$",
      "maxLength": 30
    },
    "shippingDetails": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "isDefault",
          "shippingCost",
          "shippingMethod",
          "shippingMethodId"
        ],
        "properties": {
          "isDefault": {
            "type": "string",
            "enum": [
              "Y",
              "N"
            ]
          },
          "priority": {
            "type": "integer",
            "format": "int32"
          },
          "shippingCost": {
            "type": "number",
            "format": "double"
          },
          "shippingMethod": {
            "type": "string",
            "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
            "example": "Posten Servicepakke",
            "maxLength": 256
          },
          "shippingMethodId": {
            "type": "string"
          }
        }
      }
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|addressId|integer(int32)|true|none|none|
|orderId|string|true|none|Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.|
|shippingDetails|[[ShippingDetails](#schemashippingdetails)]|true|none|none|

<h2 id="tocS_TransactionSummary">TransactionSummary</h2>
<!-- backwards compatibility -->
<a id="schematransactionsummary"></a>
<a id="schema_TransactionSummary"></a>
<a id="tocStransactionsummary"></a>
<a id="tocstransactionsummary"></a>

```json
{
  "type": "object",
  "required": [
    "capturedAmount",
    "refundedAmount",
    "remainingAmountToCapture",
    "remainingAmountToRefund"
  ],
  "properties": {
    "capturedAmount": {
      "type": "integer",
      "format": "int32",
      "description": "Total amount captured",
      "example": 20000
    },
    "refundedAmount": {
      "type": "integer",
      "format": "int32",
      "description": "Total refunded amount of the order",
      "example": 0
    },
    "remainingAmountToCapture": {
      "type": "integer",
      "format": "int32",
      "description": "Total remaining amount to capture",
      "example": 0
    },
    "remainingAmountToRefund": {
      "type": "integer",
      "format": "int32",
      "description": "Total remaining amount to refund",
      "example": 20000
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|capturedAmount|integer(int32)|true|none|Total amount captured|
|refundedAmount|integer(int32)|true|none|Total refunded amount of the order|
|remainingAmountToCapture|integer(int32)|true|none|Total remaining amount to capture|
|remainingAmountToRefund|integer(int32)|true|none|Total remaining amount to refund|

<h2 id="tocS_TransactionUpdateCallbackOneOf">TransactionUpdateCallbackOneOf</h2>
<!-- backwards compatibility -->
<a id="schematransactionupdatecallbackoneof"></a>
<a id="schema_TransactionUpdateCallbackOneOf"></a>
<a id="tocStransactionupdatecallbackoneof"></a>
<a id="tocstransactionupdatecallbackoneof"></a>

```json
{
  "oneOf": [
    {
      "type": "object",
      "required": [
        "merchantSerialNumber",
        "orderId",
        "shippingDetails",
        "userDetails",
        "transactionInfo"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        },
        "orderId": {
          "type": "string",
          "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
          "example": "order123abc",
          "pattern": "^[a-zA-Z0-9-]{1,30}$",
          "maxLength": 30
        },
        "shippingDetails": {
          "type": "object",
          "required": [
            "address",
            "shippingCost",
            "shippingMethod",
            "shippingMethodId"
          ],
          "properties": {
            "address": {
              "type": "object",
              "required": [
                "addressLine1",
                "city",
                "country",
                "postCode"
              ],
              "properties": {
                "addressLine1": {
                  "type": "string",
                  "description": "Address Line 1",
                  "example": "Dronning Eufemias gate 42"
                },
                "addressLine2": {
                  "type": "string",
                  "description": "Address Line 2",
                  "example": "Att: Rune Garborg"
                },
                "city": {
                  "type": "string",
                  "description": "City",
                  "example": "Oslo"
                },
                "country": {
                  "type": "string",
                  "description": "Country",
                  "example": "Norway",
                  "enum": [
                    "Norway"
                  ]
                },
                "postCode": {
                  "type": "string",
                  "description": "Post Code",
                  "example": 191
                }
              }
            },
            "shippingCost": {
              "type": "number",
              "format": "double",
              "description": "Shipping cost"
            },
            "shippingMethod": {
              "type": "string",
              "description": "Shipping method. Max length: 256 characters. Recommended length for readability on most screens: 25 characters.",
              "example": "Posten Servicepakke",
              "maxLength": 256
            },
            "shippingMethodId": {
              "type": "string"
            }
          }
        },
        "transactionInfo": {
          "type": "object",
          "required": [
            "amount",
            "status",
            "timeStamp",
            "transactionId"
          ],
          "properties": {
            "amount": {
              "type": "number",
              "format": "double",
              "description": "Ordered amount in øre",
              "example": 20000
            },
            "status": {
              "type": "string",
              "enum": [
                "RESERVE",
                "SALE",
                "CANCELLED",
                "REJECTED",
                "AUTO_CANCEL"
              ],
              "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#callbacks) for more information.",
              "example": "RESERVE"
            },
            "timeStamp": {
              "type": "string",
              "description": "Timestamp in ISO-8601 representing when the operation was performed.",
              "example": "2018-12-12T11:18:38.246Z"
            },
            "transactionId": {
              "type": "string",
              "description": "Vipps transaction id",
              "example": "5001420062"
            }
          }
        },
        "userDetails": {
          "type": "object",
          "required": [
            "email",
            "firstName",
            "lastName",
            "mobileNumber",
            "userId"
          ],
          "properties": {
            "bankIdVerified": {
              "type": "string",
              "description": "Optional Y/N string indicating if the user in bankId vertified, must be requested during onboarding.",
              "example": "Y",
              "enum": [
                "Y",
                "N"
              ]
            },
            "dateOfBirth": {
              "type": "string",
              "description": "Optional date of birth infomation, must be requested during onboarding.",
              "example": "12-3-1988"
            },
            "email": {
              "type": "string",
              "description": "Email address",
              "example": "user@example.com"
            },
            "firstName": {
              "type": "string",
              "description": "First name",
              "example": "Ada"
            },
            "lastName": {
              "type": "string",
              "description": "Last name",
              "example": "Lovelace"
            },
            "mobileNumber": {
              "type": "string",
              "description": "Mobile number",
              "example": "12345678",
              "minLength": 8,
              "maxLength": 12,
              "pattern": "^\\d{8,12}$"
            },
            "ssn": {
              "type": "string",
              "description": "Optional social security number for the user, must be requested during onboarding.",
              "example": "12345678901",
              "minLength": 11,
              "maxLength": 11,
              "pattern": "^\\d{11}$"
            },
            "userId": {
              "type": "string",
              "example": "uiJskNQ6qNN1iwN891uuob==",
              "maxLength": 50,
              "description": "Identifies a user in Vipps. Merchant is required to store this field for future references.",
              "pattern": "^[\\d\\w\\/=+]+$"
            }
          }
        },
        "errorInfo": {
          "type": "object",
          "properties": {
            "errorCode": {
              "type": "integer",
              "example": 45,
              "description": "The number code for the error."
            },
            "errorGroup": {
              "type": "string",
              "example": "PAYMENTS"
            },
            "errorMessage": {
              "type": "string",
              "description": "Description of the error",
              "example": "User has cancelled or not acted upon the payment"
            }
          }
        }
      }
    },
    {
      "type": "object",
      "required": [
        "merchantSerialNumber",
        "orderId",
        "transactionInfo"
      ],
      "properties": {
        "merchantSerialNumber": {
          "type": "string",
          "description": "Unique id for this merchant's sales channel: website, mobile app etc. Short name: MSN.",
          "minLength": 6,
          "maxLength": 6,
          "example": 123456,
          "pattern": "^\\d{6}$"
        },
        "orderId": {
          "type": "string",
          "description": "Id which uniquely identifies a payment. Maximum length is 30 alphanumeric characters: a-z, A-Z, 0-9 and '-'.",
          "example": "order123abc",
          "pattern": "^[a-zA-Z0-9-]{1,30}$",
          "maxLength": 30
        },
        "transactionInfo": {
          "type": "object",
          "required": [
            "amount",
            "status",
            "timeStamp",
            "transactionId"
          ],
          "properties": {
            "amount": {
              "type": "number",
              "format": "double",
              "description": "Ordered amount in øre",
              "example": 20000
            },
            "status": {
              "type": "string",
              "enum": [
                "RESERVE",
                "SALE",
                "CANCELLED",
                "REJECTED",
                "AUTO_CANCEL"
              ],
              "description": "Status which gives the current state of the payment within Vipps. See the [API guide](https://github.com/vippsas/vipps-ecom-api/blob/master/vipps-ecom-api.md#callbacks) for more information.",
              "example": "RESERVE"
            },
            "timeStamp": {
              "type": "string",
              "description": "Timestamp in ISO-8601 representing when the operation was performed.",
              "example": "2018-12-12T11:18:38.246Z"
            },
            "transactionId": {
              "type": "string",
              "description": "Vipps transaction id",
              "example": "5001420062"
            }
          }
        },
        "errorInfo": {
          "type": "object",
          "properties": {
            "errorCode": {
              "type": "integer",
              "example": 45,
              "description": "The number code for the error."
            },
            "errorGroup": {
              "type": "string",
              "example": "PAYMENTS"
            },
            "errorMessage": {
              "type": "string",
              "description": "Description of the error",
              "example": "User has cancelled or not acted upon the payment"
            }
          }
        }
      }
    }
  ]
}

```

### Properties

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ExpressCheckOutPaymentRequest](#schemaexpresscheckoutpaymentrequest)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[RegularCheckOutPaymentRequest](#schemaregularcheckoutpaymentrequest)|false|none|none|

