import re
test_string = ("An Internet Protocol address (IP address) is a numerical label such as 192.168.1.254 that is connected \n"
               "to a computer network that uses the Internet Protocol for communication.[1][2] An IP address serves two \n"
               "main functions: network interface identification and location addressing. Internet Protocol version 4 \n"
               "(IPv4) defines an IP address as a 32-bit number.[2] However, because of the growth of the Internet and \n"
               "the depletion of available IPv4 addresses, a new version of IP (IPv6), using 128 bits for the IP \n"
               "address, was standardized in 1998.[3][4][5] IPv6 deployment has been ongoing since the mid-2000s.")

###Extract all the digits from the text###

#extracting all digits separately using \d
digits = re.findall(r'\d', test_string)
print(digits)

#extracting digits like whole numbers using \d+
numbers = re.findall(r'\d+', test_string)
print(numbers)

###Extract all mentions of IP versions (IPv4, IPv6)###
versions = re.findall(r'IPv[46]', test_string)
print(versions)

###Extract whole text after phrase "128 bits"###
text = re.findall(r'128 bits(.*)', test_string, re.DOTALL)
print(text)

###Extract IP address from the text###
ip_address = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', test_string)
print(ip_address)

###Create text file which contains provided test string. Using Regular expressions extract all the text from the file
# except IP address, IP versions and numbers.###

with open("test_string.txt", "w") as f:
    f.write(test_string)

with open("test_string.txt", "r") as f:
    content = f.read()

clean_text = re.sub(r'\d{1,3}(?:\.\d{1,3}){3}|IPv[46]|\d+', '', content)
print(clean_text)
