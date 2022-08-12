""" Testing mocks """
# pylint: disable=line-too-long,too-many-lines

ACCESS_TOKEN = {
    'token_type': 'Bearer',
    'expires_in': 3599,
    'ext_expires_in': 3599,
    'access_token': 'fake_value'
}

SITE_INFO = {
    '@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#sites/$entity',
    'createdDateTime': '2021-12-10T17:48:13.98Z',
    'description': '',
    'id': 'foo.sharepoint.com,foo,helloworld',
    'lastModifiedDateTime': '2022-01-04T23:49:31Z',
    'name': 'site_name',
    'webUrl': 'https://foo.sharepoint.com/sites/site_name',
    'displayName': 'site_name',
    'root': {},
    'siteCollection': {'hostname': 'foo.sharepoint.com'}
}

FILE_INFO = {
    '@odata.context': "https://graph.microsoft.com/v1.0/$metadata#sites('foo.sharepoint.com%2C52fc6f4e')/drive/root/$entity",
    '@microsoft.graph.downloadUrl': 'https://foo.sharepoint.com/sites/site_name/_layouts/15/download.aspx?UniqueId=some_unique_string&Translate=false&tempauth=some_auth_key&ApiVersion=2.0',
    'createdDateTime': '2021-12-22T23:41:18Z',
    'eTag': '"{some_random_key},1"',
    'id': '01A6XU6UHJNZT4',
    'lastModifiedDateTime': '2021-12-22T23:41:18Z',
    'name': 'fake_file.pdf',
    'webUrl': 'https://foo.sharepoint.com/sites/site_name/Shared%20Documents/fake_file.pdf',
    'cTag': '"c:{another_random_key},1"',
    'size': 13264,
    'createdBy': {
        'user': {
            'email': 'user@email.com',
            'id': 'users_id_123',
            'displayName': 'Bob Smith'
        }
    },
    'lastModifiedBy': {
        'user': {
            'email': 'user@email.com',
            'id': 'users_id_123',
            'displayName': 'Bob Smith'
        }
    },
    'parentReference': {
        'driveId': 'drive_id_123',
        'driveType': 'documentLibrary',
        'id': 'random_key_1',
        'path': '/drive/root:'},
        'file': {
            'mimeType': 'application/pdf',
            'hashes': {'quickXorHash': 'hash_value'
        }
    },
    'fileSystemInfo': {
        'createdDateTime': '2021-12-22T23:41:18Z',
        'lastModifiedDateTime': '2021-12-22T23:41:18Z'
    }
}

DRIVE_INFO = {
    '@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#drives/$entity',
    'createdDateTime': '2021-11-07T05:21:29Z',
    'description': '',
    'id': 'drive_id',
    'lastModifiedDateTime': '2021-12-23T22:30:41Z',
    'name': 'Documents',
    'webUrl': 'https://foo.sharepoint.com/sites/site_name/Shared%20Documents',
    'driveType': 'documentLibrary',
    'createdBy': {
        'user': {
            'displayName': 'user_name'
        }
    },
    'lastModifiedBy': {
        'user': {
            'email': 'user@email.com',
            'id': 'users_id_123',
            'displayName': 'Bob Smith'
        }
    },
    'owner': {
        'user': {
            'email': 'user@email.com',
            'id': 'users_id_123',
            'displayName': 'Bob Smith'
        }
    },
    'quota': {
        'deleted': 0,
        'remaining': 27487789064939,
        'state': 'normal',
        'total': 27487790694400,
        'used': 1629461
    }
}

