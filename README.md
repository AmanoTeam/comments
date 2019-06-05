# comments
![PyPi](https://img.shields.io/pypi/v/comments.svg)
![Python 3](https://img.shields.io/badge/Python-3-2255cc.svg)

A simple Python wrapper for the https://comments.bot API.

## Basic usage

```python
import comments

client = comments.Client("YOUR_API_KEY_HERE", owner_id=YOUR_USER_ID_HERE)

post = client.createPost(type="text", text="Hello world")

print(post.post_id)
print(post.link)
```
##### You will get something like this:

```
xxxxxxxx
https://comments.bot/thread/xxxxxxxx
```

### createPost() arguments:

#### owner_id:
required if not passed on Client.

#### type:
must be `text` or `photo`. `text` is used by default if not specified.

#### text:
required if `type` equals to `text`. It must be a string betwen 0-4056 characters.

#### photo_url:
required if `type` equals to `photo`. It must be a string containing a link to the image.

#### caption:
Caption for the image. Only valid for `photo` type.

#### parse_mode:
Parse mode for the text/caption. It must be `markdown` or `html`.

#### administrators:
A string with user_ids (numbers) separated by comma. Example: `123456789,987654321,012345678`.

#### disable_notifications:
Pass True if you don't want to receive notifications about new comments for your post.