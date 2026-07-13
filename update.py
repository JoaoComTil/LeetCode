import os
from datetime import datetime

import requests

USERNAME = "Joao_G"

URL = "https://leetcode.com/graphql"

QUERY = """
query getUserProfile($username: String!) {
  matchedUser(username: $username) {
    submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
      }
    }
    profile {
      ranking
    }
  }
}
"""

headers = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "x-csrftoken": os.environ["LEETCODE_CSRF_TOKEN"],
    "Cookie": (
        f"LEETCODE_SESSION={os.environ['LEETCODE_SESSION']}; "
        f"csrftoken={os.environ['LEETCODE_CSRF_TOKEN']}"
    ),
}

payload = {
    "query": QUERY,
    "variables": {
        "username": USERNAME
    }
}

response = requests.post(URL, json=payload, headers=headers)
response.raise_for_status()

data = response.json()["data"]["matchedUser"]

stats = {}

for item in data["submitStatsGlobal"]["acSubmissionNum"]:
    stats[item["difficulty"]] = item["count"]

ranking = data["profile"]["ranking"]

readme = f"""# 👨‍💻 LeetCode Progress

Automatically updated using GitHub Actions.

## 📊 Statistics

| Difficulty | Solved |
|------------|-------:|
| Total | **{stats["All"]}** |
| Easy | **{stats["Easy"]}** |
| Medium | **{stats["Medium"]}** |
| Hard | **{stats["Hard"]}** |

## 🌎 Ranking

**{ranking:,}**

---

Last update: {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("README updated successfully.")