DRIVE_ITEMS = {
    '@odata.context': "https://graph.microsoft.com/v1.0/$metadata#drives('b%21Tm_8Ug2dZ0avZ')/root/children",
    'value': [
        {
            'createdDateTime': '2021-12-23T22:30:41Z',
            'eTag': '"{EE7E29EE},1"',
            'id': '01A6XU6',
            'lastModifiedDateTime': '2021-12-23T22:30:41Z',
            'name': 'folder1', 'webUrl': 'https://host_name/sites/site_name/Shared%20Documents/folder1',
            'cTag': '"c:{EE7E29EE},0"',
            'size': 13264,
            'createdBy': {
                'user': {
                    'email': 'user@email.com',
                    'id': 'fc0de361',
                    'displayName': 'John Doe'
                }
            },
            'lastModifiedBy': {
                'user': {
                    'email': 'user@email.com',
                    'id': 'fc0de361',
                    'displayName': 'John Doe'
                }
            },
            'parentReference': {
                'driveId': 'b!Tm_8Ug2dZ0avZWxh',
                'driveType': 'documentLibrary',
                'id': '01A6XU6UF',
                'path': '/drives/b!Tm_8Ug2dZ0avZWxh/root:'
            },
            'fileSystemInfo': {
                'createdDateTime': '2021-12-23T22:30:41Z',
                'lastModifiedDateTime': '2021-12-23T22:30:41Z'
            },
            'folder': {'childCount': 1}
        },{
            '@microsoft.graph.downloadUrl': 'https://host_name/sites/site_name/_layouts/15/download.aspx?UniqueId=3f25ce76&Translate=false&tempauth=eyJ0eXAiOiJKV1QiIn0.eyJhdWQiOiIw&ApiVersion=2.0',
            'createdDateTime': '2021-12-23T22:30:20Z',
            'eTag': '"{3F25CE76},1"',
            'id': '01A6XU6UDWZYST',
            'lastModifiedDateTime': '2021-12-23T22:30:20Z',
            'name': 'fake_file 2.pdf',
            'webUrl': 'https://host_name/sites/site_name/Shared%20Documents/fake_file%202.pdf',
            'cTag': '"c:{3F25CE76},1"',
            'size': 13264,
            'createdBy': {
                'user': {
                    'email': 'user@email.com',
                    'id': 'fc0de361',
                    'displayName': 'Michael Smith'
                }
            },
            'lastModifiedBy': {
                'user': {
                    'email': 'user@email.com',
                    'id': 'fc0de361',
                    'displayName': 'Bob Roberts'
                }
            },
            'parentReference': {
                'driveId': 'b!Tm_8Ug2dZ0av',
                'driveType': 'documentLibrary',
                'id': '01A6XU6UF',
                'path': '/drives/b!Tm_8Ug2dZ0av/root:'
            },
            'file': {
                'mimeType': 'application/pdf',
                'hashes': {
                    'quickXorHash': '/Komu+V2='
                }
            },
            'fileSystemInfo': {
                'createdDateTime': '2021-12-23T22:30:20Z',
                'lastModifiedDateTime': '2021-12-23T22:30:20Z'
            }
        }
    ]
}

UPLOAD_SESSION = {
    '@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#microsoft.graph.uploadSession',
    'expirationDateTime': '2022-01-11T23:05:14.148Z',
    'nextExpectedRanges': ['0-'],
    'uploadUrl': "https://foo.sharepoint.com/sites/site_name/_api/v2.0/drives/drive_id/items/ite_id/uploadSession?guid='some-guid'&overwrite=True&rename=False&dc=0&tempauth=some-auth-key"
}

UPLOAD_CHUNK_RESPONSE = {
    '@odata.context': 'https://foo.sharepoint.com/sites/site_name/_api/v2.0/$metadata#items/$entity',
    '@content.downloadUrl': 'https://foo.sharepoint.com/sites/site_name/_layouts/15/download.aspx?UniqueId=unique_id&Translate=false&tempauth=some-auth-key&ApiVersion=2.0',
    'createdBy': {
        'application': {
            'id': 'app_id_123',
            'displayName': 'app-name-SharePoint-API'
        },
        'user': {
            'displayName': 'SharePoint App'
        }
    },
    'createdDateTime': '2022-01-18T22:40:21Z',
    'eTag': '"{tag_uid_},4"',
    'id': 'some_id',
    'lastModifiedBy':{
        'application': {
            'id': 'app_id_123',
            'displayName': 'app-name-SharePoint-API'
        },
        'user': {
            'displayName': 'SharePoint App'
        }
    },
    'lastModifiedDateTime': '2022-01-18T22:40:24Z',
    'name': 'file-name.png',
    'parentReference': {
        'driveId': 'drive_id_123',
        'driveType': 'documentLibrary',
        'id': 'some_id', 'path': '/drives/drive_id/root:/folder1/folder2'
    },
    'webUrl': 'https://foo.sharepoint.com/sites/site_name/Shared%20Documents/folder1/folder2/file-name.png',
    'cTag': '"c:{tag-id},4"',
    'file': {
        'hashes': {
            'quickXorHash': 'quick_hash_value'},
            'irmEnabled': False,
            'mimeType': 'image/png'
        },
    'fileSystemInfo': {
            'createdDateTime': '2022-01-18T22:40:21Z',
            'lastModifiedDateTime': '2022-01-18T22:40:24Z'
    },
    'image': {},
    'size': 135855
}

