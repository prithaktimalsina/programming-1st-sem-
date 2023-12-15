compost_items = ['applecore', 'bananapeel', 'egg_shell']
recycle_items = ['glassbottle', 'aluminum_can']
trash_items = ['plasticcoatedpaper']
item = input()
if item in compost_items:
    print("compost")
elif item in recycle_items:
    print("recycle")
elif item in trash_items:
    print("trash")
else:
    print("trash")
