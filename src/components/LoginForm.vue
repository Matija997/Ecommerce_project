<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2 class="modal-header">Login</h2>
      <form @submit.prevent="submitLogin">
        <input type="email" v-model="email" placeholder="Email" required />

        <div class="password-input-container">
          <input 
            :type="showPassword ? 'text' : 'password'" 
            v-model="password" 
            placeholder="Password" 
            required 
          />
          <button
            type="button"
            class="toggle-password-btn"
            @click="showPassword = !showPassword"
          >
            <i :class="showPassword ? 'fas fa-eye' : 'fas fa-eye-slash'"></i>
          </button>
        </div>

        <label class="checkbox-container">
          <input type="checkbox" v-model="keepLoggedIn" />
          Keep me logged in
        </label>
        <button type="submit" class="login-btn">Login</button>
      </form>

      <div id="google-signin-button" class="google-btn-container"></div>

      <p class="signup-text">
        Don't have an account?
        <a href="#" @click.prevent="$emit('signup')">Sign up</a>
      </p>

      <button class="close-btn" @click="$emit('close')">×</button>
    </div>
  </div>
</template>

<script>
import { loadGoogleScript } from '@/utils/googleOAuth.js'

export default {
  data() {
    return {
      email: '',
      password: '',
      keepLoggedIn: false,
      showPassword: false,
    }
  },
  mounted() {
    const clientId = '673865342919-i1kb9q06nnl0lgheaqnp034istdfacin.apps.googleusercontent.com'
    loadGoogleScript(clientId, this.handleGoogleResponse)
  },
  methods: {
    submitLogin() {
      alert(`Logging in as ${this.email}\nKeep logged in: ${this.keepLoggedIn}`)
      this.$emit('close')
    },
    handleGoogleResponse(response) {
      console.log('Google credential response:', response.credential)

      alert('Logged in with Google!')
      this.$emit('close')
    },
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background-color: rgba(0,0,0,0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
}

.modal-content {
  background: white;
  padding: 30px 30px 40px;
  border-radius: 12px;
  position: relative;
  width: 320px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.3);
  font-family: Arial, sans-serif;
}

.modal-header {
  text-align: center;
  margin-bottom: 25px;
  font-weight: 700;
  font-size: 24px;
  color: #333;
}

.modal-content input[type="email"],
.modal-content input[type="password"] {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 6px;
  box-sizing: border-box;
}
.password-input-container {
  position: relative;
  width: 100%;
  margin-bottom: 15px;
}

.password-input-container input {
  width: 100%;
  padding-right: 40px;
  padding-left: 10px;
  padding-top: 10px;
  padding-bottom: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 6px;
  box-sizing: border-box;
}

.toggle-password-btn {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  background: transparent;
  border: none;
  color: #666;
  font-weight: 600;
  cursor: pointer;
  padding: 0;
  width: 30px;
  height: 30px; 
  font-size: 18px;
  user-select: none;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1; 
}
.toggle-password-btn i.fa-eye-slash {
  transform: translateY(-5px);
}


.toggle-password-btn:hover {
  color: #333;}

.checkbox-container {
  display: flex;
  align-items: center;
  font-size: 14px;
  margin-bottom: 20px;
  user-select: none;
}

.checkbox-container input {
  margin-right: 8px;
  width: 16px;
  height: 16px;
  cursor: pointer;
}

.login-btn {
  padding: 10px;
  width: 100%;
  background: red;
  border: none;
  color: white;
  font-weight: bold;
  cursor: pointer;
  border-radius: 6px;
  font-size: 16px;
  margin-bottom: 15px;
  transition: background-color 0.3s;
}

.login-btn:hover {
  background: #d45555;
}

.signup-text {
  text-align: center;
  font-size: 14px;
  color: #666;
}

.signup-text a {
  color: red;
  text-decoration: none;
  font-weight: 600;
  cursor: pointer;
}

.signup-text a:hover {
  text-decoration: underline;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 12px;
  background: transparent;
  border: none;
  font-size: 26px;
  font-weight: bold;
  cursor: pointer;
  color: #999;
  transition: color 0.3s;
}

.close-btn:hover {
  color: #ee6464;
}
</style>