LIST_DEFINITION = {
    "displayName": "People",
    "columns": [
        {
            "name": "First Name",
            "text": {}
        },
        {
            "name": "Last Name",
            "text": {}
        },
        {
            "name": "Age",
            "number": {}
        }
    ]
}

CREATE_LIST_RESPONSE = {
    "id": "22e03ef3-6ef4-424d-a1d3-92a337807c30",
    "createdDateTime": "2017-04-30T01:21:00Z",
    "createdBy": {
        "user": {
            "displayName": "Ryan Gregg",
            "id": "8606e4d5-d582-4f5f-aeba-7d7c18b20cfd"
        }
    },
    "lastModifiedDateTime": "2016-08-30T08:26:00Z",
    "lastModifiedBy": {
        "user": {
            "displayName": "Ryan Gregg",
            "id": "8606e4d5-d582-4f5f-aeba-7d7c18b20cfd"
        }
    }
}

GET_LISTS_RESPONSE = {
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('site_id')/lists",
    "value": [
        {
            "@odata.etag": "\"9a319024\"",
            "createdDateTime": "2022-06-17T02:25:03Z",
            "description": "SharePointHome Cache List",
            "eTag": "\"9a319024\"",
            "id": "9a319024",
            "lastModifiedDateTime": "2022-07-05T22:12:15Z",
            "name": "SharePointHomeCacheList",
            "webUrl": "https://host_name/sites/site_name/Lists/SharePointHomeCacheList",
            "displayName": "SharePointHomeCacheList",
            "createdBy": {
                "user": {
                    "email": "user@test.com",
                    "id": "1f94788",
                    "displayName": "User Name"
                }
            },
            "parentReference": {
                "siteId": "site_id"
            },
            "list": {
                "contentTypesEnabled": False,
                "hidden": True,
                "template": "genericList"
            }
        },
        {
            "@odata.etag": "\"9bca6901\"",
            "createdDateTime": "2022-07-07T22:39:56Z",
            "description": "",
            "eTag": "\"9bca6901\"",
            "id": "9bca6901",
            "lastModifiedDateTime": "2022-07-07T22:49:53Z",
            "name": "Harry Potter Characters",
            "webUrl": "https://host_name/sites/site_name/Lists/Harry%20Potter%20Characters",
            "displayName": "Hogwarts",
            "createdBy": {
                "user": {
                    "email": "user@test.com",
                    "id": "fc0de361",
                    "displayName": "User Name"
                }
            },
            "lastModifiedBy": {
                "user": {
                    "email": "user@test.com",
                    "id": "fc0de361",
                    "displayName": "User Name"
                }
            },
            "parentReference": {
                "siteId": "site_id"
            },
            "list": {
                "contentTypesEnabled": False,
                "hidden": False,
                "template": "genericList"
            }
        },
        {
            "@odata.etag": "\"e6c0beff\"",
            "createdDateTime": "2022-07-07T22:28:36Z",
            "description": "This list stores run results for the Web Template Extensions feature.",
            "eTag": "\"e6c0beff\"",
            "id": "e6c0beff",
            "lastModifiedDateTime": "2022-07-07T22:39:56Z",
            "name": "wte",
            "webUrl": "https://host_name/sites/site_name/_catalogs/wte",
            "displayName": "Web Template Extensions",
            "createdBy": {
                "user": {
                    "email": "user@test.com",
                    "id": "fc0de361",
                    "displayName": "User Name"
                }
            },
            "parentReference": {
                "siteId": "site_id"
            },
            "list": {
                "contentTypesEnabled": False,
                "hidden": True,
                "template": "webTemplateExtensionsList"
            }
        },
        {
            "@odata.etag": "\"db21fecb\"",
            "createdDateTime": "2021-11-07T05:21:29Z",
            "description": "",
            "eTag": "\"db21fecb\"",
            "id": "db21fecb",
            "lastModifiedDateTime": "2022-07-05T22:12:15Z",
            "name": "Shared Documents",
            "webUrl": "https://host_name/sites/site_name/Shared%20Documents",
            "displayName": "Documents",
            "createdBy": {
                "user": {
                    "displayName": "System Account"
                }
            },
            "lastModifiedBy": {
                "user": {
                    "email": "user@test.com",
                    "id": "fc0de361",
                    "displayName": "User Name"
                }
            },
            "parentReference": {
                "siteId": "site_id"
            },
            "list": {
                "contentTypesEnabled": False,
                "hidden": False,
                "template": "documentLibrary"
            }
        }
    ]
}

