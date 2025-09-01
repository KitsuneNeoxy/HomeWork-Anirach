def analyze_user_activity(log_file_path: str) -> dict:

    #your code here

    result = {
        "action_counts": {},
        "average_session_time": 0,
        "most_active_user": None,
        "total_users": 0
    }

    list_user = []
    login_times = []

    with open(log_file_path, 'r') as file:
        logs = file.readlines()

        for line in logs:
            part = line.strip().split()
            if len(part) < 4:
                continue

            user = part[1]
            action = part[2]

            try:
                time = int(part[3])
            except ValueError:
                continue

            if user not in list_user:
                list_user.append(user)

            if action not in result["action_counts"]:
                result["action_counts"][action] = 1
            else:
                result["action_counts"][action] += 1

            if action == 'login':
                login_times.append(time)

    result["total_users"] = len(list_user)
    result["most_active_user"] = max(list_user) if list_user else None
    result["average_session_time"] = sum(login_times) / len(login_times) if login_times else 0

    return result

if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)
    



# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}
