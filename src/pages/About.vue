<template>
  <div class="about-page">
    <div class="about-content">
      <div>
        <h2 style="padding-top: 60px;">About Us</h2>

        <p>
          Welcome to our shop! We pride ourselves on offering the best quality products
          and exceptional customer service. Our goal is to provide you with a seamless
          shopping experience, whether you visit us online or in-store.
        </p>
        <p>
          At the heart of our company is a dedication to our customers. Your feedback inspires us
          to keep improving, and your satisfaction is our greatest reward. Whether you're shopping
          for everyday basics, seasonal fashion, or something special, we aim to make your experience easy and enjoyable.
        </p>
        <p>
          Since our founding, we’ve been committed to curating a wide selection of clothing and footwear
          that combines style, comfort, and affordability. We work closely with trusted suppliers
          to ensure every item we sell meets our high standards.
        </p>
        <p>
          We’re based in Belgrade, Serbia — but we ship everywhere. With fast delivery, secure payments,
          and a friendly support team, we’re here to make sure you love every step of the journey.
        </p>
        <p>
          Thank you for being part of our story. We look forward to serving you for many years to come!
        </p>
      </div>
      <transition name="slide-up" appear>
        <div v-if="showContact" class="contact-section">
          <h2 class="contact-heading">Contact Us</h2>

          <div class="contact-content">
            <div class="contact-left">
              <p><i class="fas fa-map-marker-alt"></i> Cara Dušana 28, Belgrade, Serbia</p>
              <p><i class="fas fa-phone-alt"></i> +381 11 123 4567</p>
              <p><i class="fas fa-envelope"></i> contact@yourshop.rs</p>
              <div class="social-icons">
                <a href="https://facebook.com" target="_blank"><i class="fab fa-facebook fa-lg"></i></a>
                <a href="https://instagram.com" target="_blank"><i class="fab fa-instagram fa-lg"></i></a>
                <a href="https://twitter.com" target="_blank"><i class="fab fa-x-twitter fa-lg"></i></a>
              </div>

              <div class="map-container">
                <iframe
                  width="400"
                  height="200"
                  frameborder="0"
                  style="border:0"
                  loading="lazy"
                  allowfullscreen
                  referrerpolicy="no-referrer-when-downgrade"
                  src="https://www.google.com/maps?q=Cara+Dušana+28,+Belgrade,+Serbia&output=embed"
                ></iframe>
              </div>
            </div>

            <!-- Right: Contact Form -->
            <div class="contact-right">
              <p>Leave us a message</p>
              <form @submit.prevent="handleSubmit">
                <input type="text" placeholder="Your Name" required />
                <input type="email" placeholder="Your Email" required />
                <textarea placeholder="Your Message" rows="6" required></textarea>
                <button type="submit">Send</button>
              </form>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showContact: false
    };
  },
  mounted() {
  document.body.style.overflow = 'hidden';
  this.showContact = true;
  setTimeout(() => {
    document.body.style.overflow = 'auto';
  }, 1000);
  },
  methods: {
    handleSubmit() {
      alert('Thank you for your message!');
    }
  }
}
</script>

<style scoped>
.about-page {
  min-height: 100vh;
  background-image: url('@/assets/background.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.about-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  max-width: 1100px;
  margin: 0 auto;
  padding: 10px;
  color: #333;
}

.about-page h2 {
  text-align: center;
  margin-bottom: 20px;
}

.about-page p {
  line-height: 1.6;
  margin-bottom: 1em;
}

.contact-section {
  min-height: 300px;
  will-change: transform, opacity;
  background-color: #333;
  border-radius: 30px;
  padding: 30px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
}

.contact-heading {
  text-align: center;
  margin-top: 0;
  font-weight: bold;
  color: white;
}

.contact-content {
  display: flex;
  flex-wrap: wrap;
  gap: 40px;
  align-items: flex-start;
  margin-top: 50px;
  font-size: 12px;
  color: white;
}

.contact-left,
.contact-right {
  flex: 1;
  min-width: 300px;
}

.contact-left p {
  margin: 8px 0;
}

.map-container {
  margin-top: 10px;
  border-radius: 8px;
  overflow: hidden;
}

.contact-right form {
  display: flex;
  flex-direction: column;
}

.contact-right input,
.contact-right textarea {
  margin-bottom: 15px;
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.contact-right button {
  padding: 10px;
  background-color: #ee6464;
  color: white;
  font-size: 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.contact-right button:hover {
  background-color: #555;
}
.social-icons a {
  color: white;
  margin-right: 15px;
  font-size: 12px;
  transition: color 0.3s;
}

.social-icons a:hover {
  color: #000;
}
.slide-up-enter-from {
  opacity: 0;
  transform: translateY(100px);
}

.slide-up-enter-active {
  transition: transform 1s ease-out, opacity 1s ease-out;
}

.slide-up-enter-to {
  opacity: 1;
  transform: translateY(0);
}
</style>