GET_LIST_ITEMS_RESPONSE = {
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('site_id')/lists('list_id')/items",
    "value": [
        {
            "@odata.etag": "\"5962990b\"",
            "createdDateTime": "2022-07-07T22:40:48Z",
            "eTag": "\"5962990b\"",
            "id": "1",
            "lastModifiedDateTime": "2022-07-07T22:40:48Z",
            "webUrl": "https://host_name/sites/site_name/Lists/Harry%20Potter%20Characters/1_.000",
            "createdBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "lastModifiedBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "parentReference": {
                "siteId": "site_id"
            },
            "contentType": {
                "id": "0x010089A91AD5EBF8464CBF",
                "name": "Item"
            },
            "fields@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('site_id')/lists('list_id')/items('1')/fields/$entity",
            "fields": {
                "@odata.etag": "\"5962990b\"",
                "id": "1",
                "ContentType": "Item",
                "Title": "Harry Potter",
                "Modified": "2022-07-07T22:40:48Z",
                "Created": "2022-07-07T22:40:48Z",
                "AuthorLookupId": "13",
                "EditorLookupId": "13",
                "_UIVersionString": "1.0",
                "Attachments": False,
                "Edit": "",
                "LinkTitleNoMenu": "Harry Potter",
                "LinkTitle": "Harry Potter",
                "ItemChildCount": "0",
                "FolderChildCount": "0",
                "_ComplianceFlags": "",
                "_ComplianceTag": "",
                "_ComplianceTagWrittenTime": "",
                "_ComplianceTagUserId": "",
                "House": "Gryffindor"
            }
        },
        {
            "@odata.etag": "\"26883f79\"",
            "createdDateTime": "2022-07-07T22:42:06Z",
            "eTag": "\"26883f79\"",
            "id": "2",
            "lastModifiedDateTime": "2022-07-07T22:42:06Z",
            "webUrl": "https://host_name/sites/site_name/Lists/Harry%20Potter%20Characters/2_.000",
            "createdBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "lastModifiedBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "parentReference": {
                "siteId": "site_id"
            },
            "contentType": {
                "id": "0x010089A91AD5EBF8464CBF",
                "name": "Item"
            },
            "fields@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('site_id')/lists('list_id')/items('2')/fields/$entity",
            "fields": {
                "@odata.etag": "\"26883f79\"",
                "id": "2",
                "ContentType": "Item",
                "Title": "Thomas Marvolo Riddle",
                "Modified": "2022-07-07T22:42:06Z",
                "Created": "2022-07-07T22:42:06Z",
                "AuthorLookupId": "13",
                "EditorLookupId": "13",
                "_UIVersionString": "1.0",
                "Attachments": False,
                "Edit": "",
                "LinkTitleNoMenu": "Thomas Marvolo Riddle",
                "LinkTitle": "Thomas Marvolo Riddle",
                "ItemChildCount": "0",
                "FolderChildCount": "0",
                "_ComplianceFlags": "",
                "_ComplianceTag": "",
                "_ComplianceTagWrittenTime": "",
                "_ComplianceTagUserId": "",
                "House": "Slytherin"
            }
        },
        {
            "@odata.etag": "\"aca3a27a\"",
            "createdDateTime": "2022-07-07T22:43:54Z",
            "eTag": "\"aca3a27a\"",
            "id": "3",
            "lastModifiedDateTime": "2022-07-07T22:43:54Z",
            "webUrl": "https://host_name/sites/site_name/Lists/Harry%20Potter%20Characters/3_.000",
            "createdBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "lastModifiedBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "parentReference": {
                "siteId": "site_id"
            },
            "contentType": {
                "id": "0x010089A91AD5EBF8464CBF",
                "name": "Item"
            },
            "fields@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('site_id')/lists('list_id')/items('3')/fields/$entity",
            "fields": {
                "@odata.etag": "\"aca3a27a\"",
                "id": "3",
                "ContentType": "Item",
                "Title": "Hermione Granger",
                "Modified": "2022-07-07T22:43:54Z",
                "Created": "2022-07-07T22:43:54Z",
                "AuthorLookupId": "13",
                "EditorLookupId": "13",
                "_UIVersionString": "1.0",
                "Attachments": False,
                "Edit": "",
                "LinkTitleNoMenu": "Hermione Granger",
                "LinkTitle": "Hermione Granger",
                "ItemChildCount": "0",
                "FolderChildCount": "0",
                "_ComplianceFlags": "",
                "_ComplianceTag": "",
                "_ComplianceTagWrittenTime": "",
                "_ComplianceTagUserId": "",
                "House": "Gryffindor"
            }
        },
        {
            "@odata.etag": "\"e95e241c\"",
            "createdDateTime": "2022-07-07T22:45:04Z",
            "eTag": "\"e95e241c\"",
            "id": "4",
            "lastModifiedDateTime": "2022-07-07T22:45:04Z",
            "webUrl": "https://host_name/sites/site_name/Lists/Harry%20Potter%20Characters/4_.000",
            "createdBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "lastModifiedBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "parentReference": {
                "siteId": "site_id"
            },
            "contentType": {
                "id": "0x010089A91AD5EBF8464CBF",
                "name": "Item"
            },
            "fields@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('site_id')/lists('list_id')/items('4')/fields/$entity",
            "fields": {
                "@odata.etag": "\"e95e241c\"",
                "id": "4",
                "ContentType": "Item",
                "Title": "Cedric Diggory",
                "Modified": "2022-07-07T22:45:04Z",
                "Created": "2022-07-07T22:45:04Z",
                "AuthorLookupId": "13",
                "EditorLookupId": "13",
                "_UIVersionString": "1.0",
                "Attachments": False,
                "Edit": "",
                "LinkTitleNoMenu": "Cedric Diggory",
                "LinkTitle": "Cedric Diggory",
                "ItemChildCount": "0",
                "FolderChildCount": "0",
                "_ComplianceFlags": "",
                "_ComplianceTag": "",
                "_ComplianceTagWrittenTime": "",
                "_ComplianceTagUserId": "",
                "House": "Hufflepuff"
            }
        },
        {
            "@odata.etag": "\"c8941c7c\"",
            "createdDateTime": "2022-07-07T22:46:23Z",
            "eTag": "\"c8941c7c\"",
            "id": "5",
            "lastModifiedDateTime": "2022-07-07T22:46:23Z",
            "webUrl": "https://host_name/sites/site_name/Lists/Harry%20Potter%20Characters/5_.000",
            "createdBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "lastModifiedBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "parentReference": {
                "siteId": "site_id"
            },
            "contentType": {
                "id": "0x010089A91AD5EBF8464CBF",
                "name": "Item"
            },
            "fields@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('site_id')/lists('list_id')/items('5')/fields/$entity",
            "fields": {
                "@odata.etag": "\"c8941c7c\"",
                "id": "5",
                "ContentType": "Item",
                "Title": "Draco Malfoy",
                "Modified": "2022-07-07T22:46:23Z",
                "Created": "2022-07-07T22:46:23Z",
                "AuthorLookupId": "13",
                "EditorLookupId": "13",
                "_UIVersionString": "1.0",
                "Attachments": False,
                "Edit": "",
                "LinkTitleNoMenu": "Draco Malfoy",
                "LinkTitle": "Draco Malfoy",
                "ItemChildCount": "0",
                "FolderChildCount": "0",
                "_ComplianceFlags": "",
                "_ComplianceTag": "",
                "_ComplianceTagWrittenTime": "",
                "_ComplianceTagUserId": "",
                "House": "Slytherin"
            }
        },
        {
            "@odata.etag": "\"c7e9fa10\"",
            "createdDateTime": "2022-07-07T22:49:35Z",
            "eTag": "\"c7e9fa10\"",
            "id": "6",
            "lastModifiedDateTime": "2022-07-07T22:49:35Z",
            "webUrl": "https://host_name/sites/site_name/Lists/Harry%20Potter%20Characters/6_.000",
            "createdBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "lastModifiedBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "parentReference": {
                "siteId": "site_id"
            },
            "contentType": {
                "id": "0x010089A91AD5EBF8464CBF",
                "name": "Item"
            },
            "fields@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('site_id')/lists('list_id')/items('6')/fields/$entity",
            "fields": {
                "@odata.etag": "\"c7e9fa10\"",
                "id": "6",
                "ContentType": "Item",
                "Title": "Ron Weasley",
                "Modified": "2022-07-07T22:49:35Z",
                "Created": "2022-07-07T22:49:35Z",
                "AuthorLookupId": "13",
                "EditorLookupId": "13",
                "_UIVersionString": "1.0",
                "Attachments": False,
                "Edit": "",
                "LinkTitleNoMenu": "Ron Weasley",
                "LinkTitle": "Ron Weasley",
                "ItemChildCount": "0",
                "FolderChildCount": "0",
                "_ComplianceFlags": "",
                "_ComplianceTag": "",
                "_ComplianceTagWrittenTime": "",
                "_ComplianceTagUserId": "",
                "House": "Gryffindor"
            }
        },
        {
            "@odata.etag": "\"2c114756\"",
            "createdDateTime": "2022-07-07T22:49:53Z",
            "eTag": "\"2c114756\"",
            "id": "7",
            "lastModifiedDateTime": "2022-07-07T22:49:53Z",
            "webUrl": "https://host_name/sites/site_name/Lists/Harry%20Potter%20Characters/7_.000",
            "createdBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "lastModifiedBy": {
                "user": {
                    "email": "user@user.com",
                    "id": "fc0de361",
                    "displayName": "Username"
                }
            },
            "parentReference": {
                "siteId": "site_id"
            },
            "contentType": {
                "id": "0x010089A91AD5EBF8464CBF",
                "name": "Item"
            },
            "fields@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('site_id')/lists('list_id')/items('7')/fields/$entity",
            "fields": {
                "@odata.etag": "\"2c114756\"",
                "id": "7",
                "ContentType": "Item",
                "Title": "Cho Chang",
                "Modified": "2022-07-07T22:49:53Z",
                "Created": "2022-07-07T22:49:53Z",
                "AuthorLookupId": "13",
                "EditorLookupId": "13",
                "_UIVersionString": "1.0",
                "Attachments": False,
                "Edit": "",
                "LinkTitleNoMenu": "Cho Chang",
                "LinkTitle": "Cho Chang",
                "ItemChildCount": "0",
                "FolderChildCount": "0",
                "_ComplianceFlags": "",
                "_ComplianceTag": "",
                "_ComplianceTagWrittenTime": "",
                "_ComplianceTagUserId": "",
                "House": "Ravenclaw"
            }
        }
    ]
}

