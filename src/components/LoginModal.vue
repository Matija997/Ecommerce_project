<script setup>
import { ref, computed, onMounted } from 'vue'
import { useStore } from '../store/useStore'
import { initGoogleAuth, googleLogin } from '@/utils/googleOAuth.js'

const GOOGLE_CLIENT_ID = '673865342919-i1kb9q06nnl0lgheaqnp034istdfacin.apps.googleusercontent.com'

const { state, toggleLogin, login, logout } = useStore()

// 'signin' | 'signup'
const mode = ref('signin')

const firstName = ref('')
const lastName = ref('')
const phone = ref('')
const address = ref('')
const city = ref('')
const email = ref('')
const password = ref('')
const showPassword = ref(false)
const rememberMe = ref(false)
const error = ref('')

const title = computed(() => (mode.value === 'signin' ? 'Sign in' : 'Create account'))

onMounted(() => {
  initGoogleAuth(GOOGLE_CLIENT_ID, handleGoogleCredential)
})

function resetFields() {
  firstName.value = ''
  lastName.value = ''
  phone.value = ''
  address.value = ''
  city.value = ''
  email.value = ''
  password.value = ''
  showPassword.value = false
  error.value = ''
}

function switchMode(next) {
  mode.value = next
  error.value = ''
}

async function submit() {
  error.value = ''

  try {

    // SIGN UP
    if (mode.value === 'signup') {

      const response = await fetch('http://localhost:5000/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          first_name: firstName.value,
          last_name: lastName.value,
          email: email.value,
          password: password.value,
          phone: phone.value,
          address: address.value,
          city: city.value
        })
      })


      const data = await response.json()


      if (!response.ok) {
        error.value = data.message
        return
      }


      login(
        {
          id: data.user.id,
          name: `${data.user.first_name} ${data.user.last_name}`,
          email: data.user.email,
          role: data.user.role
        },
        data.access_token,
        rememberMe.value
      )

      resetFields()

      return
    }



    // LOGIN
    const response = await fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: email.value,
        password: password.value
      })
    })


    const data = await response.json()


    if (!response.ok) {
      error.value = data.message
      return
    }


    // Update the Vue store (also persists the user + token)
    login(
      {
        id: data.user.id,
        name: `${data.user.first_name} ${data.user.last_name}`,
        email: data.user.email,
        role: data.user.role
      },
      data.access_token,
      rememberMe.value
    )


    resetFields()


  } catch (err) {

    console.error(err)
    error.value = "Cannot connect to server."

  }
}

async function handleGoogleCredential(response) {
  error.value = ''

  try {
    const res = await fetch('http://localhost:5000/auth/google', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ credential: response.credential })
    })

    const data = await res.json()

    if (!res.ok) {
      error.value = data.message
      return
    }

    login(
      {
        id: data.user.id,
        name: `${data.user.first_name} ${data.user.last_name}`,
        email: data.user.email,
        role: data.user.role
      },
      data.access_token,
      rememberMe.value
    )

    resetFields()
  } catch (err) {
    console.error(err)
    error.value = 'Cannot connect to server.'
  }
}

function googleSignIn() {
  error.value = ''
  googleLogin()
}

function close() {
  toggleLogin(false)
  mode.value = 'signin'
  resetFields()
}
</script>

