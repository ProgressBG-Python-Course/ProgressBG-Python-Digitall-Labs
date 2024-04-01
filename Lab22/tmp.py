import json

json_str = '''{
    "content": {
        "name": "kpi222.json",
        "path": "kpi222.json",
        "sha": "1ff272201fd1e39b2083d00ad81da6b982b8ddd4",
        "size": 432,
        "url": "https://api.github.com/repos/ProgressBG-Python-Course/Shared/contents/kpi222.json?ref=main",
        "html_url": "https://github.com/ProgressBG-Python-Course/Shared/blob/main/kpi222.json",
        "git_url": "https://api.github.com/repos/ProgressBG-Python-Course/Shared/git/blobs/1ff272201fd1e39b2083d00ad81da6b982b8ddd4",
        "download_url": "https://raw.githubusercontent.com/ProgressBG-Python-Course/Shared/main/kpi222.json",
        "type": "file",
        "_links": {
            "self": "https://api.github.com/repos/ProgressBG-Python-Course/Shared/contents/kpi222.json?ref=main",
            "git": "https://api.github.com/repos/ProgressBG-Python-Course/Shared/git/blobs/1ff272201fd1e39b2083d00ad81da6b982b8ddd4",
            "html": "https://github.com/ProgressBG-Python-Course/Shared/blob/main/kpi222.json"
        }
    },
    "commit": {
        "sha": "8b829c359e05b9051c12311ac568540b7f9a0a5a",
        "node_id": "C_kwDOLl3E9doAKDhiODI5YzM1OWUwNWI5MDUxYzEyMzExYWM1Njg1NDBiN2Y5YTBhNWE",
        "url": "https://api.github.com/repos/ProgressBG-Python-Course/Shared/git/commits/8b829c359e05b9051c12311ac568540b7f9a0a5a",
        "html_url": "https://github.com/ProgressBG-Python-Course/Shared/commit/8b829c359e05b9051c12311ac568540b7f9a0a5a",
        "author": {
            "name": "Iva Popova",
            "email": "37480988+ProgressBG-Python-Course@users.noreply.github.com",
            "date": "2024-04-01T14:14:18Z"
        },
        "committer": {
            "name": "Iva Popova",
            "email": "37480988+ProgressBG-Python-Course@users.noreply.github.com",
            "date": "2024-04-01T14:14:18Z"
        },
        "tree": {
            "sha": "5799c97b57aa1d947e84556659a352a449275df6",
            "url": "https://api.github.com/repos/ProgressBG-Python-Course/Shared/git/trees/5799c97b57aa1d947e84556659a352a449275df6"
        },
        "message": "Upload file via API",
        "parents": [
            {
                "sha": "790a4a300c54875f16df96d7440f8d1a47ae0363",
                "url": "https://api.github.com/repos/ProgressBG-Python-Course/Shared/git/commits/790a4a300c54875f16df96d7440f8d1a47ae0363",
                "html_url": "https://github.com/ProgressBG-Python-Course/Shared/commit/790a4a300c54875f16df96d7440f8d1a47ae0363"
            }
        ],
        "verification": {
            "verified": false,
            "reason": "unsigned",
            "signature": null,
            "payload": null
        }
    }
}
'''


data = json.loads(json_str)
sha = data['content']['sha']
print(sha)