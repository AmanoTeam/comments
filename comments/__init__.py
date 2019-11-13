import urllib3
import json
from .errors import CommentsError
from .etc import CustomDict


http = urllib3.PoolManager()

headers = {'Content-Type': 'application/json'}


class Client:
    def __init__(self, api_key, owner_id=None):
        self.api_key = api_key
        self.owner_id = owner_id

    def create_post(self, owner_id=None, type='text', text=None, photo_url=None, caption=None, parse_mode=None,
                    administrators=None, disable_notifications=None):
        owner_id = owner_id or self.owner_id

        if type.lower() == 'text':
            dic = dict(api_key=self.api_key, owner_id=owner_id, type=type, text=text, parse_mode=parse_mode,
                       administrators=administrators)

        elif type.lower() == 'photo':
            dic = dict(api_key=self.api_key, owner_id=owner_id, type=type, photo_url=photo_url, caption=caption,
                       parse_mode=parse_mode, administrators=administrators, disable_notifications=disable_notifications)

        else:
            raise ValueError("Unsupported type '%s'" % type)

        # Clear None values from dict to avoid API errors
        dic = {x: y for x, y in dic.items() if y is not None}

        data = json.dumps(dic)
        r = http.request('POST', 'https://api.comments.bot/createPost', body=data, headers=headers)
        json_ = json.loads(r.data)
        if json_['ok']:
            super().__setattr__('post_id', json_['result']['post_id'])
            super().__setattr__('link', json_['result']['link'])
        else:
            raise CommentsError(json_['error'])

        return CustomDict(json_['result'])

    def edit_post(self, post_id, text=None, photo_url=None, caption=None, parse_mode=None):
        dic = dict(api_key=self.api_key, post_id=post_id, text=text, photo_url=photo_url,
                   caption=caption, parse_mode=parse_mode)

        # Clear None values from dict to avoid API errors
        dic = {x: y for x, y in dic.items() if y is not None}

        data = json.dumps(dic)
        r = http.request('POST', 'https://api.comments.bot/editPost', body=data, headers=headers)
        return json.loads(r.data)['ok']

    def delete_post(self, post_id):
        dic = dict(api_key=self.api_key, post_id=post_id)
        data = json.dumps(dic)
        r = http.request('POST', 'https://api.comments.bot/deletePost', body=data, headers=headers)
        return json.loads(r.data)['ok']

    # aliases
    createPost = create_post
    editPost = edit_post
    deletePost = delete_post
