from datetime import datetime, timezone
now = datetime.now(timezone.utc)

print(now.year)
print(now.month)
print(now.day)