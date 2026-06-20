# Server-Side
## 1. SQL Injection
## 2. Authentication

### 2.0 - Description 

Authentication vulnerabilities can allow attackers to gain access to sensitive data and functionality.
it's important to learn how to identify and exploit authentication vulnerabilities, and how to bypass common protection measures.

Authentication is the process of verifying the identity of a user or client. 

Something you know, such as a password or the answer to a security question. These are sometimes called "knowledge factors".

Something you have, This is a physical object such as a mobile phone or security token. These are sometimes called "possession factors".

Something you are or do. For example, your biometrics or patterns of behavior. These are sometimes called "inherence factors".


Authentication is the process of verifying that a user is who they claim to be. 
Authorization involves verifying whether a user is allowed to do something.

How do authentication vulnerabilities arise?
Most vulnerabilities in authentication mechanisms occur in one of two ways:

1) The authentication mechanisms are weak because they fail to adequately protect against brute-force attacks.
2) Logic flaws or poor coding in the implementation allow the authentication mechanisms to be bypassed entirely by an attacker. This is sometimes called "broken authentication".

Several of the labs require you to enumerate usernames and brute-force passwords. To help you with this process, we provide a shortlist of candidate usernames and passwords that you should use to solve the labs.

* https://portswigger.net/web-security/authentication/auth-lab-usernames
* https://portswigger.net/web-security/authentication/auth-lab-passwords


### 2.1 - Vulnerabilities in password-based login

<p>
For websites that adopt a password-based login process, users either register for an account themselves or they are assigned an account by an administrator. This account is associated with a unique username and a secret password, which the user enters in a login form to authenticate themselves.

In this scenario, the fact that they know the secret password is taken as sufficient proof of the user's identity. This means that the security of the website is compromised if an attacker is able to either obtain or guess the login credentials of another user.

This can be achieved in a number of ways. The following sections show how an attacker can use brute-force attacks, and some of the flaws in brute-force protection. You'll also learn about the vulnerabilities in HTTP basic authentication.
</p>

### 2.2 - Brute-force attacks

A brute-force attack is when an attacker uses a system of trial and error to guess valid user credentials. These attacks are typically automated using wordlists of usernames and passwords

### 2.3 - Brute-forcing usernames

Usernames are especially easy to guess if they conform to a recognizable pattern, such as an email address. For example, it is very common to see business logins in the format firstname.lastname@somecompany.com. However, even if there is no obvious pattern, sometimes even high-privileged accounts are created using predictable usernames, such as admin or administrator.

### 2.4 - Brute-forcing passwords

Passwords can similarly be brute-forced, with the difficulty varying based on the strength of the password. Many websites adopt some form of password policy, which forces users to create high-entropy passwords that are, theoretically at least, harder to crack using brute-force alone. This typically involves enforcing passwords with:

1. A minimum number of characters
2. A mixture of lower and uppercase letters
3. At least one special character


Rather than creating a strong password with a random combination of characters, users often take a password that they can remember and try to crowbar it into fitting the password policy. For example, if mypassword is not allowed, users may try something like Mypassword1! or Myp4$$w0rd instead.

In cases where the policy requires users to change their passwords on a regular basis, it is also common for users to just make minor, predictable changes to their preferred password. For example, Mypassword1! becomes Mypassword1? or Mypassword2!.

This knowledge of likely credentials and predictable patterns means that brute-force attacks can often be much more sophisticated, and therefore effective, than simply iterating through every possible combination of characters.

### 2.5 - Username enumeration

Username enumeration is when an attacker is able to `observe changes` in the website's behavior in order to identify whether a given username is valid.

when you enter a valid username but an incorrect password, or on registration forms when you enter a username that is already taken. This greatly reduces the time and effort required to brute-force a login because the attacker is able to quickly generate a shortlist of valid usernames.

While attempting to brute-force a login page, you should pay particular attention to any differences in:

1) Status codes: If a guess returns a different status code, this is a strong indication that the username was correct.
2) Error messages: Sometimes the returned error message is different depending on whether both the username AND password are incorrect or only the password was incorrect.
3) Response times:  If most of the requests were handled with a similar response time, any that deviate from this suggest that something different was happening behind the scenes. This is another indication that the guessed username might be correct. For example, a website might only check whether the password is correct if the username is valid. This extra step might cause a slight increase in the response time.

### 2.6 - Flawed brute-force protection

The two most common ways of preventing brute-force attacks are:

1. Locking the account that the remote user is trying to access if they make too many failed login attempts
2. Blocking the remote user's IP address if they make too many login attempts in quick succession


