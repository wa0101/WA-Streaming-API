---

# 🌐 WA-Streaming-API | Arabic Version 🌐

Welcome to **WA-Streaming-API**! If you're looking to build a streaming site like Netflix, Crunchyroll, or other streaming platforms, you’re in the right place. This API comes packed with everything you need—homepage content, detailed item info, search, pagination, and even streaming with episodes and all that cool stuff 🎥🍿

### ⚠️ Heads Up:  
Just a little note here: This API might not be fully legal since it bypasses a bunch of Cloudflare protections and simulates GET/POST requests to `egyspace.dead` to fetch data. And yeah, it might be a bit slow sometimes, but that's because it's built with a queue system for better handling.

### 📝 Quick Index

- [✨ Features](#-features)
- [🚀 Getting Started](#-getting-started)
- [🌐 Live Example Website](#-live-example-website)
- [📋 Usage Examples](#-usage-examples)
- [⚠️ Problems](#️-problems)
- [🛠️ Final Notes](#-final-notes)

## ✨ Features

- **Homepage List**: Get all the items from the homepage with images, URLs, and more!
- **Item Info**: Grab detailed info for any item from the homepage.
- **Search Content**: Search for any content like movies, series, and anime.
- **Pagination**: Navigate easily through search result pages.
- **Watch & Episodes**: Fetch direct streaming links and episode lists for any content.

### 🌟 Important Note: Arabic Content Only!  
This API is mainly for Arabic users because all the content, including subtitles, is in Arabic, and there’s no way to change it. So, if you're looking for something in another language, this might not be for you.

## 🚀 Getting Started

So, using the API is super straightforward. You can use any HTTP request library like `requests` in Python, `axios` in Node.js, or whatever you're comfy with. Just start making your requests to the API and get your data!

A few things to keep in mind:
- The API works with queues, so it might be a little slow, but that's to keep things stable.
- All requests go to `https://wa-watch-api.onrender.com/` with the right endpoints.

## 🌐 Live Example Website

Want to see this API in action? Check out this **live streaming website** built entirely using the WA-Streaming-API:

**🔗 [Live Streaming Website Example](https://careful-korella-wa-7f9ebc0e.koyeb.app/)**

This website showcases all the features of the API: streaming, searching, item info, pagination, and more. It’s a great way to see how you can utilize the API to create a full-fledged streaming platform!

## 📋 Usage Examples

Want to see some real-life code examples? Check out this script here: [example.py](https://github.com/wa0101/WA-Streaming-API/blob/main/example.py). It’s got examples for everything, from pulling the homepage list to searching, watching, and grabbing detailed info. You can copy-paste and run it in any Python environment or even convert it to another language!

### Some Quick Endpoints:

1. **`/list/`**: Get the homepage list.
2. **`/iteminfo?url={URL}`**: Fetch detailed info for any item.
3. **`/search?q={QUERY}`**: Search for any content.
4. **`/watch?url={URL}`**: Get streaming links and episode lists.
5. **`/navigation?q={QUERY}&page={PAGE}`**: Navigate through search results pages.

## ⚠️ Problems

Here are some issues you might run into when using this API:

- **Ads on the Player**: The streaming player in the iframe can have ads. This is not from the API itself, but rather from the source player. In the future, it might be possible to bypass these ads or find cleaner solutions to this.
  
- **Website Performance**: The API can be a bit slow, especially when it's under heavy traffic. This is due to the queue system in place to manage requests better. But don’t worry, there are plans to optimize this and make it more efficient in future updates.

## 🛠️ Final Notes

A couple of things to keep in mind: This API relies on making requests to a third-party site, which can bring up legal and ethical issues. So maybe keep this to educational or personal projects.

And hey, if you’ve got any questions or need help, just shout! We hope you have a great time building your streaming platform! 😉

---

