import praw

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="SavedPostsDownloader by u/YOUR_USERNAME",
    username="YOUR_REDDIT_USERNAME",
    password="YOUR_REDDIT_PASSWORD"
)

with open("saved_posts.txt", "w") as f:
    for item in reddit.user.me().saved(limit=None):
        if isinstance(item, praw.models.Submission):
            f.write(f"{item.title} - {item.url}\n")

print("Saved posts exported to saved_posts.txt")
