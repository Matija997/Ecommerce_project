<script>
export default {
  data() {
    return {
      name: '',
      lastname: '',
      email: '',
      street: '',
      city: '',
      phone:'',
      password: '',
      confirmPassword: '',
      showPassword: false,
      errorMessage: ''
    }
  },
  methods: {
    
    submitSignup() {
      this.errorMessage = ''

      if (this.password !== this.confirmPassword) {
        this.errorMessage = 'Passwords do not match'
        return
      }

      this.$emit('close')
    },

    addPrefix() {
      if (!this.phone) {
        this.phone = '+381 '
      }
    },
    filterPhone() {
      if (!this.phone.startsWith('+381')) {
        this.phone = '+381 '
        return
      }

      const digits = this.phone
        .replace('+381', '')
        .replace(/\D/g, '')

      this.phone = '+381 ' + digits
    }
  }
}
</script>
<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2 class="modal-header">Sign Up</h2>

      <form @submit.prevent="submitSignup">
        <input type="text" v-model="name" placeholder="First Name" required />
        <input type="text" v-model="lastname" placeholder="Last Name" required />
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="text" v-model="street" placeholder="Address" required />
        <input type="text" v-model="city" placeholder="City" required />
        <input type="tel" v-model="phone" autocomplete="tel" placeholder="Phone Number" inputmode="numeric" required
        @focus="addPrefix"
        @input="filterPhone"/>

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

        <div class="password-input-container">
          <input
            :type="showPassword ? 'text' : 'password'"
            v-model="confirmPassword"
            placeholder="Confirm password"
            required
          />
        </div>
        <p v-if="errorMessage" class="error-text">
          {{ errorMessage }}
        </p>

        <button type="submit" class="login-btn">Create account</button>
      </form>

      <p class="signup-text">
        Already have an account?
        <a href="#" @click.prevent="$emit('switch-to-login')">Log in</a>
      </p>

      <button class="close-btn" @click="$emit('close')">×</button>
    </div>
  </div>
</template>
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
.modal-content input[type="text"],
.modal-content input[type="email"],
.modal-content input[type="password"],
.modal-content input[type="tel"] {
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

.toggle-password-btn i {
  line-height: 1;
  display: block;
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
.toggle-password-btn i{
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

.error-text {
  color: #e53935;
  font-size: 14px;
  text-align: center;
}
</style>