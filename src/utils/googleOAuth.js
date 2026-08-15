let scriptPromise = null

function loadGoogleScript() {
  if (scriptPromise) return scriptPromise

  scriptPromise = new Promise((resolve, reject) => {
    if (window.google?.accounts?.id) {
      resolve(window.google)
      return
    }
    const script = document.createElement('script')
    script.src = 'https://accounts.google.com/gsi/client'
    script.async = true
    script.defer = true
    script.onload = () => resolve(window.google)
    script.onerror = () => reject(new Error('Failed to load Google Identity Services'))
    document.head.appendChild(script)
  })

  return scriptPromise
}

export async function initGoogleAuth(clientId, callback) {
  const google = await loadGoogleScript()
  google.accounts.id.initialize({
    client_id: clientId,
    callback
  })
}

export function googleLogin() {
  window.google.accounts.id.prompt()
}