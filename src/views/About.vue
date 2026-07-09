<script setup>
const values = [
  {
    title: 'Considered materials',
    body: 'We source natural fibers first — wool, cotton, linen — and test every fabric for wear before it reaches a collection.'
  },
  {
    title: 'Made to be worn',
    body: 'Every piece is judged against one question: does it hold up to a real week, not just a photoshoot.'
  },
  {
    title: 'Fewer, better drops',
    body: 'We release seasonally rather than weekly, so the collection stays intentional instead of disposable.'
  }
]
</script>

<template>
  <div class="about">
    <section class="about__hero container">
      <span class="eyebrow">Our story</span>
      <h1 class="about__title">Clothes built around how you actually live.</h1>
      <p class="about__lead">
        FRISO started in a small studio with one idea: fewer, better pieces
        beat a closet full of trends. Every collection is designed, tested
        and re-cut until it earns a place in daily rotation.
      </p>
    </section>

    <section class="about__image">
      <img src="https://picsum.photos/seed/friso-about/1400/700" alt="FRISO design studio" />
    </section>

    <section class="container about__values">
      <div v-for="(value, i) in values" :key="value.title" class="about__value">
        <span class="about__num">{{ String(i + 1).padStart(2, '0') }}</span>
        <h3>{{ value.title }}</h3>
        <p>{{ value.body }}</p>
      </div>
    </section>

    <section class="container about__cta">
      <h2>Come see the current collection.</h2>
      <div class="about__cta-links">
        <router-link to="/man" class="btn">Shop Man</router-link>
        <router-link to="/woman" class="btn btn-outline">Shop Woman</router-link>
      </div>
    </section>
  </div>
</template>

<style scoped>
.about__hero {
  padding: 60px 32px 40px;
  max-width: 900px;
}

.about__title {
  font-size: clamp(2.2rem, 5vw, 3.2rem);
  margin: 12px 0 20px;
}

.about__lead {
  font-size: 1.05rem;
  color: var(--taupe);
  max-width: 60ch;
}

.about__image img {
  width: 100%;
  aspect-ratio: 2 / 1;
  object-fit: cover;
}

.about__values {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
  padding: 76px 32px;
}

.about__num {
  font-family: var(--font-display);
  color: var(--accent);
  font-size: 1.3rem;
  display: block;
  margin-bottom: 14px;
}

.about__value h3 {
  font-family: var(--font-body);
  font-weight: 700;
  font-size: 1.05rem;
  margin-bottom: 10px;
}

.about__value p {
  color: var(--taupe);
  font-size: 0.92rem;
}

.about__cta {
  text-align: center;
  padding: 20px 32px 110px;
}

.about__cta h2 {
  font-size: clamp(1.8rem, 4vw, 2.4rem);
  margin-bottom: 28px;
}

.about__cta-links {
  display: flex;
  gap: 14px;
  justify-content: center;
}

@media (max-width: 780px) {
  .about__values {
    grid-template-columns: 1fr;
  }
}
</style>
