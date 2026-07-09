export function loadGoogleScript(clientId, callback) {
  const script = document.createElement('script')

  script.src = 'https://accounts.google.com/gsi/client'
  script.async = true
  script.defer = true

  script.onload = () => {
    window.google.accounts.id.initialize({
      client_id: clientId,
      callback: callback,
    })
  }

  document.head.appendChild(script)
}


export function googleLogin() {
  window.google.accounts.id.prompt()
}