
#  wishlists
# <user name>,<city 1>,<city 2>...
# User A is a travel buddy of user B if A has 50% or more of the cities in his/her wishlist in common
# with B.

# travel buddies sorted by rank.

cities = {}
city_cnt = 0
users = {}
user_city = {}
buddy_res = {}


def travel_buddy(whishlists, user1):
    global city_cnt, buddy_res
    # clear
    cities = {}
    city_cnt = 0
    users = {}
    user_city = {}
    buddy_res = {}

    whishlines = whishlists.split('\n')
    for line in whishlines:
        user_info = line.split(',')
        userid = user_info[0]
        for city in user_info[1:]:
            if city not in cities:
                cities[city] = city_cnt
                city_cnt += 1
            else:
                pass

        user_city[userid] = 0
        #print user_info
        for city in user_info[1:]:
            #print cities[city]
            user_city[userid] |= 1 << cities[city]

    user1_mask = user_city[user1]
    #print user_city
    total_cnt = city_count(user1_mask)

    for userid in user_city:
        if userid == user1:
            continue

        user_mask = user_city[userid]
        mask_res = user1_mask & user_mask
        cnt = city_count(mask_res)
        buddy_rate = cnt * 1.0 / total_cnt
        if buddy_rate >= 0.5:
            buddy_res[userid] = buddy_rate


    # sort
    buddy_res = [[v[1], v[0]] for v in buddy_res.items()]
    #print buddy_res
    buddy_res.sort(reverse=True)
    #print buddy_res

    # print
    print "This user's travel buddy rank is: "
    for user, buddy in buddy_res:
        print user, buddy

    
# count 1 in binary    
def city_count(mask_res):
    cnt = 0
    while mask_res:
        cnt += 1
        mask_res = mask_res & (mask_res-1)
        
    return cnt


# test1
whishlists = """user1,wuxi,nanjing,wuhan,chengdu
user2,hangzhou,wuxi,nanjing,shanghai
user3,suzhou,beijing
user4,nanjing,wuhan,wuxi
"""

user1="user1"
travel_buddy(whishlists, user1)

print

# test2
whishlists = """user1,wuxi,nanjing,wuhan,chengdu
user2,hangzhou,wuxi,nanjing,shanghai
user3,suzhou,beijing
user4,nanjing,wuhan,wuxi
"""

user2="user2"
travel_buddy(whishlists, user2)

print

# test3
whishlists = """user1,xiamen
user2,hangzhou,wuxi,nanjing,shanghai
user3,suzhou,beijing
user4,nanjing,wuhan,wuxi
"""

user3="user1"
travel_buddy(whishlists, user1)

print

# test4
whishlists = """user1,xiamen
user2,hangzhou,wuxi,nanjing,shanghai
user3,xiamen
user4,xiamen
"""

user4="user1"
travel_buddy(whishlists, user4)

print

# test5
whishlists = """user1,hangzhou,wuxi,nanjing,shanghai,changzhou
user2,hangzhou,wuxi,nanjing
user3,hangzhou,wuxi,nanjing,shanghai
user4,hangzhou,wuxi
"""

user4="user1"
travel_buddy(whishlists, user4)

print

# 