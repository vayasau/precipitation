#!/usr/bin/python3

# gaunamas pranesimas apie kritulius GPS koordinates nurodytoje vietoveje ir aplink

from scrap_one import web_image
from get_user import get_user_data
from coordinates import gps_to_px
from area import circle
from warning import warning_flag
from mail import send_mail
from change_flag import flag_change


def main():
    file = web_image()

    for i in get_user_data():
        user, user_data = next(iter(i.items()))
        gps, flag = next(iter(user_data.items()))
        map_point = gps_to_px(gps[0], gps[1])
        monitor_area = circle(map_point[0], map_point[1])
        message = warning_flag(monitor_area, file)
        if message != flag:
            if message == 1:
                text = "There IS precipitation in the observation area."
                new_flag = 1
            if message == 0:
                text = "There is NO precipitation in the observation area."
                new_flag = 0
            send_mail(user, text, gps)
            flag_change(gps, new_flag)


if __name__ == "__main__":
    main()
