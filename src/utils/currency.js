export function formatPrice(rsd) {
  return new Intl.NumberFormat('sr-RS').format(rsd) + ' RSD'
}
