# Sumarry

## Authentication vulnerabilities
### Lab: Username enumeration via different responses
### Lab: Username enumeration via subtly different responses

1) Invalid username or password.
2) Settings > Grep - Match `Invalid username or password.`
3) Snipper attack on username

<img width="1080" height="500" src="../BSCP/IMG/1.png" />

4) Try to find password
5) Settings > Auto-pause attack > pause if expression in the list is missing from a response `Invalid username or password`

<img width="1080" height="500" src="../BSCP/IMG/2.png" />


### Lab: Username enumeration via response timing

<p>With Burp running, submit an invalid username and password, then send the POST /login request to Burp Repeater. Experiment with different usernames and passwords. Notice that your IP will be blocked if you make too many invalid login attempts.
Identify that the X-Forwarded-For header is supported, which allows you to spoof your IP address and bypass the IP-based brute-force protection.
</p>

`X-Forwarded-For: 192.168.0.$1$` -> Random ip address
`X-Forwarded-For: $1$` -> Random number




________