### 2.7 - Account locking

One way in which websites try to prevent brute-forcing is to lock the account if certain suspicious criteria are met, usually a set number of failed login attempts.

1. Establish a list of candidate usernames that are likely to be valid. This could be through username enumeration or simply based on a list of common usernames.

2. Decide on a very small shortlist of passwords that you think at least one user is likely to have. Crucially, the number of passwords you select must not exceed the number of login attempts allowed. For example, if you have worked out that limit is 3 attempts, you need to pick a maximum of 3 password guesses.

3. Using a tool such as Burp Intruder, try each of the selected passwords with each of the candidate usernames. This way, you can attempt to brute-force every account without triggering the account lock.

Account locking does not protect against credential stuffing because each username is only being attempted once. Credential stuffing is particularly dangerous because it can sometimes result in the attacker compromising many different accounts with just a single automated attack.

### 2.8 - User rate limiting

Another way websites try to prevent brute-force attacks is through user rate limiting. In this case, making too many login requests within a short period of time causes your IP address to be blocked. Typically, the IP can only be unblocked in one of the following ways:

1. Automatically after a certain period of time has elapsed
2. Manually by an administrator
3. Manually by the user after successfully completing a CAPTCHA

there are several ways an attacker can manipulate their apparent IP in order to bypass the block.

### 2.9 - HTTP basic authentication

In HTTP basic authentication, the client receives an authentication token from the server, which is constructed by concatenating the username and password, and encoding it in Base64. This token is stored and managed by the browser, which automatically adds it to the Authorization header of every subsequent request as follows:

```
Authorization: Basic base64(username:password)
```

HTTP basic authentication is also particularly vulnerable to session-related exploits, notably CSRF, against which it offers no protection on its own.


### 2.10 - Vulnerabilities in multi-factor authentication

<p>
In this section, we'll look at some of the vulnerabilities that can occur in multi-factor authentication mechanisms.
Many websites rely exclusively on single-factor authentication using a password to authenticate users. However, some require users to prove their identity using multiple authentication factors.
</p>


**Two-factor authentication tokens**

<p>
Verification codes are usually read by the user from a physical device of some kind. Many high-security websites now provide users with a dedicated device for this purpose, such as the RSA token or keypad device that you might use to access your online banking or work laptop. In addition to being purpose-built for security, these dedicated devices also have the advantage of generating the verification code directly. It is also common for websites to use a dedicated mobile app, such as Google Authenticator, for the same reason.

On the other hand, some websites send verification codes to a user's mobile phone as a text message. While this is technically still verifying the factor of "something you have", it is open to abuse. Firstly, the code is being transmitted via SMS rather than being generated by the device itself. This creates the potential for the code to be intercepted. There is also a risk of SIM swapping, whereby an attacker fraudulently obtains a SIM card with the victim's phone number. The attacker would then receive all SMS messages sent to the victim, including the one containing their verification code.
</p>

**Bypassing two-factor authentication**

<p>
At times, the implementation of two-factor authentication is flawed to the point where it can be bypassed entirely.

If the user is first prompted to enter a password, and then prompted to enter a verification code on a separate page, the user is effectively in a "logged in" state before they have entered the verification code. 
In this case, it is worth testing to see if you can directly skip to "logged-in only" pages after completing the first authentication step. Occasionally, you will find that a website doesn't actually check whether or not you completed the second step before loading the page.
</p>


**Flawed two-factor verification logic**

Sometimes flawed logic in two-factor authentication means that after a user has completed the initial login step, the website doesn't adequately verify that the same user is completing the second step.

```
POST /login-steps/first HTTP/1.1
Host: vulnerable-website.com
...
username=carlos&password=qwerty
```

They are then assigned a cookie that relates to their account, before being taken to the second step of the login process:
For example, the user logs in with their normal credentials in the first step as follows:

```
HTTP/1.1 200 OK
Set-Cookie: account=carlos

GET /login-steps/second HTTP/1.1
Cookie: account=carlos
```

When submitting the verification code, the request uses this cookie to determine which account the user is trying to access:

```
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.com
Cookie: account=carlos
...
verification-code=123456
```

In this case, an attacker could log in using their own credentials but then change the value of the account cookie to any arbitrary username when submitting the verification code.
```
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.com
Cookie: account=victim-user
...
verification-code=123456
```

This is extremely dangerous if the attacker is then able to brute-force the verification code as it would allow them to log in to arbitrary users' accounts based entirely on their username. They would never even need to know the user's password.


**Brute-forcing 2FA verification codes**

