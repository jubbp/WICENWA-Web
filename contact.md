---
layout: default
title: Contact Us
---

# Contact WICEN WA

Get in touch with us to learn more about WICEN WA, membership, or volunteer opportunities.

<div class="contact-grid">

  <div class="contact-info">
    <h2>Contact Information</h2>
    <ul class="contact-details">
      <li>
        <span class="contact-label">Email</span>
        <a href="mailto:wicenwa@outlook.com">wicenwa@outlook.com</a>
      </li>
      <li>
        <span class="contact-label">Postal Address</span>
        <span>PO Box 425<br>Cannington WA 6987</span>
      </li>
    </ul>
  </div>

  <div class="contact-form-wrapper">
    <h2>Send Us a Message</h2>
    <form
      class="contact-form"
      action="https://formspree.io/f/mlgperar"
      method="POST"
    >
      <div class="form-group">
        <label for="name">Your Name <span class="required">*</span></label>
        <input type="text" id="name" name="name" placeholder="Jane Smith" required>
      </div>

      <div class="form-group">
        <label for="email">Your Email <span class="required">*</span></label>
        <input type="email" id="email" name="email" placeholder="jane@example.com" required>
      </div>

      <div class="form-group">
        <label for="subject">Subject <span class="required">*</span></label>
        <select id="subject" name="subject" required>
          <option value="" disabled selected>Select a topic…</option>
          <option value="membership">Membership enquiry</option>
          <option value="volunteering">Volunteering</option>
          <option value="events">Events</option>
          <option value="other">Other</option>
        </select>
      </div>

      <div class="form-group">
        <label for="message">Message <span class="required">*</span></label>
        <textarea id="message" name="message" rows="6" placeholder="Tell us how we can help…" required></textarea>
      </div>

      <!-- Honeypot spam protection -->
      <input type="text" name="_gotcha" style="display:none">

      <button type="submit" class="btn btn-submit">Send Message</button>
    </form>
  </div>

</div>
