from collections import Counter
from datetime import datetime


def _id_to_email(all_users: list) -> dict:
    """util func to map user id to email"""
    id_email_map = {}
    for user in all_users:
        if user["role"] == "student":
            id_email_map[user["id"]] = user["email"]
    return id_email_map


def _format_timestamp(date_str: str) -> str:
    """util func to format timestamp
    date_str: in format '2025-8-10-17'
    """
    t_list = date_str.split("-")
    # Join date parts and add T before hour
    date_str_parts = f"{t_list[0]}-{t_list[1]}-{t_list[2]}T{t_list[3]}:00:00Z"
    return datetime.strptime(date_str_parts, "%Y-%m-%dT%H:%M:%SZ")


def _sort_feeds(feeds: list) -> dict:
    """sort all feeds in the course based on folder.
    Assume each post only belongs to one folder."""
    feeds_by_folder = {}
    for f in feeds:
        if f["folders"]:
            folder = f["folders"][0]
            if folder not in feeds_by_folder:
                feeds_by_folder[folder] = f["log"]
            feeds_by_folder[folder].extend(f["log"])
    return feeds_by_folder


def _count_activities(folder: list, deadline):
    """count activities before deadline"""

    list_of_act = []
    for rec in folder:
        timestamp = datetime.strptime((rec["t"]), "%Y-%m-%dT%H:%M:%SZ")
        if timestamp < deadline:
            list_of_act.append(rec["u"])
    return Counter(list_of_act)


def _summarise_feeds(feeds: dict, id_email_map: dict, cutoff: dict) -> list:
    """for every folder, summarise how many activities per student since cutoff date.
    Will return a list of lists, for each record we have [internal id, email, cutoff keys*]"""
    student_activities = {}
    for k, v in id_email_map.items():
        student_activities[k] = {"email": v}

    for lm, t in cutoff.items():
        folder = feeds[lm]
        activities = _count_activities(folder, t)
        for k, v in student_activities.items():
            if k in activities:
                student_activities[k][lm] = activities[k]
            else:
                student_activities[k][lm] = 0
    return student_activities


import csv


def write_summary_to_csv(summary, cutoff, filename=...):
    # Get all cutoff keys from the first record
    cutoff_keys = [
        k + "deadline:" + str(k[cutoff])
        for k in summary[next(iter(summary))]
        if k != "email"
    ]
    header = ["internal id", "email"] + cutoff_keys

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for internal_id, info in summary.items():
            row = [internal_id, info["email"]]
            for key in cutoff_keys:
                row.append(info.get(key, 0))
            writer.writerow(row)


# def main():
#     """ask user provide cutoff date, and which folder to parse"""
#     piazza.user_login()
#     network_id = input("Input your course's Piazza network ID: ").strip()
#     course = piazza.network(network_id)


#     course = piazza.network(network_id)
#     course = piazza.network(network_id)
