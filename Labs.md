# Sumarry

## Authentication vulnerabilities
### Lab: Username enumeration via different responses
### Lab: Username enumeration via subtly different responses

1) Invalid username or password.
2) Settings > Grep - Match `Invalid username or password.`
3) Snipper attack on username

<img width="1080" height="500" src="IMG/1.png" />

4) Try to find password
5) Settings > Auto-pause attack > pause if expression in the list is missing from a response `Invalid username or password`

<img width="1080" height="500" src="IMG/2.png" />


### Lab: Username enumeration via response timing

<p>With Burp running, submit an invalid username and password, then send the POST /login request to Burp Repeater. Experiment with different usernames and passwords. Notice that your IP will be blocked if you make too many invalid login attempts. Identify that the X-Forwarded-For header is supported, which allows you to spoof your IP address and bypass the IP-based brute-force protection.
</p>

`X-Forwarded-For: 192.168.0.$1$` -> Random ip address
`X-Forwarded-For: $1$` -> Random number


### Lab: Broken brute-force protection, IP block

<p>This lab is vulnerable due to a logic flaw in its password brute-force protection. To solve the lab, brute-force the victim's password, then log in and access their account page.</p>

<p>
To solve this lab, you can log in with the valid user "wiener" every three attempts to bypass the brute-force attack protection.
To do this, you can use the script located in "scripts\create-user-pass.py".
</p>

1) carlos:password1
2) carlos:password2
3) wiener:peter
4) carlos:password3
5) carlos:password4


`Pickfork attack` and `Resource pool` current requests 1.

<img width="1420" height="500" src="IMG/4.png" />

<img width="1420" height="500" src="IMG/5.png" />

<img width="1080" height="500" src="IMG/3.png" />

________