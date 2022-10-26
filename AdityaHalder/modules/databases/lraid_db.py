from AdityaHalder.modules.databases import cli

collection = cli["Kaal"]["lraid"]


async def lraid_user(chat):
    doc = {"_id": "Lraid", "users": [chat]}
    r = await collection.find_one({"_id": "Lraid"})
    if r:
        await collection.update_one({"_id": "Lraid"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


async def get_lraid_users():
    results = await collection.find_one({"_id": "Lraid"})
    if results:
        return results["users"]
    else:
        return []


async def unlraid_user(chat):
    await collection.update_one({"_id": "Lraid"}, {"$pull": {"users": chat}})
