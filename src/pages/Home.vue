<template>
  <div class="home-hero">
    <h1>Welcome</h1>
  </div>
</template>

<style scoped>
.home-hero {
  height: 100vh;
  background-image: url('@/assets/background.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;

  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.home-hero h1 {
  color: white;
  font-size: 64px;
  font-weight: bold;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
}
</style>

