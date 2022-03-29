from github import Github

g = Github("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")

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))