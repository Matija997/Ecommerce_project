export function loadGoogleScript(clientId, callback) {
  const script = document.createElement('script')
  script.src = 'https://accounts.google.com/gsi/client?hl=en'
  script.async = true
  script.defer = true
  script.onload = () => {
    window.google.accounts.id.initialize({
      client_id: clientId,
      callback: callback,
    })
    window.google.accounts.id.renderButton(
      document.getElementById('google-signin-button'),
      { theme: 'outline', size: 'large' }
    )
  }
  document.head.appendChild(script)
}
