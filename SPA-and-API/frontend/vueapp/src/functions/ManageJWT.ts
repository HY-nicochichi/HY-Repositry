export default function() {

  const getJWT: () => string 
  = () => {
    const jwt: string | null = localStorage.getItem('JWT')
    if (jwt === null) {
      return ''
    }
    else {
      return jwt
    }
  }

  const setJWT: (jwt: string) => void 
  = (jwt) => {
    localStorage.setItem('JWT', jwt)
  }

  return {
    getJWT, setJWT
  }

}
