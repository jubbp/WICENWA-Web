---
layout: default
title: Thank You
sidebar: false
---

<style>
.thankyou-wrap {
  max-width: 680px;
  margin: 3rem auto;
  text-align: center;
}
.thankyou-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  color: var(--primary-yellow);
}
.thankyou-wrap h1 {
  font-size: 2rem;
  margin-bottom: 0.75rem;
}
.thankyou-wrap p {
  font-size: 1.05rem;
  color: #555;
  margin-bottom: 2rem;
}
.community-links {
  display: flex;
  gap: 1.25rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 2.5rem;
}
.community-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 1.5rem 2rem;
  border-radius: 6px;
  background: #f9f9f9;
  border: 2px solid #e0e0e0;
  text-decoration: none;
  color: var(--text-color);
  transition: border-color 0.15s, box-shadow 0.15s;
  min-width: 200px;
}
.community-card:hover {
  border-color: var(--primary-yellow);
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  text-decoration: none;
}
.community-card .card-icon { font-size: 2rem; }
.community-card .card-title { font-weight: 700; font-size: 1rem; }
.community-card .card-desc { font-size: 0.85rem; color: #666; text-align: center; }
.back-link { font-size: 0.9rem; color: #888; }
.back-link a { color: var(--link-color); }
</style>

<div class="thankyou-wrap">
  <div class="thankyou-icon">&#10003;</div>
  <h1>Message Sent — Thank You!</h1>
  <p>We have received your message and will be in touch shortly. In the meantime, the quickest way to connect with WICEN WA members is through our online communities.</p>

  <div class="community-links">
    <a class="community-card" href="https://groups.google.com/g/wicenwa" target="_blank" rel="noopener">
      <span class="card-icon">&#9993;</span>
      <span class="card-title">Google Group</span>
      <span class="card-desc">Join the mailing list for news, discussions, and activation notices</span>
    </a>
    <a class="community-card" href="https://discord.gg/z4Wmgp6fa7" target="_blank" rel="noopener">
      <span class="card-icon">&#127911;</span>
      <span class="card-title">Discord Server</span>
      <span class="card-desc">Chat with WICEN WA members and friends in real time</span>
    </a>
  </div>

  <p class="back-link"><a href="/">Return to the home page</a></p>
</div>
