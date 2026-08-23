---
title: "10.5. The WordPress REST API"
---

The WordPress REST API allows other applications to access our main website’s data in JSON format. It allows our web specials and microsites to dynamically fetch posts [from thelasallian.com](http://thelasallian.com). Instead of manually adding the content, our web specials and microsites can send a request to the API and automatically display the articles that fit certain criteria.

A request is made to a specific URL endpoint. The main endpoint for posts in our main website is `https://thelasallian.com/wp-json/wp/v2/posts`. You can add parameters to this URL to filter, sort, and limit the data you receive. This is crucial for performance and for getting exactly the data you need.

For example, to fetch the 5 most recent articles tagged with the “Rant & Rave” tag (with an ID of 497), and only get the featured image, date, link, title and authors, the request URL would look like this: 

`https://thelasallian.com/wp-json/wp/v2/posts?per_page=5&tags=497&_fields=jetpack_featured_media_url,date,link,title,authors`

Refer to the [WordPress REST API Handbook](https://developer.wordpress.org/rest-api/) for full documentation.
