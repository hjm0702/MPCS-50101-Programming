
import re
# Lets use a regular expression to match a date string. Ignore
# the output since we are just testing if the regex matches.
regex = r"([a-zA-Z]+) (\d+)"
if re.search(regex, "June 24, March 11"):
    # Indeed, the expression "([a-zA-Z]+) (\d+)" matches the date string

    # If we want, we can use the MatchObject's start() and end() methods
    # to retrieve where the pattern matches in the input string, and the
    # group() method to get all the matches and captured groups.
    match = re.search(regex, "June 24")

    # This will print [0, 7), since it matches at the beginning and end of the
    # string
    print "Match at index %s, %s" % (match.start(), match.end())

    # The groups contain the matched values.  In particular:
    #    match.group(0) always returns the fully matched string
    #    match.group(1), match.group(2), ... will return the capture
    #            groups in order from left to right in the input string
    #    match.group() is equivalent to match.group(0)

    # So this will print "June 24"
    print "Full match: %s" % (match.group(0))
    # So this will print "June"
    print "Month: %s" % (match.group(1))
    # So this will print "24"
    print "Day: %s" % (match.group(2))
else:
    # If re.search() does not match, then None is returned
    print "The regex pattern does not match. :("

'''------------------------------------------------------'''

# Lets use a regular expression to match a few date strings.
regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")

# print matches
for match in matches:
    # This will print:
    #   June 24
    #   August 9
    #   Dec 12
    print "Full match: %s" % (match)

# To capture the specific months of each date we can use the following pattern
regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   June
    #   August
    #   Dec
    print "Match month: %s" % (match)

# If we need the exact positions of each match
regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   0 7
    #   9 17
    #   19 25
    # which corresponds with the start and end of each match in the input string
    print "Match at index: %s, %s" % (match.start(), match.end())

'''------------------------------------------------------'''

# Lets try and reverse the order of the day and month in a date
# string. Notice how the replacement string also contains metacharacters
# (the back references to the captured groups) so we use a raw
# string for that as well.
regex = r"([a-zA-Z]+) (\d+)"

# This will reorder the string and print:
#   24 of June, 9 of August, 12 of Dec
print re.sub(regex, r"\2 of \1", "June 24, August 9, Dec 12")

'''------------------------------------------------------'''

# Lets create a pattern and extract some information with it
regex = re.compile(r"(\w+) World")
result = regex.search("Hello World is the easiest")
if result:
    # This will print:
    #   0 11
    # for the start and end of the match
    print result.start(), result.end()

# This will print:
#   Hello
#   Bonjour
# for each of the captured groups that matched
for result in regex.findall("Hello World, Bonjour World"):
    print result

# This will substitute "World" with "Earth" and print:
#   Hello Earth
print regex.sub(r"\1 Earth", "Hello World")
