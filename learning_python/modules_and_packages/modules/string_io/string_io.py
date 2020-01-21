###StringIO

# in memory file like object . This object then can be used as i/p or o/p to most functions that would excpect a standard file object.

from io import StringIO

#arbitrary string
message = " THis is just a normal message string."

#Use StringIO method to set as file object.
f = StringIO(message)

#Now we have an object f that we will be able to treat just like a file .
print(f.read())

#Writing in a file
f.write("\nsecond line written to file like object.")

# reset cursor
f.seek(0)

#read again
print(f.read())

