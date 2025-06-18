<template>
  <nav class="navbar">
    <div class="nav-left">
      <ul class="nav-links">
        <li><a href="#">Home</a></li>
        <li><a href="#">Clothing</a></li>
        <li><a href="#">Footwear</a></li>
        <li><a href="#">Sale</a></li>
        <li><a href="#">About</a></li>
      </ul>
    </div>
    <div class="nav-right">
      <button class="icon-button" title="Search">🔍</button>
      <a href="#" class="nav-link">Login</a>
      <a href="#" class="nav-link">🛒</a>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  background-color: #333;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  z-index: 1000;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.nav-left .nav-links,
.nav-right {
  display: flex;
  align-items: center;
}

.nav-links {
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-links a,
.nav-link {
  color: white;
  text-decoration: none;
  font-size: 15px;
  margin-right: 20px;
}

.nav-links a:hover,
.nav-link:hover {
  text-decoration: underline;
}

.icon-button {
  background: none;
  border: none;
  color: white;
  font-size: 18px;
  cursor: pointer;
  margin-right: 15px;
}
</style>