As with passwords, websites need to take steps to prevent brute-forcing of the 2FA verification code. This is especially important because the code is often a simple 4 or 6-digit number. Without adequate brute-force protection, cracking such a code is trivial.

Some websites attempt to prevent this by automatically logging a user out if they enter a certain number of incorrect verification codes. 
This is ineffective in practice because an advanced attacker can even automate this multi-step process by creating macros for Burp Intruder. The Turbo Intruder extension can also be used for this purpose.

* https://portswigger.net/burp/documentation/desktop/settings/sessions#macros
* https://portswigger.net/bappstore/9abaa233088242e8be252cd4ff534988
_____________

### 2.11 - Vulnerabilities in other authentication mechanisms

In addition to the basic login functionality, most websites provide supplementary functionality to allow users to manage their account. 
For example, users can typically change their password or reset their password when they forget it. These mechanisms can also introduce vulnerabilities that can be exploited by an attacker.

Websites usually take care to avoid well-known vulnerabilities in their login pages. But it is easy to overlook the fact that you need to take similar steps to ensure that related functionality is equally as robust. 

This is especially important in cases where an attacker is able to create their own account and, consequently, has easy access to study these additional pages.


**Keeping users logged in**

A common feature is the option to stay logged in even after closing a browser session. This is usually a simple checkbox labeled something like "Remember me" or "Keep me logged in". This functionality is often implemented by generating a "remember me" token of some kind, which is then stored in a persistent cookie. 
As possessing this cookie effectively allows you to bypass the entire login process, it is best practice for this cookie to be impractical to guess. 
However, some websites generate this cookie based on a predictable concatenation of static values, such as the username and a timestamp. Some even use the password as part of the cookie. 
This approach is particularly dangerous if an attacker is able to create their own account because they can study their own cookie and potentially deduce how it is generated. Once they work out the formula, they can try to brute-force other users' cookies to gain access to their accounts.
Some websites assume that if the cookie is encrypted in some way it will not be guessable even if it does use static values.
While this may be true if done correctly, naively "encrypting" the cookie using a simple two-way encoding like Base64 offers no protection whatsoever.
Even using proper encryption with a one-way hash function is not completely bulletproof. If the attacker is able to easily identify the hashing algorithm, and no salt is used, they can potentially brute-force the cookie by simply hashing their wordlists. This method can be used to bypass login attempt limits if a similar limit isn't applied to cookie guesses.


## 3. Path Transversal
## 4. Command Injection
## 5. Business Logic Vulnerabilities

## 6. Information Disclosure

Information disclosure, also known as information leakage, is when a website unintentionally reveals sensitive information to its users. Depending on the context, websites may leak all kinds of information to a potential attacker, including:

* Data about other users, such as usernames or financial information
* Sensitive commercial or business data
* Technical details about the website and its infrastructure

The dangers of leaking sensitive user or business data are fairly obvious, but disclosing technical information can sometimes be just as serious. Although some of this information will be of limited use, it can potentially be a starting point for exposing an additional attack surface, which may contain other interesting vulnerabilities.

Examples of information disclosure
Some basic examples of information disclosure are as follows:

* Revealing the names of hidden directories, their structure, and their contents via a robots.txt file or directory listing
* Providing access to source code files via temporary backups
* Explicitly mentioning database table or column names in error messages
* Unnecessarily exposing highly sensitive information, such as credit card details
* Hard-coding API keys, IP addresses, database credentials, and so on in the source code
* Hinting at the existence or absence of resources, usernames, and so on via subtle differences in application behavior

Information disclosure vulnerabilities can arise in countless different ways, but these can broadly be categorized as follows:

1) Failure to remove internal content from public content. For example, developer comments in markup are sometimes visible to users in the production environment.

2) Insecure configuration of the website and related technologies. For example, failing to disable debugging and diagnostic features can sometimes provide attackers with useful tools to help them obtain sensitive information. Default configurations can also leave websites vulnerable, for example, by displaying overly verbose error messages.

3) Flawed design and behavior of the application. For example, if a website returns distinct responses when different error states occur, this can also allow attackers to enumerate sensitive data, such as valid user credentials.

**What is the impact of information disclosure vulnerabilities?**

Information disclosure vulnerabilities can have both a direct and indirect impact depending on the purpose of the website and, therefore, what information an attacker is able to obtain. In some cases, the act of disclosing sensitive information alone can have a high impact on the affected parties. For example, an online shop leaking its customers' credit card details is likely to have severe consequences.

On the other hand, leaking technical information, such as the directory structure or which third-party frameworks are being used, may have little to no direct impact. However, in the wrong hands, this could be the key information required to construct any number of other exploits. The severity in this case depends on what the attacker is able to do with this information.

