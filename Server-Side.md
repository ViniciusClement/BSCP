## Server-Side

### SQL Injection

### Authentication

<p>
Authentication vulnerabilities can allow attackers to gain access to sensitive data and functionality.
it's important to learn how to identify and exploit authentication vulnerabilities, and how to bypass common protection measures.

Authentication is the process of verifying the identity of a user or client. 

Something you know, such as a password or the answer to a security question. These are sometimes called "knowledge factors".

Something you have, This is a physical object such as a mobile phone or security token. These are sometimes called "possession factors".

Something you are or do. For example, your biometrics or patterns of behavior. These are sometimes called "inherence factors".
</p>

<p>
Authentication is the process of verifying that a user is who they claim to be. 
Authorization involves verifying whether a user is allowed to do something.


How do authentication vulnerabilities arise?
Most vulnerabilities in authentication mechanisms occur in one of two ways:

1) The authentication mechanisms are weak because they fail to adequately protect against brute-force attacks.
2) Logic flaws or poor coding in the implementation allow the authentication mechanisms to be bypassed entirely by an attacker. This is sometimes called "broken authentication".

Several of the labs require you to enumerate usernames and brute-force passwords. To help you with this process, we provide a shortlist of candidate usernames and passwords that you should use to solve the labs.

* https://portswigger.net/web-security/authentication/auth-lab-usernames
* https://portswigger.net/web-security/authentication/auth-lab-passwords
</p>

**Vulnerabilities in password-based login**

<p>
For websites that adopt a password-based login process, users either register for an account themselves or they are assigned an account by an administrator. This account is associated with a unique username and a secret password, which the user enters in a login form to authenticate themselves.

In this scenario, the fact that they know the secret password is taken as sufficient proof of the user's identity. This means that the security of the website is compromised if an attacker is able to either obtain or guess the login credentials of another user.

This can be achieved in a number of ways. The following sections show how an attacker can use brute-force attacks, and some of the flaws in brute-force protection. You'll also learn about the vulnerabilities in HTTP basic authentication.
</p>

**Brute-force attacks**

A brute-force attack is when an attacker uses a system of trial and error to guess valid user credentials. These attacks are typically automated using wordlists of usernames and passwords

**Brute-forcing usernames**

Usernames are especially easy to guess if they conform to a recognizable pattern, such as an email address. For example, it is very common to see business logins in the format firstname.lastname@somecompany.com. However, even if there is no obvious pattern, sometimes even high-privileged accounts are created using predictable usernames, such as admin or administrator.

**Brute-forcing passwords**

Passwords can similarly be brute-forced, with the difficulty varying based on the strength of the password. Many websites adopt some form of password policy, which forces users to create high-entropy passwords that are, theoretically at least, harder to crack using brute-force alone. This typically involves enforcing passwords with:

1. A minimum number of characters
2. A mixture of lower and uppercase letters
3. At least one special character


Rather than creating a strong password with a random combination of characters, users often take a password that they can remember and try to crowbar it into fitting the password policy. For example, if mypassword is not allowed, users may try something like Mypassword1! or Myp4$$w0rd instead.

In cases where the policy requires users to change their passwords on a regular basis, it is also common for users to just make minor, predictable changes to their preferred password. For example, Mypassword1! becomes Mypassword1? or Mypassword2!.

This knowledge of likely credentials and predictable patterns means that brute-force attacks can often be much more sophisticated, and therefore effective, than simply iterating through every possible combination of characters.

**Username enumeration**

Username enumeration is when an attacker is able to `observe changes` in the website's behavior in order to identify whether a given username is valid.

when you enter a valid username but an incorrect password, or on registration forms when you enter a username that is already taken. This greatly reduces the time and effort required to brute-force a login because the attacker is able to quickly generate a shortlist of valid usernames.

While attempting to brute-force a login page, you should pay particular attention to any differences in:

1) Status codes: If a guess returns a different status code, this is a strong indication that the username was correct.
2) Error messages: Sometimes the returned error message is different depending on whether both the username AND password are incorrect or only the password was incorrect.
3) Response times:  If most of the requests were handled with a similar response time, any that deviate from this suggest that something different was happening behind the scenes. This is another indication that the guessed username might be correct. For example, a website might only check whether the password is correct if the username is valid. This extra step might cause a slight increase in the response time.

**Flawed brute-force protection**

The two most common ways of preventing brute-force attacks are:

1. Locking the account that the remote user is trying to access if they make too many failed login attempts
2. Blocking the remote user's IP address if they make too many login attempts in quick succession


**Account locking**

One way in which websites try to prevent brute-forcing is to lock the account if certain suspicious criteria are met, usually a set number of failed login attempts.

1. Establish a list of candidate usernames that are likely to be valid. This could be through username enumeration or simply based on a list of common usernames.

2. Decide on a very small shortlist of passwords that you think at least one user is likely to have. Crucially, the number of passwords you select must not exceed the number of login attempts allowed. For example, if you have worked out that limit is 3 attempts, you need to pick a maximum of 3 password guesses.

3. Using a tool such as Burp Intruder, try each of the selected passwords with each of the candidate usernames. This way, you can attempt to brute-force every account without triggering the account lock.

Account locking does not protect against credential stuffing because each username is only being attempted once. Credential stuffing is particularly dangerous because it can sometimes result in the attacker compromising many different accounts with just a single automated attack.

**User rate limiting**

Another way websites try to prevent brute-force attacks is through user rate limiting. In this case, making too many login requests within a short period of time causes your IP address to be blocked. Typically, the IP can only be unblocked in one of the following ways:

1. Automatically after a certain period of time has elapsed
2. Manually by an administrator
3. Manually by the user after successfully completing a CAPTCHA

there are several ways an attacker can manipulate their apparent IP in order to bypass the block.

**HTTP basic authentication**

In HTTP basic authentication, the client receives an authentication token from the server, which is constructed by concatenating the username and password, and encoding it in Base64. This token is stored and managed by the browser, which automatically adds it to the Authorization header of every subsequent request as follows:

```
Authorization: Basic base64(username:password)
```

HTTP basic authentication is also particularly vulnerable to session-related exploits, notably CSRF, against which it offers no protection on its own.


- [Lab: Username enumeration via different responses](#Usernamenumeration)

### Path Transversal

### Command Injection

### Business Logic Vulnerabilities

### Information Disclosure

### Access Control

### File Upload Vulnerabilities

### Race Conditions

### Server Side Request Forgery (SSRF)

### XXE Injection

### NoSQL Injection

### API Testing

### Web Cache Deception


### LABS

### Lab: Username enumeration via different responses


