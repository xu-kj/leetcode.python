#!/bin/python3

#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#

def processLogs(logs, threshold):
    transactions = {}
    for log in logs:
        parts = log.split()
        sender, recipient = int(parts[0]), int(parts[1])
        if sender in transactions:
            transactions[sender] += 1
        else:
            transactions[sender] = 1

        if recipient != sender:
            if recipient in transactions:
                transactions[recipient] += 1
            else:
                transactions[recipient] = 1

    over_threshold_users = []
    for k, v in transactions.items():
        if v >= threshold:
            over_threshold_users.append(k)
    over_threshold_users = sorted(over_threshold_users)
    return [f"{u}" for u in over_threshold_users]
