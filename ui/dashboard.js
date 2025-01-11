// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    console.log("Dashboard is live!");

    // Simulated Data for Moonlord69's Hype Activity
    const tweets = [
        {
            coin: "UFD",
            content: "🚀 $UFD is blowing up! The community vibes are insane!",
            timestamp: "2025-01-06 14:00:00"
        },
        {
            coin: "CPU",
            content: "⚡ $CPU is trending hard! Don’t miss the next big wave!",
            timestamp: "2025-01-07 16:30:00"
        },
        {
            coin: "SOLAI",
            content: "✨ $SOLAI is making waves as the next-gen meme coin!",
            timestamp: "2025-01-08 18:45:00"
        }
    ];

    const sentimentScore = 87; // Simulated sentiment score

    // Update the Latest Tweets Section
    const tweetContainer = document.querySelector('[data-moonlord="tweets"]');
    if (tweetContainer) {
        tweets.forEach((tweet) => {
            const tweetItem = document.createElement("div");
            tweetItem.className = "tweet-item";
            tweetItem.innerHTML = `
                <p><strong>${tweet.coin}</strong>: ${tweet.content}</p>
                <small>${tweet.timestamp}</small>
            `;
            tweetContainer.appendChild(tweetItem);
        });
    } else {
        console.warn("Tweet container not found in the Webflow structure.");
    }

    // Update the Sentiment Score
    const sentimentElement = document.querySelector('[data-moonlord="sentiment-score"]');
    if (sentimentElement) {
        sentimentElement.textContent = `Sentiment Score: ${sentimentScore}`;
    } else {
        console.warn("Sentiment score element not found in the Webflow structure.");
    }
});
