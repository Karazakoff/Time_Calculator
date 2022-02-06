def add_time(start, duration, day = "no day"):

  def converter(time):
    hours, minutes = time.split(':')
    # print(f"hours = {hours}, minutes = {minutes}")
    end = ' AM' if int(hours) < 12 else ' PM'
    return str(int(hours) % 12) + ':' + minutes + end if int(hours) % 12 != 0 else str(int(hours) % 12 + 12) + ':' + minutes + end
  day = day.lower()

  days_in_week = {
    0 : 'monday',
    1 : 'tuesday',
    2 : 'wednesday',
    3 : 'thursday',
    4 : 'friday',
    5 : 'saturday',
    6 : 'sunday'
  }

  weeks_in_day = {v : k for k, v in days_in_week.items()}

  def minutes(time):
    left, right = time.split()
    if right == 'PM':
      l, r = left.split(':')
      l = str(int(l) + 12)
      left = l + ":" + r
    return left
  
  start = minutes(start)

  def adder(first, second):
    hour1, minutes1 = first.split(':')
    hour2, minutes2 = second.split(':')
    
    res1 = str((int(hour1) + int(hour2)) + (int(minutes1) + int(minutes2)) // 60)
    res2 = str((int(minutes1) + int(minutes2)) % 60)
    if len(res2) == 1:
      res2 = '0' + res2
    
    if len(res1) == 1:
      res1 = '0' + res1
    return res1, res2

  hour, minute = adder(start, duration)

  # If third parameter is not given:

  if day == 'no day':
    
    days = int(hour) // 24

    hour = str(int(hour) % 24)
    if days == 0:
      print(converter(hour + ':' + minute))
    elif days == 1:
      print(converter(hour + ':' + minute) + ' (next day)')
    else:
      print(converter(hour + ':' + minute) + f' ({days} days later)')

  else:

    start_day = weeks_in_day[day]

    days = int(hour) // 24

    hour = str(int(hour) % 24)
    if days == 0:
      print(converter(hour + ':' + minute) + ", " + days_in_week[start_day + days].title())
    elif days == 1:
      print(converter(hour + ':' + minute) + ", " + days_in_week[(start_day + days) % 7].title() + ' (next day)')
    else:
      print(converter(hour + ':' + minute) + ", " + days_in_week[(start_day + days) % 7].title() + f' ({days} days later)')

  return None


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)

add_time("11:43 PM", "00:20")
# Returns: 12:03 AM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)


