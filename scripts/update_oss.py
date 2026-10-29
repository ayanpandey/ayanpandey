"""Rewrite the README's open-source section from merged PRs (run by the daily workflow)."""
import json, os, re, urllib.parse, urllib.request

LOGIN, MIN_STARS, LIMIT = "ayanpandey", 50, 8


def get(url):
    req = urllib.request.Request(url, headers={
        "Authorization": "Bearer " + os.environ["GITHUB_TOKEN"],
        "Accept": "application/vnd.github+json", "User-Agent": "profile-readme"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


q = urllib.parse.quote(f"is:pr is:merged author:{LOGIN} -user:{LOGIN}")
prs = get(f"https://api.github.com/search/issues?q={q}&sort=updated&per_page=50")["items"]
stars, lines = {}, []
for pr in prs:
    repo = pr["repository_url"].split("/repos/")[1]
    if repo not in stars:
        stars[repo] = get(pr["repository_url"])["stargazers_count"]
    if stars[repo] >= MIN_STARS:
        lines.append(f"- [{pr['title']}]({pr['html_url']}) in **{repo}** ★{stars[repo]:,}")
    if len(lines) == LIMIT:
        break
section = "\n".join(lines) or "_First merged contributions coming soon._"
readme = open("README.md").read()
new = re.sub(r"<!-- OSS:START -->.*<!-- OSS:END -->",
             f"<!-- OSS:START -->\n{section}\n<!-- OSS:END -->", readme, flags=re.S)
if new != readme:
    open("README.md", "w").write(new)
    print("updated")
