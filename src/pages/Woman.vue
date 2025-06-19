<template>
  <div class="women-page">
    <h3>Women's Collection</h3>
    <div class="slider-container">
      <div class="slider">
        <div class="card" v-for="(item, index) in cards" :key="index">
          <img :src="item.image" :alt="item.title" />
          <h3>{{ item.title }}</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import tshirtImage from '@/assets/dress.jpg';
import sneakersImage from '@/assets/shoes.jpg';
import capImage from '@/assets/bag.jpg';
export default {
  data() {
    return {
      cards: [
        { title: "Clothing", image: tshirtImage  },
        { title: "Footwear", image: sneakersImage },
        { title: "Accessories", image: capImage },
      ]
    };
  }
};
</script>

<style scoped>
.women-page {
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
</style>