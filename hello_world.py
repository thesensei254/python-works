import traceback
# print ("Hello Python World!")

message = "Hello Python World!"
print(message)

message = "Hello Python crash course world!!"

# Using try-except to catch error
# Import traceback for error handling and output of stacktrace
try:
    print(mesage)
except Exception as e:
    traceback.extract_tb(e)



