Postmrtem
It happened to my own personal project there was an outage which lasted for 6 hours from 15:00 WAT till 21:00 WAT the site was completely inaccessible. It really took a toll on my mental health


Timeline
03:00 PM: Issue detected when I attempted to access my website and received a 502 Bad Gateway error.

03:15 PM: Confirmed the issue was not local by testing access from multiple devices and networks
.
03:30 PM: Logged into the server to check the web server status and logs.

04:20 PM: Noticed repeated errors in the web server 

05:30 PM: Assumed the issue was with the web server software itself; attempted to restart the server, which failed to resolve the issue..

06:10 PM: Investigated recent changes; identified that a web server configuration file was modified during the last update.

06:30 PM: Attempted to revert to a previous version of the configuration file; however, the issue persisted.

07:00PM: Decided to take a break

08:00 PM: Reached out to online forums for advice; received suggestions to check specific settings in the configuration file.

08:15 PM: Identified the root cause as an incorrect directive in the web server configuration file.

08:35 PM: Corrected the configuration file and restarted the web server.

09:00 PM: Full service restored; website accessible to all visitors.
Root Cause and Resolution
Root Cause:
A misconfigured directive in the web server configuration file, which was introduced during a recent update, caused the web server to fail in processing requests, resulting in the 502 Bad Gateway error.
Resolution:
The configuration file was corrected by updating the incorrect directive to its proper setting. The web server was then restarted, resolving the issue and restoring access to the website.
Corrective and Preventative Measures
Improvements/Fixes:
Implement a more thorough review process for configuration changes.
Set up automated backups for configuration files before making updates.
Enhance logging and monitoring to detect configuration issues promptly.
I just hope such mistakes don’t happen again and even if they do I’ll solve it cause that’s what I do as a programmer 😀



