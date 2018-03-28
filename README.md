# Quacker
A hybrid messaging app that is themed with Ducks!

## Requirements 
* Install Python 3 or above
* Install PostgreSQL
* Install Flask
* Install psycopg2

## Phase 1: How To run

Simply run the main.py program. In this phase we are
only interested in navigating some queries from the 
database using app routes. 

## Heroku Website:
* https://quacker-pr.herokuapp.com/

## URL Locations:
##### Main Page:
* /
##### Get User Locations: 
* /users
* /users/[int:uid]
* /users/active
##### Get Credential Locations:
* /credentials
* /credentials/user/[int:uid]
##### Get Activity Locations:
* /activities
* /activities/user/[int:uid]
##### Get Contact Locations:
* /contacts
* /contacts/user/[int:uid]
##### Get Chat Locations:
* /chats
* /chats/[int:cid]
* /chats/user/[int:uid]
* /chats/admin/[int:uid]
##### Get Participant Locations:
* /participants
* /participants/chat/[int:cid]
##### Get Messages Locations:
* /messages
* /messages/[int:mid]
* /messages/user/[int:uid]
* /messages/chat/[int:cid]
##### Get Media Locations:
* /medias
* /medias/chat/[int:cid]
* /medias/message/[int:mid]
##### Get Topic Locations:
* /topics
* /topics/chat/[int:cid]
* /topics/message/[int:mid]
* /topics/user/[int:mid]
##### Get Reaction Locations:
* /reactions
* /reactions/message/[int:mid]
* /reactions/user/[int:uid]
* /reactions/like
* /reactions/like/message/[int:mid]
* /reactions/dislike
* /reactions/dislike/message/[int:mid]

