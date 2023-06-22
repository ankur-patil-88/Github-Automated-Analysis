import os
from github import Github
from github.GithubException import GithubException

# Set up your GitHub API access token
access_token = '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'

# Create a PyGitHub instance using the access token
g = Github(access_token)

# Specify the GitHub username
username = 'ankpatil18'

# Get the GitHub user
user = g.get_user(username)

# Initialize variables to track the most complex repository
most_complex_repo = None
complexity_score = 0

try:
    # Get the user's repositories
    repositories = user.get_repos()

    # Check if the user has repositories
    if repositories.totalCount > 0:
        # Iterate through the user's repositories
        for repo in repositories:
            print(repo.name)
            try:
                # Calculate complexity score based on factors of your choice
                size = repo.size
                contributors = repo.get_contributors().totalCount
                commits = repo.get_commits().totalCount
                pull_requests = repo.get_pulls().totalCount
                issues = repo.get_issues().totalCount

                complexity_score = size + contributors + commits + pull_requests + issues

                # Update the most complex repository if the current repository has a higher complexity score
                if complexity_score > complexity_score:
                    most_complex_repo = repo
                    complexity_score = complexity_score
            except GithubException as e:
                if e.status == 409 and "Git Repository is empty." in str(e):
                    print(f"Empty repository: {repo.name}")
                else:
                    raise e

        # Print the most complex repository's details
        if most_complex_repo:
            print("Most Complex Repository:")
            print("Repository Name:", most_complex_repo.name)
            print("Description:", most_complex_repo.description)
            print("URL:", most_complex_repo.html_url)
        else:
            print("No non-empty repositories found for the user:", username)
    else:
        print("No repositories found for the user:", username)

except GithubException as e:
    if e.status == 404:
        print("User not found.")
    else:
        raise e
