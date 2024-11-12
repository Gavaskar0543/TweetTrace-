const puppeteer = require('puppeteer');
require('dotenv').config();

const { TWITTER_USERNAME, TWITTER_PASSWORD, TARGET_USERNAME } = process.env;

async function loginToTwitter(page) {
    // Navigate to Twitter login
    await page.goto('https://twitter.com/login', { waitUntil: 'networkidle2' });

    // Enter the username and proceed
    await page.waitForSelector('input[name="text"]', { timeout: 10000 });
    await page.type('input[name="text"]', TWITTER_USERNAME);
    await page.keyboard.press('Enter');

    // Wait for the password field to load after the username step
    try {
        await page.waitForSelector('input[name="password"]', { timeout: 10000 });
        await page.type('input[name="password"]', TWITTER_PASSWORD);
        await page.keyboard.press('Enter');
    } catch (error) {
        console.error("Password field not found. Check if Twitter's login flow has changed.");
        return;
    }

    // Wait for navigation to complete login
    await page.waitForNavigation({ waitUntil: 'networkidle2' });
    console.log("Successfully logged in.");
}

async function scrapeTweets(page) {
    // Navigate to the target user's profile page
    await page.goto(`https://twitter.com/${TARGET_USERNAME}`, { waitUntil: 'networkidle2' });

    let tweets = [];
    let lastHeight = await page.evaluate('document.body.scrollHeight');

    // Scroll to load more tweets
    while (tweets.length < 50) {
        const newTweets = await page.evaluate(() => {
            return Array.from(document.querySelectorAll('article')).map(tweet => tweet.innerText);
        });

        newTweets.forEach(tweet => tweets.push(tweet));

        // Scroll down to load more tweets
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight)');
        await new Promise(resolve => setTimeout(resolve, 2000));

        let newHeight = await page.evaluate('document.body.scrollHeight');
        if (newHeight === lastHeight) break;
        lastHeight = newHeight;
    }

    console.log("Tweets:", tweets.slice(0, 50));
    return tweets.slice(0, 50);
}

async function scrapeFollowers(page) {
    // Navigate to the target user's followers page
    await page.goto(`https://twitter.com/${TARGET_USERNAME}/followers`, { waitUntil: 'networkidle2' });

    let followers = new Set();
    let lastHeight = await page.evaluate('document.body.scrollHeight');

    while (followers.size < 50) {
        const newFollowers = await page.evaluate(() => {
            return Array.from(document.querySelectorAll('div[role="link"] > span')).map(el => el.textContent);
        });

        newFollowers.forEach(follower => followers.add(follower));

        await page.evaluate('window.scrollTo(0, document.body.scrollHeight)');
        await new Promise(resolve => setTimeout(resolve, 2000));

        let newHeight = await page.evaluate('document.body.scrollHeight');
        if (newHeight === lastHeight) break;
        lastHeight = newHeight;
    }

    console.log("Followers:", Array.from(followers));
    return Array.from(followers);
}

async function scrapeFollowing(page) {
    await page.goto(`https://twitter.com/${TARGET_USERNAME}/following`, { waitUntil: 'networkidle2' });

    let following = new Set();
    let lastHeight = await page.evaluate('document.body.scrollHeight');

    while (following.size < 50) {
        const newFollowing = await page.evaluate(() => {
            return Array.from(document.querySelectorAll('div[role="link"] > span')).map(el => el.textContent);
        });

        newFollowing.forEach(user => following.add(user));

        await page.evaluate('window.scrollTo(0, document.body.scrollHeight)');
        await new Promise(resolve => setTimeout(resolve, 2000));

        let newHeight = await page.evaluate('document.body.scrollHeight');
        if (newHeight === lastHeight) break;
        lastHeight = newHeight;
    }

    console.log("Following:", Array.from(following));
    return Array.from(following);
}

async function scrapeTweetCount(page) {
    await page.goto(`https://twitter.com/${TARGET_USERNAME}`, { waitUntil: 'networkidle2' });

    const tweetCount = await page.evaluate(() => {
        const tweetElement = document.querySelector('a[href$="/tweets"] > span');
        return tweetElement ? tweetElement.textContent : "Tweet count not found";
    });

    console.log("Total Tweets:", tweetCount);
    return tweetCount;
}

(async () => {
    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    
    const page = await browser.newPage();
    await loginToTwitter(page);

    const tweets = await scrapeTweets(page);
    const followers = await scrapeFollowers(page);
    const following = await scrapeFollowing(page);
    const tweetCount = await scrapeTweetCount(page);

    console.log("Scraped Data:", {
        tweets,
        followers,
        following,
        tweetCount
    });

    await browser.close();
})();
