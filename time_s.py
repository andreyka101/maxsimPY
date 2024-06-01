# https://sky.pro/media/kak-rabotat-s-modulem-time-v-python/
import time
print(time.time())
present_time = time.time()
print(time.ctime(present_time))

print(time.localtime(present_time))

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(present_time))
print(formatted_time)

time_string = "2022-01-01 12:00:00"
format_string = "%Y-%m-%d %H:%M:%S"
parsed_time = time.strptime(time_string, format_string)
print(parsed_time)

print(time.mktime(parsed_time))



# for i in range(10):
#     time.sleep(3)
#     print(i)



