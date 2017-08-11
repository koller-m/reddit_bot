import praw
import time
import os

# Create Reddit instance
def bot_login():
    reddit = praw.Reddit("panic_bot", user_agent="praw01 v0.1 by /u/cryptoprodigydotcom")

    return reddit

def run_bot(reddit, comments_replied_to):
    for comment in reddit.subreddit("anxiety").comments(limit=25):
        if "panic attack" in comment.body and comment.id not in comments_replied_to and comment.author != reddit.user.me():
            print("Comment found!")
            comment.reply("Breathe... It will pass. Try inhaling through your nose to a count of 1, 2, 3, 4. Hold for 1, 2, 3, 4. Exhale through your mouth 1, 2, 3, 4. Repeat but don't over do it. It will pass. :)")
            comments_replied_to.append(comment.id)
            with open("saved_comments.txt", "a") as f:
                f.write(comment.id + "\n")

    print("Sleeping...")
    time.sleep(30)

def saved_comments():
    if not os.path.isfile("saved_comments.txt"):
        comments_replied_to = []
    else:

        with open("saved_comments.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to

reddit = bot_login()
comments_replied_to = saved_comments()
while True:
    run_bot(reddit, comments_replied_to)