GET_LIST_COLUMNS_RESPONSE = {
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('site_id')/lists('list_id')/columns",
    "value": [
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "ID",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "1d22ea11",
            "indexed": False,
            "name": "ID",
            "readOnly": True,
            "required": False
        },
        {
            "columnGroup": "_Hidden",
            "description": "",
            "displayName": "Content Type",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "c042a256",
            "indexed": False,
            "name": "ContentType",
            "readOnly": False,
            "required": False
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Title",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "fa564e0f",
            "indexed": False,
            "name": "Title",
            "readOnly": False,
            "required": True,
            "text": {
                "allowMultipleLines": False,
                "appendChangesToExistingText": False,
                "linesForEditing": 0,
                "maxLength": 255
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Modified",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "28cf69c5",
            "indexed": False,
            "name": "Modified",
            "readOnly": True,
            "required": False,
            "dateTime": {
                "displayAs": "default",
                "format": "dateTime"
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Created",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "8c06beca",
            "indexed": False,
            "name": "Created",
            "readOnly": True,
            "required": False,
            "dateTime": {
                "displayAs": "default",
                "format": "dateTime"
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Created By",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "1df5e554",
            "indexed": False,
            "name": "Author",
            "readOnly": True,
            "required": False,
            "personOrGroup": {
                "allowMultipleSelection": False,
                "displayAs": "nameWithPresence",
                "chooseFromType": "peopleAndGroups"
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Modified By",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "d31655d1",
            "indexed": False,
            "name": "Editor",
            "readOnly": True,
            "required": False,
            "personOrGroup": {
                "allowMultipleSelection": False,
                "displayAs": "nameWithPresence",
                "chooseFromType": "peopleAndGroups"
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Version",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "dce8262a",
            "indexed": False,
            "name": "_UIVersionString",
            "readOnly": True,
            "required": False,
            "text": {
                "allowMultipleLines": False,
                "appendChangesToExistingText": False,
                "linesForEditing": 0,
                "maxLength": 255
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Attachments",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "67df98f4",
            "indexed": False,
            "name": "Attachments",
            "readOnly": False,
            "required": False
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Edit",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "503f1caa",
            "indexed": False,
            "name": "Edit",
            "readOnly": True,
            "required": False
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Title",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "bc91a437",
            "indexed": False,
            "name": "LinkTitleNoMenu",
            "readOnly": True,
            "required": False
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Name",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "82642ec8",
            "indexed": False,
            "name": "LinkTitle",
            "readOnly": True,
            "required": False
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Type",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "081c6e4c",
            "indexed": False,
            "name": "DocIcon",
            "readOnly": True,
            "required": False
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Item Child Count",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "b824e17e",
            "indexed": False,
            "name": "ItemChildCount",
            "readOnly": True,
            "required": False,
            "lookup": {
                "allowMultipleValues": False,
                "allowUnlimitedLength": False,
                "columnName": "ItemChildCount",
                "listId": "",
                "primaryLookupColumnId": "ID"
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Folder Child Count",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "960ff01f",
            "indexed": False,
            "name": "FolderChildCount",
            "readOnly": True,
            "required": False,
            "lookup": {
                "allowMultipleValues": False,
                "allowUnlimitedLength": False,
                "columnName": "FolderChildCount",
                "listId": "",
                "primaryLookupColumnId": "ID"
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Label setting",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "ccc1037f",
            "indexed": False,
            "name": "_ComplianceFlags",
            "readOnly": True,
            "required": False,
            "lookup": {
                "allowMultipleValues": False,
                "allowUnlimitedLength": False,
                "columnName": "ComplianceFlags",
                "listId": "",
                "primaryLookupColumnId": "ID"
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Retention label",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "d4b6480a",
            "indexed": False,
            "name": "_ComplianceTag",
            "readOnly": True,
            "required": False,
            "lookup": {
                "allowMultipleValues": False,
                "allowUnlimitedLength": False,
                "columnName": "ComplianceTag",
                "listId": "",
                "primaryLookupColumnId": "ID"
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Retention label Applied",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "92be610e",
            "indexed": False,
            "name": "_ComplianceTagWrittenTime",
            "readOnly": True,
            "required": False,
            "lookup": {
                "allowMultipleValues": False,
                "allowUnlimitedLength": False,
                "columnName": "ComplianceTagWrittenTime",
                "listId": "",
                "primaryLookupColumnId": "ID"
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Label applied by",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "418d7676",
            "indexed": False,
            "name": "_ComplianceTagUserId",
            "readOnly": True,
            "required": False,
            "lookup": {
                "allowMultipleValues": False,
                "allowUnlimitedLength": False,
                "columnName": "ComplianceTagUserId",
                "listId": "",
                "primaryLookupColumnId": "ID"
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "App Created By",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "6bfaba20",
            "indexed": False,
            "name": "AppAuthor",
            "readOnly": True,
            "required": False,
            "lookup": {
                "allowMultipleValues": False,
                "allowUnlimitedLength": False,
                "columnName": "Title",
                "listId": "AppPrincipals"
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "App Modified By",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "e08400f3",
            "indexed": False,
            "name": "AppEditor",
            "readOnly": True,
            "required": False,
            "lookup": {
                "allowMultipleValues": False,
                "allowUnlimitedLength": False,
                "columnName": "Title",
                "listId": "AppPrincipals"
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Compliance Asset Id",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "3a6b296c",
            "indexed": False,
            "name": "ComplianceAssetId",
            "readOnly": True,
            "required": False,
            "text": {
                "allowMultipleLines": False,
                "appendChangesToExistingText": False,
                "linesForEditing": 0,
                "maxLength": 255
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "House",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "d63926b5",
            "indexed": False,
            "name": "House",
            "readOnly": False,
            "required": False,
            "choice": {
                "allowTextEntry": False,
                "choices": [
                    "Gryffindor",
                    "Slytherin",
                    "Hufflepuff",
                    "Ravenclaw"
                ],
                "displayAs": "dropDownMenu"
            }
        },
        {
            "columnGroup": "Custom Columns",
            "description": "",
            "displayName": "Item is a Record",
            "enforceUniqueValues": False,
            "hidden": False,
            "id": "8382d247",
            "indexed": False,
            "name": "_IsRecord",
            "readOnly": True,
            "required": False
        }
    ]
}

LIST_ITEM = {
    "Title": "Albus Dumbledore",
    "House": "Gryffindor"
}

ADD_ITEM_RESPONSE = {
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('site_id')/lists('Hogwarts%20Directory')/items/$entity",
    "@odata.etag": "\"ea196da0\"",
    "createdDateTime": "2022-07-09T01:24:16Z",
    "eTag": "\"ea196da0\"",
    "id": "8",
    "lastModifiedDateTime": "2022-07-09T01:24:16Z",
    "webUrl": "https://host_name/sites/site_name/Lists/Harry%20Potter%20Characters/8_.000",
    "createdBy": {
        "user": {
            "email": "user@user.com",
            "id": "fc0de361",
            "displayName": "Username"
        }
    },
    "lastModifiedBy": {
        "application": {
            "id": "de8bc8b5",
            "displayName": "Graph explorer"
        },
        "user": {
            "email": "user@user.com",
            "id": "fc0de361",
            "displayName": "Username"
        }
    },
    "parentReference": {
        "siteId": "site_id"
    },
    "contentType": {
        "id": "0x010089A91AD5EBF8464CBF",
        "name": "Item"
    },
    "fields@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('site_id')/lists('Hogwarts%20Directory')/items('8')/fields/$entity",
    "fields": {
        "@odata.etag": "\"ea196da0\"",
        "id": "8",
        "ContentType": "Item",
        "Title": "Albus Dumbledore",
        "Modified": "2022-07-09T01:24:16Z",
        "Created": "2022-07-09T01:24:16Z",
        "AuthorLookupId": "13",
        "EditorLookupId": "13",
        "_UIVersionString": "1.0",
        "Attachments": False,
        "Edit": "",
        "LinkTitleNoMenu": "Albus Dumbledore",
        "LinkTitle": "Albus Dumbledore",
        "ItemChildCount": "0",
        "FolderChildCount": "0",
        "_ComplianceFlags": "",
        "_ComplianceTag": "",
        "_ComplianceTagWrittenTime": "",
        "_ComplianceTagUserId": "",
        "AppAuthorLookupId": "19",
        "AppEditorLookupId": "19",
        "House": "Gryffindor"
    }
}

UPDATE_ITEM_REQUEST = {
    "Title": "Albus Dumbledore1"
}

UPDATE_ITEM_RESPONSE = {
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('site_id')/lists('Hogwarts%20Directory')/items('8')/fields/$entity",
    "@odata.etag": "\"ea196da0\"",
    "id": "8",
    "ContentType": "Item",
    "Title": "Albus Dumbledore1",
    "Modified": "2022-07-11T21:15:09Z",
    "Created": "2022-07-09T01:24:16Z",
    "AuthorLookupId": "13",
    "EditorLookupId": "13",
    "_UIVersionString": "2.0",
    "Attachments": False,
    "Edit": "",
    "LinkTitleNoMenu": "Albus Dumbledore1",
    "LinkTitle": "Albus Dumbledore1",
    "ItemChildCount": "0",
    "FolderChildCount": "0",
    "_ComplianceFlags": "",
    "_ComplianceTag": "",
    "_ComplianceTagWrittenTime": "",
    "_ComplianceTagUserId": "",
    "AppAuthorLookupId": "19",
    "AppEditorLookupId": "19",
    "House": "Gryffindor"
}

INVALID_REQUEST = {
    "error": {
        "code": "invalidRequest",
        "message": "Field 'Name' is not recognized",
        "innerError": {
            "date": "2022-07-14T23:02:20",
            "request-id": "0ce9ef3d",
            "client-request-id": "06566d94"
        }
    }
}

SUBSITES = {
    "value": [
        {
            "id": "contoso.sharepoint.com,da60e844",
            "name": "Team A Subsite",
            "description": "",
            "createdDateTime": "2016-10-18T03:05:59Z",
            "lastModifiedDateTime": "2016-10-18T10:40:59Z",
            "webUrl": "https://contoso.sharepoint.com/sites/site/subsiteA"
        },
        {
            "id": "contoso.sharepoint.com,da60e844",
            "name": "Team B Subsite",
            "description": "",
            "createdDateTime": "2016-10-18T03:05:59Z",
            "lastModifiedDateTime": "2016-10-18T10:40:59Z",
            "webUrl": "https://contoso.sharepoint.com/sites/site/subsiteB"
        }
    ]
}
