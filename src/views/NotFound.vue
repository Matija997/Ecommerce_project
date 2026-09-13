<script setup></script>

<template>
  <div class="notfound container">
    <span class="eyebrow">Error 404</span>
    <h1 class="notfound__title">This page walked off the rack.</h1>
    <p class="notfound__sub">
      The page you're looking for doesn't exist. Let's get you back to shopping.
    </p>
    <router-link to="/" class="btn">Back to Home</router-link>
  </div>
</template>

<style scoped>
.notfound {
  min-height: 50vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 16px;
  padding: 100px 32px;
}

.notfound__title {
  font-size: clamp(1.8rem, 4vw, 2.6rem);
  max-width: 18ch;
}

.notfound__sub {
  color: var(--taupe);
  max-width: 40ch;
  margin-bottom: 12px;
}
</style>
