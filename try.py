import os
import git
import datetime

repo_path = "file path"  # Change this to your local repo path
commit_times = int(input("Enter the number of commits: "))

repo = git.Repo(repo_path)
assert not repo.bare

file_path = os.path.join(repo_path, "x.txt")

for i in range(commit_times):
  with open(file_path, "a") as file:
    file.write(f"Commit {i+1} on {datetime.datetime.now()}\n")

    repo.index.add([file_path])
    repo.index.commit(f"Automated commit {i+1}")
    print(f"Committed {i+1} times.")

origin = repo.remote(name="origin")
origin.push()
print("All commits pushed successfully!")
