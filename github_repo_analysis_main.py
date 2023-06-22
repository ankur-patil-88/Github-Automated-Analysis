import os
import streamlit as st
from github import Github
from github.GithubException import GithubException
from dotenv import load_dotenv

load_dotenv()

# Set up your GitHub API access token
access_token = os.getenv("GITHUB_API_KEY")

# Create a PyGitHub instance using the access token
g = Github(access_token)

# Function to calculate complexity score
def calculate_complexity_score(repo):
    size = repo.size
    contributors = repo.get_contributors().totalCount
    commits = repo.get_commits().totalCount
    pull_requests = repo.get_pulls().totalCount
    issues = repo.get_issues().totalCount

    repo_complexity_score = size + contributors + commits + pull_requests + issues
    return repo_complexity_score

# Streamlit app
st.title("GitHub Repository Analyzer")

# Input GitHub username
username = st.text_input("Enter GitHub username:")

if st.button("Analyze"):
    try:
        # Get the GitHub user
        user = g.get_user(username)

        # Get the user's repositories
        repositories = user.get_repos()

        # Check if the user has repositories
        if repositories.totalCount > 0:
            most_complex_repo = None
            complexity_score = 0

            # Iterate through the user's repositories
            for repo in repositories:
                try:
                    # Calculate complexity score
                    repo_complexity_score = calculate_complexity_score(repo)

                    # Update the most complex repository if the current repository has a higher complexity score
                    if repo_complexity_score > complexity_score:
                        most_complex_repo = repo
                        complexity_score = repo_complexity_score
                except GithubException as e:
                    if e.status == 409 and "Git Repository is empty." in str(e):
                        st.write(f"Empty repository: {repo.name}")
                    else:
                        raise e

            # Display the most complex repository's details
            if most_complex_repo:
                st.write("Most Complex Repository:")
                st.write("Repository Name:", most_complex_repo.name)
                st.write("Description:", most_complex_repo.description)
                st.write("URL:", most_complex_repo.html_url)
            else:
                st.write("No non-empty repositories found for the user:", username)
        else:
            st.write("No repositories found for the user:", username)

    except GithubException as e:
        if e.status == 404:
            st.write("User not found.")
        else:
            raise e
