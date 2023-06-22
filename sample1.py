import os
from github import Github

# Set up your GitHub API access token
access_token = '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'

# Create a PyGitHub instance using the access token
g = Github(access_token)

# Specify the GitHub username
username = 'ankpatil18'

# Get the GitHub user
user = g.get_user(username)

# Get the user's repositories
print("Repositories:")
for repo in user.get_repos():
    print(repo.name)

# Get the user's commits
print("\nCommits:")
for repo in user.get_repos():
    commits = repo.get_commits()
    for commit in commits:
        print(commit.commit.message)

# Get the user's issues
print("\nIssues:")
for repo in user.get_repos():
    issues = repo.get_issues(state='all')
    for issue in issues:
        print(issue.title)

