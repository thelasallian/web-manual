---
title: "10.4. Creating a Subdomain"
---

:::caution[Legacy - cPanel has been retired]
Subdomains are no longer provisioned through cPanel.
:::

1. **Access the “Domains” page**. Log in to cPanel and scroll down to the “” section. Click on **Domains**  
     
2. **Create a new domain**. Click on the **Create a New Domain** button.  
     
3. **Enter details**. Enter the full subdomain you want to create (e.g., [ge2026.thelasallian.com](http://ge2026.thelasallian.com)). Uncheck the “Share document root” checkbox and enter the path to the folder you create in **public_html** (e.g., **public_html/ge2026**).  
     
4. **Save.** Your website will be initially available at the http://<subdomain>.The server will automatically try to issue an SSL certificate for your new subdomain to force secure HTTPS so users are automatically  redirected to https://<subdomain>. This SSL issuance may take a few minutes to a few hours, but the site is already active while its ongoing/
