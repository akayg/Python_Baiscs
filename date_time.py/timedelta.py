from datetime import datetime, timedelta

now = datetime.now()
future = now + timedelta(days=7)
threedayearly= future - timedelta(days=3)
print("Started Now:", now)
print("ENDs 7 days later:", future)
print("3 day befor ending:",threedayearly)