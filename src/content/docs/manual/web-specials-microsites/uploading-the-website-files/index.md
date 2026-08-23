---
title: "10.3. Uploading the Website Files"
---

:::caution[Legacy - cPanel has been retired]
The cPanel upload methods below are obsolete and kept for historical reference only.
:::

### 10.3.1. Method 1: cPanel

1. **Compress your project.** On your local computer, compress your entire project into a single .zip file.  
     
2. **Open cPanel.** Log in to cPanel and navigate to the **File Manager**.  
     
3. **Create a folder for the project.** Go to the **public_html** directory, then create a folder for the web special or microsite (e.g., **pride2025**).  
     
4. **Upload the .zip file.** Click on the **Upload** button in the toolbar. In the next screen, select the .zip you created.  
     
5. **Extract the .zip file.** Once the upload is complete, return to the File Manager. Select the newly uploaded .zip file and click the **Extract** button in the toolbar.  
     
6. **Delete the .zip file.** After successful extraction, you can delete the .zip file from the server to save space.

### 10.3.2. Method 2: FTP

File Transfer Protocol is another method for accessing and managing files on another server from your computer. In our case, it’s useful for making changes to an already-deployed site when the cPanel control panel is unavailable. This could also be used instead of the cPanel File Manager to deploy new projects, but you still need cPanel to create a subdomain.

You can use a graphical client like FileZilla, but you may also use the command line. The instructions below detail the commands for macOS or Linux.

1. FTP into the server through the URL [ftp.thelasallian.com](http://ftp.thelasallian.com).  The credentials are known only to the Web Editor, Web Development Consultant, and authorized staffers. You will be prompted for a username and password:  
   `ftp ftpthelasallian.com`  
     
2. **Navigate directories.** Once connected, you can navigate the server and your local machine using these commands:  
* `ls` — List files on the server  
* `cd <directory>` — Change directory or folder on the remote server  
* `!ls` — List files on your local machine  
* `lcd <directory>` — Change directory or folder on your local machine

3. **Example: Copying the contents of a folder**. To copy the contents of a folder from your computer to the server, use the `put -r` command. For example, to copy the contents of the build folder (wildcard * to upload everything inside) into public_html/pride2025:  
* Navigate to the server’s pride2025 folder:  
  `cd public_html/pride2025`  
* Navigate to the project build folder on your local machine:  
  `lcd lcd ~/Documents/Projects/tls-pride2025/build`  
* Put everything (8) from your current local directory into the current remote directory  
  `put -r *`

### 10.3.3. Technology-Specific Notes (e.g. PHP and React)

How you prepare and upload your files may depend on the technology used by the developers to create the web special or microsite. As of writing, our projects have been built in either PHP or React.js. Note the following.

For a vanilla **PHP** site, you can simply upload all your project files (.php files, CSS, JS, and assets) into the **public_html** directory as long as there is an **index.php** file. You can optionally add an **.htaccess** file in the project root to “clean URLs” (e.g., [site.thelasallian.com/page](http://site.thelasallian.com/page) instead of [site.thelasallian.com/page.php](http://site.thelasallian.com/page.php)), but you must ensure all your internal links are updated to match. A typical .htaccess file looks like this:

```
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} ! -f
RewriteRule ^([^.]+)$ $1.php [NC,L]
```

For a **React.js** site (or other JavaScript frameworks such as Vue and Svelte), you must build your application into static files first. This typically involves running a command like **npm run build**. Upload the contents of the generated **build** or **dist** folder to **public_html**, not the entire project source code. Additionally, you must add a **.htaccess** file in the same directory to handle client-side routing. Without it, users will get a **404 Not Found** error when they refresh any page other than the homepage. A typical **.htaccess** file for a React app looks like this:

```
# .htaccess for Single Page Applications (SPAs)

<IfModule mod_rewrite.c>
  RewriteEngine On

  # Do not rewrite files or directories that exist
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d

  # Rewrite all other requests to index.html
  RewriteRule ^(.*)$ index.html [L]
</IfModule>

# Optional: Set default charset to UTF-8
<IfModule mod_mime.c>
  AddDefaultCharset UTF-8
</IfModule>

# Optional: Prevent directory listings
Options -Indexes

# Optional: Gzip compression for common file types
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/plain
  AddOutputFilterByType DEFLATE text/html
  AddOutputFilterByType DEFLATE text/xml
  AddOutputFilterByType DEFLATE text/css
  AddOutputFilterByType DEFLATE application/xml
  AddOutputFilterByType DEFLATE application/xhtml+xml
  AddOutputFilterByType DEFLATE application/rss+xml
  AddOutputFilterByType DEFLATE application/javascript
  AddOutputFilterByType DEFLATE application/x-javascript
  AddOutputFilterByType DEFLATE application/json
  AddOutputFilterByType DEFLATE image/svg+xml
</IfModule>

# Optional: Cache control for static assets (adjust as needed)
<IfModule mod_headers.c>
  <FilesMatch ".(css|js|jpg|jpeg|png|gif|ico|svg|webp)$">
    Header set Cache-Control "max-age=31536000, public"
  </FilesMatch>
</IfModule>
```