**How to prevent information disclosure vulnerabilities**

* Make sure that everyone involved in producing the website is fully aware of what information is considered sensitive. Sometimes seemingly harmless information can be much more useful to an attacker than people realize. Highlighting these dangers can help make sure that sensitive information is handled more securely in general by your organization.

* Audit any code for potential information disclosure as part of your QA or build processes. It should be relatively easy to automate some of the associated tasks, such as stripping developer comments.

* Use generic error messages as much as possible. Don't provide attackers with clues about application behavior unnecessarily.

* Double-check that any debugging or diagnostic features are disabled in the production environment.

* Make sure you fully understand the configuration settings, and security implications, of any third-party technology that you implement. Take the time to investigate and disable any features and settings that you don't actually need.


**How to find and exploit information disclosure vulnerabilities**

You will often find sensitive data while testing for something else. A key skill is being able to recognize interesting information whenever and wherever you do come across it.

The following are some examples of high-level techniques and tools that you can use to help identify information disclosure vulnerabilities during testing.

* Fuzzing
* Using Burp Scanner
* Using Burp's engagement tools
* Engineering informative responses

### 6.1 - Fuzzing

If you identify interesting parameters, you can try submitting unexpected data types and specially crafted fuzz strings to see what effect this has. Pay close attention; although responses sometimes explicitly disclose interesting information, they can also hint at the application's behavior more subtly.

For example, this could be a slight difference in the time taken to process the request. Even if the content of an error message doesn't disclose anything, sometimes the fact that one error case was encountered instead of another one is useful information in itself.

You can automate much of this process using tools such as Burp Intruder. This provides several benefits. Most notably, you can:

* Add payload positions to parameters and use pre-built wordlists of fuzz strings to test a high volume of different inputs in quick succession.

* Easily identify differences in responses by comparing HTTP status codes, response times, lengths, and so on.

* Use grep matching rules to quickly identify occurrences of keywords, such as error, invalid, SELECT, SQL, and so on.

* Apply grep extraction rules to extract and compare the content of interesting items within responses.

You can also use the [Logger++](https://portswigger.net/bappstore/470b7057b86f41c396a97903377f3d81) extension, available from the BApp store. In addition to logging requests and responses from all of Burp's tools, it allows you to define advanced filters for highlighting interesting entries. This is just one of the many Burp extensions that can help you find any sensitive data that is leaked by the website.


### 6.2 - Burp Scanner

Burp Suite Professional users have the benefit of Burp Scanner. This provides live scanning features for auditing items while you browse, or you can schedule automated scans to crawl and audit the target site on your behalf. Both approaches will automatically flag many information disclosure vulnerabilities for you. For example, Burp Scanner will alert you if it finds sensitive information such as private keys, email addresses, and credit card numbers in a response. It will also identify any backup files, directory listings, and so on.

### 6.3 - Burp's Engagement Tools

Burp provides several engagement tools that you can use to find interesting information in the target website more easily. You can access the engagement tools from the context menu - just right-click on any HTTP message, Burp Proxy entry, or item in the site map and go to "Engagement tools".

The following tools are particularly useful in this context.

**Search**
You can use this tool to look for any expression within the selected item. You can fine-tune the results using various advanced search options, such as regex search or negative search. This is useful for quickly finding occurrences (or absences) of specific keywords of interest.

**Find comments**
You can use this tool to quickly extract any developer comments found in the selected item. It also provides tabs to instantly access the HTTP request/response cycle in which each comment was found.

**Discover content**
You can use this tool to identify additional content and functionality that is not linked from the website's visible content. This can be useful for finding additional directories and files that won't necessarily appear in the site map automatically.


### 6.4 - Engineering informative responses

Verbose error messages can sometimes disclose interesting information while you go about your normal testing workflow. However, by studying the way error messages change according to your input, you can take this one step further. In some cases, you will be able to manipulate the website in order to extract arbitrary data via an error message.

There are numerous methods for doing this depending on the particular scenario you encounter. One common example is to make the application logic attempt an invalid action on a specific item of data. For example, submitting an invalid parameter value might lead to a stack trace or debug response that contains interesting details. You can sometimes cause error messages to disclose the value of your desired data in the response.


________________
## 7. Access Control
## 8. File Upload Vulnerabilities
## 9. Race Conditions
## 10. Server Side Request Forgery (SSRF)
## 11. XXE Injection
## 12. NoSQL Injection
## 13. API Testing
## 14. Web Cache Deception
