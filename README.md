# Spider

## WebScraping for the Leadership research project.

## Installation

I suppose you have **Python 3.6+** and some kind of **Unix Terminal** installed.

## Ubuntu:

```shell
python3 -m venv spider 
cd spider
source bin/activate
pip3 install -r requirements.txt
```

## VK-API scraping

### Create your own VK App

1. Create your VK application [here](https://vk.com/apps?act=manage). 
You need a Standalone app. Get your `APP_ID` in the app's settings.

2. Create `execute stored procedures` in your app.
Find in the app's settings `Stored procedures`. Create new procedure `execute.singleLeader`:

```Javascript
var user = API.users.get({"user_ids": [Args.user], "fields": ["photo_id", "verified", "sex", "bdate", "city", "country", "home_town", "has_photo", "photo_50", "photo_100", "photo_200_orig", "photo_200", "photo_400_orig", "photo_max", "photo_max_orig", "online", "domain", "has_mobile", "contacts", "site", "education", "universities", "schools", "status", "last_seen", "followers_count", "common_count", "occupation", "nickname", "relatives", "relation", "personal", "connections", "exports", "activities", "interests", "music", "movies", "tv", "books", "games", "about", "quotes", "can_post", "can_see_all_posts", "can_see_audio", "can_write_private_message", "can_send_friend_request", "is_favorite", "is_hidden_from_feed", "timezone", "screen_name", "maiden_name", "crop_photo", "is_friend", "friend_status", "career", "military", "blacklisted", "blacklisted_by_me", "can_be_invited_group"]});

var groups = API.groups.get({"user_id": Args.user, "extended": 1});

var wall = API.wall.get({"owner_id": Args.user, "count": 100, "extended": 1});
  
return [user, groups, wall];
```

### Use existing VK App

3. Make sure you've downloaded `users.csv` file

4. ```python3 spider.py``` and follow the input instructions.

## You have to ensure you have the latest Firefox on your machine & path to the latest geckodriver in PATH variable!


### Usefull links

https://vk.com/dev/authcode_flow_user

https://vk.com/dev/methods

https://vk.com/dev/execute

https://vk.com/dev/users

https://vk.com/dev/groups

https://vk.com/dev/wall

https://vk.com/dev/likes 
