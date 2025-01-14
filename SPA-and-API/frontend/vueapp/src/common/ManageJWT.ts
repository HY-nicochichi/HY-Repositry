function getJWT(): string {
  let jwt: string | null = localStorage.getItem('JWT')
  if (jwt === null) {
    jwt = ''
  }
  return jwt
}

function setJWT(jwt: string): void {
  localStorage.setItem('JWT', jwt)
}

export {
  getJWT, setJWT
}
