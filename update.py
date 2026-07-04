from datetime import datetime

stats = {
    "total": 42,
    "easy": 20,
    "medium": 18,
    "hard": 4
}

content = f"""# LeetCode Stats

Last update: {datetime.utcnow()}

- Total Solved: {stats['total']}
- Easy: {stats['easy']}
- Medium: {stats['medium']}
- Hard: {stats['hard']}
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("README updated")