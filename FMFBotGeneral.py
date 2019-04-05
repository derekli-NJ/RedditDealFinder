import praw
import sys
import time

global loggedSubmissions
loggedSubmissions = []

def main_loop():
    while True:
        reddit = praw.Reddit(client_id = 'CLIENT ID HERE',
                             client_secret = 'CLIENT SECRET HERE',
                             username = 'YOUR REDDIT USERNAME HERE',
                             password = 'YOUR REDDIT PASSWORD HERE',
                             user_agent = 'FMF Bot',)
        subreddit = reddit.subreddit('frugalmalefashion')
        new_python = subreddit.new(limit = 5)        
        for submission in new_python:
            link = submission.url
            if not submission.stickied:
                if submission.title not in loggedSubmissions and submission.ups>=1 and "Discussion" not in submission.title:
                    message = "New Deal: " + submission.title + "\n\n" + "Link Here - " + link
                    loggedSubmissions.append(submission.title)
                    reddit.redditor('YOUR REDDIT USERNAME HERE').message('FMF Bot', message)
        time.sleep(60)

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)


