<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useStore } from '../store/useStore'

const { state, cartCount, toggleSearch, toggleLogin, toggleCart } = useStore()

const scrolled = ref(false)
const menuOpen = ref(false)

function onScroll() {
  scrolled.value = window.scrollY > 24
}

onMounted(() => window.addEventListener('scroll', onScroll))
onUnmounted(() => window.removeEventListener('scroll', onScroll))

const links = [
  { to: '/', label: 'Home' },
  { to: '/man', label: 'Man' },
  { to: '/woman', label: 'Woman' },
  { to: '/sale', label: 'Sale' },
  { to: '/about', label: 'About' }
]
</script>

<template>
  <header class="header" :class="{ 'header--scrolled': scrolled }">
    <div class="container header__row">
      <button
        class="header__burger"
        aria-label="Toggle menu"
        @click="menuOpen = !menuOpen"
      >
        <span></span><span></span><span></span>
      </button>

      <router-link to="/" class="header__logo">FRISO</router-link>

      <div v-if="menuOpen" class="header__nav-scrim" @click="menuOpen = false"></div>

      <nav class="header__nav" :class="{ 'header__nav--open': menuOpen }">
        <router-link
          v-for="link in links"
          :key="link.to"
          :to="link.to"
          class="header__link"
          :class="{ 'header__link--sale': link.label === 'Sale' }"
          @click="menuOpen = false"
        >
          {{ link.label }}
        </router-link>
      </nav>

      <div class="header__actions">
        <button
          class="header__icon-btn"
          aria-label="Search"
          @click="toggleSearch(true)"
        >
          <svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.6">
            <circle cx="11" cy="11" r="7" />
            <line x1="21" y1="21" x2="16.2" y2="16.2" />
          </svg>
        </button>

        <button
          class="header__icon-btn header__login"
          aria-label="Account"
          @click="toggleLogin(true)"
        >
          <svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.6">
            <circle cx="12" cy="8" r="4" />
            <path d="M4 20c1.5-4 5-6 8-6s6.5 2 8 6" />
          </svg>
          <span v-if="state.user" class="header__user-name">{{ state.user.name }}</span>
        </button>

        <button
          class="header__icon-btn header__bag"
          aria-label="Bag"
          @click="toggleCart(true)"
        >
          <svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.6">
            <path d="M6 8h12l-1 12H7L6 8Z" />
            <path d="M9 8V6a3 3 0 0 1 6 0v2" />
          </svg>
          <span v-if="cartCount > 0" class="header__badge">{{ cartCount }}</span>
        </button>
      </div>
    </div>
  </header>
</template>

<style scoped>
.header {
  position: sticky;
  top: 0;
  z-index: 40;
  background: var(--paper);
  border-bottom: 1px solid var(--line);
  transition: padding 0.2s ease, box-shadow 0.2s ease;
}

.header--scrolled {
  box-shadow: 0 6px 18px rgba(17, 17, 17, 0.06);
}

.header__row {
  display: flex;
  align-items: center;
  gap: 28px;
  height: var(--header-h);
}

.header--scrolled .header__row {
  height: 60px;
}

.header__logo {
  font-family: var(--font-display);
  font-size: 1.5rem;
  letter-spacing: 0.03em;
  transition: font-size 0.2s ease;
}

.header--scrolled .header__logo {
  font-size: 1.2rem;
}

.header__nav {
  display: flex;
  align-items: center;
  gap: 26px;
  margin-left: 8px;
}

.header__link {
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  padding-bottom: 4px;
  border-bottom: 2px solid transparent;
  transition: border-color 0.2s ease, color 0.2s ease;
}

.header__link:hover,
.header__link.router-link-exact-active {
  border-color: var(--ink);
}

.header__link--sale {
  color: var(--accent);
}

.header__link--sale.router-link-exact-active,
.header__link--sale:hover {
  border-color: var(--accent);
}

.header__actions {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-left: auto;
}

.header__icon-btn {
  position: relative;
  display: flex;
  align-items: center;
  gap: 8px;
  background: none;
  border: none;
  color: var(--ink);
  padding: 10px;
  border-radius: 999px;
  transition: background 0.15s ease;
}

.header__icon-btn:hover {
  background: var(--stone);
}

.header__user-name {
  font-size: 0.75rem;
  font-weight: 600;
}

.header__badge {
  position: absolute;
  top: 2px;
  right: 2px;
  background: var(--accent);
  color: var(--white);
  font-size: 0.62rem;
  font-weight: 700;
  min-width: 16px;
  height: 16px;
  border-radius: 999px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 3px;
}

.header__burger {
  display: none;
  flex-direction: column;
  gap: 4px;
  background: none;
  border: none;
  padding: 8px;
}

.header__burger span {
  width: 20px;
  height: 2px;
  background: var(--ink);
}

@media (max-width: 860px) {
  .header__burger {
    display: flex;
  }

  .header__row {
    position: relative;
  }

  .header__logo {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }

  .header__nav-scrim {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    height: 100vh;
    background: rgba(17, 17, 17, 0.5);
  }

  .header__nav {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    margin: 0;
    background: var(--paper);
    border-bottom: 1px solid var(--line);
    flex-direction: column;
    align-items: flex-start;
    gap: 0;
    padding: 0;
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.25s ease;
  }

  .header__nav--open {
    max-height: 320px;
    padding: 8px 0;
    box-shadow: 0 4px 10px rgba(17, 17, 17, 0.08);
  }

  .header__link {
    width: 100%;
    padding: 14px 32px;
    border-bottom: 1px solid var(--line);
    border-left: 2px solid transparent;
  }

  .header__link.router-link-exact-active {
    border-left-color: var(--ink);
    border-bottom-color: var(--line);
  }

  .header__user-name {
    display: none;
  }
}
</style>