<template>
  <transition name="fade">
    <div v-if="state.isLoginOpen" class="modal">
      <div class="modal__scrim" @click="close"></div>

      <div class="modal__panel" role="dialog" aria-modal="true">
        <button class="modal__close" aria-label="Close" @click="close">✕</button>

        <template v-if="!state.user">
          <span class="eyebrow">{{ mode === 'signin' ? 'Welcome back' : 'New here' }}</span>
          <h3 class="modal__title">{{ title }}</h3>

          <form class="modal__form" @submit.prevent="submit">
            <!-- FIRST NAME -->
            <label v-if="mode === 'signup'" class="modal__label">
              First Name
              <input v-model="firstName" type="text" placeholder="John" required />
            </label>

            <!-- LAST NAME -->
            <label v-if="mode === 'signup'" class="modal__label">
              Last Name
              <input v-model="lastName" type="text" placeholder="Doe" required />
            </label>

            <!-- PHONE -->
            <label v-if="mode === 'signup'" class="modal__label">
              Phone
              <input v-model="phone" type="text" placeholder="+381601234567" required />
            </label>

            <!-- ADDRESS -->
            <label v-if="mode === 'signup'" class="modal__label">
              Address
              <input v-model="address" type="text" placeholder="Street 12" required />
            </label>

            <!-- CITY -->
            <label v-if="mode === 'signup'" class="modal__label">
              City
              <input v-model="city" type="text" placeholder="Belgrade" required />
            </label>

            <label class="modal__label">
              Email
              <input v-model="email" type="email" placeholder="you@email.com" required />
            </label>

            <label class="modal__label">
              Password
              <div class="modal__password-wrap">
                <input
                  v-model="password"
                  :type="showPassword ? 'text' : 'password'"
                  placeholder="••••••••"
                  required
                />
                <button
                  type="button"
                  class="modal__toggle-visibility"
                  :aria-label="showPassword ? 'Hide password' : 'Show password'"
                  @click="showPassword = !showPassword"
                >
                  <svg v-if="!showPassword" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6">
                    <path d="M2 12s3.8-7 10-7 10 7 10 7-3.8 7-10 7-10-7-10-7Z" />
                    <circle cx="12" cy="12" r="3" />
                  </svg>
                  <svg v-else viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6">
                    <path d="M2 12s3.8-7 10-7 10 7 10 7-3.8 7-10 7-10-7-10-7Z" />
                    <circle cx="12" cy="12" r="3" />
                    <line x1="3" y1="21" x2="21" y2="3" />
                  </svg>
                </button>
              </div>
            </label>

            <label v-if="mode === 'signin'" class="modal__remember">
              <input v-model="rememberMe" type="checkbox" />
              Stay logged in
            </label>

            <p v-if="error" class="modal__error">{{ error }}</p>

            <button type="submit" class="btn" style="width: 100%; margin-top: 8px;">
              {{ mode === 'signin' ? 'Sign in' : 'Create account' }}
            </button>
          </form>
          <div class="modal__divider"><span>or</span></div>
          <button type="button" class="modal__google" @click="googleSignIn">
            <svg viewBox="0 0 48 48" width="18" height="18" aria-hidden="true">
              <path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.7 29.3 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.1 8 3l6-6C34.5 5.5 29.5 3.5 24 3.5 12.7 3.5 3.5 12.7 3.5 24S12.7 44.5 24 44.5 44.5 35.3 44.5 24c0-1.2-.1-2.4-.3-3.5Z"/>
              <path fill="#FF3D00" d="m6.3 14.7 6.6 4.8C14.6 15.9 18.9 13 24 13c3.1 0 5.8 1.1 8 3l6-6C34.5 6.5 29.5 4.5 24 4.5c-7.8 0-14.5 4.4-17.7 10.2Z"/>
              <path fill="#4CAF50" d="M24 44.5c5.4 0 10.3-1.8 14.1-5l-6.5-5.5c-2 1.4-4.6 2.2-7.6 2.2-5.3 0-9.7-3.3-11.3-8l-6.6 5.1C9.4 40 16.1 44.5 24 44.5Z"/>
              <path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-.8 2.3-2.3 4.3-4.2 5.7l6.5 5.5C41.4 36.5 44.5 30.8 44.5 24c0-1.2-.1-2.4-.3-3.5Z"/>
            </svg>
            Continue with Google
          </button>


          <p class="modal__foot">
            <template v-if="mode === 'signin'">
              Don't have an account?
              <button type="button" class="modal__link" @click="switchMode('signup')">Sign up</button>
            </template>
            <template v-else>
              Already have an account?
              <button type="button" class="modal__link" @click="switchMode('signin')">Sign in</button>
            </template>
          </p>
        </template>

        <template v-else>
          <span class="eyebrow">Account</span>
          <h3 class="modal__title">Hi, {{ state.user.name }}</h3>
          <p class="modal__foot" style="margin-bottom: 20px;">{{ state.user.email }}</p>
          <router-link
            v-if="['admin', 'editor'].includes(state.user.role)"
            to="/admin"
            class="btn btn-outline"
            style="width: 100%; margin-bottom: 12px;"
            @click="close"
          >
            Admin Panel
          </router-link>
          <button class="btn btn-outline" style="width: 100%;" @click="logout">
            Sign out
          </button>
        </template>
      </div>
    </div>
  </transition>
</template>

<style scoped>
.modal {
  position: fixed;
  inset: 0;
  z-index: 70;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal__scrim {
  position: absolute;
  inset: 0;
  background: rgba(17, 17, 17, 0.5);
}

.modal__panel {
  position: relative;
  background: var(--paper);
  width: 100%;
  max-width: 380px;
  padding: 40px 32px;
  margin: 16px;
  max-height: 90vh;
  overflow-y: auto;
}

.modal__close {
  position: absolute;
  top: 14px;
  right: 14px;
  background: none;
  border: none;
  font-size: 1rem;
  padding: 8px;
}

.modal__title {
  font-size: 1.6rem;
  margin: 6px 0 22px;
}

.modal__google {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background: var(--white);
  border: 1px solid var(--line);
  padding: 12px 14px;
  font-family: var(--font-body);
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--ink);
  transition: border-color 0.15s ease, background 0.15s ease;
}

.modal__google:hover {
  border-color: var(--ink);
  background: var(--stone);
}

.modal__divider {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 20px 0;
  color: var(--taupe);
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
}

.modal__divider::before,
.modal__divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--line);
}

.modal__form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.modal__label {
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  color: var(--taupe);
}

.modal__label input {
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
}

.modal__label input:focus {
  outline: none;
  border-color: var(--ink);
}

.modal__password-wrap {
  position: relative;
  display: flex;
  align-items: center;
}

.modal__password-wrap input {
  padding-right: 42px;
}

.modal__toggle-visibility {
  position: absolute;
  right: 8px;
  background: none;
  border: none;
  color: var(--taupe);
  padding: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.15s ease;
}

.modal__toggle-visibility:hover {
  color: var(--ink);
}

.modal__remember {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.82rem;
  font-weight: 400;
  text-transform: none;
  letter-spacing: normal;
  color: var(--ink);
  cursor: pointer;
}

.modal__remember input {
  width: 16px;
  height: 16px;
  accent-color: var(--ink);
}

.modal__error {
  color: var(--accent);
  font-size: 0.82rem;
}

.modal__foot {
  margin-top: 18px;
  font-size: 0.78rem;
  color: var(--taupe);
}

.modal__link {
  background: none;
  border: none;
  padding: 0;
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--ink);
  text-decoration: underline;
  text-underline-offset: 2px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
