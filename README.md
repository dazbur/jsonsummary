jsonsummary
===========

Create a readable summary of JSON structure

## Example

Input json file (generated by http://www.json-generator.com/):
```
[
{
    "_id": "54aefaaadc91b6904659b55f",
    "index": 0,
    "guid": "e5b238e0-1702-4149-a148-e5ee07f3322f",
    "isActive": true,
    "balance": "$1,168.16",
    "picture": "http://placehold.it/32x32",
    "age": 26,
    "eyeColor": "blue",
    "name": "Klein Stein",
    "gender": "male",
    "company": "NAXDIS",
    "email": "kleinstein@naxdis.com",
    "phone": "+1 (802) 435-3455",
    "address": "537 Chester Street, Wollochet, Illinois, 7743",
    "about": "Qui amet labore nulla commodo dolor aliquip velit cupidatat enim. Magna reprehenderit id nisi ut aliqua minim nulla. Lorem amet est occaecat voluptate velit laborum dolor laboris. Consequat commodo exercitation fugiat minim deserunt eu amet sit ex et esse aliquip fugiat.\r\n",
    "registered": "2014-08-04T13:36:33 +04:00",
    "latitude": -89.808044,
    "longitude": -35.967001,
    "tags": [
    "officia",
    "nostrud",
    "fugiat",
    "dolore",
    "voluptate",
    "enim",
    "consequat"
    ],
    "friends": [
    {
        "id": 0,
        "name": "Rena Gay"
    },
    {
        "id": 1,
        "name": "Peggy Munoz"
    },
    {
        "id": 2,
        "name": "Erin Mccall"
    }
    ],
    "greeting": "Hello, Klein Stein! You have 2 unread messages.",
    "favoriteFruit": "apple"
},
...
...
more objects here
...
...
]
```

## Summary output
```
list of length 6
<type 'dict'>
----guid <type 'unicode'>
----index <type 'int'>
----favoriteFruit <type 'unicode'>
----latitude <type 'float'>
----company <type 'unicode'>
----email <type 'unicode'>
----picture <type 'unicode'>
----tags <type 'list'>
--------list of length 7
--------<type 'unicode'>
----registered <type 'unicode'>
----eyeColor <type 'unicode'>
----phone <type 'unicode'>
----address <type 'unicode'>
----friends <type 'list'>
--------list of length 3
--------<type 'dict'>
------------id <type 'int'>
------------name <type 'unicode'>
----isActive <type 'bool'>
----about <type 'unicode'>
----balance <type 'unicode'>
----name <type 'unicode'>
----gender <type 'unicode'>
----age <type 'int'>
----greeting <type 'unicode'>
----longitude <type 'float'>
----_id <type 'unicode'>
```
