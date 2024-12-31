import os
import requests
import subprocess

# Function to get all repositories of a GitHub user
def get_repositories(username):
    # GitHub API endpoint to fetch the repositories
    api_url = f"https://api.github.com/users/{username}/repos"
    repos = []
    
    # Sending the request to GitHub API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        for repo in data:
            repos.append(repo['clone_url'])
    else:
        print(f"Failed to fetch repositories for {username}. Status code: {response.status_code}")
    
    return repos

# Function to clone all repositories
def clone_repositories(username):
    repos = get_repositories(username)
    
    if repos:
        # Loop through each repository and clone it
        for repo in repos:
            print(f"Cloning {repo}...")
            subprocess.run(["git", "clone", repo])
        print("All repositories have been cloned.")
    else:
        print("No repositories found to clone.")

if __name__ == "__main__":
    # Replace 'username' with the GitHub user's username
    username = input("Enter the GitHub username: ")
    clone_repositories(username)
