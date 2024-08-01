export default {
  methods: {
    getJWT() {
      const jwt = localStorage.getItem('JWT')
      if (jwt === null) {
        return ''
      }
      else {
        return jwt
      }
    },
    setJWT(jwt) {
      localStorage.setItem('JWT', jwt)
    }
  }
}
