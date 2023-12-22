import datetime
import pywhatkit as kit


def schedule_message(phone, message, hour, minute, file_path):

    if not isinstance(hour, int) or not isinstance(minute, int):
        raise ValueError("Hour and minute must be integers.")

    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        raise ValueError("Hour and minute must be within valid ranges.")

    now = datetime.datetime.now()
    scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    time_difference = scheduled_time - now


    if time_difference.total_seconds() > 0:
        scheduled_time_str = f"{hour:02d}:{minute:02d}"
        if file_path:

            kit.sendwhats_image(phone, file_path, scheduled_time_str)
        else:

            kit.sendwhatmsg(phone, message, hour, minute)
        return f"Message scheduled successfully for {scheduled_time_str}."


    raise ValueError("Invalid scheduling time. Scheduled time is in the past.")
