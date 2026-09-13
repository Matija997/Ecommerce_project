<script setup>
import { reactive, ref } from 'vue'

const form = reactive({
  name: '',
  email: '',
  message: ''
})

const sending = ref(false)
const sent = ref(false)
const error = ref('')

async function submitContact() {
  error.value = ''
  sending.value = true

  try {
    const res = await fetch('http://localhost:5000/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    })
    const data = await res.json()

    if (!res.ok) {
      error.value = data.message || 'Something went wrong.'
      return
    }

    sent.value = true
    form.name = ''
    form.email = ''
    form.message = ''
  } catch (err) {
    console.error(err)
    error.value = 'Cannot connect to server.'
  } finally {
    sending.value = false
  }
}

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

    <section id="contact" class="container about__contact">
      <span class="eyebrow">Visit us</span>
      <h2 class="about__contact-title">Get in touch.</h2>

      <div class="about__contact-grid">
        <div class="about__contact-info">
          <div class="about__contact-item">
            <span class="about__contact-label">Address</span>
            <p>Cara Dušana 15<br />Zemun, Belgrade</p>
          </div>
          <div class="about__contact-item">
            <span class="about__contact-label">Phone</span>
            <p><a href="tel:+381113167420">+381 11 316 74 20</a></p>
          </div>
          <div class="about__contact-item">
            <span class="about__contact-label">Email</span>
            <p><a href="mailto:info@friso.com">info@friso.com</a></p>
          </div>

          <form v-if="!sent" class="about__form" @submit.prevent="submitContact">
            <span class="about__contact-label">Send a message</span>

            <label class="about__form-label">
              Name
              <input v-model="form.name" type="text" required />
            </label>

            <label class="about__form-label">
              Email
              <input v-model="form.email" type="email" required />
            </label>

            <label class="about__form-label">
              Message
              <textarea v-model="form.message" rows="4" required></textarea>
            </label>

            <p v-if="error" class="about__form-error">{{ error }}</p>

            <button type="submit" class="btn" :disabled="sending">
              {{ sending ? 'Sending…' : 'Send Message' }}
            </button>
          </form>
          <p v-else class="about__form-success">
            Thanks — your message is in. We'll get back to you soon.
          </p>
        </div>

        <div class="about__map">
          <iframe
            title="FRISO store location"
            src="https://www.google.com/maps?q=Cara+Du%C5%A1ana+15,+Zemun,+Belgrade,+Serbia&output=embed"
            width="100%"
            height="100%"
            style="border: 0"
            allowfullscreen="false"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
          ></iframe>
        </div>
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

.about__contact {
  padding: 20px 32px 110px;
}

.about__contact-title {
  font-size: clamp(1.8rem, 4vw, 2.4rem);
  margin: 12px 0 40px;
}

.about__contact-grid {
  display: grid;
  grid-template-columns: 1fr 1.4fr;
  gap: 48px;
}

.about__contact-info {
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.about__contact-label {
  display: block;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  color: var(--taupe);
  margin-bottom: 8px;
}

.about__contact-item p {
  font-size: 1rem;
  line-height: 1.5;
}

.about__contact-item a {
  color: var(--ink);
}

.about__form {
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding-top: 8px;
  border-top: 1px solid var(--line);
}

.about__form-label {
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  color: var(--taupe);
}

.about__form-label input,
.about__form-label textarea {
  font-family: var(--font-body);
  font-size: 0.95rem;
  font-weight: 400;
  text-transform: none;
  letter-spacing: normal;
  color: var(--ink);
  border: 1px solid var(--line);
  background: var(--white);
  padding: 12px 14px;
  width: 100%;
  resize: vertical;
}

.about__form-label input:focus,
.about__form-label textarea:focus {
  outline: none;
  border-color: var(--ink);
}

.about__form-error {
  color: var(--accent);
  font-size: 0.82rem;
}

.about__form-success {
  padding-top: 8px;
  border-top: 1px solid var(--line);
  color: var(--taupe);
  font-size: 0.95rem;
}

.about__map {
  aspect-ratio: 4 / 3;
  border: 1px solid var(--line);
}

.about__map iframe {
  display: block;
}

@media (max-width: 780px) {
  .about__values {
    grid-template-columns: 1fr;
  }

  .about__contact-grid {
    grid-template-columns: 1fr;
  }

  .about__map {
    aspect-ratio: 16 / 10;
  }
}
</style>
