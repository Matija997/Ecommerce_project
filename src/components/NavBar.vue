<template>
  <nav class="navbar">
    <div class="nav-left">
      <ul class="nav-links">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/clothing">Clothing</router-link></li>
        <li><router-link to="/footwear">Footwear</router-link></li>
        <li><router-link to="/sale">Sale</router-link></li>
        <li><router-link to="/about">About</router-link></li>
      </ul>
    </div>
    <div class="nav-right">
      <button class="icon-button" title="Search">
        <i class="fas fa-search"></i>
      </button>
      <router-link to="/login" class="nav-link" style="margin-right: 20px;">Login</router-link>
      <router-link to="/cart" class="nav-link">
        <i class="fas fa-shopping-cart"></i>
      </router-link>
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

.nav-links {
  list-style: none;
  display: flex;
  padding: 0;
  margin: 0;
}

.nav-links li {
  margin-right: 20px;
}

.nav-links a,
.nav-link {
  color: white;
  text-decoration: none;
  font-size: 15px;
}

.nav-links a.router-link-active {
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
