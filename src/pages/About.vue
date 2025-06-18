<template>
  <div class="about-page" style="padding-top: 60px;">
    <h2>About Us</h2>
    <p>
      Welcome to our shop! We pride ourselves on offering the best quality products
      and exceptional customer service. Our goal is to provide you with a seamless
      shopping experience, whether you visit us online or in-store.
    </p>
    <p>
      Our knowledgeable staff is always here to help you find exactly what you need.
      Thank you for choosing us!
    </p>

    <div class="contact-info">
      <h3>Contact Us</h3>
      <div class="map-container">
            <iframe
                width="100%"
                height="400"
                frameborder="0"
                style="border:0"
                loading="lazy"
                allowfullscreen
                referrerpolicy="no-referrer-when-downgrade"
                :src="googleMapSrc"
            ></iframe>
        </div>
        <p>Address: Cara Dušana 28, Zemun</p>
        <p>Phone: +381 11 123 4567</p>
        <p>E-mail: shop@gmail.com</p>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    googleMapSrc() {
      return "https://www.google.com/maps?q=Cara+Dušana+28,+Zemun,+Serbia&output=embed"
    }
  }
}
</script>

<style scoped>
.about-page {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  color: #333;
}

.about-page p {
  line-height: 1.6;
  margin-bottom: 1em;
}

.map-container {
  margin: 40px 0;
  border: 2px solid #ccc;
  border-radius: 8px;
  overflow: hidden;
}

.contact-info {
  background: #f5f5f5;
  padding: 15px;
  border-radius: 8px;
}

.contact-info h3 {
  margin-top: 0;
}
</style>
