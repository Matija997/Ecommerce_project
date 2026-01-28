<template>
  <div class="men-page">
    <div class="men-content">
      <h3>Men's Collection</h3>
      <transition name="slide-in-left" appear>
        <div class="slider-container">
          <div class="slider">
            <router-link 
              v-for="(item, index) in cards" 
              :key="index" 
              :to="item.route" 
              class="card-link"
            >
              <div class="card">
                <img :src="item.image" :alt="item.title" />
                <h3>{{ item.title }}</h3>
              </div>
            </router-link>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import tshirtImage from '@/assets/t-shirt.png';
import sneakersImage from '@/assets/sneakers.png';
import capImage from '@/assets/cap.png';
export default {
  data() {
    return {
      cards: [
        { title: "Clothing", image: tshirtImage, route: "/men/clothing" },
        { title: "Footwear", image: sneakersImage, route: "/men/footwear" },
        { title: "Accessories", image: capImage, route: "/men/accessories" },
      ]
    };
  }
};
</script>

<style scoped>
.men-page{
  min-height: 100vh;
  background-image: url('@/assets/background.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  overflow-x: hidden;
}
.men-content {
  text-align: center;
  padding-top: 80px;
  font-family: Arial, sans-serif;
}

.slider-container {
  display: flex;
  justify-content: center;
  overflow-x: auto;
  scroll-behavior: smooth;
  padding: 40px 0;
}

.slider {
  display: flex;
  gap: 40px;
}

.card {
  background-color: #f0f0f0;
  border-radius: 12px;
  width: 300px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s;
  display: flex;
  flex-direction: column;
}
.card:hover {
  transform: scale(1.05);
  cursor: pointer;
}
.card-link {
  text-decoration: none;
  color: inherit;
  display: block;
  width: 300px;
}

.card img {
  width: 100%;
  height: 250px;
  object-fit: contain;
  border-top-left-radius: 12px;
  border-top-right-radius: 12px;
}

.card h3 {
  padding: 10px;
  color: #333;
}
.slide-in-left-enter-active {
  animation: slide-in-left 1s ease forwards;
}

.slide-in-left-leave-active {
  animation: slide-out-left 1s ease forwards;
}

@keyframes slide-in-left {
  from {
    transform: translateX(-100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slide-out-left {
  from {
    transform: translateX(0);
    opacity: 1;
  }
  to {
    transform: translateX(-100%);
    opacity: 0;
  }
}
</style>

