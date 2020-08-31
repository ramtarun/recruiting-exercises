def inventory_allocator(order, inventory_list):
    allocated = False
    i = 0

    allocated_inventories = []

    while not allocated:
        if sum(order.values()) != 0:
            if i == len(inventory_list):
                return []
            curr = {inventory_list[i]['name']: {}}
            for j in inventory_list[i]['inventory'].keys():
                if j in order.keys() and order[j] != 0:
                    order[j] -= inventory_list[i]['inventory'][j]
                    curr[inventory_list[i]['name']][j] = inventory_list[i]['inventory'][j]
            if len(curr[inventory_list[i]['name']].keys()) > 0:
                allocated_inventories.append(curr)
            i += 1
        else:
            allocated = True

    return allocated_inventories[::-1]
