""" Testing mocks """
# pylint: disable=line-too-long

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
            'name': 'folder1', 'webUrl': 'https://sfgov1.sharepoint.com/sites/site_name/Shared%20Documents/folder1',
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
            '@microsoft.graph.downloadUrl': 'https://sfgov1.sharepoint.com/sites/site_name/_layouts/15/download.aspx?UniqueId=3f25ce76&Translate=false&tempauth=eyJ0eXAiOiJKV1QiIn0.eyJhdWQiOiIw&ApiVersion=2.0',
            'createdDateTime': '2021-12-23T22:30:20Z',
            'eTag': '"{3F25CE76},1"',
            'id': '01A6XU6UDWZYST',
            'lastModifiedDateTime': '2021-12-23T22:30:20Z',
            'name': 'fake_file 2.pdf',
            'webUrl': 'https://sfgov1.sharepoint.com/sites/site_name/Shared%20Documents/fake_file%202.pdf',
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
