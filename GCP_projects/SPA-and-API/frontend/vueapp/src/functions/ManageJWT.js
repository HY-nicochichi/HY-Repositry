export default function() {

  const getJWT = () => {
    const jwt = localStorage.getItem('JWT')
    if (jwt === null) {
      return ''
    }
    else {
      return jwt
    }
  }

  const setJWT = (jwt) => {
    localStorage.setItem('JWT', jwt)
  }

  return {
    getJWT, setJWT
  }

}
