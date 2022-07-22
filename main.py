from cookiemonster import CookieBot

# Checking for items available in the store every 3 seconds
# 128.4 cookies/sec in 5 minutes
# 241.6 cookies/sec in 10 minutes

# After implementing the re-call of the upgrade_checker method, the 5-min cps count went down to 113.

# Bumped up the check time from 3 to 5 seconds, the 5-min cps count went up to 132.

cookie_game = CookieBot()
