<script setup>
const year = new Date().getFullYear()
</script>

<template>
  <footer class="footer">
    <div class="container footer__row">
      <div class="footer__brand">
        <h3 class="footer__logo">FRISO</h3>
        <p class="footer__tag">Clothing made for the everyday edit.</p>
      </div>

      <div class="footer__col">
        <span class="eyebrow">Shop</span>
        <router-link to="/man">Man</router-link>
        <router-link to="/woman">Woman</router-link>
        <router-link to="/sale">Sale</router-link>
      </div>

      <div class="footer__col">
        <span class="eyebrow">Company</span>
        <router-link to="/about">About</router-link>
        <a href="#">Sustainability</a>
        <a href="#">Careers</a>
      </div>

      <div class="footer__col">
        <span class="eyebrow">Help</span>
        <a href="#">Shipping &amp; Returns</a>
        <a href="#">Size Guide</a>
        <a href="#">Contact</a>
      </div>
    </div>

    <div class="container footer__bottom">
      <span>© {{ year }} FRISO. All rights reserved.</span>
      <div class="footer__socials">
        <a href="#" aria-label="Instagram">IG</a>
        <a href="#" aria-label="TikTok">TT</a>
        <a href="#" aria-label="Pinterest">PIN</a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: var(--ink);
  color: var(--paper);
  margin-top: 96px;
}

.footer__row {
  display: grid;
  grid-template-columns: 1.6fr 1fr 1fr 1fr;
  gap: 32px;
  padding: 64px 32px 40px;
}

.footer__logo {
  font-size: 1.7rem;
  margin-bottom: 10px;
}

.footer__tag {
  color: #b9b3a5;
  font-size: 0.9rem;
  max-width: 32ch;
}

.footer__col {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer__col a {
  color: #cfc9bc;
  font-size: 0.88rem;
  transition: color 0.15s ease;
}

.footer__col a:hover {
  color: var(--paper);
}

.footer__bottom {
  border-top: 1px solid #33322d;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 32px 28px;
  font-size: 0.78rem;
  color: #9e988a;
}

.footer__socials {
  display: flex;
  gap: 16px;
}

.footer__socials a {
  font-weight: 700;
  letter-spacing: 0.05em;
  color: #cfc9bc;
}

@media (max-width: 860px) {
  .footer__row {
    grid-template-columns: 1fr 1fr;
  }

  .footer__bottom {
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
  }
}
</style>
