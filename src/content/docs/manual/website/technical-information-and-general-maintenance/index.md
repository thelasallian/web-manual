---
title: "3.6. Technical Information and General Maintenance"
---

:::caution[Legacy - cPanel has been retired]
TLS no longer uses a cPanel server. The sections below are kept for historical reference only. The website and web specials are now deployed through Git-based hosting.
:::

### 3.6.1. About the Server and cPanel

Our WordPress site ([thelasallian.com](http://thelasallian.com)) operates on an external, shared server managed by Jairus, who is the point of contact of the Web Editor for any server-level concerns. The server is not owned by TLS or DLSU. Because we have shared and possibly limited storage space, we must be diligent with practices such as compressing and resizing images before uploading. The server runs on a standard LAMP stack—Linux as the operating system, Apache as the web server, MySQL as the database server, and PHP as the programming language. This is the standard combination for running WordPress. The domain [thelasallian.com](http://thelasallian.com) is managed and paid for by Jairus.

We use cPanel, a web-based control panel, to manage our allocated server space. It provides a graphical user interface for managing website files, databases, and domains. We primarily use cPanel to upload files for web specials (e.g., USG elections) and microsites (e.g, Rant and Rave) to the **home2/tls/public_html/** directory, as well as to create and manage the subdomains (e.g, [pride.thelasallian.com](http://pride.thelasallian.com)) for them. cPanel requires a paid license, which is also paid for by Jairus.

As mentioned, we are in a shared hosting scheme; there are other websites hosted on the same web server. For TLS, our home directory is located at the **home2/tls/** directory. We are only allowed to upload web special files to the **home2/tls/public_html/** directory. We are not allowed to modify or delete any other files or directories found in our home directory.

### 3.6.2. Checking the cPanel License Status

The cPanel license must be active to access the control panel. While Jairus manages the license renewal, the Web Editor and web development staffers are responsible for periodically checking the license status to prevent unexpected interruptions. If the license expires, we’ll lose access to the control panel and hinder the deployment of web specials and microsites, especially when creating a subdomain.

A common indication of an expired license is being unable to log in to cPanel, which typically displays an error message stating, “Maximum users exceeded.” You can check the license status by visiting either [cpanel.thelasallian.com](http://cpanel.thelasallian.com) or [verify.cpanel.net/app/verify](https://verify.cpanel.net/app/verify) if you don't have access to the cPanel control panel. The following instructions explain how to use the latter option.

1. SSH into the server through the address `ssh.thelasallian.com`. The credentials are known only to the Web Editor, Web Development Consultant, and authorized staffers. On macOS, the command to initiate a SSH connection to the server is:  
   `ssh <username>@ssh.thelasallian.com`

2. Execute this curl command to fetch the public IP address of the server:  
   `curl -L https://cpanel.net/myip`

3. Enter the public IP address into the cPanel license verification tool at [verify.cpanel.net/app/verify](https://verify.cpanel.net/app/verify).

### 3.6.4. WordPress Updates

WordPress releases updates that include new features, bug fixes, and security patches. Only the Web Editor or the Web Development Consultant is authorized to update WordPress. The TLS website may be inaccessible during this process. 

### 3.6.5. Precautions on Installing Plugins


Plugins extend the functionality of the website, but may break features in the website. In the past, some installed or updated plugins misconfigured the website or resulted in errors. Hence, before installing, updating, or deleting a plugin, a complete backup must be performed.
